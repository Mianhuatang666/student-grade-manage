<script setup lang="ts">
import { ref, onMounted, resolveComponent } from "vue"
import { StudentInput, StudentMap, Stats} from "../types"
import StudentForm from "../components/StudentForm.vue"
import StudentList from "../components/StudentList.vue"
import StatsPanel from "../components/StatsPanel.vue"
import {
  fetchStudents,
  createStudent,
  updateStudentScore,
  removeStudent,
  fetchStats
} from "../api/students"
import { useAuthStore } from "../stores/authStore.js"

const students = ref<StudentMap>({})
const message = ref("")
const stats = ref<Stats | null>(null)
const addLoading =ref(false)
const studentLoading = ref(false)
const updateLoadingName = ref("")
const deleteLoadingName = ref("")
const authStore = useAuthStore()

// 从后端获取所有学生，并显示到界面
async function loadStudents(){
  studentLoading.value = true
  try {
    students.value = await fetchStudents()
  } catch (error) {
    message.value = "学生列表加载失败"
  } finally {
    studentLoading.value = false
}
}

function getErrorMessage(detail: unknown) {
  if (detail === "Not authenticated") {
    return "请先登录"
  }

  if (typeof detail === "string") {
    return detail
  }

  return "请求失败"
}

// 前端输入学生与成绩，后端添加，然后显示到界面
async function addStudent(student: StudentInput) {
  addLoading.value = true
 
  try {
    const response = await createStudent(student.name, student.score)
  
    if (response.ok) {
      message.value = "添加成功"
      await loadStudents()
      await loadStats()
    } else {
     const data = await response.json()
      message.value = data.detail || "添加失败"
    }
  } finally {
    addLoading.value = false
  }
}

//从后端删除一个学生 并显示所有学生
async function deleteStudent(name: string) {
  deleteLoadingName.value = name
  try {
    const response = await removeStudent(name)
    if (response.ok) {
      message.value = "删除成功"
      await loadStudents()
      await loadStats()
    } else {
      const data = await response.json()
      message.value = data.detail || "删除失败"
    }
  } finally {
    deleteLoadingName.value = ""
  }
}

//修改一个学生 并显示所以学生
async function updateStudent(student: StudentInput) {
  updateLoadingName.value = student.name
  
  try {
    const response = await updateStudentScore(student.name, student.score)
    if (response.ok) {
      message.value = "修改成功"
      await loadStudents()
      await loadStats()
    } else {
      const data = await response.json()
      message.value = data.detail || "修改失败"
    }
  } finally {
    updateLoadingName.value = ""
  }
}

//统计学生数据
async function loadStats() {
  const response = await fetchStats()
  const data = await response.json()

  if (response.ok) {
    stats.value = data
    message.value = "统计加载成功"
  } else {
    stats.value = null
    message.value = getErrorMessage(data.detail)
  }
}

onMounted(() => {
  loadStudents()
})

</script>


<template>
    <div>
        <h1>学生成绩管理系统</h1> 

        <StudentForm
          v-if="authStore.isAdmin()"
          :loading="addLoading"
          @add-student= "addStudent" 
        />

        <button @click="loadStudents">加载学生列表</button>
        
        <p>{{ message }}</p>

        <p v-if="studentLoading">学生列表加载中...</p>

        <p v-else-if="Object.keys(students).length === 0">暂无学生</p>

        <StudentList
            :students="students"
            :update-loading-name="updateLoadingName"
            :delete-loading-name="deleteLoadingName"
            :can-edit="authStore.isAdmin()"
            @update-student="updateStudent"
            @delete-student="deleteStudent"
        />

        <StatsPanel :stats="stats" @load-stats="loadStats" />
    </div>
</template>


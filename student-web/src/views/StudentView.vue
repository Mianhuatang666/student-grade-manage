<script setup lang="ts">
import { ref, onMounted } from "vue"
import { StudentInput, StudentWithClass, StudentMap, Stats, ClassItem} from "../types"
import StudentForm from "../components/StudentForm.vue"
import StudentList from "../components/StudentList.vue"
import StatsPanel from "../components/StatsPanel.vue"
import {
  fetchStudents,
  fetchStudentsWithClass,
  createStudent,
  updateStudentScore,
  removeStudent,
  fetchStats,
  fetchClasses
} from "../api/students"
import { useAuthStore } from "../stores/authStore.js"
import { getErrorMessage } from "../api/request"

const students = ref<StudentWithClass[]>([])
const message = ref("")
const stats = ref<Stats | null>(null)
const classes = ref<ClassItem[]>([])
const addLoading =ref(false)
const studentLoading = ref(false)
const updateLoadingName = ref("")
const deleteLoadingName = ref("")
const authStore = useAuthStore()

// 从后端获取所有学生，并显示到界面
async function loadStudents(){
  studentLoading.value = true
  try {
    students.value = await fetchStudentsWithClass()
  } catch (error) {
    message.value = "学生列表加载失败"
  } finally {
    studentLoading.value = false
}
}

async function loadClasses() {
  const response = await fetchClasses()
  const data = await response.json()

  if(response.ok) {
    classes.value = data
  } else {
    message.value = await getErrorMessage(response)
  }
}

// 前端输入学生与成绩，后端添加，然后显示到界面
async function addStudent(student: StudentInput) {
  addLoading.value = true
 
  try {
    const response = await createStudent(student.name, student.score, student.class_id)
  
    if (response.ok) {
      message.value = "添加成功"
      await loadStudents()
      await loadStats()
    } else {
      message.value = await getErrorMessage(response)
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
      message.value = await getErrorMessage(response)
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
      message.value = await getErrorMessage(response)
    }
  } finally {
    updateLoadingName.value = ""
  }
}

//统计学生数据
async function loadStats() {
  const response = await fetchStats()

  if (response.ok) {
    const data = await response.json()
    stats.value = data
    message.value = "统计加载成功"
  } else {
    stats.value = null
    message.value = await getErrorMessage(response)
  }
}

onMounted(() => {
  loadStudents()
  loadClasses()
})

</script>


<template>
    <div>
        <h1>学生成绩管理系统</h1> 

        <StudentForm
          v-if="authStore.isAdmin()"
          :loading="addLoading"
          :classes="classes"
          @add-student= "addStudent" 
        />
        <div>
          <h2>班级列表</h2>
          <ul>
            <li v-for="classItem in classes" :key="classItem.id">
              {{ classItem.id }} - {{ classItem.name }}
            </li>
          </ul>
        </div>
        <button @click="loadStudents">加载学生列表</button>
        
        <p>{{ message }}</p>

        <p v-if="studentLoading">学生列表加载中...</p>

        <p v-else-if="students.length === 0">暂无学生</p>

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


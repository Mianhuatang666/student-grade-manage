<script setup lang="ts">
import { ref, onMounted, computed } from "vue"
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
const selectedClassId = ref("")
const page = ref(1)
const pageSize = ref(5)
const authStore = useAuthStore()
const keyword = ref("")
const total = ref(0)

const totalPages = computed(() => {
  return Math.ceil(total.value / pageSize.value)
})

// 从后端获取所有学生，并显示到界面
async function loadStudents() {
  const classId = selectedClassId.value === ""
    ? undefined
    : Number(selectedClassId.value)
  
  const data = await fetchStudentsWithClass(
    classId, 
    keyword.value,
    page.value,
    pageSize.value)

  students.value = data.items
  total.value = data.total
  message.value = "学生列表加载成功"
}

async function prevPage() {
  if(page.value <= 1) {
    return
  }

  page.value -= 1
  await loadStudents()
  
}

async function nextPage() {
  page.value += 1
  await loadStudents()
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

async function searchStudents() {
  page.value = 1
  await loadStudents()
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
          <label>按班级筛选：</label>

          <select v-model="selectedClassId">
            <option value="">全部班级</option>
            <option
              v-for="classItem in classes"
              :key="classItem.id"
              :value="classItem.id"
            >
              {{ classItem.name }}
            </option>
          </select>
          <input
            v-model="keyword"
            placeholder="请输入学生姓名"
          />
          
          <button @click="searchStudents">查询</button>
        </div>
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
        <div>
          <button :disabled="page <= 1" @click="prevPage">上一页</button>

          <span>当前第 {{ page }} / {{ totalPages }} 页,共 {{  total }} 条
          </span>

          <button :disabled="page >= totalPages" @click="nextPage">下一页</button>
        </div>

        <StatsPanel :stats="stats" @load-stats="loadStats" />
    </div>
</template>


<script setup lang="ts">
import { ref } from "vue"
import type { StudentInput, StudentWithClass } from "../types"
const props = defineProps<{
  students: StudentWithClass[]
  updateLoadingName: string
  deleteLoadingName: string
  canEdit: boolean
}>()

const emit = defineEmits<{
  "update-student": [student: StudentInput]
  "delete-student": [name: string]
}>()
const editScores = ref<Record<string, string>>({})

function submitUpdate(name: string) {
  const scoreText = editScores.value[name] || ""
  const score = Number(scoreText)

  if(scoreText.trim() === ""){
    alert("新成绩不能为空")
    return
  }

  if(Number.isNaN(score)){
    alert("新成绩必须是数字")
    return
  }

  if(score < 0 || score > 100){
    alert("新成绩必须在0 到 100 之间")
    return
  }

  emit("update-student", {
    name: name,
    score: score
  })

  editScores.value[name] = ""
}
</script>

<template>
  <ul>
    <li v-for="student in students" :key="student.name">
      {{ student.name }}: {{ student.score }}
      班级: {{  student.class_name ?? "未分班" }}

      <template v-if="canEdit">
        <input
          v-model="editScores[student.name]"
          placeholder="新成绩"
        />

        <button
          :disabled="updateLoadingName === student.name"
          @click="submitUpdate(student.name)"
        >
          {{ updateLoadingName === student.name ? "修改中" : "修改" }}
        </button>

        <button
          :disabled="deleteLoadingName === student.name"
          @click="emit('delete-student', student.name)"
        >
          {{ deleteLoadingName === student.name ? "删除中" : "删除" }}
        </button>
      </template>
    </li>
  </ul>
</template>

<style scoped>
li {
  margin: 8px 0;
}

li button {
  margin-left: 12px;
}

li input {
  width: 80px;
  margin-left: 12px;
  margin-right: 8px;
  padding: 8px;
}
</style>

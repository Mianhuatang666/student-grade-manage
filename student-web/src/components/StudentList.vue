<script setup lang="ts">
import { ref } from "vue"
import type { StudentInput, StudentMap } from "../types"
const props = defineProps<{
  students: StudentMap
  updateLoadingName: string
  deleteLoadingName: string
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
    <li v-for="(score, name) in students" :key="name">
      {{ name }}: {{ score }}

      <input
        v-model="editScores[name]"
        placeholder="新成绩"
      />

      <button 
        :disabled="updateLoadingName === name"
        @click="submitUpdate(name)"
      >
        {{  updateLoadingName === name ? "修改中" : "修改" }}
      </button>

      <button 
        :disabled="deleteLoadingName === name"
        @click="emit('delete-student', name)"
      >
        {{  deleteLoadingName === name ? "删除中" : "删除" }}
      </button>
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

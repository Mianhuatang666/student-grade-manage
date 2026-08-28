<script setup lang="ts">
import type { StudentInput, ClassItem } from "../types"
import { ref } from "vue"

const errorMessage = ref("")

defineProps<{
  loading: boolean
  classes: ClassItem[]
}>()

const emit = defineEmits<{
  "add-student": [student: StudentInput]
}>()

const newName = ref("")
const newScore = ref("")
const selectedClassId = ref("")


function submitStudent() {
  errorMessage.value = ""

  const score = Number(newScore.value)

  if(newName.value.trim() === ""){
    errorMessage.value = "姓名不能为空"
    return
  }

  if(newScore.value.trim() === ""){
    errorMessage.value = "成绩不能为空"
    return
  }

  if(Number.isNaN(score)){
    errorMessage.value = "成绩必须是数字"
    return
  }

  if(score < 0 || score > 100){
    errorMessage.value = "成绩必须在 0 到 100 之间"
    return
  }

  emit("add-student", {
    name: newName.value,
    score: score,
    class_id: selectedClassId.value === "" ? null : Number(selectedClassId.value)
  })

  newName.value = ""
  newScore.value = ""
  selectedClassId.value = ""
}
</script>

<template>
  <div class="form">
    <input v-model="newName" placeholder="请输入姓名" />
    <input v-model="newScore" placeholder="请输入成绩" />
    <select v-model="selectedClassId">
      <option value="">请选择班级</option>
      <option
        v-for="classItem in classes"
        :key="classItem.id"
        :value="classItem.id"
      >
        {{ classItem.name }}
      </option>
    </select>
    <button :disabled="loading" @click="submitStudent">
      {{  loading ? "添加中..." : "添加学生" }}
    </button>
    <p v-if="errorMessage" class="error">{{  errorMessage  }}</p>
  </div>
</template>

<style scoped>
.form {
  margin-bottom: 16px;
}

.error {
  color: red;
  margin-top: 8px;
}

input {
  padding: 8px;
  margin-right: 8px;
}

button:disabled{
  cursor: not-allowed;
  opacity: 0.6;
}
</style>

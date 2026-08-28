<script setup lang="ts">
import type { Stats } from "../types"
defineProps<{
  stats: Stats | null
}>()

const emit = defineEmits(["load-stats"])
</script>

<template>
  <div class="stats">
    <button @click="emit('load-stats')">查看统计</button>

    <div v-if="stats">
      <p>平均分：{{ stats.average }}</p>
      <p>最高分：{{ stats.max_score }}，学生：{{ stats.max_student }}</p>
      <p>最低分：{{ stats.min_score }}，学生：{{ stats.min_student }}</p>
    </div>
  </div>
</template>

<style scoped>
.stats {
  margin-top: 20px;
}
</style>

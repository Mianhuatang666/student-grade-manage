<script setup lang="ts">
import { useRouter } from "vue-router"
import { useAuthStore } from "./stores/authStore"

const router = useRouter()
const authStore = useAuthStore()
function logout() {
  authStore.clearToken()
  router.push("/login")
}
</script>

<template>
<div class="page">
  <nav>
    <RouterLink to="/">首页</RouterLink>
    <RouterLink to="/students">学生管理</RouterLink>
    <RouterLink to="/login">登录</RouterLink>
    <button @click="logout">退出登录</button>
  </nav>
  
  <RouterView />
</div>
</template>

<style scoped>
.page {
  max-width: 800px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}

nav {
  display: flex;
  gap: 16px;
  margin-bottom: 24px;
}
</style>

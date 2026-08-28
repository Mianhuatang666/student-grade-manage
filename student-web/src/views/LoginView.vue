<script setup lang="ts">
import { ref } from "vue"
import { useRouter } from "vue-router"
import { login } from "../api/students"
import { useAuthStore } from "../stores/authStore"

const router = useRouter()
const authStore = useAuthStore()

const username = ref("")
const password = ref("")
const message = ref("")

async function submitLogin() {
    if (username.value.trim() === "") {
        message.value = "用户名不能为空"
        return
    }

    if (password.value.trim() === "") {
        message.value = "密码不能为空"
        return
    }

    try {
        message.value = "登录中..."

        const response = await login(username.value.trim(), password.value)
        const data = await response.json()

        if(response.ok) {
            //localStorage.setItem("token", data.access_token)
            authStore.setToken(data.access_token)
            message.value = "登录成功"
            router.push("/students")
        } else {
            message.value = data.detail
        }
    } catch (error) {
        message.value = "登录请求失败，请确认后端已启动"
    }
}
</script>

<template>
    <div>
        <h1>登录</h1>

        <input v-model="username" placeholder="用户名" />
        <input v-model="password" type="password" placeholder="密码" />
        <button @click="submitLogin">登录</button>

        <p>{{ message }}</p>
    </div>
</template>

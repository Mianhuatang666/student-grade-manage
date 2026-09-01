import router from "../router"
import { useAuthStore } from "../stores/authStore"

export const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000"

export async function request(path, options = {}) {
  const authStore = useAuthStore()

  const headers = {
    ...(options.headers || {})
  }

  if (authStore.token) {
    headers.Authorization = `Bearer ${authStore.token}`
  }

  let response
  try {
    response = await fetch(`${API_BASE}${path}`, {
      ...options,
      headers
    })
  } catch {
    throw new Error("请求失败，请确认后端服务已启动")
  }

  if (response.status === 401) {
    authStore.clearToken()
    router.push("/login")
  }

  return response
}

export async function getErrorMessage(response) {
  if (response.status === 401) {
    return "登录已失效，请重新登录"
  }

  if (response.status === 403) {
    return "权限不足，无法执行该操作"
  }

  if (response.status === 500) {
    return "服务器错误，请稍后重试"
  }

  try {
    const data = await response.json()

    if (typeof data.detail === "string") {
      return data.detail
    }

    if (Array.isArray(data.detail)) {
      return data.detail[0]?.msg || "请求参数错误"
    }

    return "请求失败"
  } catch {
    return "请求失败"
  }
}
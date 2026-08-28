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

  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers
  })

  if (response.status === 401) {
    authStore.clearToken()
    router.push("/login")
  }

  return response
}

export async function getErrorMessage(response) {
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
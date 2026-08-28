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

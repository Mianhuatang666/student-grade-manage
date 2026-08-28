import { defineStore } from "pinia"
import { ref } from "vue"
import { jwtDecode }from "jwt-decode"

export const useAuthStore = defineStore("auth", () => {
  const token = ref(localStorage.getItem("token") || "")

  function setToken(newToken) {
    token.value = newToken
    localStorage.setItem("token", newToken)
  }

  function clearToken() {
    token.value = ""
    localStorage.removeItem("token")
  }

  function isLoggedIn() {
    return token.value !== ""
  }

  function getRole() {
    if(token.value === "") {
      return ""
    }

    try {
      const payload = jwtDecode(token.value)
      return payload.role || ""
    } catch {
      return ""
    }
  }

  function isAdmin() {
    return getRole() === "admin"
  }
  return {
    token,
    setToken,
    clearToken,
    isLoggedIn,
    getRole,
    isAdmin
  }
})
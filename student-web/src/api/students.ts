import type { StudentMap } from "../types"
import { API_BASE, request } from "./request"

export async function fetchStudents(): Promise<StudentMap> {
  const response = await request("/students")
  return response.json()
}

export async function createStudent(name: string, score: number): Promise<Response> {
  return request("/students", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: name,
      score: score
    })
  })
}

export async function updateStudentScore(name: string, score: number): Promise<Response> {
  return request(`/students/${name}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      score: score
    })
  })
}


export async function removeStudent(name: string): Promise<Response> {
  return request(`/students/${name}`, {
    method: "DELETE"
  })

}

export async function fetchStats(): Promise<Response> {
  return request("/stats")
}

export async function login(username: string, password: string): Promise<Response> {
  const formData = new URLSearchParams()

  formData.append("username", username)
  formData.append("password",password)

  return fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded"
    },
    body: formData
  })
}

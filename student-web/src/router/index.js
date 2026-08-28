import { createRouter, createWebHistory} from "vue-router"

import HomeView from "../views/HomeView.vue"
import StudentView from "../views/StudentView.vue"
import LoginView from "../views/LoginView.vue"
import { useAuthStore } from "../stores/authStore.js"

const routes = [
    {
        path: "/",
        component: HomeView
    },
    {
        path: "/students",
        component: StudentView,
        meta:{
            requiresAuth: true
        }
    },
    {
        path: "/login",
        component: LoginView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

router.beforeEach((to) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isLoggedIn()) {
    return "/login"
  }
})

export default router
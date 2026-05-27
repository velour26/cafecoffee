import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/auth'

export const useAuthStore = defineStore('auth', () => {
  const user = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const isAuthenticated = computed(() => !!user.value)
  const isAdmin = computed(() => user.value?.role?.name === 'admin')
  const isCustomer = computed(() => user.value?.role?.name === 'customer')

  async function login(email, password) {
    loading.value = true
    error.value = null
    try {
      const response = await authApi.login({ email, password })
      localStorage.setItem('access_token', response.data.access_token)
      await fetchCurrentUser()
      return { success: true }
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка входа'
      return { success: false, message: error.value }
    } finally {
      loading.value = false
    }
  }

  async function register(data) {
    loading.value = true
    error.value = null
    try {
      await authApi.register(data)
      return { success: true }
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка регистрации'
      return { success: false, message: error.value }
    } finally {
      loading.value = false
    }
  }

  async function fetchCurrentUser() {
    const token = localStorage.getItem('access_token')
    if (!token) return

    try {
      const response = await authApi.me()
      user.value = response.data
    } catch {
      localStorage.removeItem('access_token')
      user.value = null
    }
  }

  function logout() {
    localStorage.removeItem('access_token')
    user.value = null
  }

  return {
    user,
    loading,
    error,
    isAuthenticated,
    isAdmin,
    isCustomer,
    login,
    register,
    fetchCurrentUser,
    logout,
  }
})

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { cartApi } from '@/api/cart'
import { useAuthStore } from './auth'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const total = ref(0)
  const loading = ref(false)
  const error = ref(null)

  const itemCount = computed(() =>
    items.value.reduce((sum, item) => sum + item.quantity, 0)
  )
  const isEmpty = computed(() => items.value.length === 0)

  async function fetchCart() {
    const authStore = useAuthStore()
    if (!authStore.isAuthenticated) return

    loading.value = true
    try {
      const response = await cartApi.getCart()
      items.value = response.data.items
      total.value = response.data.total
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка загрузки корзины'
    } finally {
      loading.value = false
    }
  }

  async function addToCart(menuItemId, quantity = 1) {
    try {
      await cartApi.addItem({ menu_item_id: menuItemId, quantity })
      await fetchCart()
      return { success: true }
    } catch (err) {
      const message = err.response?.data?.detail || 'Ошибка добавления в корзину'
      return { success: false, message }
    }
  }

  async function updateItem(itemId, quantity) {
    try {
      await cartApi.updateItem(itemId, { quantity })
      await fetchCart()
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка обновления корзины'
    }
  }

  async function removeItem(itemId) {
    try {
      await cartApi.removeItem(itemId)
      await fetchCart()
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка удаления из корзины'
    }
  }

  async function clearCart() {
    try {
      await cartApi.clearCart()
      items.value = []
      total.value = 0
    } catch (err) {
      error.value = err.response?.data?.detail || 'Ошибка очистки корзины'
    }
  }

  function $reset() {
    items.value = []
    total.value = 0
    error.value = null
  }

  return {
    items,
    total,
    loading,
    error,
    itemCount,
    isEmpty,
    fetchCart,
    addToCart,
    updateItem,
    removeItem,
    clearCart,
    $reset,
  }
})

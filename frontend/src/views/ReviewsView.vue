<template>
  <div style="background:#fff;min-height:100vh">

    <div style="background:#fff;border-bottom:1px solid #f0f0f0">
      <div class="max-w-7xl mx-auto px-6 py-14">
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Кофеёчек</p>
        <div class="flex items-end justify-between flex-wrap gap-4">
          <h1 class="font-black leading-none" style="font-size:clamp(2.5rem,5vw,4rem);color:#0a0a0a">Отзывы</h1>
          <div v-if="!loading && reviews.length" class="flex items-center gap-6 mb-2">
            <div class="text-right">
              <div class="flex items-center gap-1 justify-end mb-1">
                <svg v-for="i in 5" :key="i" width="16" height="16" viewBox="0 0 24 24"
                  :fill="i <= Math.round(avgRating) ? '#c1ce56' : 'none'"
                  :stroke="i <= Math.round(avgRating) ? '#c1ce56' : '#ddd'"
                  stroke-width="1.5"
                >
                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                </svg>
              </div>
              <p class="text-xs" style="color:#aaa">
                <span style="color:#0a0a0a;font-weight:700">{{ avgRating.toFixed(1) }}</span>
                из 5 · {{ reviews.length }} отзывов
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-12">
      <div class="flex flex-col lg:flex-row gap-12">

        <div class="flex-1 min-w-0">

          <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div v-for="i in 4" :key="i" class="animate-pulse" style="background:#f5f5f5;border:1px solid #eee;height:180px"></div>
          </div>

          <div v-else-if="reviews.length" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <ReviewCard v-for="review in reviews" :key="review.id" :review="review" />
          </div>

          <div v-else class="flex flex-col items-center justify-center py-24 gap-6">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5" stroke-linecap="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            <div class="text-center">
              <p class="font-bold mb-2" style="color:#0a0a0a">Отзывов пока нет</p>
              <p class="text-sm" style="color:#aaa">Будьте первым!</p>
            </div>
          </div>
        </div>

        <aside class="lg:w-80 shrink-0">
          <div class="sticky top-24">

            <template v-if="!authStore.isAuthenticated">
              <div style="border:1px solid #f0f0f0;background:#fafafa" class="p-6">
                <p class="text-xs font-bold uppercase tracking-[0.2em] mb-3" style="color:#bbb">Оставить отзыв</p>
                <p class="text-sm mb-4" style="color:#888">Войдите в аккаунт, чтобы оставить отзыв</p>
                <RouterLink
                  to="/login"
                  class="block w-full py-3 text-xs font-bold uppercase tracking-widest text-center transition-opacity hover:opacity-85"
                  style="background:#c1ce56;color:#0a0a0a"
                >Войти</RouterLink>
              </div>
            </template>

            <template v-else-if="ordersLoading">
              <div style="border:1px solid #f0f0f0" class="p-6">
                <div class="animate-pulse space-y-3">
                  <div style="background:#f0f0f0;height:14px;width:60%"></div>
                  <div style="background:#f0f0f0;height:40px"></div>
                  <div style="background:#f0f0f0;height:80px"></div>
                  <div style="background:#f0f0f0;height:40px"></div>
                </div>
              </div>
            </template>

            <template v-else-if="!orderedItems.length">
              <div style="border:1px solid #f0f0f0;background:#fafafa" class="p-6">
                <p class="text-xs font-bold uppercase tracking-[0.2em] mb-3" style="color:#bbb">Оставить отзыв</p>
                <div class="flex flex-col items-center py-4 gap-3 text-center">
                  <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="1.5" stroke-linecap="round">
                    <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
                    <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
                  </svg>
                  <p class="text-sm font-bold" style="color:#0a0a0a">Нет заказов</p>
                  <p class="text-xs leading-relaxed" style="color:#aaa">Отзыв можно оставить только на позиции, которые вы заказывали. Сначала сделайте заказ.</p>
                  <RouterLink
                    to="/menu"
                    class="mt-1 text-xs font-bold uppercase tracking-widest px-5 py-2.5 transition-opacity hover:opacity-85"
                    style="background:#c1ce56;color:#0a0a0a"
                  >Перейти в меню</RouterLink>
                </div>
              </div>
            </template>

            <template v-else>
              <div style="border:1px solid #f0f0f0" class="p-6">
                <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#bbb">Оставить отзыв</p>

                <div v-if="successMsg" class="py-6 text-center">
                  <div class="w-10 h-10 mx-auto mb-3 flex items-center justify-center" style="background:#c1ce56">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
                  </div>
                  <p class="text-sm font-bold mb-1" style="color:#0a0a0a">Отзыв опубликован!</p>
                  <p class="text-xs" style="color:#aaa">Спасибо за ваш отзыв</p>
                  <button
                    @click="successMsg = false"
                    class="mt-4 text-xs font-bold uppercase tracking-widest px-5 py-2 transition-opacity hover:opacity-85"
                    style="background:#0a0a0a;color:#fff"
                  >Написать ещё</button>
                </div>

                <form v-else @submit.prevent="handleSubmit" class="flex flex-col gap-4">
                  <div>
                    <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Позиция</label>
                    <select
                      v-model="form.menu_item_id"
                      required
                      class="w-full px-3 py-2.5 text-sm outline-none transition-all duration-200"
                      style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a;appearance:none"
                      @focus="e => e.target.style.borderColor='#0a0a0a'"
                      @blur="e => e.target.style.borderColor='#e8e8e8'"
                    >
                      <option :value="null" disabled>Выберите позицию</option>
                      <option v-for="item in orderedItems" :key="item.id" :value="item.id">
                        {{ item.name }}
                      </option>
                    </select>
                  </div>

                  <div>
                    <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Оценка</label>
                    <div class="flex items-center gap-1">
                      <button
                        v-for="i in 5"
                        :key="i"
                        type="button"
                        @click="form.rating = i"
                        @mouseenter="hoverRating = i"
                        @mouseleave="hoverRating = 0"
                        class="p-0.5 transition-transform hover:scale-110"
                      >
                        <svg width="28" height="28" viewBox="0 0 24 24"
                          :fill="i <= (hoverRating || form.rating) ? '#c1ce56' : 'none'"
                          :stroke="i <= (hoverRating || form.rating) ? '#c1ce56' : '#ddd'"
                          stroke-width="1.5"
                        >
                          <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                        </svg>
                      </button>
                      <span class="text-xs ml-1" style="color:#aaa">{{ ratingLabel }}</span>
                    </div>
                  </div>

                  <div>
                    <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Комментарий <span style="color:#ccc;font-weight:400">(необязательно)</span></label>
                    <textarea
                      v-model="form.text"
                      rows="3"
                      placeholder="Поделитесь впечатлениями..."
                      class="w-full px-3 py-2.5 text-sm outline-none transition-all duration-200 resize-none"
                      style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
                      @focus="e => e.target.style.borderColor='#0a0a0a'"
                      @blur="e => e.target.style.borderColor='#e8e8e8'"
                    ></textarea>
                  </div>

                  <p v-if="formError" class="text-xs" style="color:#e53e3e">{{ formError }}</p>

                  <button
                    type="submit"
                    :disabled="!form.rating || !form.menu_item_id || submitting"
                    class="w-full py-3 text-xs font-bold uppercase tracking-widest transition-opacity"
                    style="background:#c1ce56;color:#0a0a0a"
                    :style="(!form.rating || !form.menu_item_id || submitting) ? 'opacity:0.4;cursor:not-allowed' : 'opacity:1'"
                  >
                    {{ submitting ? '—' : 'Опубликовать' }}
                  </button>
                </form>
              </div>
            </template>

          </div>
        </aside>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { reviewsApi } from '@/api/reviews'
import { ordersApi } from '@/api/orders'
import { useAuthStore } from '@/stores/auth'
import ReviewCard from '@/components/ReviewCard.vue'

const authStore = useAuthStore()

const reviews = ref([])
const loading = ref(false)

const orderedItems = ref([])
const ordersLoading = ref(false)

const hoverRating = ref(0)
const submitting = ref(false)
const successMsg = ref(false)
const formError = ref('')

const form = ref({ menu_item_id: null, rating: 0, text: '' })

const avgRating = computed(() => {
  if (!reviews.value.length) return 0
  return reviews.value.reduce((sum, r) => sum + r.rating, 0) / reviews.value.length
})

const ratingLabel = computed(() => {
  const labels = { 1: 'Плохо', 2: 'Так себе', 3: 'Нормально', 4: 'Хорошо', 5: 'Отлично' }
  return labels[hoverRating.value || form.value.rating] || ''
})

async function fetchReviews() {
  loading.value = true
  try {
    const r = await reviewsApi.getAll({ limit: 100 })
    reviews.value = r.data
  } finally {
    loading.value = false
  }
}

async function fetchOrderedItems() {
  if (!authStore.isAuthenticated) return
  ordersLoading.value = true
  try {
    const r = await ordersApi.getMy({ limit: 100 })
    const orders = r.data
    const seen = new Set()
    const items = []
    for (const order of orders) {
      for (const oi of order.items || []) {
        if (oi.menu_item_id && !seen.has(oi.menu_item_id)) {
          seen.add(oi.menu_item_id)
          items.push({ id: oi.menu_item_id, name: oi.item_name })
        }
      }
    }
    orderedItems.value = items
  } catch {
    orderedItems.value = []
  } finally {
    ordersLoading.value = false
  }
}

async function handleSubmit() {
  if (!form.value.rating || !form.value.menu_item_id) return
  submitting.value = true
  formError.value = ''
  try {
    await reviewsApi.create({
      menu_item_id: form.value.menu_item_id,
      rating: form.value.rating,
      text: form.value.text || null,
    })
    successMsg.value = true
    form.value = { menu_item_id: null, rating: 0, text: '' }
    await fetchReviews()
  } catch (err) {
    formError.value = err.response?.data?.detail || 'Ошибка при публикации'
  } finally {
    submitting.value = false
  }
}

onMounted(() => {
  fetchReviews()
  fetchOrderedItems()
})
</script>

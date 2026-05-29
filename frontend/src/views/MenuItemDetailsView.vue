<template>
  <div style="background:#fff;min-height:100vh">

    <div v-if="loading">
      <div style="background:#fff;border-bottom:1px solid #f0f0f0">
        <div class="max-w-7xl mx-auto px-6 py-14">
          <div class="animate-pulse space-y-4">
            <div style="background:#f0f0f0;height:12px;width:120px"></div>
            <div style="background:#f0f0f0;height:52px;width:300px"></div>
          </div>
        </div>
      </div>
      <div class="max-w-7xl mx-auto px-6 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
          <div class="animate-pulse" style="background:#f5f5f5;height:500px"></div>
          <div class="animate-pulse space-y-4 pt-4">
            <div style="background:#f0f0f0;height:14px;width:100px"></div>
            <div style="background:#f0f0f0;height:40px;width:80%"></div>
            <div style="background:#f0f0f0;height:16px"></div>
            <div style="background:#f0f0f0;height:16px;width:90%"></div>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="!item" class="flex flex-col items-center justify-center py-40 gap-6">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5" stroke-linecap="round">
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>
      <p class="font-bold text-lg" style="color:#0a0a0a">Позиция не найдена</p>
      <RouterLink
        to="/menu"
        class="text-xs font-bold uppercase tracking-widest px-6 py-3 transition-opacity hover:opacity-85"
        style="background:#c1ce56;color:#0a0a0a"
      >Вернуться к меню</RouterLink>
    </div>

    <template v-else>
      <div style="background:#fff;border-bottom:1px solid #f0f0f0">
        <div class="max-w-7xl mx-auto px-6 py-14">
          <div class="flex items-center gap-2 mb-5">
            <RouterLink
              to="/menu"
              class="text-xs font-bold uppercase tracking-[0.2em] transition-colors"
              style="color:#c1ce56"
              @mouseenter="e => e.currentTarget.style.opacity='0.7'"
              @mouseleave="e => e.currentTarget.style.opacity='1'"
            >Меню</RouterLink>
            <span style="color:#ddd">—</span>
            <span v-if="item.category" class="text-xs uppercase tracking-[0.2em]" style="color:#bbb">{{ item.category.name }}</span>
          </div>
          <h1 class="font-black leading-none" style="font-size:clamp(2rem,4vw,3.5rem);color:#0a0a0a">{{ item.name }}</h1>
        </div>
      </div>

      <div class="max-w-7xl mx-auto px-6 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 mb-20">

          <div class="relative overflow-hidden" style="background:#f5f5f3">
            <img
              v-if="item.image_url && !imageError"
              :src="getImageUrl(item.image_url)"
              :alt="item.name"
              class="w-full object-cover"
              style="height:520px;filter:brightness(0.9)"
              @error="imageError = true"
            />
            <div v-else class="w-full flex items-center justify-center" style="height:520px;background:#f0f0ee">
              <svg width="80" height="96" viewBox="0 0 80 96" fill="none" style="opacity:.1">
                <path d="M10 32 L16 84 H64 L70 32 Z" fill="none" stroke="#000" stroke-width="2"/>
                <ellipse cx="40" cy="32" rx="30" ry="8" fill="none" stroke="#000" stroke-width="2"/>
                <path d="M64 47 Q80 47 80 57 Q80 67 64 67" stroke="#000" stroke-width="2" fill="none"/>
              </svg>
            </div>

            <div
              v-if="!item.is_available"
              class="absolute inset-0 flex items-center justify-center"
              style="background:rgba(0,0,0,.55)"
            >
              <span class="text-xs font-bold uppercase tracking-widest px-4 py-2" style="border:1px solid #2a2420;color:#2a2420">
                Временно недоступно
              </span>
            </div>

            <span
              v-if="item.category"
              class="absolute top-5 left-5 text-xs font-bold uppercase tracking-wider px-3 py-1.5"
              style="background:rgba(255,255,255,.9);color:#888;backdrop-filter:blur(4px)"
            >{{ item.category.name }}</span>
          </div>

          <div class="flex flex-col justify-between gap-8 lg:py-4">
            <div>
              <div class="flex items-baseline gap-5 mb-6">
                <span class="font-black" style="font-size:2.5rem;color:#c1ce56;line-height:1">
                  {{ formatPrice(item.price) }}
                </span>
                <span v-if="item.weight_grams" class="text-sm" style="color:#bbb">{{ item.weight_grams }} г</span>
              </div>

              <p v-if="item.description" class="text-base leading-relaxed mb-8" style="color:#555;max-width:480px">
                {{ item.description }}
              </p>

              <div style="width:48px;height:2px;background:#c1ce56" class="mb-8"></div>

              <div class="flex flex-col gap-3">
                <div class="flex items-center gap-3">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                    <path d="M20 10c0 7-9 13-9 13S2 17 2 10a9 9 0 0 1 18 0z"/><circle cx="11" cy="10" r="2"/>
                  </svg>
                  <span class="text-sm" style="color:#888">{{ item.category?.name || 'Без категории' }}</span>
                </div>
                <div v-if="item.weight_grams" class="flex items-center gap-3">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                    <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
                  </svg>
                  <span class="text-sm" style="color:#888">Объём / вес: {{ item.weight_grams }} г</span>
                </div>
                <div class="flex items-center gap-3">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                    <polyline points="20 6 9 17 4 12"/>
                  </svg>
                  <span class="text-sm" :style="item.is_available ? 'color:#888' : 'color:#e53e3e'">
                    {{ item.is_available ? 'Доступно для заказа' : 'Временно недоступно' }}
                  </span>
                </div>
                <div v-if="avgRating > 0" class="flex items-center gap-3">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="#c1ce56" stroke="#c1ce56" stroke-width="1.5">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                  <span class="text-sm" style="color:#888">{{ avgRating.toFixed(1) }} из 5 ({{ reviews.length }} {{ reviewWord }})</span>
                </div>
              </div>
            </div>

            <div v-if="item.is_available">
              <div class="flex items-center gap-4 mb-4">
                <div class="flex items-center" style="border:1px solid #e8e8e8">
                  <button
                    @click="qty > 1 && qty--"
                    class="w-11 h-11 flex items-center justify-center text-lg font-bold transition-colors"
                    style="color:#aaa"
                    @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                    @mouseleave="e => e.currentTarget.style.color='#aaa'"
                  >−</button>
                  <span class="w-10 text-center font-bold text-sm" style="color:#0a0a0a">{{ qty }}</span>
                  <button
                    @click="qty++"
                    class="w-11 h-11 flex items-center justify-center text-lg font-bold transition-colors"
                    style="color:#aaa"
                    @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                    @mouseleave="e => e.currentTarget.style.color='#aaa'"
                  >+</button>
                </div>
                <span class="text-sm font-bold" style="color:#aaa">
                  Итого: <span style="color:#0a0a0a">{{ formatPrice(item.price * qty) }}</span>
                </span>
              </div>

              <button
                @click="handleAddToCart"
                :disabled="addingToCart"
                class="w-full py-4 text-xs font-bold uppercase tracking-widest transition-all duration-200"
                :style="addedToCart
                  ? 'background:#2a2420;color:#f7f3ee'
                  : 'background:#c1ce56;color:#0a0a0a'"
              >
                <span v-if="addingToCart">—</span>
                <span v-else-if="addedToCart">Добавлено в корзину</span>
                <span v-else>+ В корзину</span>
              </button>
            </div>
          </div>
        </div>

        <div style="border-top:1px solid #f0f0f0" class="pt-16">
          <div class="flex items-end justify-between mb-10">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Мнения гостей</p>
              <h2 class="font-black text-3xl" style="color:#0a0a0a">
                Отзывы
                <span v-if="reviews.length" class="text-base font-normal ml-2" style="color:#bbb">{{ reviews.length }}</span>
              </h2>
            </div>
            <div v-if="avgRating > 0" class="text-right mb-1">
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
                <span style="color:#0a0a0a;font-weight:700">{{ avgRating.toFixed(1) }}</span> из 5
              </p>
            </div>
          </div>

          <div class="flex flex-col lg:flex-row gap-12">
            <div class="flex-1 min-w-0">
              <div v-if="reviewsLoading" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div v-for="i in 4" :key="i" class="animate-pulse" style="background:#f5f5f5;height:160px"></div>
              </div>
              <div v-else-if="reviews.length" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <ReviewCard v-for="review in reviews" :key="review.id" :review="review" />
              </div>
              <div v-else class="flex flex-col items-center justify-center py-16 gap-4">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="1.5" stroke-linecap="round">
                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                </svg>
                <p class="text-sm" style="color:#bbb">Отзывов пока нет — будьте первым!</p>
              </div>
            </div>

            <div class="lg:w-72 shrink-0">
              <div class="sticky top-24">
                <div v-if="!authStore.isAuthenticated" style="border:1px solid #f0f0f0;background:#fafafa" class="p-6">
                  <p class="text-xs font-bold uppercase tracking-[0.2em] mb-3" style="color:#bbb">Ваш отзыв</p>
                  <p class="text-sm mb-4" style="color:#888">Войдите, чтобы оставить отзыв</p>
                  <RouterLink
                    to="/login"
                    class="block text-center py-3 text-xs font-bold uppercase tracking-widest transition-opacity hover:opacity-85"
                    style="background:#c1ce56;color:#0a0a0a"
                  >Войти</RouterLink>
                </div>

                <div v-else-if="reviewSuccess" style="border:1px solid #f0f0f0" class="p-6 text-center">
                  <div class="w-10 h-10 mx-auto mb-3 flex items-center justify-center" style="background:#c1ce56">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
                  </div>
                  <p class="text-sm font-bold mb-1" style="color:#0a0a0a">Отзыв опубликован!</p>
                  <p class="text-xs" style="color:#aaa">Спасибо за ваш отзыв</p>
                </div>

                <div v-else style="border:1px solid #f0f0f0" class="p-6">
                  <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#bbb">Ваш отзыв</p>
                  <form @submit.prevent="submitReview" class="flex flex-col gap-4">
                    <div>
                      <p class="text-xs font-bold uppercase tracking-[0.15em] mb-2" style="color:#888">Оценка</p>
                      <div class="flex items-center gap-1">
                        <button
                          v-for="i in 5"
                          :key="i"
                          type="button"
                          @click="reviewForm.rating = i"
                          @mouseenter="hoverRating = i"
                          @mouseleave="hoverRating = 0"
                          class="p-0.5 transition-transform hover:scale-110"
                        >
                          <svg width="26" height="26" viewBox="0 0 24 24"
                            :fill="i <= (hoverRating || reviewForm.rating) ? '#c1ce56' : 'none'"
                            :stroke="i <= (hoverRating || reviewForm.rating) ? '#c1ce56' : '#ddd'"
                            stroke-width="1.5"
                          >
                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                          </svg>
                        </button>
                      </div>
                    </div>

                    <div>
                      <p class="text-xs font-bold uppercase tracking-[0.15em] mb-2" style="color:#888">
                        Комментарий <span style="color:#ccc;font-weight:400">(необязательно)</span>
                      </p>
                      <textarea
                        v-model="reviewForm.text"
                        rows="3"
                        placeholder="Поделитесь впечатлениями..."
                        class="w-full px-3 py-2.5 text-sm outline-none resize-none transition-all duration-200"
                        style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
                        @focus="e => e.target.style.borderColor='#0a0a0a'"
                        @blur="e => e.target.style.borderColor='#e8e8e8'"
                      ></textarea>
                    </div>

                    <p v-if="reviewError" class="text-xs" style="color:#e53e3e">{{ reviewError }}</p>

                    <button
                      type="submit"
                      :disabled="!reviewForm.rating || submittingReview"
                      class="w-full py-3 text-xs font-bold uppercase tracking-widest transition-opacity"
                      style="background:#c1ce56;color:#0a0a0a"
                      :style="(!reviewForm.rating || submittingReview) ? 'opacity:0.4;cursor:not-allowed' : ''"
                    >
                      {{ submittingReview ? '—' : 'Опубликовать' }}
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { menuApi } from '@/api/menu'
import { reviewsApi } from '@/api/reviews'
import { useAuthStore } from '@/stores/auth'
import { useCartStore } from '@/stores/cart'
import { formatPrice, getImageUrl } from '@/utils/format'
import ReviewCard from '@/components/ReviewCard.vue'

const $route = useRoute()
const authStore = useAuthStore()
const cartStore = useCartStore()

const item = ref(null)
const loading = ref(false)
const imageError = ref(false)
const reviews = ref([])
const reviewsLoading = ref(false)

const qty = ref(1)
const addingToCart = ref(false)
const addedToCart = ref(false)

const reviewForm = ref({ rating: 0, text: '' })
const hoverRating = ref(0)
const submittingReview = ref(false)
const reviewError = ref('')
const reviewSuccess = ref(false)

const avgRating = computed(() => {
  if (!reviews.value.length) return 0
  return reviews.value.reduce((sum, r) => sum + r.rating, 0) / reviews.value.length
})

const reviewWord = computed(() => {
  const n = reviews.value.length
  if (n % 10 === 1 && n % 100 !== 11) return 'отзыв'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'отзыва'
  return 'отзывов'
})

async function fetchItem() {
  loading.value = true
  try {
    const r = await menuApi.getById($route.params.id)
    item.value = r.data
  } catch {
    item.value = null
  } finally {
    loading.value = false
  }
}

async function fetchReviews() {
  reviewsLoading.value = true
  try {
    const r = await menuApi.getReviews($route.params.id)
    reviews.value = r.data
  } catch {
    reviews.value = []
  } finally {
    reviewsLoading.value = false
  }
}

async function handleAddToCart() {
  if (!authStore.isAuthenticated) { return }
  addingToCart.value = true
  try {
    await cartStore.addToCart(item.value.id, qty.value)
    addedToCart.value = true
    setTimeout(() => { addedToCart.value = false }, 2500)
  } finally {
    addingToCart.value = false
  }
}

async function submitReview() {
  reviewError.value = ''
  submittingReview.value = true
  try {
    await reviewsApi.create({
      menu_item_id: item.value.id,
      rating: reviewForm.value.rating,
      text: reviewForm.value.text || null,
    })
    reviewSuccess.value = true
    reviewForm.value = { rating: 0, text: '' }
    await fetchReviews()
  } catch (err) {
    reviewError.value = err.response?.data?.detail || 'Ошибка при отправке'
  } finally {
    submittingReview.value = false
  }
}

onMounted(async () => {
  await fetchItem()
  fetchReviews()
})
</script>

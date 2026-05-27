<template>
  <div>
    <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Отзывы</h1>
        <span v-if="!loading && reviews.length" class="text-sm mb-0.5" style="color:#bbb">{{ reviews.length }} {{ reviewsWord }}</span>
      </div>
    </div>

    <div v-if="loading" class="flex flex-col gap-2">
      <div v-for="i in 6" :key="i" class="animate-pulse" style="background:#f5f5f3;height:72px;border:1px solid #f0f0f0"></div>
    </div>

    <div v-else style="background:#fff;border:1px solid #f0f0f0">
      <div v-if="reviews.length" class="overflow-x-auto">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="border-bottom:1px solid #f0f0f0">
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Автор</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Товар</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Оценка</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Комментарий</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Дата</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="review in reviews" :key="review.id" style="border-bottom:1px solid #f8f8f8">
              <td class="px-6 py-4">
                <p class="text-sm font-bold" style="color:#0a0a0a">{{ review.user?.full_name || '—' }}</p>
                <p class="text-xs mt-0.5" style="color:#bbb">{{ review.user?.email }}</p>
              </td>
              <td class="px-6 py-4 text-sm" style="color:#555;max-width:180px">
                <span class="block truncate">{{ review.menu_item?.name || '—' }}</span>
              </td>
              <td class="px-6 py-4">
                <div class="flex items-center gap-0.5">
                  <svg v-for="i in 5" :key="i" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke-width="1.5" stroke-linecap="round"
                    :fill="i <= review.rating ? '#c1ce56' : 'none'"
                    :stroke="i <= review.rating ? '#c1ce56' : '#ddd'"
                  >
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                  </svg>
                  <span class="text-xs font-bold ml-1" style="color:#888">{{ review.rating }}/5</span>
                </div>
              </td>
              <td class="px-6 py-4 text-sm" style="color:#888;max-width:240px">
                <span v-if="review.text" class="block truncate">{{ review.text }}</span>
                <span v-else class="italic" style="color:#ccc">нет комментария</span>
              </td>
              <td class="px-6 py-4 text-xs whitespace-nowrap" style="color:#bbb">{{ formatDate(review.created_at) }}</td>
              <td class="px-6 py-4">
                <button
                  @click="confirmDelete(review.id)"
                  class="flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider transition-colors"
                  style="color:#bbb"
                  @mouseenter="e => e.currentTarget.style.color='#e53e3e'"
                  @mouseleave="e => e.currentTarget.style.color='#bbb'"
                >
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
                    <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4h6v2"/>
                  </svg>
                  Удалить
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="px-6 py-14 text-center">
        <p class="text-sm font-bold" style="color:#bbb">Отзывов пока нет</p>
      </div>
    </div>

    <div v-if="deleteId" class="fixed inset-0 z-50 flex items-center justify-center px-4" style="background:rgba(0,0,0,0.5)" @click.self="deleteId = null">
      <div style="background:#fff;width:100%;max-width:360px">
        <div class="px-6 py-6">
          <p class="font-black text-base mb-2" style="color:#0a0a0a">Удалить отзыв?</p>
          <p class="text-sm" style="color:#888">Это действие нельзя отменить.</p>
        </div>
        <div class="flex" style="border-top:1px solid #f0f0f0">
          <button
            @click="deleteId = null"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-colors"
            style="color:#888;border-right:1px solid #f0f0f0"
            @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
            @mouseleave="e => e.currentTarget.style.color='#888'"
          >Отмена</button>
          <button
            @click="handleDelete"
            :disabled="deleting"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-opacity"
            style="color:#e53e3e"
            :style="deleting ? 'opacity:0.5' : ''"
          >{{ deleting ? '—' : 'Удалить' }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { reviewsApi } from '@/api/reviews'
import { formatDate } from '@/utils/format'

const reviews = ref([])
const loading = ref(false)
const deleteId = ref(null)
const deleting = ref(false)

const reviewsWord = computed(() => {
  const n = reviews.value.length
  if (n % 10 === 1 && n % 100 !== 11) return 'отзыв'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'отзыва'
  return 'отзывов'
})

async function fetchReviews() {
  loading.value = true
  try {
    const r = await reviewsApi.getAll({ limit: 200 })
    reviews.value = r.data
  } finally {
    loading.value = false
  }
}

function confirmDelete(id) { deleteId.value = id }

async function handleDelete() {
  deleting.value = true
  try {
    await reviewsApi.delete(deleteId.value)
    reviews.value = reviews.value.filter(r => r.id !== deleteId.value)
    deleteId.value = null
  } catch (err) {
    alert(err.response?.data?.detail || 'Ошибка при удалении')
  } finally {
    deleting.value = false
  }
}

onMounted(fetchReviews)
</script>

<template>
  <div style="background:#fff;min-height:100vh">

    <div style="background:#fff;border-bottom:1px solid #f0f0f0">
      <div class="max-w-7xl mx-auto px-6 py-14">
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Кофеёчек</p>
        <h1 class="font-black leading-none" style="font-size:clamp(2.5rem,5vw,4rem);color:#0a0a0a">Меню</h1>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-10">
      <div class="flex flex-col lg:flex-row gap-10">

        <aside class="lg:w-56 shrink-0">
          <div class="sticky top-24">
            <MenuFilterPanel
              :categories="categories"
              :initial-category="initialCategory"
              @filter="handleFilter"
            />
          </div>
        </aside>

        <div class="flex-1 min-w-0">

          <div class="flex items-center justify-between mb-8 min-h-[28px]">
            <span class="text-xs" style="color:#aaa">
              <template v-if="!loading">
                <span style="color:#c1ce56;font-weight:700">{{ total }}</span>
                <span> позиций</span>
              </template>
            </span>
            <button
              v-if="activeFilters"
              @click="resetFilters"
              class="flex items-center gap-2 text-xs transition-colors"
              style="color:#aaa"
              @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
              @mouseleave="e => e.currentTarget.style.color='#aaa'"
            >
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              Сбросить фильтры
            </button>
          </div>

          <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4">
            <div
              v-for="i in 6"
              :key="i"
              class="animate-pulse"
              style="background:#f5f5f5;border:1px solid #eee;height:300px"
            ></div>
          </div>

          <div v-else-if="items.length" class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4">
            <MenuItemCard
              v-for="item in items"
              :key="item.id"
              :item="item"
              :on-add-success="handleAddSuccess"
            />
          </div>

          <div v-else class="flex flex-col items-center justify-center py-32 gap-6">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ccc" stroke-width="1.5" stroke-linecap="round">
              <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
            </svg>
            <div class="text-center">
              <p class="font-bold mb-2" style="color:#0a0a0a">Ничего не найдено</p>
              <p class="text-sm" style="color:#aaa">Попробуйте изменить параметры поиска</p>
            </div>
            <button
              @click="resetFilters"
              class="text-xs font-bold uppercase tracking-widest px-6 py-3 transition-opacity hover:opacity-85"
              style="background:#c1ce56;color:#0a0a0a"
            >Сбросить фильтры</button>
          </div>

          <div v-if="hasMore && !loading" class="mt-12 text-center">
            <button
              @click="loadMore"
              :disabled="loadingMore"
              class="text-xs font-bold uppercase tracking-widest px-10 py-4 transition-all duration-200"
              style="border:1px solid #e8e8e8;color:#aaa"
              @mouseenter="e => { e.currentTarget.style.borderColor='#0a0a0a'; e.currentTarget.style.color='#0a0a0a' }"
              @mouseleave="e => { e.currentTarget.style.borderColor='#e8e8e8'; e.currentTarget.style.color='#aaa' }"
            >
              {{ loadingMore ? '—' : 'Показать ещё' }}
            </button>
          </div>

        </div>
      </div>
    </div>

    <div
      v-if="toastMsg"
      class="fixed bottom-8 left-1/2 -translate-x-1/2 px-6 py-3 text-xs font-bold uppercase tracking-widest z-50 transition-all duration-300"
      style="background:#c1ce56;color:#0a0a0a;pointer-events:none"
    >
      {{ toastMsg }}
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { menuApi } from '@/api/menu'
import { categoriesApi } from '@/api/categories'
import MenuItemCard from '@/components/MenuItemCard.vue'
import MenuFilterPanel from '@/components/MenuFilterPanel.vue'
import Loader from '@/components/Loader.vue'

const $route = useRoute()

const items = ref([])
const categories = ref([])
const loading = ref(false)
const loadingMore = ref(false)
const total = ref(0)
const currentFilters = ref({})
const skip = ref(0)
const LIMIT = 12
const toastMsg = ref('')
let toastTimer = null

const initialCategory = $route.query.category ? Number($route.query.category) : null

const activeFilters = computed(() => Object.keys(currentFilters.value).length > 0)
const hasMore = computed(() => items.value.length < total.value)

async function loadCategories() {
  try {
    const r = await categoriesApi.getAll()
    categories.value = r.data
  } catch {}
}

async function fetchItems(filters = {}, append = false) {
  if (!append) { loading.value = true; skip.value = 0 }
  else loadingMore.value = true
  try {
    const params = { ...filters, skip: append ? skip.value : 0, limit: LIMIT }
    const r = await menuApi.getItems(params)
    const data = r.data
    if (append) items.value.push(...(data.items || []))
    else items.value = data.items || []
    total.value = data.total || 0
    skip.value = (append ? skip.value : 0) + LIMIT
  } catch {
    if (!append) items.value = []
  } finally {
    loading.value = false
    loadingMore.value = false
  }
}

function handleFilter(filters) {
  currentFilters.value = Object.fromEntries(
    Object.entries(filters).filter(([, v]) => v !== undefined && v !== null && v !== '')
  )
  fetchItems(currentFilters.value)
}

function resetFilters() {
  currentFilters.value = {}
  fetchItems({})
}

function loadMore() {
  fetchItems(currentFilters.value, true)
}

function handleAddSuccess(name) {
  clearTimeout(toastTimer)
  toastMsg.value = `«${name}» добавлен в корзину`
  toastTimer = setTimeout(() => { toastMsg.value = '' }, 2500)
}

onMounted(async () => {
  await loadCategories()
  const catId = $route.query.category
  if (catId) currentFilters.value = { category_id: Number(catId) }
  fetchItems(currentFilters.value)
})
</script>

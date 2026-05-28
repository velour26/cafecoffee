<template>
  <div class="relative" ref="rootRef">

    <!-- Input wrapper -->
    <div class="relative flex items-center">
      <svg
        class="absolute left-3 pointer-events-none shrink-0"
        width="13" height="13" viewBox="0 0 24 24"
        fill="none" stroke="#aaa" stroke-width="2" stroke-linecap="round"
      >
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>

      <input
        ref="inputRef"
        v-model="query"
        type="text"
        placeholder="Поиск по меню..."
        autocomplete="off"
        class="transition-all duration-200 outline-none text-sm pl-9 pr-8 py-2"
        :style="[
          'background:#f3ede7;border:1px solid #e0d9d2;color:#1a1714;',
          isFocused
            ? 'width:280px;border-color:#c1ce56'
            : 'width:180px;border-color:#e0d9d2',
        ].join('')"
        @focus="isFocused = true"
        @blur="handleBlur"
        @keydown.enter.prevent="goToMenu"
        @keydown.escape="clear"
        @input="handleInput"
      />

      <!-- Крестик очистки -->
      <button
        v-if="query"
        @mousedown.prevent
        @click="clear"
        class="absolute right-2.5 flex items-center justify-center w-4 h-4 transition-opacity"
        style="color:#bbb"
        @mouseenter="e => e.currentTarget.style.color='#555'"
        @mouseleave="e => e.currentTarget.style.color='#bbb'"
      >
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
          <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
    </div>

    <!-- Дропдаун с результатами -->
    <Transition name="search-drop">
      <div
        v-if="isFocused && query.length >= 1"
        class="absolute top-full right-0 mt-1 z-50 overflow-hidden"
        style="width:320px;background:#fff;border:1px solid #e8e2db;box-shadow:0 8px 32px rgba(0,0,0,.10)"
        @mousedown.prevent
      >
        <!-- Загрузка -->
        <div v-if="loading" class="flex items-center gap-3 px-4 py-4">
          <div class="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" style="color:#c1ce56"></div>
          <span class="text-xs" style="color:#aaa">Поиск...</span>
        </div>

        <!-- Результаты -->
        <template v-else-if="results.length">
          <RouterLink
            v-for="item in results"
            :key="item.id"
            :to="`/menu/${item.id}`"
            @click="clear"
            class="flex items-center gap-3 px-4 py-3 transition-colors duration-100"
            style="border-bottom:1px solid #f5f0eb;text-decoration:none"
            @mouseenter="e => e.currentTarget.style.background='#faf7f2'"
            @mouseleave="e => e.currentTarget.style.background=''"
          >
            <div
              class="w-10 h-10 shrink-0 overflow-hidden"
              style="background:#f3ede7"
            >
              <img
                v-if="item.image_url && !brokenImages.has(item.id)"
                :src="item.image_url"
                :alt="item.name"
                class="w-full h-full object-cover"
                @error="brokenImages.add(item.id)"
              />
              <div v-else class="w-full h-full flex items-center justify-center">
                <svg width="80" height="96" viewBox="0 0 80 96" fill="none" style="opacity:0.1;width:100%;height:100%">
                  <path d="M10 32 L16 84 H64 L70 32 Z" fill="none" stroke="#000" stroke-width="2"/>
                  <ellipse cx="40" cy="32" rx="30" ry="8" fill="none" stroke="#000" stroke-width="2"/>
                  <path d="M64 47 Q80 47 80 57 Q80 67 64 67" stroke="#000" stroke-width="2" fill="none"/>
                </svg>
              </div>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-bold truncate" style="color:#1a1714">{{ item.name }}</p>
              <p class="text-xs mt-0.5" style="color:#aaa">{{ formatPrice(item.price) }}</p>
            </div>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="2" stroke-linecap="round">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </RouterLink>

          <!-- Ссылка «все результаты» если совпадений много -->
          <button
            v-if="hasMore"
            @mousedown.prevent
            @click="goToMenu"
            class="w-full flex items-center justify-between px-4 py-3 text-xs font-bold uppercase tracking-wider transition-colors duration-100"
            style="color:#c1ce56;border-top:1px solid #f0ece7"
            @mouseenter="e => e.currentTarget.style.background='#faf7f2'"
            @mouseleave="e => e.currentTarget.style.background=''"
          >
            <span>Смотреть все результаты</span>
            <span>→</span>
          </button>
        </template>

        <!-- Пусто -->
        <div v-else class="px-4 py-6 text-center">
          <p class="text-sm font-bold mb-1" style="color:#bbb">Ничего не найдено</p>
          <p class="text-xs" style="color:#ccc">Попробуйте другой запрос</p>
        </div>
      </div>
    </Transition>

  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { menuApi } from '@/api/menu'
import { formatPrice } from '@/utils/format'

const router = useRouter()
const rootRef  = ref(null)
const inputRef = ref(null)

const query   = ref('')
const results = ref([])
const loading = ref(false)
const isFocused = ref(false)
const hasMore = ref(false)
const brokenImages = reactive(new Set())

const LIMIT = 6
let debounceTimer = null

function handleInput() {
  clearTimeout(debounceTimer)
  if (query.value.trim().length < 1) {
    results.value = []
    hasMore.value = false
    return
  }
  debounceTimer = setTimeout(search, 280)
}

async function search() {
  if (!query.value.trim()) return
  loading.value = true
  try {
    const r = await menuApi.getItems({ search: query.value.trim(), limit: LIMIT + 1, skip: 0 })
    const items = r.data?.items || r.data || []
    hasMore.value = items.length > LIMIT
    results.value = items.slice(0, LIMIT)
  } catch {
    results.value = []
  } finally {
    loading.value = false
  }
}

function goToMenu() {
  if (!query.value.trim()) return
  router.push({ path: '/menu', query: { search: query.value.trim() } })
  clear()
}

function clear() {
  query.value = ''
  results.value = []
  hasMore.value = false
  isFocused.value = false
  inputRef.value?.blur()
}

function handleBlur() {
  // Небольшая задержка, чтобы успел сработать click по ссылкам в дропдауне
  setTimeout(() => { isFocused.value = false }, 150)
}

// Открыть из внешнего кода (мобильное меню)
defineExpose({ focus: () => { isFocused.value = true; inputRef.value?.focus() } })
</script>

<style scoped>
.search-drop-enter-active,
.search-drop-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.search-drop-enter-from,
.search-drop-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>

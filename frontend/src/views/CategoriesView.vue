<template>
  <div style="background:#fff;min-height:100vh">

    <div style="background:#fff;border-bottom:1px solid #f0f0f0">
      <div class="max-w-7xl mx-auto px-6 py-14">
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Кофеёчек</p>
        <div class="flex items-end justify-between">
          <h1 class="font-black leading-none" style="font-size:clamp(2.5rem,5vw,4rem);color:#0a0a0a">
            Категории
          </h1>
          <span v-if="!loading" class="text-sm mb-2" style="color:#bbb">
            {{ categories.length }} раздела
          </span>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-16">

      <div v-if="loading" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-px" style="background:#f0f0f0">
        <div
          v-for="i in 4" :key="i"
          class="animate-pulse"
          style="background:#fff;height:220px"
        ></div>
      </div>

      <div
        v-else-if="categories.length"
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-px"
        style="background:#f0f0f0"
      >
        <RouterLink
          v-for="(cat, i) in categories"
          :key="cat.id"
          :to="{ name: 'menu', query: { category: cat.id } }"
          class="group relative flex flex-col justify-between p-10 transition-all duration-300 overflow-hidden"
          style="background:#fff;min-height:220px"
          @mouseenter="e => e.currentTarget.style.background='#fafaf8'"
          @mouseleave="e => e.currentTarget.style.background='#fff'"
        >
          <span class="text-xs font-bold" style="color:#e8e8e8">
            {{ String(i + 1).padStart(2, '0') }}
          </span>

          <div>
            <div
              class="w-8 h-0.5 mb-4 transition-all duration-500 group-hover:w-16"
              style="background:#c1ce56"
            ></div>

            <h3
              class="font-black text-2xl leading-tight mb-3 transition-colors duration-200"
              style="color:#0a0a0a"
            >{{ cat.name }}</h3>

            <p
              v-if="cat.description"
              class="text-sm leading-relaxed"
              style="color:#aaa"
            >{{ cat.description }}</p>
          </div>

          <div
            class="flex items-center gap-2 mt-6 transition-all duration-300 translate-x-0 group-hover:translate-x-2"
          >
            <span class="text-xs font-bold uppercase tracking-widest" style="color:#c1ce56">
              Смотреть
            </span>
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none" style="color:#c1ce56">
              <path d="M1 7h12M8 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>

          <span
            class="absolute right-6 bottom-4 font-black select-none pointer-events-none transition-all duration-300 group-hover:opacity-100"
            style="font-size:6rem;line-height:1;color:#f5f5f3;opacity:0"
          >{{ String(i + 1) }}</span>
        </RouterLink>
      </div>

      <div v-else class="flex flex-col items-center justify-center py-32 gap-4">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#e0e0e0" stroke-width="1.5" stroke-linecap="round">
          <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/>
          <rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>
        </svg>
        <p class="font-bold" style="color:#ccc">Категории не найдены</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { categoriesApi } from '@/api/categories'

const categories = ref([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const r = await categoriesApi.getAll()
    categories.value = r.data
  } finally {
    loading.value = false
  }
})
</script>

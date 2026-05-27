<template>
  <div class="min-h-screen" style="background:#f5f5f3">
    <Navbar />

    <div class="max-w-7xl mx-auto px-4 py-8 md:py-10 flex gap-8">

      <aside class="w-48 shrink-0 hidden md:block">
        <div class="sticky top-8" style="background:#0a0a0a">
          <div class="px-5 py-5" style="border-bottom:1px solid #1f1f1f">
            <p class="text-xs font-bold uppercase tracking-[0.3em]" style="color:#c1ce56">Панель</p>
            <p class="text-sm font-black mt-0.5" style="color:#fff">Администратор</p>
          </div>
          <nav class="flex flex-col py-2">
            <RouterLink
              v-for="link in links"
              :key="link.to"
              :to="link.to"
              class="flex items-center gap-3 px-5 py-3 text-sm font-bold transition-colors duration-150"
              :style="isActive(link.to)
                ? 'color:#fff;border-left:3px solid #c1ce56;background:#161616'
                : 'color:#666;border-left:3px solid transparent'"
              @mouseenter="e => { if (!isActive(link.to)) e.currentTarget.style.color = '#ccc' }"
              @mouseleave="e => { if (!isActive(link.to)) e.currentTarget.style.color = '#666' }"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" v-html="link.icon"></svg>
              {{ link.label }}
            </RouterLink>
          </nav>
        </div>
      </aside>

      <div class="flex-1 min-w-0 pb-20 md:pb-0">
        <RouterView />
      </div>

    </div>

    <nav
      class="md:hidden fixed bottom-0 left-0 right-0 z-40 flex"
      style="background:#0a0a0a;border-top:1px solid #1f1f1f;height:60px"
    >
      <RouterLink
        v-for="link in links"
        :key="link.to"
        :to="link.to"
        class="flex-1 flex flex-col items-center justify-center gap-1 transition-colors duration-150"
        :style="isActive(link.to) ? 'color:#c1ce56' : 'color:#555'"
      >
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" v-html="link.icon"></svg>
        <span class="text-[9px] font-bold uppercase tracking-wide leading-none">{{ link.shortLabel }}</span>
      </RouterLink>
    </nav>

  </div>
</template>

<script setup>
import { RouterView, RouterLink, useRoute } from 'vue-router'
import Navbar from '@/components/Navbar.vue'

const $route = useRoute()

const links = [
  {
    to: '/admin',
    label: 'Дашборд',
    shortLabel: 'Главная',
    icon: '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>',
  },
  {
    to: '/admin/categories',
    label: 'Категории',
    shortLabel: 'Категории',
    icon: '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7" stroke-width="3"/>',
  },
  {
    to: '/admin/menu',
    label: 'Меню',
    shortLabel: 'Меню',
    icon: '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>',
  },
  {
    to: '/admin/orders',
    label: 'Заказы',
    shortLabel: 'Заказы',
    icon: '<polyline points="21 8 21 21 3 21 3 8"/><rect x="1" y="3" width="22" height="5"/><line x1="10" y1="12" x2="14" y2="12"/>',
  },
  {
    to: '/admin/reviews',
    label: 'Отзывы',
    shortLabel: 'Отзывы',
    icon: '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
  },
]

function isActive(to) {
  if (to === '/admin') return $route.path === '/admin'
  return $route.path.startsWith(to)
}
</script>

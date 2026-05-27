<template>
  <div style="background:#fff;min-height:100vh">
    <Navbar />
    <div class="max-w-7xl mx-auto px-6 py-12 flex flex-col lg:flex-row gap-10">

      <aside class="lg:w-56 shrink-0">
        <div class="sticky top-24">
          <div class="mb-6 flex flex-col items-start gap-3">
            <div
              class="w-14 h-14 flex items-center justify-center text-lg font-black"
              style="background:#c1ce56;color:#0a0a0a"
            >
              {{ initials }}
            </div>
            <div>
              <p class="font-black text-sm leading-tight" style="color:#0a0a0a">
                {{ $authStore.user?.full_name || 'Гость' }}
              </p>
              <p class="text-xs mt-0.5" style="color:#bbb">{{ $authStore.user?.email }}</p>
            </div>
          </div>

          <div style="border-top:1px solid #f0f0f0" class="pt-5">
            <nav class="flex flex-col gap-1">
              <RouterLink
                v-for="link in links"
                :key="link.to"
                :to="link.to"
                class="flex items-center gap-3 px-3 py-2.5 text-sm font-bold uppercase tracking-wider transition-all duration-200"
                :style="$route.path.startsWith(link.to)
                  ? 'color:#0a0a0a;border-left:2px solid #c1ce56;padding-left:10px'
                  : 'color:#aaa;border-left:2px solid transparent;padding-left:10px'"
                @mouseenter="e => { if (!$route.path.startsWith(link.to)) e.currentTarget.style.color='#0a0a0a' }"
                @mouseleave="e => { if (!$route.path.startsWith(link.to)) e.currentTarget.style.color='#aaa' }"
              >
                <component :is="link.icon" />
                {{ link.label }}
              </RouterLink>
            </nav>
          </div>
        </div>
      </aside>

      <div class="flex-1 min-w-0">
        <RouterView />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { RouterView, RouterLink, useRoute } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
import { useAuthStore } from '@/stores/auth'

const $route = useRoute()
const $authStore = useAuthStore()

const initials = computed(() => {
  const name = $authStore.user?.full_name || 'U'
  return name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2)
})

const links = [
  { to: '/account/profile', label: 'Профиль', icon: 'span' },
  { to: '/account/orders', label: 'Мои заказы', icon: 'span' },
]
</script>

<template>
  <header style="background:#fff;border-bottom:1px solid #f0f0f0" class="sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 h-16 flex items-center gap-4 sm:gap-8">

      <AppLogo :dark="false" :size="32" font-size="1rem" />

      <nav class="hidden md:flex items-center justify-center flex-1 gap-1">
        <RouterLink
          v-for="link in navLinks"
          :key="link.to"
          :to="link.to"
          class="relative px-5 py-2 text-xs font-bold uppercase tracking-[0.18em] transition-colors duration-200 whitespace-nowrap"
          :style="isActive(link.to) ? 'color:#0a0a0a' : 'color:#aaa'"
          @mouseenter="e => { if (!isActive(link.to)) e.currentTarget.style.color = '#0a0a0a' }"
          @mouseleave="e => { if (!isActive(link.to)) e.currentTarget.style.color = '#aaa' }"
        >
          {{ link.label }}
          <span
            v-if="isActive(link.to)"
            class="absolute bottom-0 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full"
            style="background:#c1ce56"
          ></span>
        </RouterLink>
      </nav>

      <!-- Поиск (десктоп) -->
      <div class="hidden md:flex items-center shrink-0">
        <NavSearch />
      </div>

      <div class="flex items-center gap-2 sm:gap-3 shrink-0 ml-3">

        <RouterLink
          v-if="authStore.isAuthenticated"
          to="/cart"
          class="relative flex items-center justify-center w-9 h-9 transition-all duration-200"
          style="color:#aaa;border:1px solid #e8e8e8"
          @mouseenter="e => { e.currentTarget.style.color='#0a0a0a'; e.currentTarget.style.borderColor='#ccc' }"
          @mouseleave="e => { e.currentTarget.style.color='#aaa'; e.currentTarget.style.borderColor='#e8e8e8' }"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 2 L3 6 v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/>
            <line x1="3" y1="6" x2="21" y2="6"/>
            <path d="M16 10a4 4 0 0 1-8 0"/>
          </svg>
          <span
            v-if="cartStore.itemCount > 0"
            class="absolute -top-1.5 -right-1.5 w-4 h-4 flex items-center justify-center rounded-full font-black"
            style="background:#c1ce56;color:#0a0a0a;font-size:9px"
          >{{ cartStore.itemCount > 9 ? '9+' : cartStore.itemCount }}</span>
        </RouterLink>

        <div v-if="authStore.isAuthenticated" class="relative hidden md:block" ref="menuRef">
          <button
            @click="menuOpen = !menuOpen"
            class="flex items-center gap-2.5 pl-3 pr-2 py-1.5 transition-all duration-200"
            style="border:1px solid #e8e8e8"
            @mouseenter="e => e.currentTarget.style.borderColor='#ccc'"
            @mouseleave="e => e.currentTarget.style.borderColor='#e8e8e8'"
          >
            <span class="w-6 h-6 rounded-full flex items-center justify-center font-black text-xs shrink-0" style="background:#c1ce56;color:#0a0a0a">
              {{ userInitials }}
            </span>
            <span class="hidden sm:block max-w-[110px] truncate text-xs font-medium" style="color:#888">
              {{ authStore.user?.full_name }}
            </span>
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none" style="color:#ccc;flex-shrink:0">
              <path d="M2 3.5 L5 6.5 L8 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>

          <Transition name="dropdown">
            <div
              v-if="menuOpen"
              class="absolute right-0 mt-2 w-52 py-1 z-50"
              style="background:#fff;border:1px solid #f0f0f0;box-shadow:0 8px 32px rgba(0,0,0,.08)"
            >
              <RouterLink to="/account/profile" @click="menuOpen = false"
                class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors"
                style="color:#888"
                @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                @mouseleave="e => e.currentTarget.style.color='#888'">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
                Профиль
              </RouterLink>
              <RouterLink to="/account/orders" @click="menuOpen = false"
                class="flex items-center gap-3 px-4 py-2.5 text-sm transition-colors"
                style="color:#888"
                @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                @mouseleave="e => e.currentTarget.style.color='#888'">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
                Мои заказы
              </RouterLink>
              <RouterLink v-if="authStore.isAdmin" to="/admin" @click="menuOpen = false"
                class="flex items-center gap-3 px-4 py-2.5 text-sm font-medium"
                style="color:#c1ce56">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
                Администрирование
              </RouterLink>
              <div style="border-top:1px solid #f5f5f5;margin:4px 0"></div>
              <button @click="handleLogout"
                class="flex items-center gap-3 w-full px-4 py-2.5 text-sm transition-colors"
                style="color:#ccc"
                @mouseenter="e => e.currentTarget.style.color='#f87171'"
                @mouseleave="e => e.currentTarget.style.color='#ccc'">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
                Выйти
              </button>
            </div>
          </Transition>
        </div>

        <template v-if="!authStore.isAuthenticated">
          <RouterLink
            to="/login"
            class="hidden md:inline-flex text-xs font-semibold uppercase tracking-widest px-5 py-2.5 transition-all duration-200"
            style="color:#aaa;border:1px solid #e8e8e8"
            @mouseenter="e => { e.currentTarget.style.color='#0a0a0a'; e.currentTarget.style.borderColor='#bbb' }"
            @mouseleave="e => { e.currentTarget.style.color='#aaa'; e.currentTarget.style.borderColor='#e8e8e8' }"
          >Войти</RouterLink>
          <RouterLink
            to="/register"
            class="hidden md:inline-flex text-xs font-bold uppercase tracking-widest px-5 py-2.5 transition-opacity hover:opacity-85"
            style="background:#c1ce56;color:#0a0a0a"
          >Регистрация</RouterLink>
        </template>

        <button
          class="md:hidden flex items-center justify-center w-9 h-9"
          style="border:1px solid #e8e8e8;color:#888"
          @click="mobileOpen = !mobileOpen"
        >
          <svg v-if="!mobileOpen" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/>
          </svg>
          <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>

      </div>
    </div>

    <Transition name="mobile-menu">
      <div
        v-if="mobileOpen"
        class="md:hidden fixed inset-0 z-40"
        style="top:64px"
      >
        <div
          class="absolute inset-0"
          style="background:rgba(0,0,0,0.3)"
          @click="mobileOpen = false"
        ></div>

        <div class="relative h-full overflow-y-auto" style="background:#fff;max-width:320px;width:100%">

          <!-- Поиск (мобильный) -->
          <div class="px-6 py-4" style="border-bottom:1px solid #f0f0f0">
            <p class="text-xs font-bold uppercase tracking-[0.3em] mb-3" style="color:#c1ce56">Поиск</p>
            <NavSearch ref="mobileSearchRef" class="block" style="width:100%" />
          </div>

          <div style="border-bottom:1px solid #f0f0f0">
            <p class="text-xs font-bold uppercase tracking-[0.3em] px-6 pt-5 pb-3" style="color:#c1ce56">Навигация</p>
            <RouterLink
              v-for="link in navLinks"
              :key="link.to"
              :to="link.to"
              @click="mobileOpen = false"
              class="flex items-center justify-between px-6 py-4"
              style="border-top:1px solid #f8f8f8"
              :style="isActive(link.to) ? 'color:#0a0a0a' : 'color:#888'"
            >
              <span class="text-sm font-bold">{{ link.label }}</span>
              <span v-if="isActive(link.to)" class="w-1.5 h-1.5 rounded-full" style="background:#c1ce56"></span>
            </RouterLink>
          </div>

          <div v-if="authStore.isAuthenticated" style="border-bottom:1px solid #f0f0f0">
            <p class="text-xs font-bold uppercase tracking-[0.3em] px-6 pt-5 pb-3" style="color:#c1ce56">Аккаунт</p>

            <RouterLink to="/account/profile" @click="mobileOpen = false"
              class="flex items-center gap-4 px-6 py-4"
              style="border-top:1px solid #f8f8f8;color:#555">
              <span class="w-8 h-8 rounded-full flex items-center justify-center font-black text-xs shrink-0" style="background:#c1ce56;color:#0a0a0a">
                {{ userInitials }}
              </span>
              <div>
                <p class="text-sm font-bold" style="color:#0a0a0a">{{ authStore.user?.full_name }}</p>
                <p class="text-xs" style="color:#bbb">{{ authStore.user?.email }}</p>
              </div>
            </RouterLink>

            <RouterLink to="/account/orders" @click="mobileOpen = false"
              class="flex items-center gap-3 px-6 py-4 text-sm font-bold"
              style="border-top:1px solid #f8f8f8;color:#555">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
              Мои заказы
            </RouterLink>

            <RouterLink to="/cart" @click="mobileOpen = false"
              class="flex items-center gap-3 px-6 py-4 text-sm font-bold"
              style="border-top:1px solid #f8f8f8;color:#555">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 2 L3 6 v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
              Корзина
              <span v-if="cartStore.itemCount > 0" class="ml-auto w-5 h-5 flex items-center justify-center rounded-full font-black" style="background:#c1ce56;color:#0a0a0a;font-size:10px">
                {{ cartStore.itemCount }}
              </span>
            </RouterLink>

            <RouterLink v-if="authStore.isAdmin" to="/admin" @click="mobileOpen = false"
              class="flex items-center gap-3 px-6 py-4 text-sm font-bold"
              style="border-top:1px solid #f8f8f8;color:#c1ce56">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
              Администрирование
            </RouterLink>
          </div>

          <div v-else class="px-6 py-6 flex flex-col gap-3">
            <RouterLink to="/login" @click="mobileOpen = false"
              class="w-full text-center text-xs font-bold uppercase tracking-widest py-3 transition-all"
              style="color:#0a0a0a;border:1px solid #e8e8e8">Войти</RouterLink>
            <RouterLink to="/register" @click="mobileOpen = false"
              class="w-full text-center text-xs font-bold uppercase tracking-widest py-3"
              style="background:#c1ce56;color:#0a0a0a">Регистрация</RouterLink>
          </div>

          <div v-if="authStore.isAuthenticated" class="px-6 py-5">
            <button
              @click="handleLogout"
              class="flex items-center gap-3 text-sm font-bold w-full"
              style="color:#ccc"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
              Выйти
            </button>
          </div>

        </div>
      </div>
    </Transition>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useCartStore } from '@/stores/cart'
import AppLogo from '@/components/AppLogo.vue'
import NavSearch from '@/components/NavSearch.vue'

const authStore = useAuthStore()
const cartStore = useCartStore()
const $route = useRoute()
const $router = useRouter()
const menuOpen = ref(false)
const menuRef = ref(null)
const mobileOpen = ref(false)

const navLinks = [
  { to: '/',           label: 'Главная'   },
  { to: '/menu',       label: 'Меню'      },
  { to: '/categories', label: 'Категории' },
  { to: '/reviews',    label: 'Отзывы'    },
  { to: '/about',      label: 'О нас'     },
  { to: '/contacts',   label: 'Контакты'  },
]

function isActive(path) {
  return path === '/' ? $route.path === '/' : $route.path.startsWith(path)
}

const userInitials = computed(() => {
  const name = authStore.user?.full_name || ''
  return name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2) || '?'
})

async function handleLogout() {
  menuOpen.value = false
  mobileOpen.value = false
  authStore.logout()
  cartStore.$reset()
  await $router.push('/')
}

function handleClickOutside(e) {
  if (menuRef.value && !menuRef.value.contains(e.target)) menuOpen.value = false
}

watch(() => $route.path, () => { mobileOpen.value = false })

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  if (authStore.isAuthenticated) cartStore.fetchCart()
})
onUnmounted(() => document.removeEventListener('click', handleClickOutside))
</script>

<style scoped>
.dropdown-enter-active, .dropdown-leave-active {
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.dropdown-enter-from, .dropdown-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}

.mobile-menu-enter-active, .mobile-menu-leave-active {
  transition: opacity 0.2s ease;
}
.mobile-menu-enter-active .relative,
.mobile-menu-leave-active .relative {
  transition: transform 0.25s ease;
}
.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
}
.mobile-menu-enter-from .relative,
.mobile-menu-leave-to .relative {
  transform: translateX(-16px);
}
</style>

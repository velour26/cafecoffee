<template>
  <div class="flex" style="background:#0a0a0a;min-height:calc(100vh - 65px)">

    <div class="hidden lg:flex flex-col justify-between flex-1 px-16 py-16 relative overflow-hidden" style="border-right:1px solid #1a1a1a">

      <div class="absolute inset-0 pointer-events-none select-none" aria-hidden="true">
        <svg style="position:absolute;top:8%;left:8%;width:22px;opacity:.2;transform:rotate(20deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:20%;left:70%;width:18px;opacity:.15;transform:rotate(-35deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:55%;left:15%;width:24px;opacity:.35;transform:rotate(40deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:75%;left:60%;width:20px;opacity:.3;transform:rotate(-20deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:88%;left:30%;width:16px;opacity:.18;transform:rotate(60deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
      </div>

      <div class="relative z-10">
        <RouterLink to="/" class="inline-block mb-12">
          <AppLogo :dark="true" :size="28" font-size="0.9rem" />
        </RouterLink>
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Добро пожаловать</p>
        <h2 class="font-black leading-[0.92]" style="font-size:clamp(2.5rem,4vw,3.5rem);color:#fff">
          Рады<br>снова<br>видеть.
        </h2>
      </div>

      <div class="relative z-10 flex justify-center">
        <svg viewBox="0 0 160 200" fill="none" style="width:200px;opacity:0.7">
          <path d="M52 40 C49 30 55 20 52 10" stroke="#2a2a2a" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M80 34 C77 24 83 14 80 4" stroke="#2a2a2a" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M108 40 C105 30 111 20 108 10" stroke="#2a2a2a" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M20 58 L30 158 H130 L140 58 Z" fill="#161616" stroke="#222" stroke-width="2" stroke-linejoin="round"/>
          <ellipse cx="80" cy="58" rx="60" ry="14" fill="#111" stroke="#222" stroke-width="2"/>
          <ellipse cx="80" cy="58" rx="44" ry="10" fill="#1a1a1a"/>
          <ellipse cx="80" cy="58" rx="28" ry="6.5" fill="none" stroke="#c1ce56" stroke-width="1.5" opacity="0.7"/>
          <ellipse cx="80" cy="58" rx="14" ry="3.5" fill="none" stroke="#c1ce56" stroke-width="1" opacity="0.35"/>
          <path d="M138 84 Q162 84 162 104 Q162 124 138 124" stroke="#222" stroke-width="3.5" fill="none" stroke-linecap="round"/>
          <ellipse cx="80" cy="162" rx="68" ry="10" fill="#141414" stroke="#1e1e1e" stroke-width="1.5"/>
        </svg>
      </div>

      <div class="relative z-10">
        <p class="text-sm leading-relaxed" style="color:#333;max-width:320px">
          «Хороший кофе начинается с хорошего настроения.
          Войдите — и закажите себе что-нибудь вкусное.»
        </p>
      </div>
    </div>

    <div class="flex-1 lg:max-w-md flex flex-col justify-center px-8 sm:px-12 lg:px-16 py-16">

      <RouterLink to="/" class="lg:hidden mb-10">
        <AppLogo :dark="true" :size="26" font-size="0.85rem" />
      </RouterLink>

      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Аккаунт</p>
      <h1 class="font-black mb-10" style="font-size:2rem;color:#fff;line-height:1">Вход</h1>

      <form @submit.prevent="handleLogin" class="flex flex-col gap-5">

        <div>
          <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Email</label>
          <input
            v-model="form.email"
            type="email"
            placeholder="your@email.com"
            autocomplete="email"
            required
            class="w-full px-4 py-3.5 text-sm outline-none transition-all"
            style="background:#111;border:1px solid #222;color:#fff"
            @focus="e => e.target.style.borderColor='#c1ce56'"
            @blur="e => e.target.style.borderColor='#222'"
          />
        </div>

        <div>
          <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Пароль</label>
          <div class="relative">
            <input
              v-model="form.password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="••••••••"
              autocomplete="current-password"
              required
              class="w-full px-4 py-3.5 pr-12 text-sm outline-none transition-all"
              style="background:#111;border:1px solid #222;color:#fff"
              @focus="e => e.target.style.borderColor='#c1ce56'"
              @blur="e => e.target.style.borderColor='#222'"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute right-4 top-1/2 -translate-y-1/2 transition-colors"
              style="color:#333"
              @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
              @mouseleave="e => e.currentTarget.style.color='#333'"
            >
              <svg v-if="!showPassword" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
              <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
            </button>
          </div>
        </div>

        <div v-if="error" class="flex items-center gap-3 px-4 py-3 text-xs" style="background:#1a0a0a;border:1px solid #3a1515;color:#f87171">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          {{ error }}
        </div>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-4 text-xs font-bold uppercase tracking-[0.25em] transition-opacity mt-1"
          style="background:#c1ce56;color:#0a0a0a"
          :style="loading ? 'opacity:0.6' : ''"
        >
          {{ loading ? '—' : 'Войти' }}
        </button>

      </form>

      <div class="flex items-center gap-4 my-8">
        <div class="flex-1 h-px" style="background:#1e1e1e"></div>
        <span class="text-xs" style="color:#333">или</span>
        <div class="flex-1 h-px" style="background:#1e1e1e"></div>
      </div>

      <p class="text-sm text-center" style="color:#444">
        Нет аккаунта?
        <RouterLink
          to="/register"
          class="font-bold ml-1 transition-colors"
          style="color:#fff"
          @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
          @mouseleave="e => e.currentTarget.style.color='#fff'"
        >Зарегистрироваться</RouterLink>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useCartStore } from '@/stores/cart'
import AppLogo from '@/components/AppLogo.vue'

const $router = useRouter()
const $route = useRoute()
const authStore = useAuthStore()
const cartStore = useCartStore()

const form = ref({ email: '', password: '' })
const loading = ref(false)
const error = ref('')
const showPassword = ref(false)

async function handleLogin() {
  loading.value = true
  error.value = ''
  const result = await authStore.login(form.value.email, form.value.password)
  loading.value = false
  if (result.success) {
    await cartStore.fetchCart()
    const redirect = $route.query.redirect || '/'
    $router.push(redirect)
  } else {
    error.value = result.message
  }
}
</script>

<template>
  <div class="flex" style="background:#0a0a0a;min-height:calc(100vh - 65px)">

    <div class="hidden lg:flex flex-col justify-between flex-1 px-16 py-16 relative overflow-hidden" style="border-right:1px solid #1a1a1a">

      <div class="absolute inset-0 pointer-events-none select-none" aria-hidden="true">
        <svg style="position:absolute;top:10%;left:12%;width:20px;opacity:.2;transform:rotate(-15deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:25%;left:72%;width:18px;opacity:.15;transform:rotate(45deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:50%;left:10%;width:24px;opacity:.35;transform:rotate(-40deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:70%;left:65%;width:20px;opacity:.3;transform:rotate(25deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:85%;left:25%;width:16px;opacity:.18;transform:rotate(-60deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
      </div>

      <div class="relative z-10">
        <RouterLink to="/" class="inline-block mb-12">
          <AppLogo :dark="true" :size="28" font-size="0.9rem" />
        </RouterLink>
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Добро пожаловать</p>
        <h2 class="font-black leading-[0.92]" style="font-size:clamp(2.5rem,4vw,3.5rem);color:#fff">
          Начните<br>свой<br>путь.
        </h2>
      </div>

      <div class="relative z-10 flex flex-col gap-5">
        <div v-for="perk in perks" :key="perk.text" class="flex items-start gap-4">
          <div class="w-8 h-8 shrink-0 flex items-center justify-center" style="background:#1a1a1a;border:1px solid #2a2a2a">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round" v-html="perk.icon"></svg>
          </div>
          <div>
            <p class="text-sm font-bold mb-0.5" style="color:#fff">{{ perk.title }}</p>
            <p class="text-xs" style="color:#444">{{ perk.text }}</p>
          </div>
        </div>
      </div>

      <div class="relative z-10">
        <p class="text-sm leading-relaxed" style="color:#333;max-width:320px">
          «Каждый большой путь начинается с первого шага.
          Создайте аккаунт — и закажите себе первую чашку.»
        </p>
      </div>
    </div>

    <div class="flex-1 lg:max-w-md flex flex-col justify-center px-8 sm:px-12 lg:px-16 py-16">

      <RouterLink to="/" class="lg:hidden mb-10">
        <AppLogo :dark="true" :size="26" font-size="0.85rem" />
      </RouterLink>

      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Аккаунт</p>
      <h1 class="font-black mb-10" style="font-size:2rem;color:#fff;line-height:1">Регистрация</h1>

      <div v-if="success" class="flex flex-col gap-5">
        <div class="flex items-center gap-4 px-5 py-4" style="background:#0f1a00;border:1px solid #2a3a00">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
          <div>
            <p class="text-sm font-bold mb-0.5" style="color:#c1ce56">Аккаунт создан!</p>
            <p class="text-xs" style="color:#556">Теперь войдите, чтобы начать заказывать.</p>
          </div>
        </div>
        <RouterLink
          to="/login"
          class="w-full py-4 text-xs font-bold uppercase tracking-[0.25em] text-center transition-opacity hover:opacity-80"
          style="background:#c1ce56;color:#0a0a0a;display:block"
        >
          Войти в аккаунт
        </RouterLink>
      </div>

      <form v-else @submit.prevent="handleRegister" class="flex flex-col gap-5">

        <div>
          <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Имя и фамилия</label>
          <input
            v-model="form.full_name"
            type="text"
            placeholder="Иван Иванов"
            autocomplete="name"
            required
            class="w-full px-4 py-3.5 text-sm outline-none transition-all"
            style="background:#111;border:1px solid #222;color:#fff"
            @focus="e => e.target.style.borderColor='#c1ce56'"
            @blur="e => e.target.style.borderColor='#222'"
          />
        </div>

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
          <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">
            Телефон
            <span class="normal-case font-normal tracking-normal ml-1" style="color:#333">(необязательно)</span>
          </label>
          <input
            v-model="form.phone"
            type="tel"
            placeholder="+7 (999) 000-00-00"
            autocomplete="tel"
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
              placeholder="Минимум 6 символов"
              autocomplete="new-password"
              required
              minlength="6"
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

        <div>
          <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Повтор пароля</label>
          <div class="relative">
            <input
              v-model="form.password2"
              :type="showPassword2 ? 'text' : 'password'"
              placeholder="Повторите пароль"
              autocomplete="new-password"
              required
              class="w-full px-4 py-3.5 pr-12 text-sm outline-none transition-all"
              :style="`background:#111;border:1px solid ${passwordMismatch ? '#3a1515' : '#222'};color:#fff`"
              @focus="e => e.target.style.borderColor = passwordMismatch ? '#3a1515' : '#c1ce56'"
              @blur="e => e.target.style.borderColor = passwordMismatch ? '#3a1515' : '#222'"
            />
            <button
              type="button"
              @click="showPassword2 = !showPassword2"
              class="absolute right-4 top-1/2 -translate-y-1/2 transition-colors"
              style="color:#333"
              @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
              @mouseleave="e => e.currentTarget.style.color='#333'"
            >
              <svg v-if="!showPassword2" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
              <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>
            </button>
          </div>
          <p v-if="passwordMismatch" class="text-xs mt-2" style="color:#f87171">Пароли не совпадают</p>
        </div>

        <div v-if="error" class="flex items-center gap-3 px-4 py-3 text-xs" style="background:#1a0a0a;border:1px solid #3a1515;color:#f87171">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          {{ error }}
        </div>

        <button
          type="submit"
          :disabled="loading || passwordMismatch"
          class="w-full py-4 text-xs font-bold uppercase tracking-[0.25em] transition-opacity mt-1"
          style="background:#c1ce56;color:#0a0a0a"
          :style="(loading || passwordMismatch) ? 'opacity:0.5' : ''"
        >
          {{ loading ? '—' : 'Создать аккаунт' }}
        </button>

      </form>

      <div class="flex items-center gap-4 my-8">
        <div class="flex-1 h-px" style="background:#1e1e1e"></div>
        <span class="text-xs" style="color:#333">или</span>
        <div class="flex-1 h-px" style="background:#1e1e1e"></div>
      </div>

      <p class="text-sm text-center" style="color:#444">
        Уже есть аккаунт?
        <RouterLink
          to="/login"
          class="font-bold ml-1 transition-colors"
          style="color:#fff"
          @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
          @mouseleave="e => e.currentTarget.style.color='#fff'"
        >Войти</RouterLink>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import AppLogo from '@/components/AppLogo.vue'

const authStore = useAuthStore()
const form = ref({ full_name: '', email: '', phone: '', password: '', password2: '' })
const loading = ref(false)
const error = ref('')
const success = ref(false)
const showPassword = ref(false)
const showPassword2 = ref(false)

const passwordMismatch = computed(
  () => form.value.password2 && form.value.password !== form.value.password2
)

const perks = [
  {
    title: 'Заказывайте онлайн',
    text: 'Выбирайте из полного меню и оформляйте заказ в один клик',
    icon: '<path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 0 1-8 0"/>',
  },
  {
    title: 'История заказов',
    text: 'Все ваши заказы сохраняются в личном кабинете',
    icon: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
  },
  {
    title: 'Оставляйте отзывы',
    text: 'Делитесь впечатлениями и помогайте другим выбрать лучшее',
    icon: '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
  },
]

async function handleRegister() {
  if (passwordMismatch.value) return
  loading.value = true
  error.value = ''
  success.value = false

  const result = await authStore.register({
    full_name: form.value.full_name,
    email: form.value.email,
    phone: form.value.phone || null,
    password: form.value.password,
  })

  loading.value = false
  if (result.success) {
    success.value = true
    form.value = { full_name: '', email: '', phone: '', password: '', password2: '' }
  } else {
    error.value = result.message
  }
}
</script>

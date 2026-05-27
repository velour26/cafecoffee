<template>
  <div>
    <div class="mb-10" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Аккаунт</p>
      <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Профиль</h1>
    </div>

    <div class="flex flex-col gap-8 max-w-lg">

      <section>
        <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#bbb">Личные данные</p>
        <form @submit.prevent="handleUpdate" class="flex flex-col gap-4">
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Имя и фамилия</label>
            <input
              v-model="form.full_name"
              type="text"
              required
              class="w-full px-4 py-3 text-sm outline-none transition-all duration-200"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Email</label>
            <input
              v-model="form.email"
              type="email"
              required
              class="w-full px-4 py-3 text-sm outline-none transition-all duration-200"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Телефон</label>
            <input
              v-model="form.phone"
              type="tel"
              placeholder="+7 (999) 000-00-00"
              class="w-full px-4 py-3 text-sm outline-none transition-all duration-200"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>

          <div v-if="updateError" class="px-4 py-3 text-xs" style="background:#fff5f5;color:#e53e3e;border:1px solid #fed7d7">
            {{ updateError }}
          </div>
          <div v-if="updateSuccess" class="flex items-center gap-2 px-4 py-3 text-xs" style="background:#f0fff4;color:#276749;border:1px solid #c6f6d5">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
            Данные сохранены
          </div>

          <div>
            <button
              type="submit"
              :disabled="updateLoading"
              class="px-8 py-3 text-xs font-bold uppercase tracking-widest transition-opacity"
              style="background:#c1ce56;color:#0a0a0a"
              :style="updateLoading ? 'opacity:0.5' : 'opacity:1'"
            >
              {{ updateLoading ? '—' : 'Сохранить' }}
            </button>
          </div>
        </form>
      </section>

      <div style="border-top:1px solid #f0f0f0"></div>

      <section>
        <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#bbb">Смена пароля</p>
        <form @submit.prevent="handlePasswordChange" class="flex flex-col gap-4">
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Новый пароль</label>
            <input
              v-model="passwordForm.password"
              type="password"
              minlength="6"
              required
              class="w-full px-4 py-3 text-sm outline-none transition-all duration-200"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Повторите пароль</label>
            <input
              v-model="passwordForm.password2"
              type="password"
              required
              class="w-full px-4 py-3 text-sm outline-none transition-all duration-200"
              :style="passwordMismatch
                ? 'background:#fff;border:1px solid #e53e3e;color:#0a0a0a'
                : 'background:#fff;border:1px solid #e8e8e8;color:#0a0a0a'"
              @focus="e => e.target.style.borderColor= passwordMismatch ? '#e53e3e' : '#0a0a0a'"
              @blur="e => e.target.style.borderColor = passwordMismatch ? '#e53e3e' : '#e8e8e8'"
            />
            <p v-if="passwordMismatch" class="text-xs mt-1" style="color:#e53e3e">Пароли не совпадают</p>
          </div>

          <div v-if="passwordError" class="px-4 py-3 text-xs" style="background:#fff5f5;color:#e53e3e;border:1px solid #fed7d7">
            {{ passwordError }}
          </div>
          <div v-if="passwordSuccess" class="flex items-center gap-2 px-4 py-3 text-xs" style="background:#f0fff4;color:#276749;border:1px solid #c6f6d5">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
            Пароль изменён
          </div>

          <div>
            <button
              type="submit"
              :disabled="passwordLoading || passwordMismatch || !passwordForm.password"
              class="px-8 py-3 text-xs font-bold uppercase tracking-widest transition-opacity"
              style="background:#0a0a0a;color:#fff"
              :style="(passwordLoading || passwordMismatch || !passwordForm.password) ? 'opacity:0.35' : 'opacity:1'"
            >
              {{ passwordLoading ? '—' : 'Изменить пароль' }}
            </button>
          </div>
        </form>
      </section>

      <div style="border-top:1px solid #f0f0f0"></div>

      <section class="flex items-center justify-between">
        <div>
          <p class="text-xs font-bold uppercase tracking-[0.15em] mb-1" style="color:#bbb">Роль</p>
          <p class="text-sm font-bold" style="color:#0a0a0a">
            {{ authStore.user?.role?.name === 'admin' ? 'Администратор' : 'Покупатель' }}
          </p>
        </div>
        <button
          @click="handleLogout"
          class="flex items-center gap-2 text-xs font-bold uppercase tracking-widest px-5 py-2.5 transition-all duration-200"
          style="color:#aaa;border:1px solid #e8e8e8"
          @mouseenter="e => { e.currentTarget.style.color='#e53e3e'; e.currentTarget.style.borderColor='#e53e3e' }"
          @mouseleave="e => { e.currentTarget.style.color='#aaa'; e.currentTarget.style.borderColor='#e8e8e8' }"
        >
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/>
          </svg>
          Выйти
        </button>
      </section>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'

const authStore = useAuthStore()
const $router = useRouter()

const form = ref({ full_name: '', email: '', phone: '' })
const updateLoading = ref(false)
const updateError = ref('')
const updateSuccess = ref(false)

const passwordForm = ref({ password: '', password2: '' })
const passwordLoading = ref(false)
const passwordError = ref('')
const passwordSuccess = ref(false)

const passwordMismatch = computed(
  () => passwordForm.value.password2 && passwordForm.value.password !== passwordForm.value.password2
)

onMounted(() => {
  if (authStore.user) {
    form.value.full_name = authStore.user.full_name || ''
    form.value.email = authStore.user.email || ''
    form.value.phone = authStore.user.phone || ''
  }
})

async function handleUpdate() {
  updateLoading.value = true
  updateError.value = ''
  updateSuccess.value = false
  try {
    await authApi.updateMe({
      full_name: form.value.full_name,
      email: form.value.email,
      phone: form.value.phone || null,
    })
    await authStore.fetchCurrentUser()
    updateSuccess.value = true
    setTimeout(() => { updateSuccess.value = false }, 3000)
  } catch (err) {
    updateError.value = err.response?.data?.detail || 'Ошибка при сохранении'
  } finally {
    updateLoading.value = false
  }
}

async function handlePasswordChange() {
  if (passwordMismatch.value) return
  passwordLoading.value = true
  passwordError.value = ''
  passwordSuccess.value = false
  try {
    await authApi.changePassword({ password: passwordForm.value.password })
    passwordForm.value = { password: '', password2: '' }
    passwordSuccess.value = true
    setTimeout(() => { passwordSuccess.value = false }, 3000)
  } catch (err) {
    passwordError.value = err.response?.data?.detail || 'Ошибка при смене пароля'
  } finally {
    passwordLoading.value = false
  }
}

function handleLogout() {
  authStore.logout()
  $router.push('/')
}
</script>

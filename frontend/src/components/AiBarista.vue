<script setup>
import { ref } from 'vue'
import { askBarista } from '@/api/ai'

const question = ref('')
const answer = ref('')
const loading = ref(false)
const error = ref('')

const examples = [
  'На улице холодно, хочу согреться',
  'Что взять с собой утром на пробежку?',
  'Подбери десерт под латте',
]

async function ask(text) {
  const q = (text ?? question.value ?? '').trim()
  if (!q) return
  question.value = q
  loading.value = true
  error.value = ''
  answer.value = ''
  try {
    const data = await askBarista(q)
    answer.value = data?.answer || 'Ответ пуст.'
  } catch (e) {
    error.value = e?.response?.data?.detail || e?.message || 'AI-сервис недоступен'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="bg-amber-50 py-16">
    <div class="container mx-auto px-6 max-w-3xl">
      <div class="bg-white rounded-3xl border border-amber-100 shadow-sm p-8 md:p-10">
        <div class="flex items-center gap-3 mb-2">
          <span class="text-3xl">☕</span>
          <h2 class="text-3xl font-bold text-amber-900">AI-бариста</h2>
        </div>
        <p class="text-amber-800/70 mb-6">
          Расскажите о настроении или задаче — подберу напиток или блюдо из меню.
        </p>

        <form @submit.prevent="ask()" class="flex flex-col sm:flex-row gap-3 mb-4">
          <input
            v-model="question"
            type="text"
            placeholder="Например: что-нибудь сладкое к чаю"
            class="flex-1 px-4 py-3 rounded-xl border border-amber-200 focus:border-amber-500 focus:outline-none"
            :disabled="loading"
          />
          <button
            type="submit"
            class="px-6 py-3 rounded-xl bg-amber-600 text-white font-semibold hover:bg-amber-700 disabled:opacity-50 transition"
            :disabled="loading || !question.trim()"
          >
            {{ loading ? 'Думаю…' : 'Спросить' }}
          </button>
        </form>

        <div class="flex flex-wrap gap-2 mb-4">
          <button
            v-for="ex in examples"
            :key="ex"
            type="button"
            @click="ask(ex)"
            class="text-xs px-3 py-1.5 rounded-full bg-amber-100 hover:bg-amber-200 text-amber-900"
            :disabled="loading"
          >
            {{ ex }}
          </button>
        </div>

        <div v-if="error" class="text-red-600 text-sm mb-3">{{ error }}</div>

        <div
          v-if="answer"
          class="bg-amber-50 rounded-2xl p-5 whitespace-pre-line text-amber-950 leading-relaxed"
        >
          {{ answer }}
        </div>
      </div>
    </div>
  </section>
</template>

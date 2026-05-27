<template>
  <div>
    <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Обратная связь</h1>
        <span v-if="!loading" class="text-sm mb-0.5" style="color:#bbb">{{ messages.length }} {{ msgsWord }}</span>
      </div>
    </div>

    <!-- фильтр непрочитанных -->
    <div class="flex gap-2 mb-6">
      <button
        v-for="f in filters"
        :key="f.value"
        @click="activeFilter = f.value"
        class="text-xs font-bold uppercase tracking-wider px-4 py-2 transition-colors duration-150"
        :style="activeFilter === f.value
          ? 'background:#0a0a0a;color:#fff'
          : 'background:#fff;color:#888;border:1px solid #e8e8e8'"
        @mouseenter="e => { if (activeFilter !== f.value) e.currentTarget.style.borderColor='#0a0a0a' }"
        @mouseleave="e => { if (activeFilter !== f.value) e.currentTarget.style.borderColor='#e8e8e8' }"
      >{{ f.label }}</button>
    </div>

    <div v-if="loading" class="flex flex-col gap-2">
      <div v-for="i in 5" :key="i" class="animate-pulse" style="background:#f5f5f3;height:72px;border:1px solid #f0f0f0"></div>
    </div>

    <div v-else style="background:#fff;border:1px solid #f0f0f0">
      <div v-if="filtered.length">
        <div
          v-for="msg in filtered"
          :key="msg.id"
          class="flex items-start gap-4 px-5 py-5 cursor-pointer transition-colors duration-150"
          style="border-bottom:1px solid #f8f8f8"
          :style="!msg.is_read ? 'background:#fffef5' : ''"
          @click="openMsg(msg)"
          @mouseenter="e => { if (msg.is_read) e.currentTarget.style.background='#fafafa'; else e.currentTarget.style.background='#faf9e8' }"
          @mouseleave="e => { e.currentTarget.style.background = msg.is_read ? '' : '#fffef5' }"
        >
          <!-- индикатор непрочитанного -->
          <div class="w-2 h-2 rounded-full mt-2 shrink-0" :style="msg.is_read ? 'background:#e8e8e8' : 'background:#c1ce56'"></div>

          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between gap-3 mb-1">
              <div class="flex items-center gap-3">
                <span class="text-sm font-black" style="color:#0a0a0a">{{ msg.name }}</span>
                <span class="text-xs" style="color:#bbb">{{ msg.email }}</span>
                <span v-if="msg.topic" class="text-xs font-bold px-2 py-0.5" style="background:#f5f5f3;color:#888">{{ msg.topic }}</span>
              </div>
              <span class="text-xs whitespace-nowrap" style="color:#bbb">{{ formatDate(msg.created_at) }}</span>
            </div>
            <p class="text-sm truncate" style="color:#555">{{ msg.message }}</p>
          </div>

          <button
            @click.stop="confirmDelete(msg.id)"
            class="shrink-0 flex items-center justify-center w-7 h-7 transition-colors"
            style="color:#ddd"
            @mouseenter="e => e.currentTarget.style.color='#e53e3e'"
            @mouseleave="e => e.currentTarget.style.color='#ddd'"
            title="Удалить"
          >
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
              <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4h6v2"/>
            </svg>
          </button>
        </div>
      </div>
      <div v-else class="px-6 py-14 text-center">
        <p class="text-sm font-bold" style="color:#bbb">Сообщений нет</p>
      </div>
    </div>

    <!-- Модалка просмотра -->
    <div
      v-if="selectedMsg"
      class="fixed inset-0 z-50 flex items-center justify-center px-4 py-8"
      style="background:rgba(0,0,0,0.5)"
      @click.self="selectedMsg = null"
    >
      <div style="background:#fff;width:100%;max-width:540px;max-height:90vh;overflow-y:auto">
        <div class="flex items-center justify-between px-6 py-5" style="border-bottom:1px solid #f0f0f0;position:sticky;top:0;background:#fff;z-index:1">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#c1ce56">Сообщение</p>
            <p class="font-black text-lg mt-0.5" style="color:#0a0a0a;line-height:1.2">{{ selectedMsg.name }}</p>
          </div>
          <button
            @click="selectedMsg = null"
            style="color:#bbb"
            @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
            @mouseleave="e => e.currentTarget.style.color='#bbb'"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
              <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="px-6 py-6 flex flex-col gap-5">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.15em] mb-1" style="color:#bbb">Отправитель</p>
              <p class="text-sm font-bold" style="color:#0a0a0a">{{ selectedMsg.name }}</p>
              <a :href="'mailto:' + selectedMsg.email" class="text-xs hover:underline" style="color:#c1ce56">{{ selectedMsg.email }}</a>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.15em] mb-1" style="color:#bbb">Тема</p>
              <p class="text-sm font-bold" style="color:#0a0a0a">{{ selectedMsg.topic || '—' }}</p>
            </div>
          </div>

          <div style="border-top:1px solid #f0f0f0;padding-top:1.25rem">
            <p class="text-xs font-bold uppercase tracking-[0.15em] mb-3" style="color:#bbb">Сообщение</p>
            <p class="text-sm leading-relaxed whitespace-pre-wrap" style="color:#333">{{ selectedMsg.message }}</p>
          </div>

          <p class="text-xs" style="color:#bbb">{{ formatDate(selectedMsg.created_at) }}</p>

          <div class="flex gap-3 pt-2" style="border-top:1px solid #f0f0f0">
            <a
              :href="'mailto:' + selectedMsg.email + '?subject=Re: ' + (selectedMsg.topic || 'Ваше сообщение')"
              class="flex items-center gap-2 px-4 py-2.5 text-xs font-bold uppercase tracking-wider transition-opacity hover:opacity-80"
              style="background:#c1ce56;color:#0a0a0a"
            >
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
              Ответить
            </a>
            <button
              @click="confirmDelete(selectedMsg.id); selectedMsg = null"
              class="flex items-center gap-2 px-4 py-2.5 text-xs font-bold uppercase tracking-wider transition-colors"
              style="border:1px solid #e8e8e8;color:#bbb"
              @mouseenter="e => { e.currentTarget.style.borderColor='#e53e3e'; e.currentTarget.style.color='#e53e3e' }"
              @mouseleave="e => { e.currentTarget.style.borderColor='#e8e8e8'; e.currentTarget.style.color='#bbb' }"
            >
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
                <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/>
              </svg>
              Удалить
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Подтверждение удаления -->
    <div
      v-if="deleteId"
      class="fixed inset-0 z-50 flex items-center justify-center px-4"
      style="background:rgba(0,0,0,0.5)"
      @click.self="deleteId = null"
    >
      <div style="background:#fff;width:100%;max-width:360px">
        <div class="px-6 py-6">
          <p class="font-black text-base mb-2" style="color:#0a0a0a">Удалить сообщение?</p>
          <p class="text-sm" style="color:#888">Это действие нельзя отменить.</p>
        </div>
        <div class="flex" style="border-top:1px solid #f0f0f0">
          <button
            @click="deleteId = null"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-colors"
            style="color:#888;border-right:1px solid #f0f0f0"
            @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
            @mouseleave="e => e.currentTarget.style.color='#888'"
          >Отмена</button>
          <button
            @click="handleDelete"
            :disabled="deleting"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-opacity"
            style="color:#e53e3e"
            :style="deleting ? 'opacity:0.5' : ''"
          >{{ deleting ? '—' : 'Удалить' }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { contactApi } from '@/api/contact'
import { formatDate } from '@/utils/format'

const messages = ref([])
const loading = ref(false)
const deleteId = ref(null)
const deleting = ref(false)
const selectedMsg = ref(null)
const activeFilter = ref('all')

const filters = [
  { value: 'all',    label: 'Все' },
  { value: 'unread', label: 'Непрочитанные' },
  { value: 'read',   label: 'Прочитанные' },
]

const filtered = computed(() => {
  if (activeFilter.value === 'unread') return messages.value.filter(m => !m.is_read)
  if (activeFilter.value === 'read')   return messages.value.filter(m =>  m.is_read)
  return messages.value
})

const msgsWord = computed(() => {
  const n = messages.value.length
  if (n % 10 === 1 && n % 100 !== 11) return 'сообщение'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'сообщения'
  return 'сообщений'
})

async function fetchMessages() {
  loading.value = true
  try {
    const r = await contactApi.getAll({ limit: 500 })
    messages.value = r.data
  } finally {
    loading.value = false
  }
}

async function openMsg(msg) {
  selectedMsg.value = msg
  if (!msg.is_read) {
    try {
      await contactApi.markRead(msg.id)
      msg.is_read = true
    } catch { /* не критично */ }
  }
}

function confirmDelete(id) { deleteId.value = id }

async function handleDelete() {
  deleting.value = true
  try {
    await contactApi.delete(deleteId.value)
    messages.value = messages.value.filter(m => m.id !== deleteId.value)
    deleteId.value = null
  } catch (err) {
    alert(err.response?.data?.detail || 'Ошибка при удалении')
  } finally {
    deleting.value = false
  }
}

onMounted(fetchMessages)
</script>

<template>
  <div>
    <div class="mb-10" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Аккаунт</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Мои заказы</h1>
        <span v-if="!loading && orders.length" class="text-sm mb-0.5" style="color:#bbb">
          {{ orders.length }} {{ ordersWord }}
        </span>
      </div>
    </div>

    <div v-if="loading" class="flex flex-col gap-3">
      <div v-for="i in 3" :key="i" class="animate-pulse" style="height:100px;background:#f5f5f5;border:1px solid #eee"></div>
    </div>

    <div v-else-if="!orders.length" class="flex flex-col items-center py-24 gap-6 text-center">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="1.2" stroke-linecap="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>
      </svg>
      <div>
        <p class="font-black text-lg mb-2" style="color:#0a0a0a">Заказов пока нет</p>
        <p class="text-sm" style="color:#aaa">Оформите первый заказ из нашего меню</p>
      </div>
      <RouterLink
        to="/menu"
        class="text-xs font-bold uppercase tracking-widest px-7 py-3 transition-opacity hover:opacity-85"
        style="background:#c1ce56;color:#0a0a0a"
      >Перейти в меню</RouterLink>
    </div>

    <div v-else class="flex flex-col gap-3">
      <RouterLink
        v-for="order in orders"
        :key="order.id"
        :to="`/account/orders/${order.id}`"
        class="block group transition-all duration-200"
        style="border:1px solid #f0f0f0"
        @mouseenter="e => e.currentTarget.style.borderColor='#ddd'"
        @mouseleave="e => e.currentTarget.style.borderColor='#f0f0f0'"
      >
        <div class="flex items-stretch">
          <div class="w-1 shrink-0 transition-all duration-200"
            :style="statusAccent(order.status)"
          ></div>

          <div class="flex-1 px-5 py-4 flex items-center justify-between gap-4">
            <div class="flex flex-col gap-1 min-w-0">
              <div class="flex items-center gap-3">
                <span class="text-sm font-black" style="color:#0a0a0a">Заказ #{{ order.id }}</span>
                <span
                  class="text-xs font-bold uppercase tracking-wider px-2 py-0.5"
                  :style="statusBadgeStyle(order.status)"
                >{{ getStatusLabel(order.status) }}</span>
              </div>
              <div class="flex items-center gap-3 text-xs" style="color:#bbb">
                <span>{{ formatDate(order.created_at) }}</span>
                <span style="color:#e8e8e8">·</span>
                <span class="flex items-center gap-1">
                  <svg v-if="order.delivery_type === 'delivery'" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
                    <rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
                  </svg>
                  <svg v-else width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
                    <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
                  </svg>
                  {{ order.delivery_type === 'delivery' ? 'Доставка' : 'Самовывоз' }}
                </span>
                <span style="color:#e8e8e8">·</span>
                <span>{{ order.items?.length || 0 }} {{ posWord(order.items?.length) }}</span>
              </div>
            </div>

            <div class="flex items-center gap-4 shrink-0">
              <span class="font-black text-base" style="color:#c1ce56">{{ formatPrice(order.total_amount) }}</span>
              <svg
                width="14" height="14" viewBox="0 0 14 14" fill="none"
                class="transition-transform duration-200 group-hover:translate-x-1"
                style="color:#ddd"
              >
                <path d="M1 7h12M8 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
          </div>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { ordersApi } from '@/api/orders'
import { formatPrice, formatDate, getStatusLabel } from '@/utils/format'

const orders = ref([])
const loading = ref(false)

const ordersWord = computed(() => {
  const n = orders.value.length
  if (n % 10 === 1 && n % 100 !== 11) return 'заказ'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'заказа'
  return 'заказов'
})

function posWord(n = 0) {
  if (n % 10 === 1 && n % 100 !== 11) return 'позиция'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'позиции'
  return 'позиций'
}

function statusAccent(status) {
  const colors = {
    new: '#c1ce56',
    confirmed: '#68d391',
    preparing: '#f6ad55',
    ready: '#63b3ed',
    completed: '#a0aec0',
    cancelled: '#fc8181',
  }
  return `background:${colors[status] || '#e8e8e8'}`
}

function statusBadgeStyle(status) {
  const styles = {
    new: 'background:#f8fce8;color:#7a8a1a',
    confirmed: 'background:#f0fff4;color:#276749',
    preparing: 'background:#fffaf0;color:#9c6a04',
    ready: 'background:#ebf8ff;color:#2b6cb0',
    completed: 'background:#f7fafc;color:#718096',
    cancelled: 'background:#fff5f5;color:#c53030',
  }
  return styles[status] || 'background:#f7fafc;color:#718096'
}

onMounted(async () => {
  loading.value = true
  try {
    const r = await ordersApi.getMy()
    orders.value = r.data
  } finally {
    loading.value = false
  }
})
</script>

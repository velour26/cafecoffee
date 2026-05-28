<template>
  <div>
    <RouterLink
      to="/account/orders"
      class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider mb-8 transition-colors"
      style="color:#bbb"
      @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
      @mouseleave="e => e.currentTarget.style.color='#bbb'"
    >
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
        <path d="M13 7H1M6 2L1 7l5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      Мои заказы
    </RouterLink>

    <div v-if="loading">
      <div class="animate-pulse mb-8">
        <div style="background:#f0f0f0;height:28px;width:200px;margin-bottom:12px"></div>
        <div style="background:#f0f0f0;height:14px;width:140px"></div>
      </div>
      <div class="animate-pulse space-y-3">
        <div style="background:#f5f5f5;height:80px"></div>
        <div style="background:#f5f5f5;height:80px"></div>
      </div>
    </div>

    <div v-else-if="!order" class="flex flex-col items-center py-20 gap-5 text-center">
      <p class="font-black text-xl" style="color:#0a0a0a">Заказ не найден</p>
      <RouterLink to="/account/orders" class="text-xs font-bold uppercase tracking-widest px-6 py-3" style="background:#c1ce56;color:#0a0a0a">
        К моим заказам
      </RouterLink>
    </div>

    <template v-else>
      <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Заказ</p>
        <div class="flex items-start justify-between gap-4 flex-wrap">
          <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">#{{ order.id }}</h1>
          <span
            class="text-xs font-bold uppercase tracking-wider px-3 py-1.5 mt-1"
            :style="statusBadgeStyle(order.status)"
          >{{ getStatusLabel(order.status) }}</span>
        </div>
        <p class="text-sm mt-2" style="color:#bbb">{{ formatDate(order.created_at) }}</p>
      </div>

      <div class="flex flex-col gap-6 max-w-lg">

        <div style="border:1px solid #f0f0f0">
          <div class="flex items-center gap-3 px-5 py-4" style="border-bottom:1px solid #f0f0f0">
            <div class="w-8 h-8 flex items-center justify-center shrink-0" style="background:#f5f5f3">
              <svg v-if="order.delivery_type === 'delivery'" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                <rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
              </svg>
              <svg v-else width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-wider" style="color:#bbb">
                {{ order.delivery_type === 'delivery' ? 'Доставка' : 'Самовывоз' }}
              </p>
              <p class="text-sm font-bold mt-0.5" style="color:#0a0a0a">
                {{ order.delivery_type === 'delivery'
                  ? (order.delivery_address || 'Адрес не указан')
                  : 'ул. Кофейная, 42' }}
              </p>
            </div>
          </div>

          <div v-if="order.comment" class="px-5 py-4">
            <p class="text-xs font-bold uppercase tracking-wider mb-1" style="color:#bbb">Комментарий</p>
            <p class="text-sm" style="color:#555">{{ order.comment }}</p>
          </div>
        </div>

        <div style="border:1px solid #f0f0f0">
          <div class="px-5 py-4" style="border-bottom:1px solid #f0f0f0">
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#bbb">Состав заказа</p>
          </div>

          <div>
            <div
              v-for="item in order.items"
              :key="item.id"
              class="flex items-center justify-between px-5 py-4"
              style="border-bottom:1px solid #f8f8f8"
            >
              <div>
                <p class="text-sm font-bold" style="color:#0a0a0a">{{ item.item_name }}</p>
                <p class="text-xs mt-0.5" style="color:#bbb">
                  {{ formatPrice(item.price) }} × {{ item.quantity }}
                </p>
              </div>
              <p class="text-sm font-black" style="color:#0a0a0a">{{ formatPrice(item.subtotal) }}</p>
            </div>
          </div>

          <div class="flex items-center justify-between px-5 py-4">
            <span class="text-xs font-bold uppercase tracking-wider" style="color:#0a0a0a">Итого</span>
            <span class="font-black text-xl" style="color:#c1ce56">{{ formatPrice(order.total_amount) }}</span>
          </div>
        </div>

        <div style="border:1px solid #f0f0f0;padding:20px 20px">
          <p class="text-xs font-bold uppercase tracking-[0.2em] mb-4" style="color:#bbb">Статус заказа</p>
          <div class="flex flex-col gap-3">
            <div
              v-for="step in statusSteps"
              :key="step.key"
              class="flex items-center gap-3"
            >
              <div
                class="w-5 h-5 shrink-0 flex items-center justify-center"
                :style="isStepDone(step.key) ? 'background:#c1ce56' : isStepCancelled(step.key) ? 'background:#fc8181' : 'background:#f0f0f0'"
              >
                <svg v-if="isStepDone(step.key)" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
                <svg v-else-if="isStepCancelled(step.key)" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#2a2420" stroke-width="3" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
                <div v-else class="w-1.5 h-1.5" style="background:#ccc"></div>
              </div>
              <span
                class="text-sm"
                :style="isStepDone(step.key) ? 'color:#0a0a0a;font-weight:700' : 'color:#bbb'"
              >{{ step.label }}</span>
            </div>
          </div>
        </div>

      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { ordersApi } from '@/api/orders'
import { formatPrice, formatDate, getStatusLabel } from '@/utils/format'

const $route = useRoute()
const order = ref(null)
const loading = ref(false)

const statusSteps = [
  { key: 'new',       label: 'Заказ принят' },
  { key: 'confirmed', label: 'Подтверждён' },
  { key: 'preparing', label: 'Готовится' },
  { key: 'ready',     label: 'Готов к выдаче' },
  { key: 'completed', label: 'Выполнен' },
]

const statusOrder = ['new', 'confirmed', 'preparing', 'ready', 'completed']

function isStepDone(key) {
  if (!order.value) return false
  if (order.value.status === 'cancelled') return false
  const currentIdx = statusOrder.indexOf(order.value.status)
  const stepIdx = statusOrder.indexOf(key)
  return stepIdx <= currentIdx
}

function isStepCancelled(key) {
  return order.value?.status === 'cancelled' && key === 'new'
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
    const r = await ordersApi.getById($route.params.id)
    order.value = r.data
  } catch {
    order.value = null
  } finally {
    loading.value = false
  }
})
</script>

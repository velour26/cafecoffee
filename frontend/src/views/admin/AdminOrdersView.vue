<template>
  <div>
    <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Заказы</h1>
        <span v-if="!loading" class="text-sm mb-0.5" style="color:#bbb">{{ filteredOrders.length }} {{ ordersWord }}</span>
      </div>
    </div>

    <div class="flex flex-wrap gap-2 mb-6">
      <button
        v-for="s in statusFilters"
        :key="s.value"
        @click="activeStatus = s.value"
        class="text-xs font-bold uppercase tracking-wider px-4 py-2 transition-colors duration-150"
        :style="activeStatus === s.value
          ? 'background:#0a0a0a;color:#fff'
          : 'background:#fff;color:#888;border:1px solid #e8e8e8'"
        @mouseenter="e => { if (activeStatus !== s.value) e.currentTarget.style.borderColor = '#0a0a0a' }"
        @mouseleave="e => { if (activeStatus !== s.value) e.currentTarget.style.borderColor = '#e8e8e8' }"
      >{{ s.label }}</button>
    </div>

    <div v-if="loading" class="flex flex-col gap-2">
      <div v-for="i in 6" :key="i" class="animate-pulse" style="background:#f5f5f3;height:56px;border:1px solid #f0f0f0"></div>
    </div>

    <div v-else style="background:#fff;border:1px solid #f0f0f0">
      <div v-if="filteredOrders.length" class="overflow-x-auto">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="border-bottom:1px solid #f0f0f0">
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">№</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Клиент</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Позиций</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Сумма</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Статус</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Дата</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Действие</th>
              <th class="px-5 py-3" style="background:#fafafa"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="order in filteredOrders"
              :key="order.id"
              style="border-bottom:1px solid #f8f8f8"
            >
              <td class="px-5 py-4 text-sm font-black" style="color:#0a0a0a">#{{ order.id }}</td>
              <td class="px-5 py-4 text-sm" style="color:#555">{{ order.user?.full_name || order.user?.email || '—' }}</td>
              <td class="px-5 py-4 text-sm" style="color:#888">{{ order.items?.length || 0 }}</td>
              <td class="px-5 py-4 text-sm font-black" style="color:#c1ce56">{{ formatPrice(order.total_amount) }}</td>
              <td class="px-5 py-4">
                <span class="text-xs font-bold uppercase tracking-wider px-2 py-1" :style="statusBadgeStyle(order.status)">
                  {{ getStatusLabel(order.status) }}
                </span>
              </td>
              <td class="px-5 py-4 text-xs" style="color:#bbb">{{ formatDate(order.created_at) }}</td>
              <td class="px-5 py-4">
                <select
                  :value="order.status"
                  @change="handleStatusChange(order.id, $event.target.value)"
                  class="text-xs font-bold outline-none px-3 py-1.5 transition-colors"
                  style="border:1px solid #e8e8e8;color:#0a0a0a;background:#fff;cursor:pointer"
                >
                  <option v-for="s in orderStatuses" :key="s.value" :value="s.value">{{ s.label }}</option>
                </select>
              </td>
              <td class="px-5 py-4">
                <button
                  @click="openDetails(order)"
                  class="text-xs font-bold uppercase tracking-wider whitespace-nowrap"
                  style="color:#bbb"
                  @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                  @mouseleave="e => e.currentTarget.style.color='#bbb'"
                >Подробнее</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="px-6 py-14 text-center">
        <p class="text-sm font-bold" style="color:#bbb">Заказов нет</p>
      </div>
    </div>

    <div
      v-if="selectedOrder"
      class="fixed inset-0 z-50 flex items-center justify-center px-4 py-8"
      style="background:rgba(0,0,0,0.5)"
      @click.self="selectedOrder = null"
    >
      <div style="background:#fff;width:100%;max-width:520px;max-height:90vh;overflow-y:auto">
        <div class="flex items-center justify-between px-6 py-5" style="border-bottom:1px solid #f0f0f0;position:sticky;top:0;background:#fff;z-index:1">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#c1ce56">Заказ</p>
            <p class="font-black text-xl" style="color:#0a0a0a;line-height:1.2">#{{ selectedOrder.id }}</p>
          </div>
          <button
            @click="selectedOrder = null"
            style="color:#bbb"
            @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
            @mouseleave="e => e.currentTarget.style.color='#bbb'"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
              <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>

        <div class="px-6 py-6 flex flex-col gap-6">

          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.15em] mb-1" style="color:#bbb">Клиент</p>
              <p class="text-sm font-bold" style="color:#0a0a0a">{{ selectedOrder.user?.full_name || '—' }}</p>
              <p class="text-xs mt-0.5" style="color:#bbb">{{ selectedOrder.user?.email }}</p>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.15em] mb-1" style="color:#bbb">Статус</p>
              <span class="text-xs font-bold uppercase tracking-wider px-2 py-1" :style="statusBadgeStyle(selectedOrder.status)">
                {{ getStatusLabel(selectedOrder.status) }}
              </span>
            </div>
          </div>

          <div style="border:1px solid #f0f0f0">
            <div class="flex items-center gap-3 px-4 py-3" style="border-bottom:1px solid #f0f0f0">
              <div class="w-7 h-7 flex items-center justify-center shrink-0" style="background:#f5f5f3">
                <svg v-if="selectedOrder.delivery_type === 'delivery'" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                  <rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
                </svg>
                <svg v-else width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                  <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
                </svg>
              </div>
              <div>
                <p class="text-xs font-bold uppercase tracking-wider" style="color:#bbb">
                  {{ selectedOrder.delivery_type === 'delivery' ? 'Доставка' : 'Самовывоз' }}
                </p>
                <p class="text-sm font-bold mt-0.5" style="color:#0a0a0a">
                  {{ selectedOrder.delivery_type === 'delivery'
                    ? (selectedOrder.delivery_address || 'Адрес не указан')
                    : 'ул. Кофейная, 42' }}
                </p>
              </div>
            </div>
            <div v-if="selectedOrder.comment" class="px-4 py-3">
              <p class="text-xs font-bold uppercase tracking-wider mb-1" style="color:#bbb">Комментарий</p>
              <p class="text-sm" style="color:#555">{{ selectedOrder.comment }}</p>
            </div>
          </div>

          <div style="border:1px solid #f0f0f0">
            <div class="px-4 py-3" style="border-bottom:1px solid #f0f0f0">
              <p class="text-xs font-bold uppercase tracking-[0.15em]" style="color:#bbb">Состав заказа</p>
            </div>
            <div v-for="item in selectedOrder.items" :key="item.id" class="flex items-center justify-between px-4 py-3" style="border-bottom:1px solid #f8f8f8">
              <div>
                <p class="text-sm font-bold" style="color:#0a0a0a">{{ item.item_name }}</p>
                <p class="text-xs mt-0.5" style="color:#bbb">{{ formatPrice(item.price) }} × {{ item.quantity }}</p>
              </div>
              <p class="text-sm font-black" style="color:#0a0a0a">{{ formatPrice(item.subtotal) }}</p>
            </div>
            <div class="flex items-center justify-between px-4 py-3">
              <span class="text-xs font-bold uppercase tracking-wider" style="color:#0a0a0a">Итого</span>
              <span class="font-black text-lg" style="color:#c1ce56">{{ formatPrice(selectedOrder.total_amount) }}</span>
            </div>
          </div>

          <p class="text-xs" style="color:#bbb">{{ formatDate(selectedOrder.created_at) }}</p>

        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ordersApi } from '@/api/orders'
import { formatPrice, formatDate, getStatusLabel } from '@/utils/format'

const orders = ref([])
const loading = ref(false)
const activeStatus = ref('all')
const selectedOrder = ref(null)

function openDetails(order) { selectedOrder.value = order }

const statusFilters = [
  { value: 'all', label: 'Все' },
  { value: 'new', label: 'Новые' },
  { value: 'confirmed', label: 'Подтверждены' },
  { value: 'preparing', label: 'Готовятся' },
  { value: 'ready', label: 'Готовы' },
  { value: 'completed', label: 'Выполнены' },
  { value: 'cancelled', label: 'Отменены' },
]

const orderStatuses = [
  { value: 'new', label: 'Новый' },
  { value: 'confirmed', label: 'Подтверждён' },
  { value: 'preparing', label: 'Готовится' },
  { value: 'ready', label: 'Готов' },
  { value: 'completed', label: 'Выполнен' },
  { value: 'cancelled', label: 'Отменён' },
]

const filteredOrders = computed(() =>
  activeStatus.value === 'all' ? orders.value : orders.value.filter(o => o.status === activeStatus.value)
)

const ordersWord = computed(() => {
  const n = filteredOrders.value.length
  if (n % 10 === 1 && n % 100 !== 11) return 'заказ'
  if ([2,3,4].includes(n % 10) && ![12,13,14].includes(n % 100)) return 'заказа'
  return 'заказов'
})

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

async function fetchOrders() {
  loading.value = true
  try {
    const r = await ordersApi.getAll({ limit: 200, skip: 0 })
    orders.value = r.data.items || r.data
  } finally {
    loading.value = false
  }
}

async function handleStatusChange(orderId, newStatus) {
  try {
    await ordersApi.updateStatus(orderId, newStatus)
    const order = orders.value.find(o => o.id === orderId)
    if (order) order.status = newStatus
  } catch (err) {
    alert(err.response?.data?.detail || 'Ошибка при смене статуса')
    await fetchOrders()
  }
}

onMounted(fetchOrders)
</script>

<template>
  <div>
    <div class="mb-10" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Дашборд</h1>
    </div>

    <div v-if="loading" class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-10">
      <div v-for="i in 4" :key="i" class="animate-pulse" style="background:#f5f5f3;height:100px;border:1px solid #f0f0f0"></div>
    </div>
    <div v-else class="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-10">
      <div style="background:#fff;border:1px solid #f0f0f0;padding:24px 20px">
        <p class="text-xs font-bold uppercase tracking-[0.15em] mb-3" style="color:#bbb">Заказов</p>
        <p class="font-black" style="font-size:2.2rem;color:#0a0a0a;line-height:1">{{ stats.ordersTotal }}</p>
      </div>
      <div style="background:#fff;border:1px solid #f0f0f0;padding:24px 20px">
        <p class="text-xs font-bold uppercase tracking-[0.15em] mb-3" style="color:#bbb">Ожидают</p>
        <p class="font-black" style="font-size:2.2rem;color:#c1ce56;line-height:1">{{ stats.ordersPending }}</p>
      </div>
      <div style="background:#fff;border:1px solid #f0f0f0;padding:24px 20px">
        <p class="text-xs font-bold uppercase tracking-[0.15em] mb-3" style="color:#bbb">Позиций меню</p>
        <p class="font-black" style="font-size:2.2rem;color:#0a0a0a;line-height:1">{{ stats.menuItems }}</p>
      </div>
      <div style="background:#fff;border:1px solid #f0f0f0;padding:24px 20px">
        <p class="text-xs font-bold uppercase tracking-[0.15em] mb-3" style="color:#bbb">Отзывов</p>
        <p class="font-black" style="font-size:2.2rem;color:#0a0a0a;line-height:1">{{ stats.reviews }}</p>
      </div>
    </div>

    <div style="background:#fff;border:1px solid #f0f0f0">
      <div class="px-6 py-5" style="border-bottom:1px solid #f0f0f0">
        <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#bbb">Последние заказы</p>
      </div>

      <div v-if="ordersLoading" class="px-6 py-8 flex flex-col gap-3">
        <div v-for="i in 5" :key="i" class="animate-pulse" style="background:#f5f5f3;height:44px"></div>
      </div>

      <div v-else-if="recentOrders.length" class="overflow-x-auto">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="border-bottom:1px solid #f0f0f0">
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">№</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Клиент</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Сумма</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Статус</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Дата</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="order in recentOrders"
              :key="order.id"
              style="border-bottom:1px solid #f8f8f8;cursor:default"
            >
              <td class="px-6 py-4 text-sm font-black" style="color:#0a0a0a">#{{ order.id }}</td>
              <td class="px-6 py-4 text-sm" style="color:#555">{{ order.user?.full_name || order.user?.email || '—' }}</td>
              <td class="px-6 py-4 text-sm font-black" style="color:#c1ce56">{{ formatPrice(order.total_amount) }}</td>
              <td class="px-6 py-4">
                <span class="text-xs font-bold uppercase tracking-wider px-2 py-1" :style="statusBadgeStyle(order.status)">
                  {{ getStatusLabel(order.status) }}
                </span>
              </td>
              <td class="px-6 py-4 text-xs" style="color:#bbb">{{ formatDate(order.created_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-else class="px-6 py-12 text-center">
        <p class="text-sm font-bold" style="color:#bbb">Заказов пока нет</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ordersApi } from '@/api/orders'
import { menuApi } from '@/api/menu'
import { reviewsApi } from '@/api/reviews'
import { formatPrice, formatDate, getStatusLabel } from '@/utils/format'

const loading = ref(false)
const ordersLoading = ref(false)
const recentOrders = ref([])
const stats = ref({ ordersTotal: 0, ordersPending: 0, menuItems: 0, reviews: 0 })

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
  ordersLoading.value = true
  try {
    const [ordersRes, menuRes, reviewsRes] = await Promise.all([
      ordersApi.getAll({ limit: 100 }),
      menuApi.getAll({ limit: 1 }),
      reviewsApi.getAll({ limit: 200 }),
    ])
    const allOrders = ordersRes.data.items || ordersRes.data
    stats.value.ordersTotal = ordersRes.data.total || allOrders.length
    stats.value.ordersPending = allOrders.filter(o => o.status === 'new').length
    stats.value.menuItems = menuRes.data.total || 0
    stats.value.reviews = Array.isArray(reviewsRes.data) ? reviewsRes.data.length : (reviewsRes.data.total || 0)
  } finally {
    loading.value = false
  }

  try {
    const r = await ordersApi.getAll({ limit: 10, skip: 0 })
    recentOrders.value = r.data.items || r.data
  } finally {
    ordersLoading.value = false
  }
})
</script>

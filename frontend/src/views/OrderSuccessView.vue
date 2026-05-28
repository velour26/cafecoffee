<template>
  <div style="background:#fff;min-height:100vh">
    <div class="max-w-2xl mx-auto px-6 py-24 flex flex-col items-center text-center">

      <div v-if="loading" class="animate-pulse flex flex-col items-center gap-6 w-full">
        <div style="width:80px;height:80px;background:#f0f0f0"></div>
        <div style="background:#f0f0f0;height:36px;width:280px"></div>
        <div style="background:#f0f0f0;height:16px;width:200px"></div>
      </div>

      <template v-else-if="order">
        <div
          class="flex items-center justify-center mb-8"
          style="width:80px;height:80px;background:#c1ce56"
        >
          <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"/>
          </svg>
        </div>

        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Заказ принят</p>
        <h1 class="font-black mb-3" style="font-size:clamp(2rem,4vw,3rem);color:#0a0a0a;line-height:1.1">
          Спасибо за заказ!
        </h1>
        <p class="text-base mb-10" style="color:#aaa">
          Ваш заказ <span style="color:#0a0a0a;font-weight:700">#{{ order.id }}</span> успешно оформлен
        </p>

        <div class="w-full mb-10" style="border:1px solid #f0f0f0">
          <div class="flex items-start gap-4 p-6" style="border-bottom:1px solid #f0f0f0">
            <div class="w-10 h-10 shrink-0 flex items-center justify-center" style="background:#f5f5f3">
              <svg v-if="order.delivery_type === 'delivery'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                <rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>
              </svg>
              <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div class="text-left">
              <p class="text-xs font-bold uppercase tracking-wider mb-1" style="color:#bbb">
                {{ order.delivery_type === 'delivery' ? 'Доставка' : 'Самовывоз' }}
              </p>
              <p class="text-sm font-bold" style="color:#0a0a0a">
                {{ order.delivery_type === 'delivery'
                  ? (order.delivery_address || 'Адрес не указан')
                  : 'ул. Кофейная, 42' }}
              </p>
            </div>
          </div>

          <div class="p-6" style="border-bottom:1px solid #f0f0f0">
            <p class="text-xs font-bold uppercase tracking-[0.2em] mb-4" style="color:#bbb">Состав заказа</p>
            <div class="space-y-2">
              <div
                v-for="oi in order.items"
                :key="oi.id"
                class="flex justify-between text-sm"
              >
                <span style="color:#555">{{ oi.item_name }} × {{ oi.quantity }}</span>
                <span class="font-bold" style="color:#0a0a0a">{{ formatPrice(oi.subtotal) }}</span>
              </div>
            </div>
          </div>

          <div class="p-6">
            <div class="flex items-center justify-between mb-4">
              <span class="text-sm font-bold uppercase tracking-wider" style="color:#0a0a0a">Итого</span>
              <span class="font-black text-xl" style="color:#c1ce56">{{ formatPrice(order.total_amount) }}</span>
            </div>
            <div v-if="order.comment" class="pt-4" style="border-top:1px solid #f0f0f0">
              <p class="text-xs" style="color:#aaa">Комментарий: <span style="color:#555">{{ order.comment }}</span></p>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-3 mb-10 px-5 py-3 w-full" style="background:#f9f9f7;border:1px solid #f0f0f0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
            <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>
          </svg>
          <p class="text-xs" style="color:#888">Мы уже начали готовить ваш заказ. Следите за статусом в разделе «Мои заказы».</p>
        </div>

        <div class="flex flex-col sm:flex-row gap-3 w-full">
          <RouterLink
            :to="{ name: 'my-orders' }"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-widest text-center transition-opacity hover:opacity-85"
            style="background:#2a2420;color:#f7f3ee"
          >Мои заказы</RouterLink>
          <RouterLink
            to="/menu"
            class="flex-1 py-3 text-xs font-bold uppercase tracking-widest text-center transition-all duration-200"
            style="color:#aaa;border:1px solid #e8e8e8"
            @mouseenter="e => { e.currentTarget.style.color='#0a0a0a'; e.currentTarget.style.borderColor='#0a0a0a' }"
            @mouseleave="e => { e.currentTarget.style.color='#aaa'; e.currentTarget.style.borderColor='#e8e8e8' }"
          >Продолжить покупки</RouterLink>
        </div>
      </template>

      <div v-else class="text-center">
        <p class="font-bold text-lg mb-4" style="color:#0a0a0a">Заказ не найден</p>
        <RouterLink to="/menu" class="text-xs font-bold uppercase tracking-widest px-6 py-3" style="background:#c1ce56;color:#0a0a0a">
          В меню
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { ordersApi } from '@/api/orders'
import { formatPrice } from '@/utils/format'

const $route = useRoute()
const order = ref(null)
const loading = ref(false)

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

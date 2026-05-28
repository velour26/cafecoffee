<template>
  <div style="background:#fff;min-height:100vh">

    <div style="background:#fff;border-bottom:1px solid #f0f0f0">
      <div class="max-w-7xl mx-auto px-6 py-14">
        <p class="text-xs font-bold uppercase tracking-[0.3em] mb-4" style="color:#c1ce56">Кофеёчек</p>
        <div class="flex items-end justify-between gap-4">
          <h1 class="font-black leading-none" style="font-size:clamp(2.5rem,5vw,4rem);color:#0a0a0a">Корзина</h1>
          <span v-if="!cartStore.loading && !cartStore.isEmpty" class="text-sm mb-2" style="color:#bbb">
            {{ cartStore.itemCount }} {{ itemWord }}
          </span>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-6 py-12">

      <div v-if="cartStore.loading" class="flex flex-col lg:flex-row gap-12">
        <div class="flex-1 space-y-4">
          <div v-for="i in 3" :key="i" class="animate-pulse flex gap-5 py-5" style="border-bottom:1px solid #f0f0f0">
            <div style="width:72px;height:72px;background:#f0f0f0;shrink:0"></div>
            <div class="flex-1 space-y-2 pt-1">
              <div style="background:#f0f0f0;height:14px;width:60%"></div>
              <div style="background:#f0f0f0;height:12px;width:30%"></div>
            </div>
          </div>
        </div>
        <div class="lg:w-80 animate-pulse" style="background:#f5f5f5;height:400px"></div>
      </div>

      <div v-else-if="cartStore.isEmpty" class="flex flex-col items-center justify-center py-32 gap-6">
        <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="1.2" stroke-linecap="round">
          <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
        </svg>
        <div class="text-center">
          <p class="font-black text-xl mb-2" style="color:#0a0a0a">Корзина пуста</p>
          <p class="text-sm" style="color:#aaa">Добавьте что-нибудь из нашего меню</p>
        </div>
        <RouterLink
          to="/menu"
          class="text-xs font-bold uppercase tracking-widest px-8 py-4 transition-opacity hover:opacity-85"
          style="background:#c1ce56;color:#0a0a0a"
        >Перейти в меню</RouterLink>
      </div>

      <div v-else class="flex flex-col lg:flex-row gap-12">

        <div class="flex-1 min-w-0">
          <CartItemRow
            v-for="cartItem in cartStore.items"
            :key="cartItem.id"
            :item="cartItem"
            @update="handleUpdate"
            @remove="handleRemove"
          />

          <div class="pt-6">
            <button
              @click="handleClear"
              :disabled="clearing"
              class="text-xs uppercase tracking-widest transition-colors"
              style="color:#ccc"
              @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
              @mouseleave="e => e.currentTarget.style.color='#ccc'"
            >Очистить корзину</button>
          </div>
        </div>

        <div class="lg:w-80 shrink-0">
          <div class="sticky top-24" style="border:1px solid #f0f0f0">

            <div class="p-6" style="border-bottom:1px solid #f0f0f0">
              <p class="text-xs font-bold uppercase tracking-[0.2em] mb-5" style="color:#bbb">Ваш заказ</p>

              <div class="space-y-2 mb-4">
                <div
                  v-for="cartItem in cartStore.items"
                  :key="cartItem.id"
                  class="flex justify-between text-sm"
                >
                  <span class="truncate mr-2" style="color:#888">
                    {{ cartItem.menu_item?.name }} × {{ cartItem.quantity }}
                  </span>
                  <span class="shrink-0 font-bold" style="color:#0a0a0a">
                    {{ formatPrice((cartItem.menu_item?.price || 0) * cartItem.quantity) }}
                  </span>
                </div>
              </div>

              <div class="flex items-center justify-between pt-4" style="border-top:1px solid #f0f0f0">
                <span class="text-sm font-bold uppercase tracking-wider" style="color:#0a0a0a">Итого</span>
                <span class="font-black text-xl" style="color:#c1ce56">{{ formatPrice(cartStore.total) }}</span>
              </div>
            </div>

            <div class="p-6" style="border-bottom:1px solid #f0f0f0">
              <p class="text-xs font-bold uppercase tracking-[0.2em] mb-4" style="color:#bbb">Способ получения</p>

              <div class="flex gap-2 mb-4">
                <button
                  @click="deliveryType = 'pickup'"
                  class="flex-1 py-2.5 text-xs font-bold uppercase tracking-wider transition-all duration-200"
                  :style="deliveryType === 'pickup'
                    ? 'background:#2a2420;color:#f7f3ee'
                    : 'background:#fff;color:#aaa;border:1px solid #e8e8e8'"
                >Самовывоз</button>
                <button
                  @click="deliveryType = 'delivery'"
                  class="flex-1 py-2.5 text-xs font-bold uppercase tracking-wider transition-all duration-200"
                  :style="deliveryType === 'delivery'
                    ? 'background:#2a2420;color:#f7f3ee'
                    : 'background:#fff;color:#aaa;border:1px solid #e8e8e8'"
                >Доставка</button>
              </div>

              <div v-if="deliveryType === 'pickup'" class="flex items-start gap-3">
                <svg class="shrink-0 mt-0.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2" stroke-linecap="round">
                  <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
                </svg>
                <p class="text-xs leading-relaxed" style="color:#888">
                  Заберите заказ самостоятельно по адресу:<br>
                  <span class="font-bold" style="color:#0a0a0a">ул. Кофейная, 42</span>
                </p>
              </div>

              <div v-else class="flex flex-col gap-2">
                <label class="text-xs font-bold uppercase tracking-[0.15em]" style="color:#888">Адрес доставки</label>
                <input
                  v-model="deliveryAddress"
                  type="text"
                  placeholder="Улица, дом, квартира..."
                  class="w-full px-3 py-2.5 text-sm outline-none transition-all duration-200"
                  style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
                  @focus="e => e.target.style.borderColor='#0a0a0a'"
                  @blur="e => e.target.style.borderColor='#e8e8e8'"
                />
              </div>
            </div>

            <div class="p-6" style="border-bottom:1px solid #f0f0f0">
              <p class="text-xs font-bold uppercase tracking-[0.2em] mb-3" style="color:#bbb">
                Комментарий <span style="color:#ddd;font-weight:400">(необязательно)</span>
              </p>
              <textarea
                v-model="comment"
                rows="2"
                placeholder="Пожелания к заказу..."
                class="w-full px-3 py-2.5 text-sm outline-none resize-none transition-all duration-200"
                style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
                @focus="e => e.target.style.borderColor='#0a0a0a'"
                @blur="e => e.target.style.borderColor='#e8e8e8'"
              ></textarea>
            </div>

            <div v-if="orderError" class="px-6 pt-4">
              <p class="text-xs" style="color:#e53e3e">{{ orderError }}</p>
            </div>

            <div class="p-6">
              <button
                @click="handleCreateOrder"
                :disabled="ordering || (deliveryType === 'delivery' && !deliveryAddress.trim())"
                class="w-full py-4 text-xs font-bold uppercase tracking-widest transition-opacity"
                style="background:#c1ce56;color:#0a0a0a"
                :style="(ordering || (deliveryType === 'delivery' && !deliveryAddress.trim())) ? 'opacity:0.4;cursor:not-allowed' : ''"
              >
                {{ ordering ? '—' : 'Оформить заказ' }}
              </button>
              <p v-if="deliveryType === 'delivery' && !deliveryAddress.trim()" class="text-xs mt-2 text-center" style="color:#bbb">
                Укажите адрес доставки
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useCartStore } from '@/stores/cart'
import { ordersApi } from '@/api/orders'
import { formatPrice } from '@/utils/format'
import CartItemRow from '@/components/CartItemRow.vue'

const cartStore = useCartStore()
const $router = useRouter()

const deliveryType = ref('pickup')
const deliveryAddress = ref('')
const comment = ref('')
const ordering = ref(false)
const orderError = ref('')
const clearing = ref(false)

const itemWord = computed(() => {
  const n = cartStore.itemCount
  if (n % 10 === 1 && n % 100 !== 11) return 'товар'
  if ([2, 3, 4].includes(n % 10) && ![12, 13, 14].includes(n % 100)) return 'товара'
  return 'товаров'
})

async function handleUpdate(id, qty) {
  if (qty < 1) {
    await cartStore.removeItem(id)
  } else {
    await cartStore.updateItem(id, qty)
  }
}

async function handleRemove(id) {
  await cartStore.removeItem(id)
}

async function handleClear() {
  clearing.value = true
  try { await cartStore.clearCart() } finally { clearing.value = false }
}

async function handleCreateOrder() {
  if (deliveryType.value === 'delivery' && !deliveryAddress.value.trim()) return
  ordering.value = true
  orderError.value = ''
  try {
    const r = await ordersApi.create({
      delivery_type: deliveryType.value,
      delivery_address: deliveryType.value === 'delivery' ? deliveryAddress.value.trim() : null,
      comment: comment.value.trim() || null,
    })
    await cartStore.fetchCart()
    $router.push({ name: 'order-success', params: { id: r.data.id } })
  } catch (err) {
    orderError.value = err.response?.data?.detail || 'Ошибка при создании заказа'
  } finally {
    ordering.value = false
  }
}

onMounted(() => cartStore.fetchCart())
</script>

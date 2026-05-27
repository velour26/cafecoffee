<template>
  <div
    class="group cursor-pointer flex flex-col overflow-hidden transition-all duration-300"
    style="background:#fff;border:1px solid #f0f0f0"
    @click="$router.push({ name: 'menu-item', params: { id: item.id } })"
    @mouseenter="e => e.currentTarget.style.borderColor='#ddd'"
    @mouseleave="e => e.currentTarget.style.borderColor='#f0f0f0'"
  >
    <div class="relative overflow-hidden" style="height:200px;background:#f5f5f3">
      <img
        v-if="item.image_url && !imageError"
        :src="item.image_url"
        :alt="item.name"
        class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        style="filter:brightness(0.85)"
        @error="imageError = true"
      />
      <div
        v-else
        class="w-full h-full flex items-center justify-center"
        style="background:#f0f0ee"
      >
        <svg width="48" height="48" viewBox="0 0 80 96" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:.15">
          <path d="M10 32 L16 84 H64 L70 32 Z" fill="none" stroke="#fff" stroke-width="2"/>
          <ellipse cx="40" cy="32" rx="30" ry="8" fill="none" stroke="#fff" stroke-width="2"/>
          <path d="M64 47 Q80 47 80 57 Q80 67 64 67" stroke="#fff" stroke-width="2" fill="none"/>
        </svg>
      </div>

      <div
        v-if="!item.is_available"
        class="absolute inset-0 flex items-center justify-center"
        style="background:rgba(0,0,0,.6)"
      >
        <span class="text-xs font-bold uppercase tracking-widest px-3 py-1.5" style="color:#fff;border:1px solid #fff">
          Недоступно
        </span>
      </div>

      <span
        v-if="item.category"
        class="absolute top-3 left-3 text-xs font-bold uppercase tracking-wider px-2.5 py-1"
        style="background:rgba(255,255,255,.85);color:#888;backdrop-filter:blur(4px)"
      >{{ item.category.name }}</span>

      <Transition name="fade">
        <div
          v-if="item.is_available"
          class="absolute inset-0 flex items-end p-3 opacity-0 group-hover:opacity-100 transition-opacity duration-300"
          style="background:linear-gradient(to top,rgba(0,0,0,.7) 0%,transparent 60%)"
        >
          <button
            @click.stop="handleAddToCart"
            :disabled="addingToCart"
            class="w-full py-2.5 text-xs font-bold uppercase tracking-widest transition-all duration-200"
            :style="added
              ? 'background:#c1ce56;color:#0a0a0a'
              : 'background:rgba(255,255,255,.15);color:#fff;border:1px solid rgba(255,255,255,.3);backdrop-filter:blur(4px)'"
            @mouseenter="e => { if(!added) e.currentTarget.style.background='#c1ce56'; if(!added) e.currentTarget.style.color='#0a0a0a' }"
            @mouseleave="e => { if(!added) e.currentTarget.style.background='rgba(255,255,255,.15)'; if(!added) e.currentTarget.style.color='#fff' }"
          >
            <span v-if="addingToCart">—</span>
            <span v-else-if="added">Добавлено</span>
            <span v-else>+ В корзину</span>
          </button>
        </div>
      </Transition>
    </div>

    <div class="flex flex-col flex-1 p-4 gap-2">
      <div class="flex items-start justify-between gap-2">
        <h3 class="font-bold text-sm leading-tight" style="color:#0a0a0a">
          {{ item.name }}
        </h3>
        <span class="font-black text-sm shrink-0" style="color:#c1ce56">
          {{ formatPrice(item.price) }}
        </span>
      </div>

      <p v-if="item.description" class="text-xs leading-relaxed line-clamp-2" style="color:#888">
        {{ item.description }}
      </p>

      <div v-if="item.weight_grams" class="mt-auto">
        <span class="text-xs" style="color:#bbb">{{ item.weight_grams }} г</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useCartStore } from '@/stores/cart'
import { formatPrice } from '@/utils/format'

const props = defineProps({
  item: { type: Object, required: true },
  onAddSuccess: { type: Function, default: null },
})

const $router = useRouter()
const authStore = useAuthStore()
const cartStore = useCartStore()
const addingToCart = ref(false)
const imageError = ref(false)
const added = ref(false)

async function handleAddToCart() {
  if (!authStore.isAuthenticated) { $router.push('/login'); return }
  addingToCart.value = true
  try {
    const result = await cartStore.addToCart(props.item.id, 1)
    if (result?.success) {
      added.value = true
      props.onAddSuccess?.(props.item.name)
      setTimeout(() => { added.value = false }, 2000)
    }
  } finally {
    addingToCart.value = false
  }
}
</script>

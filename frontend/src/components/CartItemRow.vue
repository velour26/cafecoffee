<template>
  <div
    class="flex items-center gap-5 py-5 transition-all duration-200"
    style="border-bottom:1px solid #f0f0f0"
  >
    <div class="shrink-0 overflow-hidden" style="width:72px;height:72px;background:#f5f5f3">
      <img
        v-if="item.menu_item?.image_url"
        :src="item.menu_item.image_url"
        :alt="item.menu_item?.name"
        class="w-full h-full object-cover"
        style="filter:brightness(0.9)"
      />
      <div v-else class="w-full h-full flex items-center justify-center">
        <svg width="28" height="34" viewBox="0 0 80 96" fill="none" style="opacity:.15">
          <path d="M10 32 L16 84 H64 L70 32 Z" fill="none" stroke="#000" stroke-width="3"/>
          <ellipse cx="40" cy="32" rx="30" ry="8" fill="none" stroke="#000" stroke-width="3"/>
          <path d="M64 47 Q80 47 80 57 Q80 67 64 67" stroke="#000" stroke-width="3" fill="none"/>
        </svg>
      </div>
    </div>

    <div class="flex-1 min-w-0">
      <p class="font-bold text-sm mb-1 truncate" style="color:#0a0a0a">
        {{ item.menu_item?.name || 'Позиция удалена' }}
      </p>
      <p class="text-xs" style="color:#aaa">
        {{ formatPrice(item.menu_item?.price || 0) }} за шт.
      </p>
    </div>

    <div class="flex items-center shrink-0" style="border:1px solid #e8e8e8">
      <button
        @click="$emit('update', item.id, item.quantity - 1)"
        class="w-9 h-9 flex items-center justify-center text-base font-bold transition-colors"
        style="color:#bbb"
        @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
        @mouseleave="e => e.currentTarget.style.color='#bbb'"
      >−</button>
      <span class="w-8 text-center text-sm font-bold" style="color:#0a0a0a">{{ item.quantity }}</span>
      <button
        @click="$emit('update', item.id, item.quantity + 1)"
        class="w-9 h-9 flex items-center justify-center text-base font-bold transition-colors"
        style="color:#bbb"
        @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
        @mouseleave="e => e.currentTarget.style.color='#bbb'"
      >+</button>
    </div>

    <p class="text-sm font-black w-20 text-right shrink-0" style="color:#0a0a0a">
      {{ formatPrice((item.menu_item?.price || 0) * item.quantity) }}
    </p>

    <button
      @click="$emit('remove', item.id)"
      class="shrink-0 w-7 h-7 flex items-center justify-center transition-colors"
      style="color:#ddd"
      @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
      @mouseleave="e => e.currentTarget.style.color='#ddd'"
      title="Удалить"
    >
      <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
        <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
      </svg>
    </button>
  </div>
</template>

<script setup>
import { formatPrice } from '@/utils/format'
defineProps({ item: { type: Object, required: true } })
defineEmits(['update', 'remove'])
</script>

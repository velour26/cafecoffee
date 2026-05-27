<template>
  <div
    class="flex flex-col gap-4 p-6 transition-all duration-300"
    style="background:#fff;border:1px solid #f0f0f0"
    @mouseenter="e => e.currentTarget.style.borderColor='#ddd'"
    @mouseleave="e => e.currentTarget.style.borderColor='#f0f0f0'"
  >
    <div class="flex items-start justify-between gap-3">
      <div class="flex items-center gap-3">
        <div
          class="w-10 h-10 shrink-0 flex items-center justify-center text-xs font-black"
          style="background:#c1ce56;color:#0a0a0a"
        >
          {{ initials }}
        </div>
        <div>
          <p class="text-sm font-bold leading-tight" style="color:#0a0a0a">
            {{ review.user?.full_name || 'Гость' }}
          </p>
          <p class="text-xs mt-0.5" style="color:#bbb">{{ formatDate(review.created_at) }}</p>
        </div>
      </div>

      <div class="flex items-center gap-0.5 shrink-0">
        <svg
          v-for="i in 5"
          :key="i"
          width="14" height="14" viewBox="0 0 24 24"
          :fill="i <= review.rating ? '#c1ce56' : 'none'"
          :stroke="i <= review.rating ? '#c1ce56' : '#ddd'"
          stroke-width="1.5"
        >
          <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
        </svg>
      </div>
    </div>

    <p v-if="review.text" class="text-sm leading-relaxed flex-1" style="color:#555">
      {{ review.text }}
    </p>
    <p v-else class="text-sm italic" style="color:#ccc">Без текста</p>

    <div v-if="review.menu_item" class="flex items-center gap-2 pt-2" style="border-top:1px solid #f5f5f5">
      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2.5" stroke-linecap="round">
        <path d="M20 10c0 7-9 13-9 13S2 17 2 10a9 9 0 0 1 18 0z"/><circle cx="11" cy="10" r="2"/>
      </svg>
      <span class="text-xs font-bold uppercase tracking-wider" style="color:#c1ce56">
        {{ review.menu_item.name }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { formatDate } from '@/utils/format'

const props = defineProps({
  review: { type: Object, required: true },
})

const initials = computed(() => {
  const name = props.review.user?.full_name || 'Г'
  return name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2)
})
</script>

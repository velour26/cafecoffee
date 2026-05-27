<template>
  <RouterLink to="/" class="inline-flex items-center gap-3 hover:opacity-80 transition-opacity shrink-0">
    <svg :width="size" :height="size" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="36" height="36" rx="8" :fill="dark ? '#c1ce56' : '#c1ce56'"/>
      <path d="M10 13 L12 26 H24 L26 13 Z" :fill="dark ? '#0a0a0a' : '#0a0a0a'" />
      <rect x="10" y="11" width="16" height="3" rx="1.5" :fill="dark ? '#0a0a0a' : '#0a0a0a'" />
      <path d="M24 17 Q29 17 29 20.5 Q29 24 24 24" :stroke="dark ? '#0a0a0a' : '#0a0a0a'" stroke-width="2" fill="none" stroke-linecap="round"/>
      <path d="M16 9 C15.5 7.5 16.5 6 16 4.5" :stroke="dark ? '#0a0a0a' : '#0a0a0a'" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.6"/>
      <path d="M20 9 C19.5 7.5 20.5 6 20 4.5" :stroke="dark ? '#0a0a0a' : '#0a0a0a'" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.6"/>
    </svg>
    <span
      v-if="!iconOnly"
      class="font-black tracking-tight leading-none select-none"
      :style="{ fontSize: fontSize, color: dark ? '#fff' : '#0a0a0a' }"
    >Кофеёчек</span>
  </RouterLink>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  dark:     { type: Boolean, default: true },
  iconOnly: { type: Boolean, default: false },
  size:     { type: Number,  default: 36 },
  fontSize: { type: String,  default: '1.1rem' },
})
</script>

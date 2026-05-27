<template>
  <div class="flex flex-col items-center justify-center py-20 text-center">
    <div class="text-6xl mb-4">{{ icon }}</div>
    <h3 class="text-lg font-semibold text-gray-700 mb-2">{{ title }}</h3>
    <p v-if="subtitle" class="text-sm text-gray-500 max-w-sm mb-6">{{ subtitle }}</p>
    <slot />
  </div>
</template>

<script setup>
defineProps({
  icon: { type: String, default: '📭' },
  title: { type: String, default: 'Ничего не найдено' },
  subtitle: { type: String, default: '' },
})
</script>

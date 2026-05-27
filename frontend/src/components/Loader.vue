<template>
  <div class="flex flex-col items-center justify-center py-16 gap-3">
    <div class="relative w-12 h-12">
      <div class="absolute inset-0 border-4 border-coffee-200 rounded-full"></div>
      <div
        class="absolute inset-0 border-4 border-coffee-600 rounded-full border-t-transparent animate-spin"
      ></div>
    </div>
    <p v-if="text" class="text-sm text-gray-500">{{ text }}</p>
  </div>
</template>

<script setup>
defineProps({ text: { type: String, default: 'Загрузка...' } })
</script>

<template>
  <RouterLink
    :to="{ name: 'menu', query: { category_id: category.id } }"
    class="card p-6 flex flex-col items-center text-center hover:shadow-md transition-all hover:-translate-y-0.5 cursor-pointer group"
  >
    <div class="text-5xl mb-3 group-hover:scale-110 transition-transform">{{ emoji }}</div>
    <h3 class="font-semibold text-gray-800 group-hover:text-coffee-700 transition-colors">
      {{ category.name }}
    </h3>
    <p v-if="category.description" class="text-sm text-gray-500 mt-1 line-clamp-2">
      {{ category.description }}
    </p>
  </RouterLink>
</template>

<script setup>
import { computed } from 'vue'
import { RouterLink } from 'vue-router'

const props = defineProps({
  category: { type: Object, required: true },
})

const emoji = computed(() => {
  const name = props.category.name?.toLowerCase() || ''
  if (name.includes('кофе')) return '☕'
  if (name.includes('чай')) return '🍵'
  if (name.includes('десерт')) return '🍰'
  if (name.includes('завтрак')) return '🍳'
  return '🍽️'
})
</script>

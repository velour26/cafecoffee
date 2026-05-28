<template>
  <div class="flex flex-col gap-6">

    <div class="relative">
      <svg class="absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2" stroke-linecap="round">
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>
      <input
        v-model="localSearch"
        type="text"
        placeholder="Поиск по меню..."
        class="w-full pl-10 pr-4 py-3 text-sm outline-none transition-all duration-200"
        style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
        @focus="e => e.target.style.borderColor='#0a0a0a'"
        @blur="e => e.target.style.borderColor='#e8e8e8'"
        @keydown.enter="handleApply"
      />
    </div>

    <div>
      <p class="text-xs font-bold uppercase tracking-[0.2em] mb-4" style="color:#bbb">Категория</p>
      <div class="flex flex-col gap-1.5">
        <button
          @click="selectCategory(null)"
          class="text-left text-sm font-medium px-3 py-2 transition-all duration-200"
          :style="!localCategory
            ? 'color:#0a0a0a;border-left:2px solid #c1ce56;padding-left:10px;font-weight:700'
            : 'color:#aaa;border-left:2px solid transparent;padding-left:10px'"
          @mouseenter="e => { if(localCategory !== null) e.currentTarget.style.color='#0a0a0a' }"
          @mouseleave="e => { if(localCategory !== null) e.currentTarget.style.color='#aaa' }"
        >Все категории</button>
        <button
          v-for="cat in categories"
          :key="cat.id"
          @click="selectCategory(cat.id)"
          class="text-left text-sm font-medium px-3 py-2 transition-all duration-200"
          :style="localCategory === cat.id
            ? 'color:#0a0a0a;border-left:2px solid #c1ce56;padding-left:10px;font-weight:700'
            : 'color:#aaa;border-left:2px solid transparent;padding-left:10px'"
          @mouseenter="e => { if(localCategory !== cat.id) e.currentTarget.style.color='#0a0a0a' }"
          @mouseleave="e => { if(localCategory !== cat.id) e.currentTarget.style.color='#aaa' }"
        >{{ cat.name }}</button>
      </div>
    </div>

    <div style="border-top:1px solid #f0f0f0"></div>

    <div>
      <p class="text-xs font-bold uppercase tracking-[0.2em] mb-4" style="color:#bbb">Цена, ₽</p>
      <div class="grid grid-cols-2 gap-3">
        <input
          v-model.number="localMinPrice"
          type="number"
          placeholder="от"
          min="0"
          class="w-full px-3 py-2.5 text-sm outline-none transition-all duration-200"
          style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
          @focus="e => e.target.style.borderColor='#0a0a0a'"
          @blur="e => e.target.style.borderColor='#e8e8e8'"
        />
        <input
          v-model.number="localMaxPrice"
          type="number"
          placeholder="до"
          min="0"
          class="w-full px-3 py-2.5 text-sm outline-none transition-all duration-200"
          style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
          @focus="e => e.target.style.borderColor='#0a0a0a'"
          @blur="e => e.target.style.borderColor='#e8e8e8'"
        />
      </div>
    </div>

    <div class="flex flex-col gap-2">
      <button
        @click="handleApply"
        class="w-full py-3 text-xs font-bold uppercase tracking-widest transition-opacity hover:opacity-85"
        style="background:#c1ce56;color:#0a0a0a"
      >Применить</button>
      <button
        @click="handleReset"
        class="w-full py-3 text-xs font-semibold uppercase tracking-widest transition-all duration-200"
        style="background:transparent;color:#bbb;border:1px solid #e8e8e8"
        @mouseenter="e => { e.currentTarget.style.color='#0a0a0a'; e.currentTarget.style.borderColor='#0a0a0a' }"
        @mouseleave="e => { e.currentTarget.style.color='#bbb'; e.currentTarget.style.borderColor='#e8e8e8' }"
      >Сбросить</button>
    </div>

  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  categories:      { type: Array,  default: () => [] },
  initialCategory: { type: Number, default: null },
  initialSearch:   { type: String, default: '' },
})
const emit = defineEmits(['filter'])

const localSearch   = ref(props.initialSearch)
const localCategory = ref(props.initialCategory)

watch(() => props.initialSearch, (val) => { localSearch.value = val })
const localMinPrice = ref(null)
const localMaxPrice = ref(null)

function handleApply() {
  emit('filter', {
    search: localSearch.value || undefined,
    category_id: localCategory.value || undefined,
    min_price: localMinPrice.value || undefined,
    max_price: localMaxPrice.value || undefined,
  })
}

// Категория применяется мгновенно при клике (без кнопки «Применить»)
function selectCategory(catId) {
  localCategory.value = catId
  handleApply()
}

function handleReset() {
  localSearch.value = ''
  localCategory.value = null
  localMinPrice.value = null
  localMaxPrice.value = null
  emit('filter', {})
}
</script>

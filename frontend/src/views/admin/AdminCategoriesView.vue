<template>
  <div>
    <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Категории</h1>
        <button
          @click="openCreate"
          class="flex items-center gap-2 text-xs font-bold uppercase tracking-widest px-5 py-2.5 mb-0.5 transition-opacity hover:opacity-80"
          style="background:#c1ce56;color:#0a0a0a"
        >
          <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
          Добавить
        </button>
      </div>
    </div>

    <div v-if="loading" class="flex flex-col gap-2">
      <div v-for="i in 4" :key="i" class="animate-pulse" style="background:#f5f5f3;height:56px;border:1px solid #f0f0f0"></div>
    </div>

    <div v-else style="background:#fff;border:1px solid #f0f0f0">
      <div v-if="categories.length" class="overflow-x-auto">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="border-bottom:1px solid #f0f0f0">
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">ID</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Название</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Описание</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-6 py-3" style="color:#bbb;background:#fafafa">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="cat in categories" :key="cat.id" style="border-bottom:1px solid #f8f8f8">
              <td class="px-6 py-4 text-xs font-bold" style="color:#bbb">{{ cat.id }}</td>
              <td class="px-6 py-4 text-sm font-bold" style="color:#0a0a0a">{{ cat.name }}</td>
              <td class="px-6 py-4 text-sm" style="color:#888">{{ cat.description || '—' }}</td>
              <td class="px-6 py-4">
                <div class="flex items-center gap-4">
                  <button
                    @click="openEdit(cat)"
                    class="text-xs font-bold uppercase tracking-wider transition-colors"
                    style="color:#0a0a0a"
                    @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
                    @mouseleave="e => e.currentTarget.style.color='#0a0a0a'"
                  >Изменить</button>
                  <button
                    @click="confirmDelete(cat.id)"
                    class="text-xs font-bold uppercase tracking-wider transition-colors"
                    style="color:#bbb"
                    @mouseenter="e => e.currentTarget.style.color='#e53e3e'"
                    @mouseleave="e => e.currentTarget.style.color='#bbb'"
                  >Удалить</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="px-6 py-14 text-center">
        <p class="text-sm font-bold" style="color:#bbb">Категорий нет</p>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center px-4" style="background:rgba(0,0,0,0.5)" @click.self="closeModal">
      <div style="background:#fff;width:100%;max-width:440px">
        <div class="flex items-center justify-between px-6 py-5" style="border-bottom:1px solid #f0f0f0">
          <p class="text-sm font-black" style="color:#0a0a0a">{{ editingId ? 'Редактировать категорию' : 'Новая категория' }}</p>
          <button @click="closeModal" style="color:#bbb" @mouseenter="e => e.currentTarget.style.color='#0a0a0a'" @mouseleave="e => e.currentTarget.style.color='#bbb'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
        <form @submit.prevent="handleSave" class="px-6 py-6 flex flex-col gap-4">
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Название</label>
            <input
              v-model="form.name" type="text" required
              class="w-full px-4 py-3 text-sm outline-none transition-all"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Описание</label>
            <input
              v-model="form.description" type="text"
              class="w-full px-4 py-3 text-sm outline-none transition-all"
              style="background:#fff;border:1px solid #e8e8e8;color:#0a0a0a"
              @focus="e => e.target.style.borderColor='#0a0a0a'"
              @blur="e => e.target.style.borderColor='#e8e8e8'"
            />
          </div>
          <div v-if="formError" class="px-4 py-3 text-xs" style="background:#fff5f5;color:#e53e3e;border:1px solid #fed7d7">{{ formError }}</div>
          <div class="flex gap-3 justify-end pt-2">
            <button type="button" @click="closeModal" class="px-5 py-2.5 text-xs font-bold uppercase tracking-wider transition-colors" style="border:1px solid #e8e8e8;color:#888" @mouseenter="e => e.currentTarget.style.borderColor='#0a0a0a'" @mouseleave="e => e.currentTarget.style.borderColor='#e8e8e8'">Отмена</button>
            <button type="submit" :disabled="saving" class="px-6 py-2.5 text-xs font-bold uppercase tracking-wider transition-opacity" style="background:#0a0a0a;color:#fff" :style="saving ? 'opacity:0.5' : ''">
              {{ saving ? '—' : 'Сохранить' }}
            </button>
          </div>
        </form>
      </div>
    </div>

    <div v-if="deleteId" class="fixed inset-0 z-50 flex items-center justify-center px-4" style="background:rgba(0,0,0,0.5)" @click.self="deleteId = null">
      <div style="background:#fff;width:100%;max-width:360px">
        <div class="px-6 py-6">
          <p class="font-black text-base mb-2" style="color:#0a0a0a">Удалить категорию?</p>
          <p class="text-sm" style="color:#888">Это действие нельзя отменить.</p>
        </div>
        <div class="flex" style="border-top:1px solid #f0f0f0">
          <button @click="deleteId = null" class="flex-1 py-3 text-xs font-bold uppercase tracking-wider" style="color:#888;border-right:1px solid #f0f0f0" @mouseenter="e => e.currentTarget.style.color='#0a0a0a'" @mouseleave="e => e.currentTarget.style.color='#888'">Отмена</button>
          <button @click="handleDelete" :disabled="deleting" class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-opacity" style="color:#e53e3e" :style="deleting ? 'opacity:0.5' : ''" @mouseenter="e => !deleting && (e.currentTarget.style.background='#fff5f5')" @mouseleave="e => e.currentTarget.style.background='#fff'">
            {{ deleting ? '—' : 'Удалить' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { categoriesApi } from '@/api/categories'

const categories = ref([])
const loading = ref(false)
const showModal = ref(false)
const editingId = ref(null)
const form = ref({ name: '', description: '' })
const saving = ref(false)
const formError = ref('')
const deleteId = ref(null)
const deleting = ref(false)

async function fetchCategories() {
  loading.value = true
  try {
    const r = await categoriesApi.getAll()
    categories.value = r.data
  } finally {
    loading.value = false
  }
}

function openCreate() {
  editingId.value = null
  form.value = { name: '', description: '' }
  formError.value = ''
  showModal.value = true
}

function openEdit(cat) {
  editingId.value = cat.id
  form.value = { name: cat.name, description: cat.description || '' }
  formError.value = ''
  showModal.value = true
}

function closeModal() { showModal.value = false }

async function handleSave() {
  saving.value = true
  formError.value = ''
  try {
    const payload = { name: form.value.name, description: form.value.description || null }
    if (editingId.value) {
      await categoriesApi.update(editingId.value, payload)
    } else {
      await categoriesApi.create(payload)
    }
    closeModal()
    await fetchCategories()
  } catch (err) {
    formError.value = err.response?.data?.detail || 'Ошибка при сохранении'
  } finally {
    saving.value = false
  }
}

function confirmDelete(id) { deleteId.value = id }

async function handleDelete() {
  deleting.value = true
  try {
    await categoriesApi.delete(deleteId.value)
    deleteId.value = null
    await fetchCategories()
  } catch (err) {
    alert(err.response?.data?.detail || 'Ошибка при удалении')
  } finally {
    deleting.value = false
  }
}

onMounted(fetchCategories)
</script>

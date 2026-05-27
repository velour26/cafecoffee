<template>
  <div>
    <div class="mb-8" style="border-bottom:1px solid #f0f0f0;padding-bottom:2rem">
      <p class="text-xs font-bold uppercase tracking-[0.3em] mb-2" style="color:#c1ce56">Администрирование</p>
      <div class="flex items-end justify-between gap-4">
        <h1 class="font-black" style="font-size:2rem;color:#0a0a0a;line-height:1">Меню</h1>
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

    <div v-if="fetchError" class="px-4 py-3 text-xs mb-6" style="background:#fff5f5;color:#e53e3e;border:1px solid #fed7d7">{{ fetchError }}</div>

    <div v-if="loading" class="flex flex-col gap-2">
      <div v-for="i in 5" :key="i" class="animate-pulse" style="background:#f5f5f3;height:56px;border:1px solid #f0f0f0"></div>
    </div>

    <div v-else style="background:#fff;border:1px solid #f0f0f0">
      <div v-if="items.length" class="overflow-x-auto">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="border-bottom:1px solid #f0f0f0">
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Название</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Категория</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Цена</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Доступность</th>
              <th class="text-left text-xs font-bold uppercase tracking-[0.15em] px-5 py-3" style="color:#bbb;background:#fafafa">Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items" :key="item.id" style="border-bottom:1px solid #f8f8f8">
              <td class="px-5 py-4 text-sm font-bold" style="color:#0a0a0a">{{ item.name }}</td>
              <td class="px-5 py-4 text-sm" style="color:#888">{{ item.category?.name || '—' }}</td>
              <td class="px-5 py-4 text-sm font-black" style="color:#c1ce56">{{ formatPrice(item.price) }}</td>
              <td class="px-5 py-4">
                <span
                  class="text-xs font-bold uppercase tracking-wider px-2 py-1"
                  :style="item.is_available
                    ? 'background:#f0fff4;color:#276749'
                    : 'background:#fff5f5;color:#c53030'"
                >{{ item.is_available ? 'Доступно' : 'Недоступно' }}</span>
              </td>
              <td class="px-5 py-4">
                <div class="flex items-center gap-4">
                  <button
                    @click="openEdit(item)"
                    class="text-xs font-bold uppercase tracking-wider"
                    style="color:#0a0a0a"
                    @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
                    @mouseleave="e => e.currentTarget.style.color='#0a0a0a'"
                  >Изменить</button>
                  <button
                    @click="confirmDelete(item.id)"
                    class="text-xs font-bold uppercase tracking-wider"
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
        <p class="text-sm font-bold" style="color:#bbb">Позиций нет</p>
      </div>
    </div>

    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center px-4 py-8 overflow-y-auto" style="background:rgba(0,0,0,0.5)" @click.self="closeModal">
      <div style="background:#fff;width:100%;max-width:500px">
        <div class="flex items-center justify-between px-6 py-5" style="border-bottom:1px solid #f0f0f0">
          <p class="text-sm font-black" style="color:#0a0a0a">{{ editingId ? 'Редактировать позицию' : 'Новая позиция' }}</p>
          <button @click="closeModal" style="color:#bbb" @mouseenter="e => e.currentTarget.style.color='#0a0a0a'" @mouseleave="e => e.currentTarget.style.color='#bbb'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          </button>
        </div>
        <form @submit.prevent="handleSave" class="px-6 py-6 flex flex-col gap-4">
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Название</label>
            <input v-model="form.name" type="text" required class="w-full px-4 py-3 text-sm outline-none" style="border:1px solid #e8e8e8;color:#0a0a0a" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'" />
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Описание</label>
            <textarea v-model="form.description" rows="2" class="w-full px-4 py-3 text-sm outline-none resize-none" style="border:1px solid #e8e8e8;color:#0a0a0a" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'"></textarea>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Цена (₽)</label>
              <input v-model.number="form.price" type="number" step="0.01" min="0" required class="w-full px-4 py-3 text-sm outline-none" style="border:1px solid #e8e8e8;color:#0a0a0a" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'" />
            </div>
            <div>
              <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Вес (г)</label>
              <input v-model.number="form.weight_grams" type="number" min="0" class="w-full px-4 py-3 text-sm outline-none" style="border:1px solid #e8e8e8;color:#0a0a0a" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'" />
            </div>
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">Категория</label>
            <select v-model="form.category_id" class="w-full px-4 py-3 text-sm outline-none" style="border:1px solid #e8e8e8;color:#0a0a0a;background:#fff" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'">
              <option :value="null">Без категории</option>
              <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
            </select>
          </div>
          <div>
            <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#888">URL изображения</label>
            <input v-model="form.image_url" type="url" placeholder="https://..." class="w-full px-4 py-3 text-sm outline-none" style="border:1px solid #e8e8e8;color:#0a0a0a" @focus="e => e.target.style.borderColor='#0a0a0a'" @blur="e => e.target.style.borderColor='#e8e8e8'" />
          </div>
          <label class="flex items-center gap-3 cursor-pointer">
            <div
              class="w-5 h-5 flex items-center justify-center shrink-0 transition-colors"
              :style="form.is_available ? 'background:#c1ce56' : 'background:#f0f0f0;border:1px solid #ddd'"
              @click="form.is_available = !form.is_available"
            >
              <svg v-if="form.is_available" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="#0a0a0a" stroke-width="3" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
            </div>
            <span class="text-sm" style="color:#555">Доступно для заказа</span>
          </label>
          <div v-if="formError" class="px-4 py-3 text-xs" style="background:#fff5f5;color:#e53e3e;border:1px solid #fed7d7">{{ formError }}</div>
          <div class="flex gap-3 justify-end pt-2">
            <button type="button" @click="closeModal" class="px-5 py-2.5 text-xs font-bold uppercase tracking-wider" style="border:1px solid #e8e8e8;color:#888" @mouseenter="e => e.currentTarget.style.borderColor='#0a0a0a'" @mouseleave="e => e.currentTarget.style.borderColor='#e8e8e8'">Отмена</button>
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
          <p class="font-black text-base mb-2" style="color:#0a0a0a">Удалить позицию?</p>
          <p class="text-sm" style="color:#888">Это действие нельзя отменить.</p>
        </div>
        <div class="flex" style="border-top:1px solid #f0f0f0">
          <button @click="deleteId = null" class="flex-1 py-3 text-xs font-bold uppercase tracking-wider" style="color:#888;border-right:1px solid #f0f0f0" @mouseenter="e => e.currentTarget.style.color='#0a0a0a'" @mouseleave="e => e.currentTarget.style.color='#888'">Отмена</button>
          <button @click="handleDelete" :disabled="deleting" class="flex-1 py-3 text-xs font-bold uppercase tracking-wider transition-opacity" style="color:#e53e3e" :style="deleting ? 'opacity:0.5' : ''">
            {{ deleting ? '—' : 'Удалить' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { menuApi } from '@/api/menu'
import { categoriesApi } from '@/api/categories'
import { formatPrice } from '@/utils/format'

const items = ref([])
const categories = ref([])
const loading = ref(false)
const fetchError = ref('')
const showModal = ref(false)
const editingId = ref(null)
const saving = ref(false)
const formError = ref('')
const deleteId = ref(null)
const deleting = ref(false)

const emptyForm = () => ({ name: '', description: '', price: 0, weight_grams: null, category_id: null, image_url: '', is_available: true })
const form = ref(emptyForm())

async function fetchItems() {
  loading.value = true
  fetchError.value = ''
  try {
    const r = await menuApi.getAll({ limit: 200, include_inactive: true })
    items.value = r.data.items || r.data || []
  } catch (err) {
    fetchError.value = err.response?.data?.detail || err.message || 'Ошибка загрузки меню'
    items.value = []
  } finally {
    loading.value = false
  }
}

async function fetchCategories() {
  try {
    const r = await categoriesApi.getAll()
    categories.value = r.data
  } catch {}
}

function openCreate() {
  editingId.value = null
  form.value = emptyForm()
  formError.value = ''
  showModal.value = true
}

function openEdit(item) {
  editingId.value = item.id
  form.value = {
    name: item.name,
    description: item.description || '',
    price: item.price,
    weight_grams: item.weight_grams || null,
    category_id: item.category_id || null,
    image_url: item.image_url || '',
    is_available: item.is_available,
  }
  formError.value = ''
  showModal.value = true
}

function closeModal() { showModal.value = false }

async function handleSave() {
  saving.value = true
  formError.value = ''
  try {
    const payload = {
      ...form.value,
      description: form.value.description || null,
      image_url: form.value.image_url || null,
      weight_grams: form.value.weight_grams || null,
    }
    if (editingId.value) {
      await menuApi.update(editingId.value, payload)
    } else {
      await menuApi.create(payload)
    }
    closeModal()
    await fetchItems()
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
    await menuApi.delete(deleteId.value)
    deleteId.value = null
    await fetchItems()
  } catch (err) {
    alert(err.response?.data?.detail || 'Ошибка при удалении')
  } finally {
    deleting.value = false
  }
}

onMounted(() => Promise.all([fetchItems(), fetchCategories()]))
</script>

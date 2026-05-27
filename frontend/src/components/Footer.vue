<template>
  <footer style="background:#fff;border-top:1px solid #f0f0f0">
    <div class="max-w-7xl mx-auto px-6 py-16">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">

        <div class="md:col-span-2">
          <AppLogo :dark="false" :size="32" font-size="1.05rem" class="mb-5" />
          <p class="text-sm leading-relaxed mb-6" style="color:#aaa;max-width:300px">
            Уютное кафе, где каждая чашка приготовлена с любовью.
            Приходите за кофе — оставайтесь ради атмосферы.
          </p>
          <div class="flex items-center gap-3">
            <a
              v-for="soc in socials"
              :key="soc.label"
              :href="soc.href"
              :title="soc.label"
              target="_blank"
              rel="noopener"
              class="flex items-center justify-center w-9 h-9 rounded transition-all duration-200"
              style="border:1px solid #e8e8e8;color:#bbb"
              @mouseenter="e => { e.currentTarget.style.borderColor='#c1ce56'; e.currentTarget.style.color='#c1ce56' }"
              @mouseleave="e => { e.currentTarget.style.borderColor='#e8e8e8'; e.currentTarget.style.color='#bbb' }"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" v-html="soc.icon"></svg>
            </a>
          </div>
        </div>

        <div>
          <p class="text-xs font-bold uppercase tracking-[0.25em] mb-6" style="color:#c1ce56">Навигация</p>
          <ul class="space-y-3">
            <li v-for="link in links" :key="link.to">
              <RouterLink
                :to="link.to"
                class="text-sm transition-colors"
                style="color:#aaa"
                @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
                @mouseleave="e => e.currentTarget.style.color='#aaa'"
              >{{ link.label }}</RouterLink>
            </li>
          </ul>
        </div>

        <div>
          <p class="text-xs font-bold uppercase tracking-[0.25em] mb-6" style="color:#c1ce56">Контакты</p>
          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <svg class="shrink-0 mt-0.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2" stroke-linecap="round">
                <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
              </svg>
              <span class="text-sm" style="color:#aaa">ул. Кофейная, 42</span>
            </li>
            <li class="flex items-start gap-3">
              <svg class="shrink-0 mt-0.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2" stroke-linecap="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.4 2 2 0 0 1 3.6 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.96a16 16 0 0 0 6 6l.95-.95a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16.92z"/>
              </svg>
              <span class="text-sm" style="color:#aaa">+7 (999) 000-12-34 </span>
            </li>
            <li class="flex items-start gap-3">
              <svg class="shrink-0 mt-0.5" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2" stroke-linecap="round">
                <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
              </svg>
              <span class="text-sm" style="color:#aaa">Пн–Вс: 08:00 – 22:00</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pt-8" style="border-top:1px solid #f0f0f0">
        <span class="text-xs" style="color:#ddd">© 2026 Кофеёчек</span>
        <RouterLink
          to="/privacy"
          class="text-xs transition-colors"
          style="color:#ddd"
          @mouseenter="e => e.currentTarget.style.color='#0a0a0a'"
          @mouseleave="e => e.currentTarget.style.color='#ddd'"
        >Политика конфиденциальности</RouterLink>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import AppLogo from '@/components/AppLogo.vue'

const links = [
  { to: '/menu',       label: 'Меню'      },
  { to: '/categories', label: 'Категории' },
  { to: '/reviews',    label: 'Отзывы'    },
  { to: '/about',      label: 'О нас'     },
  { to: '/contacts',   label: 'Контакты'  },
]

const socials = [
  {
    label: 'VK',
    href: '#',
    icon: '<path d="M15.684 0H8.316C1.592 0 0 1.592 0 8.316v7.368C0 22.408 1.592 24 8.316 24h7.368C22.408 24 24 22.408 24 15.684V8.316C24 1.592 22.408 0 15.684 0zm3.692 17.123h-1.744c-.66 0-.864-.525-2.05-1.727-1.033-1-1.49-1.135-1.744-1.135-.356 0-.458.102-.458.593v1.575c0 .424-.135.678-1.253.678-1.846 0-3.896-1.118-5.335-3.202C4.624 10.857 4 8.408 4 7.932c0-.254.102-.491.593-.491h1.744c.44 0 .61.203.78.677.863 2.49 2.303 4.675 2.896 4.675.22 0 .322-.102.322-.66V9.721c-.068-1.186-.695-1.287-.695-1.71 0-.203.169-.407.44-.407h2.744c.373 0 .508.203.508.643v3.473c0 .372.169.508.271.508.22 0 .407-.136.813-.542 1.253-1.406 2.151-3.574 2.151-3.574.119-.254.322-.491.763-.491h1.744c.525 0 .643.27.525.643-.22 1.017-2.354 4.031-2.354 4.031-.186.305-.254.44 0 .78.186.254.796.779 1.203 1.253.745.847 1.32 1.558 1.473 2.05.17.49-.085.745-.576.745z"/>',
  },
  {
    label: 'Telegram',
    href: '#',
    icon: '<path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>',
  },
  {
    label: 'Instagram',
    href: '#',
    icon: '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/>',
  },
  {
    label: 'WhatsApp',
    href: '#',
    icon: '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/>',
  },
]
</script>

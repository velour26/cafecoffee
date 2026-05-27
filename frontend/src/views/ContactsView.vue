<template>
  <div>

    <section class="relative overflow-hidden" style="background:#0a0a0a">
      <div class="absolute inset-0 pointer-events-none select-none" aria-hidden="true">
        <svg style="position:absolute;top:10%;left:5%;width:22px;opacity:.18;transform:rotate(25deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:60%;left:88%;width:26px;opacity:.15;transform:rotate(-35deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#fff"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:35%;left:60%;width:18px;opacity:.4;transform:rotate(15deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:75%;left:25%;width:20px;opacity:.35;transform:rotate(-50deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
      </div>
      <div class="relative z-10 max-w-7xl mx-auto px-6 py-24">
        <p class="text-xs font-bold uppercase tracking-[0.4em] mb-6" style="color:#c1ce56">Кофеёчек</p>
        <h1 class="font-black leading-[0.92] mb-6" style="font-size:clamp(3rem,8vw,6rem);color:#fff">
          Контакты
        </h1>
        <p class="text-base" style="color:#555;max-width:480px">
          Мы на связи каждый день. Приходите в гости, пишите или звоните —
          ответим на любой вопрос.
        </p>
      </div>
      <div class="absolute bottom-0 inset-x-0 h-12 pointer-events-none" style="background:linear-gradient(to top,#0a0a0a,transparent)"></div>
    </section>


    <section style="background:#0a0a0a;border-top:1px solid #1a1a1a">
      <div class="max-w-7xl mx-auto px-6 py-20">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px" style="background:#1e1e1e">

          <div v-for="card in cards" :key="card.title"
            class="flex flex-col gap-5 p-8 transition-colors duration-200"
            style="background:#0a0a0a"
            @mouseenter="e => e.currentTarget.style.background='#111'"
            @mouseleave="e => e.currentTarget.style.background='#0a0a0a'"
          >
            <div class="w-11 h-11 flex items-center justify-center" style="background:#161616">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" v-html="card.icon"></svg>
            </div>
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.2em] mb-3" style="color:#c1ce56">{{ card.title }}</p>
              <div class="flex flex-col gap-1.5">
                <p v-for="line in card.lines" :key="line" class="text-sm font-bold" style="color:#fff">{{ line }}</p>
              </div>
              <p v-if="card.note" class="text-xs mt-3" style="color:#444">{{ card.note }}</p>
            </div>
          </div>

        </div>
      </div>
    </section>


    <section style="background:#0f0f0f;border-top:1px solid #1a1a1a">
      <div class="max-w-7xl mx-auto px-6 py-20">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">

          <div class="flex flex-col gap-6">
            <div>
              <p class="text-xs font-bold uppercase tracking-[0.3em] mb-3" style="color:#c1ce56">Как добраться</p>
              <h2 class="font-black text-2xl" style="color:#fff">ул. Кофейная, 42</h2>
              <p class="text-sm mt-2" style="color:#444">Центральный район</p>
            </div>

            <div class="relative overflow-hidden" style="border:1px solid #1e1e1e;min-height:340px;height:340px">
              <iframe
                src="https://www.openstreetmap.org/export/embed.html?bbox=37.5976%2C55.7458%2C37.6376%2C55.7658&amp;layer=mapnik&amp;marker=55.7558%2C37.6176"
                style="width:100%;height:100%;border:0;display:block;filter:invert(0.9) hue-rotate(180deg) saturate(0.7) brightness(0.85)"
                allowfullscreen
                loading="lazy"
                title="Карта кафе Кофеёчек"
              ></iframe>
              <a
                href="https://www.openstreetmap.org/?mlat=55.7558&mlon=37.6176#map=16/55.7558/37.6176"
                target="_blank"
                rel="noopener"
                class="absolute bottom-2 right-2 text-xs font-bold px-2 py-1 z-10"
                style="background:rgba(0,0,0,0.7);color:#c1ce56;backdrop-filter:blur(4px)"
              >Открыть карту ↗</a>
            </div>

            <div class="grid grid-cols-2 gap-3">
              <div class="flex items-center gap-3 px-4 py-3" style="background:#161616">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round"><circle cx="8" cy="18" r="2"/><circle cx="18" cy="18" r="2"/><path d="M1 3h1l3.5 9h11L20 7H6"/></svg>
                <div>
                  <p class="text-xs font-bold" style="color:#fff">Парковка</p>
                  <p class="text-xs" style="color:#555">Рядом с домом</p>
                </div>
              </div>
            </div>
          </div>

          <div>
            <p class="text-xs font-bold uppercase tracking-[0.3em] mb-3" style="color:#c1ce56">Напишите нам</p>
            <h2 class="font-black text-2xl mb-8" style="color:#fff">Есть вопрос?</h2>

            <form @submit.prevent="handleSubmit" class="flex flex-col gap-5">
              <div class="grid grid-cols-2 gap-4">
                <div>
                  <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Имя</label>
                  <input
                    v-model="form.name" type="text" required
                    placeholder="Ваше имя"
                    class="w-full px-4 py-3 text-sm outline-none transition-all"
                    style="background:#161616;border:1px solid #222;color:#fff"
                    @focus="e => e.target.style.borderColor='#c1ce56'"
                    @blur="e => e.target.style.borderColor='#222'"
                  />
                </div>
                <div>
                  <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Email</label>
                  <input
                    v-model="form.email" type="email" required
                    placeholder="your@email.com"
                    class="w-full px-4 py-3 text-sm outline-none transition-all"
                    style="background:#161616;border:1px solid #222;color:#fff"
                    @focus="e => e.target.style.borderColor='#c1ce56'"
                    @blur="e => e.target.style.borderColor='#222'"
                  />
                </div>
              </div>
              <div>
                <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Тема</label>
                <select
                  v-model="form.topic"
                  class="w-full px-4 py-3 text-sm outline-none transition-all"
                  style="background:#161616;border:1px solid #222;color:#fff"
                  @focus="e => e.target.style.borderColor='#c1ce56'"
                  @blur="e => e.target.style.borderColor='#222'"
                >
                  <option value="">Выберите тему</option>
                  <option>Заказ и доставка</option>
                  <option>Качество продукции</option>
                  <option>Сотрудничество</option>
                  <option>Другое</option>
                </select>
              </div>
              <div>
                <label class="text-xs font-bold uppercase tracking-[0.15em] block mb-2" style="color:#555">Сообщение</label>
                <textarea
                  v-model="form.message" rows="5" required
                  placeholder="Расскажите подробнее..."
                  class="w-full px-4 py-3 text-sm outline-none transition-all resize-none"
                  style="background:#161616;border:1px solid #222;color:#fff"
                  @focus="e => e.target.style.borderColor='#c1ce56'"
                  @blur="e => e.target.style.borderColor='#222'"
                ></textarea>
              </div>

              <div v-if="sent" class="flex items-center gap-3 px-4 py-3" style="background:#0f1e0f;border:1px solid #1a3a1a">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>
                <p class="text-sm font-bold" style="color:#c1ce56">Сообщение отправлено! Мы ответим в течение дня.</p>
              </div>

              <div v-if="sendError" class="flex items-center gap-3 px-4 py-3" style="background:#1e0f0f;border:1px solid #3a1a1a">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#e53e3e" stroke-width="2.5" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                <p class="text-sm font-bold" style="color:#e53e3e">{{ sendError }}</p>
              </div>

              <button
                v-if="!sent"
                type="submit"
                :disabled="sending"
                class="flex items-center justify-center gap-3 py-4 text-xs font-bold uppercase tracking-[0.25em] transition-opacity"
                style="background:#c1ce56;color:#0a0a0a"
                :style="sending ? 'opacity:0.6' : ''"
              >
                <svg v-if="!sending" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                {{ sending ? '—' : 'Отправить сообщение' }}
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>


    <section style="background:#0a0a0a;border-top:1px solid #1a1a1a">
      <div class="max-w-7xl mx-auto px-6 py-20">
        <div class="flex flex-col md:flex-row items-center justify-between gap-8">
          <div>
            <p class="text-xs font-bold uppercase tracking-[0.3em] mb-3" style="color:#c1ce56">Мы в соцсетях</p>
            <h2 class="font-black text-2xl" style="color:#fff">Следите за нами</h2>
            <p class="text-sm mt-2" style="color:#444">Новинки, акции и закулисье кофейни</p>
          </div>
          <div class="flex items-center gap-4">
            <a
              v-for="soc in socials"
              :key="soc.label"
              href="#"
              :title="soc.label"
              class="flex items-center gap-3 px-5 py-3 text-sm font-bold transition-all duration-200"
              style="border:1px solid #222;color:#555"
              @mouseenter="e => { e.currentTarget.style.borderColor='#c1ce56'; e.currentTarget.style.color='#c1ce56' }"
              @mouseleave="e => { e.currentTarget.style.borderColor='#222'; e.currentTarget.style.color='#555' }"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" v-html="soc.icon"></svg>
              {{ soc.label }}
            </a>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { contactApi } from '@/api/contact'

const form = ref({ name: '', email: '', topic: '', message: '' })
const sending = ref(false)
const sent = ref(false)
const sendError = ref('')

async function handleSubmit() {
  sending.value = true
  sendError.value = ''
  try {
    await contactApi.send({
      name: form.value.name,
      email: form.value.email,
      topic: form.value.topic || null,
      message: form.value.message,
    })
    sent.value = true
    form.value = { name: '', email: '', topic: '', message: '' }
  } catch (err) {
    sendError.value = err.response?.data?.detail || 'Ошибка при отправке. Попробуйте позже.'
  } finally {
    sending.value = false
  }
}

const cards = [
  {
    title: 'Адрес',
    icon: '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    lines: ['ул. Кофейная, 42'],
    note: 'Центральный район',
  },
  {
    title: 'Телефон',
    icon: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.4 2 2 0 0 1 3.6 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.96a16 16 0 0 0 6 6l.95-.95a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16.92z"/>',
    lines: ['+7 (999) 000-12-34'],
    note: 'Ежедневно с 08:00 до 22:00',
  },
  {
    title: 'Email',
    icon: '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    lines: ['hello@coffeechek.ru'],
    note: 'Ответим в течение одного рабочего дня',
  },
  {
    title: 'Часы работы',
    icon: '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    lines: ['Пн – Пт: 08:00 – 22:00', 'Сб – Вс: 09:00 – 23:00'],
    note: 'Без выходных и праздников',
  },
]

const socials = [
  { label: 'VK',       icon: '<path d="M15.684 0H8.316C1.592 0 0 1.592 0 8.316v7.368C0 22.408 1.592 24 8.316 24h7.368C22.408 24 24 22.408 24 15.684V8.316C24 1.592 22.408 0 15.684 0zm3.692 17.123h-1.744c-.66 0-.864-.525-2.05-1.727-1.033-1-1.49-1.135-1.744-1.135-.356 0-.458.102-.458.593v1.575c0 .424-.135.678-1.253.678-1.846 0-3.896-1.118-5.335-3.202C4.624 10.857 4 8.408 4 7.932c0-.254.102-.491.593-.491h1.744c.44 0 .61.203.78.677.863 2.49 2.303 4.675 2.896 4.675.22 0 .322-.102.322-.66V9.721c-.068-1.186-.695-1.287-.695-1.71 0-.203.169-.407.44-.407h2.744c.373 0 .508.203.508.643v3.473c0 .372.169.508.271.508.22 0 .407-.136.813-.542 1.253-1.406 2.151-3.574 2.151-3.574.119-.254.322-.491.763-.491h1.744c.525 0 .643.27.525.643-.22 1.017-2.354 4.031-2.354 4.031-.186.305-.254.44 0 .78.186.254.796.779 1.203 1.253.745.847 1.32 1.558 1.473 2.05.17.49-.085.745-.576.745z"/>' },
  { label: 'Telegram', icon: '<path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>' },
]
</script>

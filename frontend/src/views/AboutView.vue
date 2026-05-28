<template>
  <div>

    <section class="relative overflow-hidden flex items-center" style="background:#f7f3ee;min-height:80vh">

      <div class="absolute inset-0 pointer-events-none select-none" aria-hidden="true">
        <svg style="position:absolute;top:8%;left:6%;width:26px;opacity:.2;transform:rotate(20deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:22%;left:80%;width:20px;opacity:.18;transform:rotate(-40deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:60%;left:15%;width:18px;opacity:.15;transform:rotate(55deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:75%;left:70%;width:24px;opacity:.2;transform:rotate(-20deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:40%;left:90%;width:16px;opacity:.15;transform:rotate(75deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:12%;left:50%;width:14px;opacity:.25;transform:rotate(-10deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:55%;left:48%;width:20px;opacity:.4;transform:rotate(30deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
        <svg style="position:absolute;top:85%;left:32%;width:22px;opacity:.35;transform:rotate(-50deg)" viewBox="0 0 40 22" fill="none"><ellipse cx="20" cy="11" rx="19" ry="10" fill="#c1ce56"/><path d="M20 2 Q28 11 20 20 Q12 11 20 2Z" fill="#0a0a0a"/></svg>
      </div>

      <div class="relative z-10 max-w-7xl mx-auto px-6 py-28 w-full flex flex-col lg:flex-row items-center gap-16">

        <div class="flex-1">
          <p class="text-xs font-bold uppercase tracking-[0.4em] mb-7" style="color:#c1ce56">О нас</p>
          <h1 class="font-black leading-[0.92] mb-8" style="font-size:clamp(3rem,8vw,6.5rem);color:#1a1714">
            Мы варим<br>кофе<br>
            <em style="color:#c1ce56;font-style:normal">с душой.</em>
          </h1>
          <p class="text-base leading-relaxed mb-10" style="color:#555;max-width:440px">
            С 2016 года «Кофеёчек» — место, где каждая чашка сделана вручную,
            с уважением к зерну, к гостю и к моменту.
          </p>
          <RouterLink
            to="/menu"
            class="inline-flex items-center gap-4 text-xs font-bold uppercase tracking-[0.25em] px-8 py-4 transition-all duration-300"
            style="border:1px solid #2a2420;color:#2a2420"
            onmouseenter="this.style.background='#fff';this.style.color='#0a0a0a'"
            onmouseleave="this.style.background='transparent';this.style.color='#2a2420'"
          >
            Наше меню <span>→</span>
          </RouterLink>
        </div>

        <div class="flex-1 flex justify-center lg:justify-end">
          <div class="relative" style="max-width:380px">
            <svg width="60" height="44" viewBox="0 0 60 44" fill="none" style="position:absolute;top:-24px;left:-16px;opacity:0.12">
              <path d="M0 44V26C0 10.536 8.954 2.28 26.862 1.228L28 8.772C20.572 9.74 16.858 13.88 16.858 21.192V24H28V44H0ZM32 44V26C32 10.536 40.954 2.28 58.862 1.228L60 8.772C52.572 9.74 48.858 13.88 48.858 21.192V24H60V44H32Z" fill="#c1ce56"/>
            </svg>
            <blockquote class="font-black leading-tight" style="font-size:clamp(1.6rem,3vw,2.4rem);color:#1a1714">
              Хороший кофе — это не напиток. Это ритуал, который начинает день.
            </blockquote>
            <p class="mt-6 text-xs font-bold uppercase tracking-widest" style="color:#c1ce56">— Основатель кафе</p>
          </div>
        </div>

      </div>

      <div class="absolute bottom-0 inset-x-0 h-16 pointer-events-none" style="background:linear-gradient(to top,#f7f3ee,transparent)"></div>
    </section>


    <section style="background:#f7f3ee;border-top:1px solid #e0d9d2">
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid grid-cols-1 lg:grid-cols-2" style="min-height:540px">

          <div class="relative overflow-hidden" style="min-height:360px">
            <img
              src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=900&q=80&auto=format&fit=crop"
              alt="История кофейни"
              class="absolute inset-0 w-full h-full object-cover"
              style="filter:grayscale(20%) brightness(0.7)"
            />
            <div class="absolute inset-0" style="background:linear-gradient(to right,transparent 50%,#0a0a0a)"></div>
            <div class="absolute bottom-8 left-8">
              <span class="text-xs font-bold uppercase tracking-[0.25em] px-4 py-2" style="background:#c1ce56;color:#0a0a0a">
                с 2016 года
              </span>
            </div>
          </div>

          <div class="flex flex-col justify-center px-8 lg:px-16 py-16">
            <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Наша история</p>
            <h2 class="font-black leading-tight mb-8" style="font-size:clamp(1.8rem,3vw,2.8rem);color:#1a1714">
              Всё началось<br>с одной чашки
            </h2>
            <div class="flex flex-col gap-5" style="color:#555;font-size:0.9375rem;line-height:1.75">
              <p>
                В 2016 году два друга открыли небольшую кофейню в центре города с одной идеей:
                делать кофе так, как они сами хотели бы его пить — без спешки, с хорошим зерном
                и с вниманием к каждому гостю.
              </p>
              <p>
                Сегодня «Кофеёчек» — это больше, чем кафе. Это место, куда возвращаются.
                Мы по-прежнему обжариваем зерно вручную, разговариваем с гостями по именам
                и считаем каждый отзыв поводом стать лучше.
              </p>
            </div>
          </div>

        </div>
      </div>
    </section>


    <section style="background:#efe9e3;border-top:1px solid #e0d9d2">
      <div class="max-w-7xl mx-auto px-6 py-24">
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-px" style="background:#dbd5ce">
          <div v-for="stat in stats" :key="stat.value" class="flex flex-col px-8 py-10" style="background:#111">
            <p class="font-black mb-2" style="font-size:clamp(2rem,4vw,3rem);color:#1a1714;line-height:1">{{ stat.value }}</p>
            <p class="text-xs font-bold uppercase tracking-wider mb-2" style="color:#c1ce56">{{ stat.label }}</p>
            <p class="text-sm leading-relaxed" style="color:#3a3a3a">{{ stat.desc }}</p>
          </div>
        </div>
      </div>
    </section>


    <section style="background:#f7f3ee;border-top:1px solid #e0d9d2">
      <div class="max-w-7xl mx-auto px-6 py-24">

        <div class="max-w-xl mb-16">
          <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Наши ценности</p>
          <h2 class="font-black leading-tight" style="font-size:clamp(1.8rem,4vw,3rem);color:#1a1714">
            То, на чём<br>мы держимся
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-px" style="background:#dbd5ce">
          <div
            v-for="(val, i) in values"
            :key="i"
            class="flex flex-col p-10 transition-colors duration-300"
            style="background:#f7f3ee"
            @mouseenter="e => e.currentTarget.style.background='#efe9e3'"
            @mouseleave="e => e.currentTarget.style.background='#f7f3ee'"
          >
            <div class="w-12 h-12 flex items-center justify-center mb-8" style="background:#e9e3dc;border:1px solid #ddd7d0">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" v-html="val.icon"></svg>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.25em] mb-4" style="color:#c1ce56">{{ String(i+1).padStart(2,'0') }}</p>
            <h3 class="font-black text-xl mb-4" style="color:#1a1714">{{ val.title }}</h3>
            <p class="text-sm leading-relaxed" style="color:#444">{{ val.text }}</p>
          </div>
        </div>

      </div>
    </section>


    <section style="background:#f3ede7;border-top:1px solid #e0d9d2">
      <div class="max-w-7xl mx-auto px-6 py-24">

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">

          <div>
            <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Процесс</p>
            <h2 class="font-black leading-tight mb-12" style="font-size:clamp(1.8rem,3vw,2.8rem);color:#1a1714">
              От зерна<br>до чашки
            </h2>
            <div class="flex flex-col gap-0">
              <div
                v-for="(step, i) in process"
                :key="i"
                class="flex gap-6 items-start"
              >
                <div class="flex flex-col items-center shrink-0">
                  <div class="w-8 h-8 flex items-center justify-center font-black text-xs shrink-0" style="background:#c1ce56;color:#0a0a0a">
                    {{ String(i+1).padStart(2,'0') }}
                  </div>
                  <div v-if="i < process.length - 1" class="w-px flex-1 mt-2 mb-2" style="background:#dbd5ce;min-height:32px"></div>
                </div>
                <div :class="i < process.length - 1 ? 'pb-8' : ''">
                  <p class="font-black text-base mb-1" style="color:#1a1714">{{ step.title }}</p>
                  <p class="text-sm leading-relaxed" style="color:#444">{{ step.text }}</p>
                </div>
              </div>
            </div>
          </div>

          <div class="flex justify-center lg:justify-end">
            <svg viewBox="0 0 200 260" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:min(320px,100%);opacity:0.85">
              <path d="M72 58 C68 44 76 30 72 16" stroke="#2a2a2a" stroke-width="3" stroke-linecap="round" fill="none"/>
              <path d="M100 50 C96 36 104 22 100 8" stroke="#2a2a2a" stroke-width="3" stroke-linecap="round" fill="none"/>
              <path d="M128 58 C124 44 132 30 128 16" stroke="#2a2a2a" stroke-width="3" stroke-linecap="round" fill="none"/>
              <path d="M28 86 L40 214 H160 L172 86 Z" fill="#161616" stroke="#222" stroke-width="2.5" stroke-linejoin="round"/>
              <ellipse cx="100" cy="86" rx="72" ry="18" fill="#111" stroke="#222" stroke-width="2.5"/>
              <ellipse cx="100" cy="86" rx="55" ry="13" fill="#1a1a1a"/>
              <ellipse cx="100" cy="86" rx="36" ry="8.5" fill="none" stroke="#c1ce56" stroke-width="1.5" opacity="0.6"/>
              <ellipse cx="100" cy="86" rx="18" ry="4.5" fill="none" stroke="#c1ce56" stroke-width="1" opacity="0.35"/>
              <path d="M170 122 Q202 122 202 150 Q202 178 170 178" stroke="#222" stroke-width="4" fill="none" stroke-linecap="round"/>
              <ellipse cx="100" cy="218" rx="84" ry="13" fill="#141414" stroke="#1e1e1e" stroke-width="2"/>
              <ellipse cx="100" cy="215" rx="62" ry="8" fill="#181818"/>
              <line x1="60" y1="130" x2="140" y2="130" stroke="#1e1e1e" stroke-width="1"/>
              <line x1="50" y1="160" x2="150" y2="160" stroke="#1e1e1e" stroke-width="1"/>
              <line x1="44" y1="190" x2="156" y2="190" stroke="#1e1e1e" stroke-width="1"/>
            </svg>
          </div>

        </div>
      </div>
    </section>


    <section style="background:#f7f3ee;border-top:1px solid #e0d9d2">
      <div class="max-w-7xl mx-auto px-6 py-24">

        <div class="max-w-xl mb-16">
          <p class="text-xs font-bold uppercase tracking-[0.3em] mb-5" style="color:#c1ce56">Контакты</p>
          <h2 class="font-black leading-tight" style="font-size:clamp(1.8rem,4vw,3rem);color:#1a1714">
            Приходите<br>в гости
          </h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-px" style="background:#dbd5ce">

          <div class="flex flex-col gap-4 p-10" style="background:#f7f3ee">
            <div class="w-10 h-10 flex items-center justify-center" style="background:#e9e3dc">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round">
                <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#c1ce56">Адрес</p>
            <p class="font-black text-lg leading-tight" style="color:#1a1714">ул. Кофейная, 42</p>
            <p class="text-sm" style="color:#444">Центральный район</p>
          </div>

          <div class="flex flex-col gap-4 p-10" style="background:#f7f3ee">
            <div class="w-10 h-10 flex items-center justify-center" style="background:#e9e3dc">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round">
                <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
              </svg>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#c1ce56">Часы работы</p>
            <div class="flex flex-col gap-2">
              <div class="flex justify-between text-sm">
                <span style="color:#555">Пн — Пт</span>
                <span class="font-bold" style="color:#1a1714">08:00 — 22:00</span>
              </div>
              <div class="flex justify-between text-sm">
                <span style="color:#555">Сб — Вс</span>
                <span class="font-bold" style="color:#1a1714">09:00 — 23:00</span>
              </div>
            </div>
          </div>

          <div class="flex flex-col gap-4 p-10" style="background:#f7f3ee">
            <div class="w-10 h-10 flex items-center justify-center" style="background:#e9e3dc">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#c1ce56" stroke-width="1.5" stroke-linecap="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.63 3.4 2 2 0 0 1 3.6 1.22h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.78a16 16 0 0 0 6 6l.94-.94a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16l.19.92z"/>
              </svg>
            </div>
            <p class="text-xs font-bold uppercase tracking-[0.2em]" style="color:#c1ce56">Связаться</p>
            <div class="flex flex-col gap-2">
              <a href="tel:+79990001234" class="text-sm font-bold transition-colors" style="color:#1a1714"
                @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
                @mouseleave="e => e.currentTarget.style.color='#2a2420'">
                +7 (999) 000-12-34
              </a>
              <a href="mailto:hello@coffeechek.ru" class="text-sm transition-colors" style="color:#444"
                @mouseenter="e => e.currentTarget.style.color='#c1ce56'"
                @mouseleave="e => e.currentTarget.style.color='#444'">
                hello@coffeechek.ru
              </a>
            </div>
          </div>

        </div>
      </div>
    </section>


    <section style="background:#f7f3ee;border-top:1px solid #e0d9d2">
      <div class="max-w-4xl mx-auto px-6 py-28 text-center">
        <p class="text-xs font-bold uppercase tracking-[0.35em] mb-6" style="color:#c1ce56">Попробуйте</p>
        <h2 class="font-black leading-tight mb-6" style="font-size:clamp(2rem,5vw,3.5rem);color:#1a1714">
          Первая чашка —<br>и вы всё поймёте.
        </h2>
        <p class="text-base mb-12" style="color:#555">
          Загляните лично или оформите заказ онлайн
        </p>
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
          <RouterLink
            to="/menu"
            class="inline-flex items-center gap-3 px-10 py-4 text-xs font-bold uppercase tracking-[0.25em] transition-opacity hover:opacity-85"
            style="background:#c1ce56;color:#0a0a0a"
          >Перейти к меню</RouterLink>
          <RouterLink
            to="/reviews"
            class="inline-flex items-center gap-3 px-10 py-4 text-xs font-bold uppercase tracking-[0.25em] transition-all"
            style="border:1px solid #d5cfc8;color:#555"
            onmouseenter="this.style.borderColor='#555';this.style.color='#2a2420'"
            onmouseleave="this.style.borderColor='#2a2a2a';this.style.color='#555'"
          >Читать отзывы</RouterLink>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

const stats = [
  { value: '8 лет',  label: 'На рынке',         desc: 'Открылись в 2016, работаем без остановок' },
  { value: '5 000+', label: 'Чашек в месяц',     desc: 'Свежий кофе каждый день, без выходных' },
  { value: '12',     label: 'Сортов зерна',      desc: 'Моносорта и авторские купажи' },
  { value: '98%',    label: 'Довольных гостей',  desc: 'По оценкам за последние 6 месяцев' },
]

const values = [
  {
    title: 'Качество зерна',
    text: 'Прямые поставки с ферм Эфиопии, Колумбии и Бразилии. Каждая партия проходит каппинг перед закупкой.',
    icon: '<path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/>',
  },
  {
    title: 'Забота о госте',
    text: 'Мы помним постоянных гостей, их предпочтения и любимые напитки. Каждый визит — персональный опыт.',
    icon: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
  },
  {
    title: 'Любовь к делу',
    text: 'Наши бариста — призёры городских чемпионатов. Постоянное обучение, эксперименты и поиск идеального вкуса.',
    icon: '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
  },
]

const process = [
  { title: 'Отбор зерна',       text: 'Выбираем партии с оценкой SCA от 85 баллов, пробуем каждый лот вслепую.' },
  { title: 'Обжарка',           text: 'Небольшие партии в ручном режиме — каждое зерно доходит до нужной точки.' },
  { title: 'Помол под заказ',   text: 'Кофе мелется непосредственно перед приготовлением — не раньше.' },
  { title: 'Приготовление',     text: 'Температура воды, давление, тайминг — всё контролируется вручную.' },
  { title: 'Подача',            text: 'Ваша чашка готова. Пейте, пока горячо — и возвращайтесь.' },
]
</script>

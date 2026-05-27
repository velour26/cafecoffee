/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        coffee: {
          50:  '#fdf8f0',
          100: '#faefd8',
          200: '#f5dcb0',
          300: '#edc37e',
          400: '#e4a54a',
          500: '#dd8f28',
          600: '#c8731d',
          700: '#a65819',
          800: '#85461b',
          900: '#6c3a19',
          950: '#3d1d09',
        },
        cream: {
          50:  '#fefdf8',
          100: '#fdf9ed',
          200: '#faf0d0',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}

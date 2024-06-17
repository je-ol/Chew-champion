/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}", ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Ubuntu', 'sans-serif'] 
      }
    },
    screens: {
      'md': { 'min': '1280px', 'max': '1706px' },
      /* 'lg': { 'min': '1535px', 'max': '1705px' }, */
    }
  },
  plugins: [],
}

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
      'lg': { 'min': '1281px', 'max': '1536px' },
      'md': { 'min': '1028px', 'max': '1280px' },
    }
  },
  plugins: [],
}

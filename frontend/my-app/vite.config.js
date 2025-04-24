import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite' // ⬅️ اضافه کن

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(), // ⬅️ اضافه کن به لیست پلاگین‌ها
  ],
})

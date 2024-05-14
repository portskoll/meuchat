/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./core/templates/core/**/*.html', './room/templates/room/**/*.html'], // Caminho para os arquivos HTML do seu projeto
  theme: {
    extend: {}, // Aqui você pode estender o tema padrão do Tailwind, se necessário
  },
  plugins: [], // Adicione plugins personalizados aqui, se aplicável
}


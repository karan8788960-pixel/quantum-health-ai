export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        midnight: '#050b17',
        cyanGlow: '#67e8f9',
        electric: '#3b82f6',
        violetGlow: '#8b5cf6',
      },
      boxShadow: {
        glow: '0 0 25px rgba(103, 232, 249, 0.35)',
      },
      backgroundImage: {
        grid: 'radial-gradient(circle, rgba(103, 232, 249, 0.18) 1px, transparent 1px)',
      },
    },
  },
  plugins: [],
};

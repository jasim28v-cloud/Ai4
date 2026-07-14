const THEMES = {
    neon: { bg: '#0a0a0f', snake: '#00ffcc', food: '#ff44aa', grid: 'rgba(255,255,255,0.03)', accent: '#ffaa00' },
    rose: { bg: '#0a0508', snake: '#ec4899', food: '#f472b6', grid: 'rgba(236,72,153,0.05)', accent: '#a855f7' },
    gold: { bg: '#0a0a05', snake: '#f59e0b', food: '#fbbf24', grid: 'rgba(245,158,11,0.05)', accent: '#fcd34d' },
    ocean: { bg: '#050a14', snake: '#06b6d4', food: '#22d3ee', grid: 'rgba(6,182,212,0.05)', accent: '#67e8f9' },
    forest: { bg: '#050a05', snake: '#10b981', food: '#34d399', grid: 'rgba(16,185,129,0.05)', accent: '#6ee7b7' },
    lava: { bg: '#0f0505', snake: '#ef4444', food: '#f87171', grid: 'rgba(239,68,68,0.05)', accent: '#fca5a5' }
};
let currentTheme = 'neon';
function getTheme(){return THEMES[currentTheme] || THEMES['neon']}
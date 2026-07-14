const THEMES = {
    neon: { name: 'نيون', bg: '#0a0a0f', bg2: '#1a0a2e', snake: '#00ffcc', snakeGlow: 'rgba(0,255,204,0.6)', food: '#ff44aa', foodGlow: 'rgba(255,68,170,0.8)', grid: 'rgba(255,255,255,0.03)', accent: '#ffaa00', orb1: '#ff44aa', orb2: '#00ffcc', orb3: '#ffaa00' },
    rose: { name: 'روز', bg: '#0a0508', bg2: '#1a0a15', snake: '#ec4899', snakeGlow: 'rgba(236,72,153,0.6)', food: '#f472b6', foodGlow: 'rgba(244,114,182,0.8)', grid: 'rgba(236,72,153,0.05)', accent: '#a855f7', orb1: '#ec4899', orb2: '#a855f7', orb3: '#f472b6' },
    gold: { name: 'ذهبي', bg: '#0a0a05', bg2: '#1a1505', snake: '#f59e0b', snakeGlow: 'rgba(245,158,11,0.6)', food: '#fbbf24', foodGlow: 'rgba(251,191,36,0.8)', grid: 'rgba(245,158,11,0.05)', accent: '#fcd34d', orb1: '#f59e0b', orb2: '#fbbf24', orb3: '#fcd34d' },
    ocean: { name: 'محيط', bg: '#050a14', bg2: '#051020', snake: '#06b6d4', snakeGlow: 'rgba(6,182,212,0.6)', food: '#22d3ee', foodGlow: 'rgba(34,211,238,0.8)', grid: 'rgba(6,182,212,0.05)', accent: '#67e8f9', orb1: '#06b6d4', orb2: '#22d3ee', orb3: '#67e8f9' },
    forest: { name: 'غابة', bg: '#050a05', bg2: '#051008', snake: '#10b981', snakeGlow: 'rgba(16,185,129,0.6)', food: '#34d399', foodGlow: 'rgba(52,211,153,0.8)', grid: 'rgba(16,185,129,0.05)', accent: '#6ee7b7', orb1: '#10b981', orb2: '#34d399', orb3: '#6ee7b7' },
    lava: { name: 'حمم', bg: '#0f0505', bg2: '#1a0505', snake: '#ef4444', snakeGlow: 'rgba(239,68,68,0.6)', food: '#f87171', foodGlow: 'rgba(248,113,113,0.8)', grid: 'rgba(239,68,68,0.05)', accent: '#fca5a5', orb1: '#ef4444', orb2: '#f87171', orb3: '#fca5a5' }
};
let currentTheme = 'neon';
function getTheme(){ return THEMES[currentTheme] || THEMES['neon']; }
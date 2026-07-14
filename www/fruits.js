const FRUITS = [
    { type: 'normal', emoji: '🍎', points: 10, color: '#ff4444', chance: 60 },
    { type: 'golden', emoji: '⭐', points: 50, color: '#ffd700', chance: 15 },
    { type: 'speed', emoji: '⚡', points: 20, color: '#00bfff', chance: 10 },
    { type: 'slow', emoji: '🐢', points: 15, color: '#90ee90', chance: 10 },
    { type: 'poison', emoji: '☠️', points: -30, color: '#8b008b', chance: 5 }
];
function getRandomFruit(){const r=Math.random()*100;let acc=0;for(let f of FRUITS){acc+=f.chance;if(r<=acc)return f}return FRUITS[0]}
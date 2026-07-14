let particles = [];
function initParticles() {
    const c = document.getElementById('particlesContainer');
    c.innerHTML = '';
    for (let i = 0; i < 40; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*100}%;width:${Math.random()*4+1}px;height:${Math.random()*4+1}px;background:radial-gradient(circle,${['#00ffcc','#ff44aa','#ffaa00'][i%3]} 0%,transparent 70%);animation:particleFloat ${Math.random()*6+4}s ease-in infinite;animation-delay:${Math.random()*5}s`;
        c.appendChild(p);
        particles.push(p);
    }
}
function setParticleColors(theme) {
    const colors = { neon: ['#00ffcc','#ff44aa','#ffaa00'], rose: ['#ec4899','#f472b6','#a855f7'], gold: ['#f59e0b','#fbbf24','#fcd34d'], ocean: ['#06b6d4','#22d3ee','#67e8f9'], forest: ['#10b981','#34d399','#6ee7b7'], lava: ['#ef4444','#f87171','#fca5a5'] };
    const clrs = colors[theme] || colors['neon'];
    particles.forEach((p, i) => { p.style.background = `radial-gradient(circle,${clrs[i%3]} 0%,transparent 70%)`; });
}
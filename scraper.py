import os

def create_website_files():
    """إنشاء لعبة Fishing Pro الأسطورية الواقعية"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Fishing Pro | Legendary</title>
    <style>
        :root {
            --bg: #000;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --neon-blue: #00aaff;
            --text: #e0d5c0;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #000;
            font-family: 'Segoe UI', system-ui, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            touch-action: manipulation;
            user-select: none;
            -webkit-user-select: none;
            -webkit-tap-highlight-color: transparent;
            overflow: hidden;
        }

        .game-wrapper {
            width: 100%;
            max-width: 480px;
            padding: 6px;
            position: relative;
            z-index: 1;
        }

        .header {
            text-align: center;
            margin-bottom: 4px;
        }

        .title {
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(180deg, #00aaff, #fff, #00aaff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 15px rgba(0,170,255,0.5));
        }

        .subtitle {
            font-size: 7px;
            color: #6b6355;
            letter-spacing: 4px;
            text-transform: uppercase;
        }

        .hud {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 6px 12px;
            margin-bottom: 4px;
            background: rgba(8,8,8,0.85);
            border: 1px solid #1a1a1a;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }

        .hud-item { text-align: center; flex: 1; }
        .hud-label { font-size: 6px; color: #555; letter-spacing: 2px; text-transform: uppercase; }
        .hud-val { font-size: 13px; font-weight: 900; }
        .divider-v { width: 1px; height: 18px; background: linear-gradient(180deg, transparent, #1a1a1a, transparent); }

        .canvas-container {
            position: relative;
            border: 1px solid #1a1a1a;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 60px rgba(0,100,255,0.06), 0 20px 40px rgba(0,0,0,0.8);
            background: #000;
        }

        canvas { display: block; width: 100%; height: auto; }

        .cast-btn {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 14px 35px;
            background: linear-gradient(135deg, #ff8800, #ff6600);
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 25px;
            font-size: 13px;
            letter-spacing: 2px;
            text-transform: uppercase;
            box-shadow: 0 6px 25px rgba(255,136,0,0.4);
            z-index: 20;
            font-family: inherit;
            transition: all 0.3s;
        }
        .cast-btn:active { transform: translateX(-50%) scale(0.93); }
        .cast-btn.reel { background: linear-gradient(135deg, #00ff88, #00cc66); box-shadow: 0 6px 25px rgba(0,255,136,0.4); }

        .power-bar-container {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            width: 20px;
            height: 60%;
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 10px;
            z-index: 15;
            overflow: hidden;
        }
        .power-bar-fill {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: linear-gradient(to top, #ff0000, #ff8800, #00ff88);
            border-radius: 10px;
            transition: height 0.05s;
        }

        .overlay {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background: rgba(0,0,0,0.9);
            border-radius: 12px;
            z-index: 10;
            transition: all 0.5s;
            backdrop-filter: blur(5px);
        }
        .overlay.hidden { opacity: 0; pointer-events: none; }

        .overlay-icon { font-size: 40px; animation: float 2s ease-in-out infinite; }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .overlay-title {
            font-size: 16px; font-weight: 900;
            letter-spacing: 3px; margin: 5px 0;
            color: #00aaff;
            text-shadow: 0 0 20px rgba(0,170,255,0.5);
        }
        .overlay-score {
            font-size: 28px; font-weight: 900;
            background: linear-gradient(135deg, #ff3344, #c9a84c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 3px 0;
        }
        .overlay-sub { font-size: 9px; color: #666; letter-spacing: 2px; margin-bottom: 8px; }

        .btn-play {
            padding: 10px 30px;
            background: linear-gradient(135deg, #00aaff, #0088ff);
            background-size: 200% 200%;
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 22px;
            font-size: 11px;
            letter-spacing: 2px;
            text-transform: uppercase;
            box-shadow: 0 6px 20px rgba(0,170,255,0.3);
            animation: gradientShift 3s ease-in-out infinite;
            font-family: inherit;
        }
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        .btn-play:active { transform: scale(0.93); }

        .fish-caught-popup {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%) translateY(-120px);
            background: rgba(0,0,0,0.85);
            border: 1px solid #ff8800;
            color: #ffaa00;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 900;
            letter-spacing: 2px;
            z-index: 25;
            transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }
        .fish-caught-popup.show { transform: translateX(-50%) translateY(0); }

        .footer {
            text-align: center; margin-top: 3px;
            font-size: 6px; color: #0a0a0a; letter-spacing: 2px;
        }
    </style>
</head>
<body>
    <div class="game-wrapper">
        <div class="header">
            <h1 class="title">FISHING PRO</h1>
            <p class="subtitle">✦ Legendary Edition ✦</p>
        </div>

        <div class="hud">
            <div class="hud-item"><span class="hud-label">Score</span><span class="hud-val" id="score" style="color:#00aaff">0</span></div>
            <div class="divider-v"></div>
            <div class="hud-item"><span class="hud-label">Best</span><span class="hud-val" id="bestScore" style="color:#c9a84c">0</span></div>
            <div class="divider-v"></div>
            <div class="hud-item"><span class="hud-label">Fish</span><span class="hud-val" id="fishCount" style="color:#ff8800">0</span></div>
            <div class="divider-v"></div>
            <div class="hud-item"><span class="hud-label">Streak</span><span class="hud-val" id="streak" style="color:#00ff88">0</span></div>
        </div>

        <div class="canvas-container" id="canvasContainer">
            <canvas id="gameCanvas"></canvas>
            
            <div class="power-bar-container" id="powerBarContainer">
                <div class="power-bar-fill" id="powerBarFill" style="height:0%"></div>
            </div>

            <button class="cast-btn" id="castBtn" onclick="handleCast()">🎣 CAST</button>

            <div class="fish-caught-popup" id="fishPopup"></div>

            <div class="overlay" id="startOverlay">
                <div class="overlay-icon">🎣</div>
                <div class="overlay-title">FISHING PRO</div>
                <div class="overlay-sub">CAST • HOOK • REEL</div>
                <button class="btn-play" onclick="startGame()">✦ START FISHING ✦</button>
            </div>

            <div class="overlay hidden" id="gameOverOverlay">
                <div class="overlay-icon">🏆</div>
                <div class="overlay-title">TIME'S UP!</div>
                <div class="overlay-score" id="finalScore">0</div>
                <button class="btn-play" onclick="restartGame()">✦ FISH AGAIN ✦</button>
            </div>
        </div>

        <p class="footer">FISHING PRO • CAST • HOOK • REEL • COLLECT</p>
    </div>

    <script>
        // ==================== CANVAS ====================
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const container = document.getElementById('canvasContainer');
        let W, H;

        function resize() {
            W = container.clientWidth;
            H = Math.max(W * 1.25, 440);
            canvas.width = W;
            canvas.height = H;
        }
        resize();
        window.addEventListener('resize', resize);

        // ==================== AUDIO ====================
        let audioCtx;
        function initAudio() {
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        function beep(f, d, t, v) {
            if (!audioCtx) return;
            try {
                const o = audioCtx.createOscillator();
                const g = audioCtx.createGain();
                o.type = t || 'square';
                o.frequency.setValueAtTime(f, audioCtx.currentTime);
                g.gain.setValueAtTime(v || 0.04, audioCtx.currentTime);
                g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + d);
                o.connect(g); g.connect(audioCtx.destination);
                o.start(); o.stop(audioCtx.currentTime + d);
            } catch(e) {}
        }

        // ==================== STATE ====================
        let score = 0, fishCount = 0, streak = 0;
        let bestScore = parseInt(localStorage.getItem('fishingpro_best') || '0');
        let gameState = 'idle';
        let gameTime = 90, gameTimer = null;

        // Fishing state
        let castPower = 0, isCharging = false;
        let hookX, hookY, hookTargetX, hookTargetY;
        let isHookInWater = false, isReeling = false;
        let currentFish = null;
        let fishes = [];
        let bubbles = [];
        let ripples = [];
        let particles = [];
        let clouds = [];
        let birds = [];
        let sunPosition = { x: 0, y: 0 };
        let waterOffset = 0;

        document.getElementById('bestScore').textContent = bestScore;

        // Generate environment
        function generateEnvironment() {
            clouds = [];
            for (let i = 0; i < 4; i++) {
                clouds.push({
                    x: Math.random() * W,
                    y: Math.random() * H * 0.3 + 20,
                    w: Math.random() * 80 + 60,
                    h: Math.random() * 25 + 15,
                    speed: Math.random() * 0.3 + 0.1
                });
            }

            birds = [];
            for (let i = 0; i < 3; i++) {
                birds.push({
                    x: Math.random() * W,
                    y: Math.random() * H * 0.25 + 30,
                    speed: Math.random() * 0.8 + 0.3,
                    wingPhase: Math.random() * Math.PI * 2
                });
            }

            bubbles = [];
            ripples = [];
            sunPosition = { x: W * 0.75, y: H * 0.18 };
        }

        function spawnFishes() {
            fishes = [];
            const types = [
                { name: 'Bass', color: '#44aa44', size: 35, points: 50, speed: 1.2, pattern: 'stripes' },
                { name: 'Trout', color: '#ff8866', size: 30, points: 75, speed: 1.8, pattern: 'spots' },
                { name: 'Salmon', color: '#ff4466', size: 38, points: 100, speed: 1.5, pattern: 'scales' },
                { name: 'Golden Carp', color: '#ffaa00', size: 42, points: 200, speed: 0.9, pattern: 'golden' },
                { name: 'Catfish', color: '#665544', size: 45, points: 150, speed: 0.6, pattern: 'whiskers' },
                { name: 'Pike', color: '#88aa66', size: 40, points: 120, speed: 1.4, pattern: 'camo' },
                { name: 'Blue Marlin', color: '#3366cc', size: 50, points: 500, speed: 2.2, pattern: 'shiny', rare: true },
                { name: 'Red Snapper', color: '#ff3333', size: 32, points: 80, speed: 1.6, pattern: 'solid' },
            ];

            for (let i = 0; i < 8; i++) {
                const type = types[Math.floor(Math.random() * types.length)];
                fishes.push({
                    x: Math.random() * (W * 0.7) + W * 0.1,
                    y: Math.random() * (H * 0.3) + H * 0.35,
                    w: type.size,
                    h: type.size * 0.55,
                    vx: (Math.random() - 0.5) * type.speed,
                    vy: (Math.random() - 0.5) * 0.6,
                    type: type,
                    tailPhase: Math.random() * Math.PI * 2,
                    alive: true
                });
            }
        }

        function spawnBubbles(x, y) {
            for (let i = 0; i < 4; i++) {
                bubbles.push({
                    x: x + (Math.random() - 0.5) * 20,
                    y: y,
                    size: Math.random() * 4 + 1,
                    vy: -(Math.random() * 1.5 + 0.5),
                    life: 1
                });
            }
        }

        function addRipple(x, y) {
            ripples.push({ x, y, radius: 2, life: 1 });
        }

        function addParticles(x, y, color, count) {
            for (let i = 0; i < count; i++) {
                particles.push({
                    x, y,
                    vx: (Math.random() - 0.5) * 5,
                    vy: (Math.random() - 0.5) * 5 - 3,
                    life: 1,
                    color
                });
            }
        }

        function initGame() {
            score = 0; fishCount = 0; streak = 0; gameTime = 90;
            hookX = W / 2; hookY = H * 0.22;
            hookTargetX = hookX; hookTargetY = hookY;
            isHookInWater = false; isReeling = false; isCharging = false;
            castPower = 0;
            currentFish = null;
            fishes = [];
            bubbles = [];
            ripples = [];
            particles = [];
            generateEnvironment();
            spawnFishes();
            updateHUD();
        }

        function updateHUD() {
            document.getElementById('score').textContent = score;
            document.getElementById('bestScore').textContent = bestScore;
            document.getElementById('fishCount').textContent = fishCount;
            document.getElementById('streak').textContent = streak;
            document.getElementById('powerBarFill').style.height = (castPower / 100 * 100) + '%';
        }

        // ==================== GAME LOOP ====================
        function update() {
            // Clouds
            clouds.forEach(c => { c.x += c.speed; if (c.x > W + 100) c.x = -100; });

            // Birds
            birds.forEach(b => {
                b.x += b.speed;
                b.wingPhase += 0.08;
                if (b.x > W + 50) b.x = -50;
            });

            // Water
            waterOffset += 0.02;

            // Bubbles
            bubbles = bubbles.filter(b => {
                b.y += b.vy;
                b.life -= 0.02;
                return b.life > 0 && b.y > H * 0.2;
            });

            // Ripples
            ripples = ripples.filter(r => {
                r.radius += 0.3;
                r.life -= 0.03;
                return r.life > 0;
            });

            // Particles
            particles = particles.filter(p => {
                p.x += p.vx; p.y += p.vy;
                p.vy += 0.1;
                p.life -= 0.025;
                return p.life > 0;
            });

            // Fishes
            fishes.forEach(f => {
                if (!f.alive) return;
                f.x += f.vx;
                f.y += f.vy;
                f.tailPhase += 0.15;

                // Bounce off walls
                if (f.x < W * 0.05 || f.x > W * 0.95) f.vx = -f.vx;
                if (f.y < H * 0.32 || f.y > H * 0.85) f.vy = -f.vy;

                // Random movement
                if (Math.random() < 0.01) f.vy = (Math.random() - 0.5) * f.type.speed * 2;
                if (Math.random() < 0.01) f.vx = (Math.random() - 0.5) * f.type.speed * 2;

                // Spawn bubbles occasionally
                if (Math.random() < 0.008) spawnBubbles(f.x, f.y);
            });

            // Charging
            if (isCharging) {
                castPower = Math.min(100, castPower + 1.8);
                updateHUD();
            }

            // Hook movement
            if (isHookInWater && !isReeling) {
                hookX += (hookTargetX - hookX) * 0.15;
                hookY += (hookTargetY - hookY) * 0.15;

                // Check fish collision
                if (!currentFish) {
                    for (const f of fishes) {
                        if (!f.alive) continue;
                        const dx = hookX - f.x;
                        const dy = hookY - f.y;
                        const dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < f.w * 0.7) {
                            currentFish = f;
                            beep(600, 0.1, 'square', 0.05);
                            showFishPopup(f.type.name + '!', f.type.points);
                            break;
                        }
                    }
                }

                // Bubbles near hook
                if (Math.random() < 0.2) spawnBubbles(hookX, hookY);
            }

            // Reeling
            if (isReeling && currentFish) {
                hookY -= 1.5;
                currentFish.y += (hookY - currentFish.y) * 0.3;
                currentFish.x += (hookX - currentFish.x) * 0.3;

                if (hookY <= H * 0.22) {
                    // Fish caught!
                    score += currentFish.type.points;
                    fishCount++;
                    streak++;
                    if (score > bestScore) {
                        bestScore = score;
                        localStorage.setItem('fishingpro_best', bestScore);
                    }
                    addParticles(hookX, hookY, currentFish.type.color, 15);
                    beep(800, 0.15, 'triangle', 0.06);
                    beep(1000, 0.2, 'triangle', 0.05);
                    currentFish.alive = false;
                    currentFish = null;
                    isReeling = false;
                    isHookInWater = false;
                    hookY = H * 0.22;
                    document.getElementById('castBtn').textContent = '🎣 CAST';
                    document.getElementById('castBtn').classList.remove('reel');
                    
                    // Respawn fish
                    if (fishes.filter(f => f.alive).length < 5) spawnFishes();
                }

                if (Math.random() < 0.3) spawnBubbles(hookX, hookY);
            }

            // Update hook position smoothly
            if (!isHookInWater && !isReeling) {
                hookX += (W / 2 - hookX) * 0.1;
                hookY += (H * 0.22 - hookY) * 0.1;
            }

            updateHUD();
        }

        // ==================== DRAWING ====================
        function draw() {
            // Sky gradient
            const skyGrad = ctx.createLinearGradient(0, 0, 0, H * 0.35);
            skyGrad.addColorStop(0, '#1a3a5c');
            skyGrad.addColorStop(0.4, '#4a8ab5');
            skyGrad.addColorStop(0.8, '#88ccdd');
            skyGrad.addColorStop(1, '#aaddff');
            ctx.fillStyle = skyGrad;
            ctx.fillRect(0, 0, W, H * 0.35);

            // Sun
            const sunGrad = ctx.createRadialGradient(sunPosition.x, sunPosition.y, 15, sunPosition.x, sunPosition.y, 80);
            sunGrad.addColorStop(0, '#ffffcc');
            sunGrad.addColorStop(0.3, '#ffdd88');
            sunGrad.addColorStop(0.7, '#ffaa44');
            sunGrad.addColorStop(1, 'rgba(255,100,30,0)');
            ctx.fillStyle = sunGrad;
            ctx.beginPath();
            ctx.arc(sunPosition.x, sunPosition.y, 80, 0, Math.PI * 2);
            ctx.fill();

            // Sun body
            ctx.fillStyle = '#fffde0';
            ctx.beginPath();
            ctx.arc(sunPosition.x, sunPosition.y, 22, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#ffecb3';
            ctx.beginPath();
            ctx.arc(sunPosition.x, sunPosition.y, 18, 0, Math.PI * 2);
            ctx.fill();

            // Mountains
            ctx.fillStyle = '#2a4a3a';
            ctx.beginPath();
            ctx.moveTo(0, H * 0.32);
            ctx.quadraticCurveTo(W * 0.15, H * 0.15, W * 0.3, H * 0.28);
            ctx.quadraticCurveTo(W * 0.5, H * 0.12, W * 0.7, H * 0.3);
            ctx.quadraticCurveTo(W * 0.85, H * 0.18, W, H * 0.26);
            ctx.lineTo(W, H * 0.35);
            ctx.lineTo(0, H * 0.35);
            ctx.closePath();
            ctx.fill();

            // Snow caps
            ctx.fillStyle = '#ddeeff';
            ctx.beginPath();
            ctx.moveTo(W * 0.45, H * 0.16);
            ctx.lineTo(W * 0.5, H * 0.12);
            ctx.lineTo(W * 0.55, H * 0.17);
            ctx.fill();

            // Far mountains
            ctx.fillStyle = '#1a3025';
            ctx.beginPath();
            ctx.moveTo(0, H * 0.34);
            ctx.quadraticCurveTo(W * 0.25, H * 0.22, W * 0.5, H * 0.33);
            ctx.quadraticCurveTo(W * 0.75, H * 0.24, W, H * 0.31);
            ctx.lineTo(W, H * 0.35);
            ctx.lineTo(0, H * 0.35);
            ctx.closePath();
            ctx.fill();

            // Clouds
            clouds.forEach(c => {
                ctx.fillStyle = 'rgba(255,255,255,0.8)';
                ctx.beginPath();
                ctx.arc(c.x, c.y, c.h * 0.7, 0, Math.PI * 2);
                ctx.arc(c.x + c.w * 0.25, c.y - c.h * 0.2, c.h * 0.6, 0, Math.PI * 2);
                ctx.arc(c.x + c.w * 0.5, c.y, c.h * 0.65, 0, Math.PI * 2);
                ctx.arc(c.x + c.w * 0.35, c.y + c.h * 0.1, c.h * 0.5, 0, Math.PI * 2);
                ctx.fill();
            });

            // Birds
            birds.forEach(b => {
                const wingY = Math.sin(b.wingPhase) * 5;
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 1.2;
                ctx.beginPath();
                ctx.moveTo(b.x - 6, b.y);
                ctx.quadraticCurveTo(b.x - 3, b.y - 4 - wingY, b.x, b.y);
                ctx.quadraticCurveTo(b.x + 3, b.y - 4 - wingY, b.x + 6, b.y);
                ctx.stroke();
            });

            // Ground
            ctx.fillStyle = '#3a6a3a';
            ctx.fillRect(0, H * 0.33, W, H * 0.03);
            ctx.fillStyle = '#4a8a3a';
            ctx.fillRect(0, H * 0.34, W, H * 0.02);

            // Water
            const waterGrad = ctx.createLinearGradient(0, H * 0.35, 0, H);
            waterGrad.addColorStop(0, '#3388aa');
            waterGrad.addColorStop(0.3, '#2266aa');
            waterGrad.addColorStop(0.7, '#114488');
            waterGrad.addColorStop(1, '#0a2255');
            ctx.fillStyle = waterGrad;
            ctx.fillRect(0, H * 0.35, W, H * 0.65);

            // Water surface shine
            for (let i = 0; i < 20; i++) {
                const wx = (i * 137 + waterOffset * 50) % W;
                const wy = H * 0.35 + Math.sin(i * 2.7 + waterOffset * 3) * 3;
                ctx.fillStyle = 'rgba(255,255,255,0.15)';
                ctx.fillRect(wx, wy, 15 + Math.sin(i) * 10, 1.5);
            }

            // Water caustics
            for (let i = 0; i < 30; i++) {
                const cx = (i * 97 + waterOffset * 30) % W;
                const cy = H * 0.4 + (i * 53) % (H * 0.5);
                ctx.fillStyle = 'rgba(255,255,255,0.03)';
                ctx.beginPath();
                ctx.arc(cx, cy, 8 + Math.sin(i + waterOffset) * 4, 0, Math.PI * 2);
                ctx.fill();
            }

            // Ripples
            ripples.forEach(r => {
                ctx.strokeStyle = `rgba(255,255,255,${r.life * 0.4})`;
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.arc(r.x, r.y, r.radius, 0, Math.PI * 2);
                ctx.stroke();
            });

            // Bubbles
            bubbles.forEach(b => {
                ctx.strokeStyle = `rgba(255,255,255,${b.life * 0.5})`;
                ctx.lineWidth = 0.8;
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.size, 0, Math.PI * 2);
                ctx.stroke();
                ctx.fillStyle = `rgba(255,255,255,${b.life * 0.15})`;
                ctx.fill();
            });

            // Fishes
            fishes.forEach(f => {
                if (!f.alive) return;
                drawFish(f);
            });

            // Fishing rod
            drawFishingRod();

            // Hook and line
            if (isHookInWater || isReeling) {
                ctx.strokeStyle = '#888';
                ctx.lineWidth = 1;
                ctx.setLineDash([4, 3]);
                ctx.beginPath();
                ctx.moveTo(W / 2, H * 0.22);
                ctx.lineTo(hookX, hookY);
                ctx.stroke();
                ctx.setLineDash([]);

                // Hook
                ctx.fillStyle = '#ccc';
                ctx.beginPath();
                ctx.arc(hookX, hookY, 5, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#999';
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                ctx.arc(hookX, hookY + 5, 4, Math.PI, Math.PI * 2);
                ctx.stroke();
            }

            // Current fish on hook
            if (currentFish && isReeling) {
                drawFishOnHook(currentFish, hookX, hookY);
            }

            // Particles
            particles.forEach(p => {
                ctx.fillStyle = p.color.replace(')', `,${p.life})`).replace('rgb', 'rgba');
                ctx.beginPath();
                ctx.arc(p.x, p.y, 3 * p.life, 0, Math.PI * 2);
                ctx.fill();
            });

            // Island on the side
            drawIsland();
        }

        function drawIsland() {
            const ix = W * 0.08;
            const iy = H * 0.3;
            
            ctx.fillStyle = '#c9a84c';
            ctx.beginPath();
            ctx.arc(ix, iy, 25, Math.PI, 0);
            ctx.fill();
            
            ctx.fillStyle = '#5a8a3a';
            ctx.beginPath();
            ctx.arc(ix, iy - 8, 18, Math.PI, 0);
            ctx.fill();

            // Palm tree
            ctx.fillStyle = '#8B4513';
            ctx.fillRect(ix - 2, iy - 35, 4, 30);
            
            ctx.fillStyle = '#228B22';
            for (let a = 0; a < Math.PI * 2; a += Math.PI / 4) {
                ctx.beginPath();
                ctx.moveTo(ix, iy - 35);
                ctx.quadraticCurveTo(
                    ix + Math.cos(a) * 20, iy - 45 - Math.random() * 5,
                    ix + Math.cos(a) * 30, iy - 35
                );
                ctx.fill();
            }
        }

        function drawFish(f) {
            ctx.save();
            ctx.translate(f.x, f.y);
            
            const dir = f.vx > 0 ? 1 : -1;
            if (dir < 0) ctx.scale(-1, 1);

            const w = f.w, h = f.h;
            const t = f.type;

            // Body
            const bodyGrad = ctx.createLinearGradient(-w/2, 0, w/2, 0);
            bodyGrad.addColorStop(0, t.color);
            bodyGrad.addColorStop(0.5, t.color.replace('44', '88').replace('66', 'aa').replace('33', '77'));
            bodyGrad.addColorStop(1, t.color);
            ctx.fillStyle = bodyGrad;
            ctx.beginPath();
            ctx.ellipse(0, 0, w/2, h/2, 0, 0, Math.PI * 2);
            ctx.fill();

            // Tail
            const tailSwing = Math.sin(f.tailPhase) * h * 0.3;
            ctx.fillStyle = t.color;
            ctx.beginPath();
            ctx.moveTo(-w/2 + 5, 0);
            ctx.quadraticCurveTo(-w/2 - 8, -h/2 + tailSwing, -w/2 - h * 0.6, -h * 0.4 + tailSwing);
            ctx.quadraticCurveTo(-w/2 - 5, tailSwing, -w/2 - h * 0.6, h * 0.4 + tailSwing);
            ctx.quadraticCurveTo(-w/2 - 8, h/2 + tailSwing, -w/2 + 5, 0);
            ctx.fill();

            // Eye
            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.arc(w/2 - w*0.2, -h*0.15, h*0.2, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#000';
            ctx.beginPath();
            ctx.arc(w/2 - w*0.17, -h*0.13, h*0.1, 0, Math.PI * 2);
            ctx.fill();

            // Special patterns
            if (t.pattern === 'golden') {
                ctx.fillStyle = 'rgba(255,255,255,0.3)';
                ctx.fillRect(-w*0.1, -h*0.1, w*0.3, h*0.2);
                ctx.fillStyle = '#ffdd44';
                ctx.beginPath();
                ctx.arc(w*0.2, 0, h*0.12, 0, Math.PI * 2);
                ctx.fill();
            } else if (t.pattern === 'shiny') {
                ctx.fillStyle = 'rgba(255,255,255,0.25)';
                ctx.fillRect(-w*0.15, -h*0.35, w*0.5, h*0.7);
            }

            // Fins
            ctx.fillStyle = t.color.replace('44', '55').replace('66', '77').replace('33', '44');
            ctx.beginPath();
            ctx.moveTo(0, -h/2);
            ctx.quadraticCurveTo(w*0.1, -h, -w*0.1, -h/2 + 2);
            ctx.fill();

            if (t.pattern === 'whiskers') {
                ctx.strokeStyle = '#aaa';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(w/2, 0);
                ctx.quadraticCurveTo(w/2 + 6, h*0.3, w/2 + 8, h*0.6);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(w/2, h*0.1);
                ctx.quadraticCurveTo(w/2 + 6, h*0.4, w/2 + 8, h*0.7);
                ctx.stroke();
            }

            ctx.restore();
        }

        function drawFishOnHook(f, hx, hy) {
            ctx.save();
            ctx.translate(hx, hy);
            ctx.scale(1.2, 1.2);

            const w = f.w, h = f.h;
            const t = f.type;

            const bodyGrad = ctx.createLinearGradient(-w/2, 0, w/2, 0);
            bodyGrad.addColorStop(0, t.color);
            bodyGrad.addColorStop(1, t.color);
            ctx.fillStyle = bodyGrad;
            ctx.beginPath();
            ctx.ellipse(0, 0, w/2, h/2, 0, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.arc(w/2 - w*0.2, -h*0.15, h*0.2, 0, Math.PI * 2);
            ctx.fill();
            ctx.fillStyle = '#000';
            ctx.beginPath();
            ctx.arc(w/2 - w*0.17, -h*0.13, h*0.1, 0, Math.PI * 2);
            ctx.fill();

            ctx.restore();
        }

        function drawFishingRod() {
            const rx = W / 2;
            const ry = H * 0.22;

            // Rod
            ctx.strokeStyle = '#8B4513';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(rx - 8, ry + 20);
            ctx.quadraticCurveTo(rx - 3, ry - 5, rx + 30, ry - 50);
            ctx.stroke();

            ctx.strokeStyle = '#6B3410';
            ctx.lineWidth = 2.5;
            ctx.beginPath();
            ctx.moveTo(rx - 6, ry + 18);
            ctx.quadraticCurveTo(rx - 2, ry - 3, rx + 28, ry - 46);
            ctx.stroke();

            // Reel
            ctx.fillStyle = '#555';
            ctx.beginPath();
            ctx.arc(rx - 5, ry + 15, 8, 0, Math.PI * 2);
            ctx.fill();
            ctx.strokeStyle = '#777';
            ctx.lineWidth = 1;
            ctx.stroke();
            ctx.fillStyle = '#888';
            ctx.beginPath();
            ctx.arc(rx - 5, ry + 15, 4, 0, Math.PI * 2);
            ctx.fill();
        }

        // ==================== CONTROLS ====================
        function handleCast() {
            initAudio();
            if (gameState === 'idle') startGame();

            if (!isHookInWater && !isReeling) {
                // Start charging
                if (!isCharging) {
                    isCharging = true;
                    castPower = 0;
                    document.getElementById('castBtn').textContent = '⚡ CHARGING...';
                }
            } else if (isHookInWater && !isReeling && currentFish) {
                // Start reeling
                isReeling = true;
                document.getElementById('castBtn').textContent = '🎣 REELING...';
                document.getElementById('castBtn').classList.add('reel');
                beep(400, 0.08);
            }
        }

        // Release to cast
        document.addEventListener('pointerup', () => {
            if (isCharging && !isHookInWater && !isReeling) {
                isCharging = false;
                if (castPower > 10) {
                    hookTargetX = W/2 + (castPower - 50) * 2;
                    hookTargetY = H * 0.35 + (castPower / 100) * H * 0.5;
                    isHookInWater = true;
                    addRipple(hookTargetX, hookTargetY);
                    beep(300 + castPower * 2, 0.15, 'triangle', 0.04);
                    document.getElementById('castBtn').textContent = '🎣 WAITING...';
                } else {
                    castPower = 0;
                    updateHUD();
                    document.getElementById('castBtn').textContent = '🎣 CAST';
                }
            }
        });

        // Keyboard
        document.addEventListener('keydown', e => {
            if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                handleCast();
            }
        });

        function showFishPopup(name, points) {
            const popup = document.getElementById('fishPopup');
            popup.textContent = '🐟 ' + name + '! +' + points;
            popup.classList.add('show');
            setTimeout(() => popup.classList.remove('show'), 2000);
        }

        // ==================== GAME LOOP ====================
        function gameLoop() {
            if (gameState === 'playing') {
                update();
                gameTime -= 1/60;
                if (gameTime <= 0) {
                    gameState = 'gameover';
                    if (score > bestScore) {
                        bestScore = score;
                        localStorage.setItem('fishingpro_best', bestScore);
                    }
                    document.getElementById('finalScore').textContent = 'Score: ' + score;
                    document.getElementById('gameOverOverlay').classList.remove('hidden');
                }
            }
            draw();
            requestAnimationFrame(gameLoop);
        }

        function startGame() {
            initAudio();
            initGame();
            gameState = 'playing';
            document.getElementById('startOverlay').classList.add('hidden');
            document.getElementById('gameOverOverlay').classList.add('hidden');
            updateHUD();
        }

        function restartGame() {
            gameState = 'idle';
            document.getElementById('startOverlay').classList.remove('hidden');
            document.getElementById('gameOverOverlay').classList.add('hidden');
            initGame();
        }

        // ==================== INIT ====================
        generateEnvironment();
        spawnFishes();
        gameLoop();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  🎣 Fishing Pro - Legendary Edition    ║")
    print("║  🐟 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🎣 المميزات الواقعية:")
    print("  🌅 سماء متدرجة مع شمس")
    print("  ⛰️ جبال بتفاصيل وقمم ثلجية")
    print("  ☁️ سحب متحركة")
    print("  🐦 طيور بأجنحة متحركة")
    print("  🏝️ جزيرة بنخلة")
    print("  🌊 مياه بتموجات وتأثيرات ضوئية")
    print("  🫧 فقاعات")
    print("  🎣 صنارة بقصبة وبكرة")
    print("  🐟 8 أنواع أسماك بتصاميم مختلفة")
    print("  ⚡ شريط قوة الرمي")
    print("  💫 جسيمات عند الصيد")
    print("  📊 Streak counter")
    print("  ⏱️ 90 ثانية للعب")

if __name__ == "__main__":
    create_website_files()

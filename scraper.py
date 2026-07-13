import os

def create_website_files():
    """إنشاء لعبة Snake X الأسطورية"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Snake X | Legendary</title>
    <style>
        :root {
            --bg: #000;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --gold-glow: rgba(201,168,76,0.5);
            --neon-green: #00ff88;
            --neon-red: #ff3344;
            --text: #e0d5c0;
            --text-dim: #6b6355;
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
            max-width: 440px;
            padding: 10px;
        }

        /* Header */
        .header {
            text-align: center;
            margin-bottom: 8px;
        }

        .title {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(180deg, var(--gold-light), var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 15px var(--gold-glow));
        }

        .subtitle {
            font-size: 8px;
            color: var(--text-dim);
            letter-spacing: 5px;
            text-transform: uppercase;
        }

        /* Score Panel */
        .score-panel {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 14px;
            margin-bottom: 8px;
            background: #080808;
            border: 1px solid #1a1a1a;
            border-radius: 16px;
        }

        .score-item {
            text-align: center;
        }

        .score-label {
            font-size: 7px;
            color: var(--text-dim);
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .score-value {
            font-size: 22px;
            font-weight: 900;
            color: var(--gold);
        }

        .high-score .score-value {
            color: var(--neon-green);
        }

        .best-score .score-value {
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .divider-v {
            width: 1px;
            height: 30px;
            background: linear-gradient(180deg, transparent, #222, transparent);
        }

        /* Canvas */
        .canvas-container {
            position: relative;
            border: 1px solid #1a1a1a;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 0 40px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.02) inset;
            background: #020202;
        }

        canvas {
            display: block;
            width: 100%;
            height: auto;
            image-rendering: pixelated;
        }

        /* Overlay */
        .overlay {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background: rgba(0,0,0,0.85);
            border-radius: 16px;
            transition: all 0.4s;
            z-index: 10;
        }

        .overlay.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .overlay-icon {
            font-size: 60px;
            animation: float 2s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .overlay-title {
            font-size: 22px;
            font-weight: 900;
            color: var(--gold);
            letter-spacing: 3px;
            margin: 8px 0;
        }

        .overlay-score {
            font-size: 40px;
            font-weight: 900;
            background: linear-gradient(135deg, var(--neon-red), var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 4px 0;
        }

        .overlay-best {
            font-size: 12px;
            color: var(--text-dim);
            letter-spacing: 2px;
            margin-bottom: 12px;
        }

        .btn-play {
            padding: 14px 40px;
            background: linear-gradient(135deg, var(--gold), var(--gold-light), var(--gold));
            background-size: 200% 200%;
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 30px;
            font-size: 14px;
            letter-spacing: 3px;
            text-transform: uppercase;
            box-shadow: 0 6px 25px var(--gold-glow);
            animation: gradientShift 3s ease-in-out infinite;
            font-family: inherit;
            transition: all 0.3s;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .btn-play:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 35px var(--gold-glow);
        }

        .btn-play:active {
            transform: scale(0.95);
        }

        .overlay-hint {
            font-size: 9px;
            color: #333;
            letter-spacing: 2px;
            margin-top: 12px;
            text-transform: uppercase;
        }

        /* Controls */
        .controls {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
            margin-top: 10px;
            max-width: 280px;
            margin-left: auto;
            margin-right: auto;
        }

        .ctrl-btn {
            aspect-ratio: 1;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            color: var(--text);
            cursor: pointer;
            border-radius: 14px;
            font-size: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            -webkit-tap-highlight-color: transparent;
        }

        .ctrl-btn:active {
            background: rgba(201,168,76,0.15);
            border-color: var(--gold);
            transform: scale(0.9);
            box-shadow: 0 0 20px var(--gold-glow);
        }

        .ctrl-empty {
            background: transparent;
            border: none;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #0a0a0a;
            border: 1px solid var(--gold);
            color: var(--gold);
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 11px;
            letter-spacing: 2px;
            z-index: 200;
            transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 15px 40px rgba(0,0,0,0.9), 0 0 30px var(--gold-glow);
        }

        .toast.show {
            transform: translateX(-50%) translateY(0);
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 10px;
            font-size: 7px;
            color: #111;
            letter-spacing: 3px;
        }
        .footer span { color: var(--gold); }
    </style>
</head>
<body>
    <div class="game-wrapper">
        <!-- Header -->
        <div class="header">
            <h1 class="title">SNAKE X</h1>
            <p class="subtitle">✦ Legendary Edition ✦</p>
        </div>

        <!-- Score -->
        <div class="score-panel">
            <div class="score-item">
                <span class="score-label">Score</span>
                <span class="score-value" id="score">0</span>
            </div>
            <div class="divider-v"></div>
            <div class="score-item high-score">
                <span class="score-label">High</span>
                <span class="score-value" id="highScore">0</span>
            </div>
            <div class="divider-v"></div>
            <div class="score-item best-score">
                <span class="score-label">Best</span>
                <span class="score-value" id="bestScore">0</span>
            </div>
        </div>

        <!-- Canvas -->
        <div class="canvas-container" id="canvasContainer">
            <canvas id="gameCanvas"></canvas>
            
            <!-- Start Overlay -->
            <div class="overlay" id="startOverlay">
                <div class="overlay-icon">👑</div>
                <div class="overlay-title">SNAKE X</div>
                <button class="btn-play" onclick="startGame()">✦ Play ✦</button>
                <p class="overlay-hint">Swipe or use arrows</p>
            </div>

            <!-- Game Over Overlay -->
            <div class="overlay hidden" id="gameOverOverlay">
                <div class="overlay-icon">💀</div>
                <div class="overlay-title">GAME OVER</div>
                <div class="overlay-score" id="finalScore">0</div>
                <div class="overlay-best" id="newBest"></div>
                <button class="btn-play" onclick="startGame()">✦ Play Again ✦</button>
            </div>
        </div>

        <!-- Controls -->
        <div class="controls">
            <div class="ctrl-empty"></div>
            <button class="ctrl-btn" onclick="changeDirection('up')">▲</button>
            <div class="ctrl-empty"></div>
            <button class="ctrl-btn" onclick="changeDirection('left')">◀</button>
            <button class="ctrl-btn" onclick="changeDirection('down')">▼</button>
            <button class="ctrl-btn" onclick="changeDirection('right')">▶</button>
        </div>

        <p class="footer">
            <span>◆</span> Snake X Legendary <span>•</span> Offline Game <span>◆</span>
        </p>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script>
        // ==================== CANVAS SETUP ====================
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const container = document.getElementById('canvasContainer');

        const GRID_SIZE = 20;
        let CELL_SIZE;
        let COLS, ROWS;

        function resizeCanvas() {
            const containerWidth = container.clientWidth;
            CELL_SIZE = Math.floor(containerWidth / GRID_SIZE);
            COLS = GRID_SIZE;
            ROWS = GRID_SIZE;
            canvas.width = COLS * CELL_SIZE;
            canvas.height = ROWS * CELL_SIZE;
        }

        resizeCanvas();
        window.addEventListener('resize', () => {
            resizeCanvas();
            if (gameState === 'playing') draw();
        });

        // ==================== GAME STATE ====================
        let snake = [];
        let food = {};
        let specialFood = null;
        let specialFoodTimer = 0;
        let direction = 'right';
        let nextDirection = 'right';
        let score = 0;
        let highScore = parseInt(localStorage.getItem('snakex_high') || '0');
        let bestScore = parseInt(localStorage.getItem('snakex_best') || '0');
        let gameState = 'idle'; // idle | playing | over
        let gameLoop = null;
        let speed = 100;
        let particles = [];

        document.getElementById('highScore').textContent = highScore;
        document.getElementById('bestScore').textContent = bestScore;

        // ==================== AUDIO (Simple beeps) ====================
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        let audioCtx;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new AudioContext();
            }
        }

        function playBeep(freq, duration, type = 'square') {
            if (!audioCtx) return;
            try {
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start(audioCtx.currentTime);
                osc.stop(audioCtx.currentTime + duration);
            } catch(e) {}
        }

        // ==================== INIT GAME ====================
        function initGame() {
            const midX = Math.floor(COLS / 2);
            const midY = Math.floor(ROWS / 2);
            
            snake = [
                { x: midX, y: midY },
                { x: midX - 1, y: midY },
                { x: midX - 2, y: midY }
            ];
            
            direction = 'right';
            nextDirection = 'right';
            score = 0;
            speed = 100;
            particles = [];
            specialFood = null;
            specialFoodTimer = 0;
            
            document.getElementById('score').textContent = '0';
            document.getElementById('highScore').textContent = highScore;
            document.getElementById('bestScore').textContent = bestScore;
            
            spawnFood();
        }

        // ==================== FOOD ====================
        function spawnFood() {
            let pos;
            do {
                pos = {
                    x: Math.floor(Math.random() * COLS),
                    y: Math.floor(Math.random() * ROWS)
                };
            } while (snake.some(s => s.x === pos.x && s.y === pos.y));
            
            food = pos;
            food.type = Math.random() < 0.2 ? 'golden' : 'normal';
        }

        function spawnSpecialFood() {
            let pos;
            do {
                pos = {
                    x: Math.floor(Math.random() * COLS),
                    y: Math.floor(Math.random() * ROWS)
                };
            } while (snake.some(s => s.x === pos.x && s.y === pos.y) || (food.x === pos.x && food.y === pos.y));
            
            specialFood = pos;
            specialFoodTimer = 50; // disappears after 50 frames
        }

        // ==================== PARTICLES ====================
        function addParticles(x, y, color) {
            for (let i = 0; i < 8; i++) {
                particles.push({
                    x: x * CELL_SIZE + CELL_SIZE / 2,
                    y: y * CELL_SIZE + CELL_SIZE / 2,
                    vx: (Math.random() - 0.5) * 4,
                    vy: (Math.random() - 0.5) * 4,
                    life: 1,
                    color: color
                });
            }
        }

        function updateParticles() {
            particles = particles.filter(p => {
                p.x += p.vx;
                p.y += p.vy;
                p.life -= 0.03;
                return p.life > 0;
            });
        }

        // ==================== GAME LOGIC ====================
        function changeDirection(dir) {
            initAudio();
            
            const opposites = {
                'up': 'down',
                'down': 'up',
                'left': 'right',
                'right': 'left'
            };
            
            if (direction !== opposites[dir]) {
                nextDirection = dir;
            }
        }

        function update() {
            direction = nextDirection;
            
            const head = { ...snake[0] };
            
            switch(direction) {
                case 'up': head.y--; break;
                case 'down': head.y++; break;
                case 'left': head.x--; break;
                case 'right': head.x++; break;
            }
            
            // Wall collision
            if (head.x < 0 || head.x >= COLS || head.y < 0 || head.y >= ROWS) {
                gameOver();
                return;
            }
            
            // Self collision
            if (snake.some(s => s.x === head.x && s.y === head.y)) {
                gameOver();
                return;
            }
            
            snake.unshift(head);
            
            // Food collision
            if (head.x === food.x && head.y === food.y) {
                const points = food.type === 'golden' ? 5 : 1;
                score += points;
                document.getElementById('score').textContent = score;
                
                addParticles(food.x, food.y, food.type === 'golden' ? '#c9a84c' : '#00ff88');
                playBeep(food.type === 'golden' ? 800 : 400, 0.1);
                
                spawnFood();
                
                // Speed up
                if (score % 10 === 0) {
                    speed = Math.max(50, speed - 5);
                }
                
                // Special food chance
                if (Math.random() < 0.15 && !specialFood) {
                    spawnSpecialFood();
                }
            } else if (specialFood && head.x === specialFood.x && head.y === specialFood.y) {
                score += 3;
                document.getElementById('score').textContent = score;
                addParticles(specialFood.x, specialFood.y, '#ff6600');
                playBeep(600, 0.15, 'triangle');
                specialFood = null;
                
                // Grow extra
                snake.push({ ...snake[snake.length - 1] });
            } else {
                snake.pop();
            }
            
            // Special food timer
            if (specialFood) {
                specialFoodTimer--;
                if (specialFoodTimer <= 0) {
                    specialFood = null;
                }
            }
            
            // Random special food
            if (!specialFood && Math.random() < 0.005) {
                spawnSpecialFood();
            }
            
            updateParticles();
            updateScore();
        }

        function updateScore() {
            if (score > highScore) {
                highScore = score;
                localStorage.setItem('snakex_high', highScore);
                document.getElementById('highScore').textContent = highScore;
            }
            if (score > bestScore) {
                bestScore = score;
                localStorage.setItem('snakex_best', bestScore);
                document.getElementById('bestScore').textContent = bestScore;
            }
        }

        function gameOver() {
            gameState = 'over';
            clearInterval(gameLoop);
            playBeep(200, 0.3, 'sawtooth');
            playBeep(150, 0.4, 'sawtooth');
            
            updateScore();
            
            document.getElementById('finalScore').textContent = score;
            
            const newBestEl = document.getElementById('newBest');
            if (score >= bestScore && score > 0) {
                newBestEl.textContent = '🏆 NEW BEST SCORE! 🏆';
            } else {
                newBestEl.textContent = 'Best: ' + bestScore;
            }
            
            document.getElementById('gameOverOverlay').classList.remove('hidden');
            
            if (score > 0 && score % 20 === 0) {
                showToast('🔥 Amazing! Score: ' + score);
            }
        }

        // ==================== DRAWING ====================
        function draw() {
            // Clear
            ctx.fillStyle = '#020202';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Grid
            ctx.strokeStyle = 'rgba(255,255,255,0.015)';
            ctx.lineWidth = 0.5;
            for (let x = 0; x < COLS; x++) {
                for (let y = 0; y < ROWS; y++) {
                    ctx.strokeRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE);
                }
            }
            
            // Food
            const fx = food.x * CELL_SIZE + CELL_SIZE / 2;
            const fy = food.y * CELL_SIZE + CELL_SIZE / 2;
            const fr = CELL_SIZE / 2 - 2;
            
            if (food.type === 'golden') {
                // Golden apple with glow
                const gradient = ctx.createRadialGradient(fx, fy, 0, fx, fy, fr + 4);
                gradient.addColorStop(0, '#e2c97e');
                gradient.addColorStop(0.6, '#c9a84c');
                gradient.addColorStop(1, '#8b7300');
                
                ctx.shadowColor = 'rgba(201,168,76,0.8)';
                ctx.shadowBlur = 12;
                ctx.fillStyle = gradient;
                ctx.beginPath();
                ctx.arc(fx, fy, fr, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;
                
                // Crown icon
                ctx.fillStyle = '#000';
                ctx.font = `${CELL_SIZE * 0.6}px Arial`;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('👑', fx, fy);
            } else {
                // Normal food - neon green
                ctx.shadowColor = 'rgba(0,255,136,0.6)';
                ctx.shadowBlur = 8;
                ctx.fillStyle = '#00ff88';
                ctx.beginPath();
                ctx.arc(fx, fy, fr, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;
            }
            
            // Special food
            if (specialFood) {
                const sfx = specialFood.x * CELL_SIZE + CELL_SIZE / 2;
                const sfy = specialFood.y * CELL_SIZE + CELL_SIZE / 2;
                
                ctx.shadowColor = 'rgba(255,102,0,0.8)';
                ctx.shadowBlur = 10;
                ctx.fillStyle = '#ff6600';
                ctx.beginPath();
                
                // Diamond shape
                const s = CELL_SIZE / 2 - 2;
                ctx.moveTo(sfx, sfy - s);
                ctx.lineTo(sfx + s, sfy);
                ctx.lineTo(sfx, sfy + s);
                ctx.lineTo(sfx - s, sfy);
                ctx.closePath();
                ctx.fill();
                ctx.shadowBlur = 0;
                
                // Blinking effect
                if (specialFoodTimer < 15 && Math.floor(specialFoodTimer / 3) % 2 === 0) {
                    ctx.fillStyle = 'rgba(255,255,255,0.4)';
                    ctx.fill();
                }
            }
            
            // Snake
            snake.forEach((segment, index) => {
                const sx = segment.x * CELL_SIZE;
                const sy = segment.y * CELL_SIZE;
                const padding = 1;
                
                if (index === 0) {
                    // Head - golden
                    const gradient = ctx.createLinearGradient(sx, sy, sx + CELL_SIZE, sy + CELL_SIZE);
                    gradient.addColorStop(0, '#e2c97e');
                    gradient.addColorStop(1, '#c9a84c');
                    
                    ctx.shadowColor = 'rgba(201,168,76,0.6)';
                    ctx.shadowBlur = 8;
                    ctx.fillStyle = gradient;
                    ctx.beginPath();
                    ctx.roundRect(sx + padding, sy + padding, CELL_SIZE - padding * 2, CELL_SIZE - padding * 2, 6);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                    
                    // Eyes
                    ctx.fillStyle = '#000';
                    const eyeSize = CELL_SIZE * 0.2;
                    let ex1, ey1, ex2, ey2;
                    
                    switch(direction) {
                        case 'right':
                            ex1 = sx + CELL_SIZE * 0.65; ey1 = sy + CELL_SIZE * 0.25;
                            ex2 = sx + CELL_SIZE * 0.65; ey2 = sy + CELL_SIZE * 0.65;
                            break;
                        case 'left':
                            ex1 = sx + CELL_SIZE * 0.35; ey1 = sy + CELL_SIZE * 0.25;
                            ex2 = sx + CELL_SIZE * 0.35; ey2 = sy + CELL_SIZE * 0.65;
                            break;
                        case 'up':
                            ex1 = sx + CELL_SIZE * 0.25; ey1 = sy + CELL_SIZE * 0.35;
                            ex2 = sx + CELL_SIZE * 0.65; ey2 = sy + CELL_SIZE * 0.35;
                            break;
                        case 'down':
                            ex1 = sx + CELL_SIZE * 0.25; ey1 = sy + CELL_SIZE * 0.65;
                            ex2 = sx + CELL_SIZE * 0.65; ey2 = sy + CELL_SIZE * 0.65;
                            break;
                    }
                    
                    ctx.beginPath();
                    ctx.arc(ex1, ey1, eyeSize, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.beginPath();
                    ctx.arc(ex2, ey2, eyeSize, 0, Math.PI * 2);
                    ctx.fill();
                } else {
                    // Body - gradient from gold to green
                    const ratio = index / snake.length;
                    const r = Math.floor(0 + ratio * 0);
                    const g = Math.floor(200 - ratio * 150);
                    const b = Math.floor(0 + ratio * 100);
                    
                    ctx.fillStyle = `rgb(${r},${g},${b})`;
                    ctx.beginPath();
                    ctx.roundRect(sx + padding, sy + padding, CELL_SIZE - padding * 2, CELL_SIZE - padding * 2, 5);
                    ctx.fill();
                }
            });
            
            // Particles
            particles.forEach(p => {
                ctx.fillStyle = p.color.replace(')', `,${p.life})`).replace('rgb', 'rgba');
                ctx.beginPath();
                ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
                ctx.fill();
            });
        }

        // ==================== GAME LOOP ====================
        function gameStep() {
            update();
            draw();
        }

        function startGame() {
            initAudio();
            initGame();
            gameState = 'playing';
            
            document.getElementById('startOverlay').classList.add('hidden');
            document.getElementById('gameOverOverlay').classList.add('hidden');
            
            if (gameLoop) clearInterval(gameLoop);
            gameLoop = setInterval(gameStep, speed);
            
            draw();
            playBeep(500, 0.05);
        }

        // ==================== CONTROLS ====================
        // Keyboard
        document.addEventListener('keydown', (e) => {
            const keys = {
                'ArrowUp': 'up',
                'ArrowDown': 'down',
                'ArrowLeft': 'left',
                'ArrowRight': 'right',
                'w': 'up', 'W': 'up',
                's': 'down', 'S': 'down',
                'a': 'left', 'A': 'left',
                'd': 'right', 'D': 'right'
            };
            
            if (keys[e.key]) {
                e.preventDefault();
                if (gameState === 'idle') startGame();
                changeDirection(keys[e.key]);
            }
            
            if (e.key === ' ' || e.key === 'Enter') {
                e.preventDefault();
                if (gameState !== 'playing') startGame();
            }
        });

        // Touch swipe
        let touchStartX = 0;
        let touchStartY = 0;

        canvas.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
            touchStartY = e.touches[0].clientY;
            
            if (gameState === 'idle') startGame();
        });

        canvas.addEventListener('touchmove', (e) => {
            e.preventDefault();
            
            const dx = e.touches[0].clientX - touchStartX;
            const dy = e.touches[0].clientY - touchStartY;
            
            if (Math.abs(dx) > 20 || Math.abs(dy) > 20) {
                if (Math.abs(dx) > Math.abs(dy)) {
                    changeDirection(dx > 0 ? 'right' : 'left');
                } else {
                    changeDirection(dy > 0 ? 'down' : 'up');
                }
                touchStartX = e.touches[0].clientX;
                touchStartY = e.touches[0].clientY;
            }
        });

        // ==================== TOAST ====================
        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.textContent = msg;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2000);
        }

        // ==================== POLYFILL ====================
        if (!ctx.roundRect) {
            ctx.roundRect = function(x, y, w, h, r) {
                if (typeof r === 'number') r = { tl: r, tr: r, br: r, bl: r };
                ctx.beginPath();
                ctx.moveTo(x + r.tl, y);
                ctx.lineTo(x + w - r.tr, y);
                ctx.quadraticCurveTo(x + w, y, x + w, y + r.tr);
                ctx.lineTo(x + w, y + h - r.br);
                ctx.quadraticCurveTo(x + w, y + h, x + w - r.br, y + h);
                ctx.lineTo(x + r.bl, y + h);
                ctx.quadraticCurveTo(x, y + h, x, y + h - r.bl);
                ctx.lineTo(x, y + r.tl);
                ctx.quadraticCurveTo(x, y, x + r.tl, y);
                ctx.closePath();
            };
        }

        // ==================== INIT ====================
        initGame();
        draw();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  👑 Snake X - Legendary Edition        ║")
    print("║  🐍 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🐍 المميزات الأسطورية:")
    print("  👑 ثعبان ذهبي برأس فاخر")
    print("  👀 عيون تتحرك مع الاتجاه")
    print("  🍎 فواكه عادية (خضراء نيون)")
    print("  👑 فواكه ذهبية (5 نقاط)")
    print("  💎 فواكه خاصة (3 نقاط + نمو إضافي)")
    print("  ✨ جسيمات انفجارية")
    print("  🎵 مؤثرات صوتية")
    print("  📊 3 عدادات (Score, High, Best)")
    print("  💀 Game Over بشاشة النتيجة")
    print("  🏆 رسالة NEW BEST SCORE")
    print("  📱 تحكم باللمس (Swipe)")
    print("  ⌨️ تحكم بالكيبورد (أسهم + WASD)")
    print("  🎮 أزرار تحكم على الشاشة")
    print("  ⚡ سرعة متزايدة")
    print("  💾 حفظ أفضل نتيجة تلقائي")
    print("  🌑 شبكة خلفية أنيقة")
    print("  🔥 تأثيرات توهج (Glow)")

if __name__ == "__main__":
    create_website_files()

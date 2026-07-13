import os

def create_website_files():
    """إنشاء لعبة Mario X الأسطورية مع 5 مراحل"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Mario X | Legendary</title>
    <style>
        :root {
            --bg: #000;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --gold-glow: rgba(201,168,76,0.5);
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
            padding: 8px;
        }

        /* Header */
        .header {
            text-align: center;
            margin-bottom: 4px;
        }

        .title {
            font-size: 26px;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(180deg, #ff4444, #ff8800, var(--gold-light));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 15px rgba(255,68,68,0.5));
        }

        .subtitle {
            font-size: 8px;
            color: #6b6355;
            letter-spacing: 5px;
            text-transform: uppercase;
        }

        /* HUD */
        .hud {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 14px;
            margin-bottom: 6px;
            background: #080808;
            border: 1px solid #1a1a1a;
            border-radius: 14px;
            gap: 10px;
        }

        .hud-item {
            text-align: center;
            flex: 1;
        }

        .hud-label {
            font-size: 7px;
            color: #555;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .hud-val {
            font-size: 16px;
            font-weight: 900;
            color: #ff8800;
        }

        .hud-val.coins { color: #ffaa00; }
        .hud-val.world { color: #00ff88; font-size: 10px; }
        .hud-val.lives { color: #ff4444; }

        .divider-v {
            width: 1px;
            height: 25px;
            background: linear-gradient(180deg, transparent, #1a1a1a, transparent);
        }

        /* Canvas */
        .canvas-container {
            position: relative;
            border: 1px solid #1a1a1a;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 0 50px rgba(0,0,0,0.6);
            background: #000;
        }

        canvas {
            display: block;
            width: 100%;
            height: auto;
        }

        /* Overlays */
        .overlay {
            position: absolute;
            inset: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            background: rgba(0,0,0,0.9);
            border-radius: 16px;
            z-index: 10;
            transition: all 0.4s;
            backdrop-filter: blur(5px);
        }

        .overlay.hidden { opacity: 0; pointer-events: none; }

        .overlay-icon {
            font-size: 50px;
            animation: float 2s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .overlay-title {
            font-size: 22px;
            font-weight: 900;
            color: #ff4444;
            letter-spacing: 4px;
            margin: 8px 0;
        }

        .overlay-level {
            font-size: 30px;
            font-weight: 900;
            background: linear-gradient(135deg, #ff4444, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 6px 0;
        }

        .overlay-sub {
            font-size: 10px;
            color: #666;
            letter-spacing: 2px;
            margin-bottom: 16px;
        }

        .btn-play {
            padding: 14px 40px;
            background: linear-gradient(135deg, #ff4444, #ff8800, var(--gold));
            background-size: 200% 200%;
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 30px;
            font-size: 14px;
            letter-spacing: 3px;
            text-transform: uppercase;
            box-shadow: 0 8px 30px rgba(255,68,68,0.4);
            animation: gradientShift 3s ease-in-out infinite;
            font-family: inherit;
            transition: all 0.3s;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .btn-play:active { transform: scale(0.93); }

        /* Controls */
        .controls {
            display: flex;
            gap: 8px;
            margin-top: 8px;
            justify-content: center;
        }

        .ctrl-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
            align-items: center;
        }

        .ctrl-row {
            display: flex;
            gap: 4px;
        }

        .ctrl-btn {
            width: 55px;
            height: 55px;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            color: #888;
            cursor: pointer;
            border-radius: 14px;
            font-size: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.15s;
            -webkit-tap-highlight-color: transparent;
        }

        .ctrl-btn:active {
            background: rgba(255,68,68,0.2);
            border-color: #ff4444;
            transform: scale(0.88);
            color: #ff4444;
        }

        .ctrl-jump {
            width: 120px;
            height: 60px;
            font-size: 16px;
            letter-spacing: 2px;
            font-weight: 700;
            color: #ff8800;
            border-color: #ff8800;
        }

        .ctrl-jump:active {
            background: rgba(255,136,0,0.2);
            border-color: #ff8800;
            color: #ff8800;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #0a0a0a;
            border: 1px solid #ff8800;
            color: #ff8800;
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 11px;
            letter-spacing: 2px;
            z-index: 200;
            transition: transform 0.5s;
            box-shadow: 0 15px 40px rgba(0,0,0,0.9);
        }

        .toast.show { transform: translateX(-50%) translateY(0); }

        .footer {
            text-align: center;
            margin-top: 6px;
            font-size: 7px;
            color: #0a0a0a;
            letter-spacing: 3px;
        }
        .footer span { color: #ff4444; }
    </style>
</head>
<body>
    <div class="game-wrapper">
        <!-- Header -->
        <div class="header">
            <h1 class="title">MARIO X</h1>
            <p class="subtitle">✦ Legendary Platform ✦</p>
        </div>

        <!-- HUD -->
        <div class="hud">
            <div class="hud-item">
                <span class="hud-label">Score</span>
                <span class="hud-val" id="score">0</span>
            </div>
            <div class="divider-v"></div>
            <div class="hud-item">
                <span class="hud-label">Coins</span>
                <span class="hud-val coins" id="coins">0</span>
            </div>
            <div class="divider-v"></div>
            <div class="hud-item">
                <span class="hud-label">World</span>
                <span class="hud-val world" id="worldDisplay">1-1</span>
            </div>
            <div class="divider-v"></div>
            <div class="hud-item">
                <span class="hud-label">Lives</span>
                <span class="hud-val lives" id="lives">❤️❤️❤️</span>
            </div>
        </div>

        <!-- Canvas -->
        <div class="canvas-container" id="canvasContainer">
            <canvas id="gameCanvas"></canvas>
            
            <!-- Start -->
            <div class="overlay" id="startOverlay">
                <div class="overlay-icon">🌟</div>
                <div class="overlay-title">MARIO X</div>
                <div class="overlay-level">World 1-1</div>
                <div class="overlay-sub">5 WORLDS • BOSS FIGHT</div>
                <button class="btn-play" onclick="startGame()">✦ START ✦</button>
            </div>

            <!-- Level Complete -->
            <div class="overlay hidden" id="levelOverlay">
                <div class="overlay-icon">🎉</div>
                <div class="overlay-title">LEVEL CLEAR!</div>
                <div class="overlay-level" id="levelScore">0</div>
                <div class="overlay-sub" id="nextWorld">Next: World 1-2</div>
                <button class="btn-play" onclick="nextLevel()">✦ NEXT LEVEL ✦</button>
            </div>

            <!-- Game Over -->
            <div class="overlay hidden" id="gameOverOverlay">
                <div class="overlay-icon">💀</div>
                <div class="overlay-title">GAME OVER</div>
                <div class="overlay-level" id="finalScore">0</div>
                <button class="btn-play" onclick="restartGame()">✦ RETRY ✦</button>
            </div>

            <!-- Win -->
            <div class="overlay hidden" id="winOverlay">
                <div class="overlay-icon">👑</div>
                <div class="overlay-title">YOU WIN!</div>
                <div class="overlay-level" id="winScore">0</div>
                <div class="overlay-sub">🏆 ALL WORLDS CLEARED! 🏆</div>
                <button class="btn-play" onclick="restartGame()">✦ PLAY AGAIN ✦</button>
            </div>
        </div>

        <!-- Controls -->
        <div class="controls">
            <div class="ctrl-group">
                <div class="ctrl-row">
                    <div class="ctrl-btn"></div>
                    <button class="ctrl-btn" onpointerdown="keys.up=true" onpointerup="keys.up=false" onpointerleave="keys.up=false">▲</button>
                    <div class="ctrl-btn"></div>
                </div>
                <div class="ctrl-row">
                    <button class="ctrl-btn" onpointerdown="keys.left=true" onpointerup="keys.left=false" onpointerleave="keys.left=false">◀</button>
                    <button class="ctrl-btn" onpointerdown="keys.down=true" onpointerup="keys.down=false" onpointerleave="keys.down=false">▼</button>
                    <button class="ctrl-btn" onpointerdown="keys.right=true" onpointerup="keys.right=false" onpointerleave="keys.right=false">▶</button>
                </div>
            </div>
            <button class="ctrl-btn ctrl-jump" onpointerdown="keys.space=true" onpointerup="keys.space=false" onpointerleave="keys.space=false">JUMP ⬆</button>
        </div>

        <p class="footer"><span>◆</span> MARIO X LEGENDARY <span>•</span> 5 WORLDS <span>◆</span></p>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script>
        // ==================== CANVAS ====================
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const container = document.getElementById('canvasContainer');

        const COLS = 40;
        const ROWS = 18;
        let TILE;

        function resize() {
            TILE = Math.floor(container.clientWidth / COLS);
            canvas.width = COLS * TILE;
            canvas.height = ROWS * TILE;
        }
        resize();
        window.addEventListener('resize', resize);

        // ==================== AUDIO ====================
        let audioCtx;
        function initAudio() {
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        function beep(f, d, t) {
            if (!audioCtx) return;
            try {
                const o = audioCtx.createOscillator();
                const g = audioCtx.createGain();
                o.type = t || 'square';
                o.frequency.setValueAtTime(f, audioCtx.currentTime);
                g.gain.setValueAtTime(0.05, audioCtx.currentTime);
                g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + d);
                o.connect(g); g.connect(audioCtx.destination);
                o.start(); o.stop(audioCtx.currentTime + d);
            } catch(e) {}
        }

        // ==================== INPUT ====================
        const keys = { left: false, right: false, up: false, down: false, space: false };

        document.addEventListener('keydown', e => {
            if (e.key === 'ArrowLeft' || e.key === 'a') keys.left = true;
            if (e.key === 'ArrowRight' || e.key === 'd') keys.right = true;
            if (e.key === 'ArrowUp' || e.key === 'w') { keys.up = true; e.preventDefault(); }
            if (e.key === 'ArrowDown' || e.key === 's') keys.down = true;
            if (e.key === ' ') { keys.space = true; e.preventDefault(); }
        });

        document.addEventListener('keyup', e => {
            if (e.key === 'ArrowLeft' || e.key === 'a') keys.left = false;
            if (e.key === 'ArrowRight' || e.key === 'd') keys.right = false;
            if (e.key === 'ArrowUp' || e.key === 'w') keys.up = false;
            if (e.key === 'ArrowDown' || e.key === 's') keys.down = false;
            if (e.key === ' ') keys.space = false;
        });

        // ==================== LEVELS ====================
        const levels = [
            { // World 1-1: Green World
                name: '1-1', color: '#2d5a1e', sky: '#87CEEB', ground: '#4a8c2a',
                map: [
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '          ?   ?                         ',
                    '                                        ',
                    '              ===                       ',
                    '    ?   ?                               ',
                    '  =====                                  ',
                    '                     ?                   ',
                    '         =========           ====        ',
                    '                            ====        ',
                    '========================================',
                ],
                coins: [[6,9],[10,9],[14,12],[20,8],[30,13]],
                enemies: [[12,16],[18,16],[25,16],[32,16]],
                flag: { x: 36, y: 8 }
            },
            { // World 1-2: Mountain
                name: '1-2', color: '#4a3728', sky: '#4a6fa5', ground: '#6b5b4f',
                map: [
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '              ===                       ',
                    '                                        ',
                    '       ===                              ',
                    '                    ===                 ',
                    '    ?                                  ',
                    '  ===              ?                   ',
                    '                          ===          ',
                    '        ?                               ',
                    '      ===     ?        ===             ',
                    '              ===           ===        ',
                    '                            ===        ',
                    '========================================',
                ],
                coins: [[8,12],[15,10],[22,13],[28,11],[35,13]],
                enemies: [[10,16],[20,16],[30,16],[34,16]],
                flag: { x: 37, y: 7 }
            },
            { // World 1-3: Space
                name: '1-3', color: '#0a0a2e', sky: '#000033', ground: '#1a1a4e',
                map: [
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '         ===                            ',
                    '                                        ',
                    '               ===                     ',
                    '                                        ',
                    '    ===                                 ',
                    '                      ===              ',
                    '                                        ',
                    '          ===                           ',
                    '                              ===       ',
                    '    ?          ?          ?             ',
                    '  ===   =========   =========   ===     ',
                    '  ===   =========   =========   ===     ',
                    '========================================',
                ],
                coins: [[5,14],[12,14],[19,14],[26,14],[33,14]],
                enemies: [[8,16],[16,16],[24,16],[32,16],[36,16]],
                flag: { x: 37, y: 5 }
            },
            { // World 1-4: Volcano
                name: '1-4', color: '#2a0a0a', sky: '#1a0000', ground: '#4a1a1a',
                map: [
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '       ===     ===     ===              ',
                    '                                        ',
                    '             ===     ===                ',
                    '                                        ',
                    '    ===     ===     ===     ===         ',
                    '                                        ',
                    '                                        ',
                    '       ===     ===     ===              ',
                    '                                        ',
                    '    ?     ?     ?     ?     ?           ',
                    '  === ===== ===== ===== ===== ===       ',
                    '  === ===== ===== ===== ===== ===       ',
                    '========================================',
                ],
                coins: [[6,14],[12,14],[18,14],[24,14],[30,14]],
                enemies: [[4,16],[10,16],[16,16],[22,16],[28,16],[34,16]],
                flag: { x: 37, y: 3 }
            },
            { // World 1-5: Castle Boss
                name: '1-5', color: '#1a1a1a', sky: '#000', ground: '#333',
                map: [
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '    ===                                 ',
                    '                                        ',
                    '              ===                      ',
                    '                                        ',
                    '                      ===              ',
                    '                                        ',
                    '    ===     ===     ===     ===         ',
                    '                                        ',
                    '                                        ',
                    '                                        ',
                    '    ?     ?     ?     ?     ?           ',
                    '  =========     ===     =========       ',
                    '  =========     ===     =========       ',
                    '========================================',
                ],
                coins: [[5,14],[10,14],[20,14],[25,14],[35,14]],
                enemies: [],
                boss: { x: 30, y: 8, hp: 3 },
                flag: { x: 37, y: 4 }
            }
        ];

        // ==================== STATE ====================
        let currentLevel = 0;
        let player, coins, enemies, boss, flag;
        let score = 0, coinCount = 0, lives = 3;
        let gameState = 'idle';
        let gravity = 0.5;
        let particles = [];
        let cameraX = 0;

        function initLevel(lvl) {
            const level = levels[lvl];
            player = {
                x: 2 * TILE, y: (ROWS - 3) * TILE,
                w: TILE * 0.7, h: TILE * 0.9,
                vx: 0, vy: 0,
                onGround: false,
                facing: 1,
                animFrame: 0
            };
            coins = level.coins.map(c => ({ x: c[0] * TILE + TILE/2, y: c[1] * TILE + TILE/2, collected: false }));
            enemies = level.enemies.map(e => ({ x: e[0] * TILE, y: e[1] * TILE, vx: -2, alive: true }));
            boss = level.boss ? { x: level.boss.x * TILE, y: level.boss.y * TILE, hp: level.boss.hp, vx: -1.5, dir: -1, timer: 0 } : null;
            flag = level.flag ? { x: level.flag.x * TILE, y: level.flag.y * TILE, reached: false } : null;
            particles = [];
            cameraX = 0;
        }

        function getTile(x, y) {
            const col = Math.floor(x / TILE);
            const row = Math.floor(y / TILE);
            if (col < 0 || col >= COLS || row < 0 || row >= ROWS) return '=';
            const level = levels[currentLevel];
            const char = level.map[row] ? level.map[row][col] : ' ';
            return char === '=' ? '=' : char === '?' ? '?' : ' ';
        }

        function isSolid(x, y) {
            return getTile(x, y) === '=';
        }

        // ==================== GAME LOGIC ====================
        function update() {
            // Player movement
            if (keys.left) { player.vx = -3.5; player.facing = -1; }
            else if (keys.right) { player.vx = 3.5; player.facing = 1; }
            else { player.vx *= 0.7; }

            if ((keys.space || keys.up) && player.onGround) {
                player.vy = -9;
                player.onGround = false;
                beep(300, 0.1);
            }

            player.vy += gravity;
            player.x += player.vx;
            player.y += player.vy;

            // Collision
            player.onGround = false;
            const checkPoints = [
                [player.x, player.y + player.h],
                [player.x + player.w, player.y + player.h],
                [player.x, player.y],
                [player.x + player.w, player.y],
                [player.x + player.w/2, player.y + player.h]
            ];

            for (const [cx, cy] of checkPoints) {
                if (isSolid(cx, cy)) {
                    if (player.vy > 0) {
                        player.y = Math.floor(cy / TILE) * TILE - player.h;
                        player.vy = 0;
                        player.onGround = true;
                    } else if (player.vy < 0) {
                        player.y = Math.floor(cy / TILE) * TILE + TILE;
                        player.vy = 0;
                    }
                }
            }

            // Bounds
            if (player.x < 0) player.x = 0;
            if (player.y > ROWS * TILE) { die(); return; }

            // Camera
            cameraX = player.x - canvas.width / 3;
            if (cameraX < 0) cameraX = 0;

            // Coins
            coins.forEach(c => {
                if (!c.collected) {
                    const dx = player.x + player.w/2 - c.x;
                    const dy = player.y + player.h/2 - c.y;
                    if (Math.sqrt(dx*dx + dy*dy) < TILE * 0.5) {
                        c.collected = true;
                        coinCount++;
                        score += 100;
                        beep(600, 0.08, 'triangle');
                        addParticles(c.x, c.y, '#ffaa00');
                    }
                }
            });

            // Enemies
            enemies.forEach(e => {
                if (!e.alive) return;
                e.x += e.vx;
                const ex = e.x, ey = e.y, ew = TILE * 0.7, eh = TILE * 0.7;
                if (!isSolid(e.x + (e.vx > 0 ? ew : -1), ey + eh - 1)) {
                    e.vx = -e.vx;
                }

                // Player stomp
                const px = player.x, py = player.y, pw = player.w, ph = player.h;
                if (px < ex + ew && px + pw > ex && py < ey + eh && py + ph > ey) {
                    if (player.vy > 0 && py + ph - ey < TILE * 0.5) {
                        e.alive = false;
                        player.vy = -6;
                        score += 200;
                        beep(500, 0.12, 'sawtooth');
                        addParticles(ex + ew/2, ey + eh/2, '#ff4444');
                    } else {
                        die();
                    }
                }
            });

            // Boss
            if (boss && boss.hp > 0) {
                boss.timer++;
                boss.x += boss.vx;
                if (!isSolid(boss.x + (boss.vx > 0 ? TILE*2 : -1), boss.y + TILE*2 - 1)) {
                    boss.vx = -boss.vx;
                    boss.dir = -boss.dir;
                }

                const bx = boss.x, by = boss.y, bw = TILE * 2, bh = TILE * 2;
                const px = player.x, py = player.y, pw = player.w, ph = player.h;
                if (px < bx + bw && px + pw > bx && py < by + bh && py + ph > by) {
                    if (player.vy > 0 && py + ph - by < TILE * 0.7) {
                        boss.hp--;
                        player.vy = -7;
                        score += 500;
                        beep(700, 0.15, 'triangle');
                        addParticles(bx + bw/2, by + bh/2, '#ff8800');
                        if (boss.hp <= 0) {
                            addParticles(bx + bw/2, by + bh/2, '#ffaa00');
                            addParticles(bx + bw/2, by + bh/2, '#ff4444');
                        }
                    } else {
                        die();
                    }
                }
            }

            // Flag
            if (flag && !flag.reached) {
                const dx = player.x + player.w/2 - flag.x;
                const dy = player.y + player.h/2 - flag.y;
                if (Math.abs(dx) < TILE && dy < TILE * 4) {
                    flag.reached = true;
                    beep(800, 0.2);
                    beep(1000, 0.2);
                    beep(1200, 0.3);
                    levelComplete();
                }
            }

            // Particles
            particles = particles.filter(p => { p.life -= 0.03; return p.life > 0; });
        }

        function die() {
            lives--;
            updateHUD();
            beep(200, 0.3, 'sawtooth');
            if (lives <= 0) {
                gameState = 'gameover';
                document.getElementById('finalScore').textContent = 'Score: ' + score;
                document.getElementById('gameOverOverlay').classList.remove('hidden');
            } else {
                initLevel(currentLevel);
            }
        }

        function levelComplete() {
            gameState = 'leveldone';
            if (currentLevel < levels.length - 1) {
                document.getElementById('levelScore').textContent = 'Score: ' + score;
                document.getElementById('nextWorld').textContent = 'Next: World ' + levels[currentLevel + 1].name;
                document.getElementById('levelOverlay').classList.remove('hidden');
            } else {
                document.getElementById('winScore').textContent = 'Final Score: ' + score;
                document.getElementById('winOverlay').classList.remove('hidden');
            }
        }

        function nextLevel() {
            currentLevel++;
            initLevel(currentLevel);
            gameState = 'playing';
            document.getElementById('levelOverlay').classList.add('hidden');
            updateHUD();
            update();
            draw();
        }

        function startGame() {
            initAudio();
            currentLevel = 0;
            score = 0;
            coinCount = 0;
            lives = 3;
            initLevel(0);
            gameState = 'playing';
            document.getElementById('startOverlay').classList.add('hidden');
            document.getElementById('gameOverOverlay').classList.add('hidden');
            document.getElementById('levelOverlay').classList.add('hidden');
            document.getElementById('winOverlay').classList.add('hidden');
            updateHUD();
            update();
            draw();
            beep(500, 0.1);
        }

        function restartGame() {
            gameState = 'idle';
            document.getElementById('startOverlay').classList.remove('hidden');
            document.getElementById('gameOverOverlay').classList.add('hidden');
            document.getElementById('winOverlay').classList.add('hidden');
            document.getElementById('levelOverlay').classList.add('hidden');
            score = 0; coinCount = 0; lives = 3;
            updateHUD();
        }

        function addParticles(x, y, color) {
            for (let i = 0; i < 8; i++) {
                particles.push({
                    x, y,
                    vx: (Math.random() - 0.5) * 6,
                    vy: (Math.random() - 0.5) * 6 - 2,
                    life: 1,
                    color
                });
            }
        }

        function updateHUD() {
            document.getElementById('score').textContent = score;
            document.getElementById('coins').textContent = coinCount;
            document.getElementById('worldDisplay').textContent = 'W-' + levels[currentLevel].name;
            document.getElementById('lives').textContent = '❤️'.repeat(Math.max(0, lives));
        }

        // ==================== DRAWING ====================
        function draw() {
            const level = levels[currentLevel];
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Sky
            ctx.fillStyle = level.sky;
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Stars in space level
            if (currentLevel === 2) {
                ctx.fillStyle = '#fff';
                for (let i = 0; i < 30; i++) {
                    const sx = (i * 137 + 50) % canvas.width;
                    const sy = (i * 73 + 20) % (canvas.height * 0.6);
                    ctx.fillRect(sx, sy, 2, 2);
                }
            }

            ctx.save();
            ctx.translate(-cameraX, 0);

            // Map
            for (let row = 0; row < ROWS; row++) {
                for (let col = 0; col < COLS; col++) {
                    const char = level.map[row] ? level.map[row][col] : ' ';
                    const x = col * TILE, y = row * TILE;

                    if (char === '=') {
                        // Ground block
                        const grad = ctx.createLinearGradient(x, y, x, y + TILE);
                        grad.addColorStop(0, level.ground);
                        grad.addColorStop(1, level.color);
                        ctx.fillStyle = grad;
                        ctx.fillRect(x, y, TILE, TILE);
                        ctx.strokeStyle = 'rgba(0,0,0,0.3)';
                        ctx.strokeRect(x, y, TILE, TILE);
                        ctx.fillStyle = 'rgba(255,255,255,0.1)';
                        ctx.fillRect(x, y, TILE, 2);
                    } else if (char === '?') {
                        // Question block
                        ctx.fillStyle = '#ffaa00';
                        ctx.fillRect(x, y, TILE, TILE);
                        ctx.strokeStyle = '#000';
                        ctx.lineWidth = 2;
                        ctx.strokeRect(x, y, TILE, TILE);
                        ctx.fillStyle = '#fff';
                        ctx.font = `${TILE*0.6}px Arial`;
                        ctx.textAlign = 'center';
                        ctx.fillText('?', x + TILE/2, y + TILE*0.7);
                    }
                }
            }

            // Coins
            coins.forEach(c => {
                if (!c.collected) {
                    ctx.fillStyle = '#ffaa00';
                    ctx.shadowColor = 'rgba(255,170,0,0.6)';
                    ctx.shadowBlur = 6;
                    ctx.beginPath();
                    ctx.arc(c.x, c.y, TILE * 0.2, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            });

            // Enemies
            enemies.forEach(e => {
                if (!e.alive) return;
                ctx.fillStyle = '#cc4400';
                ctx.beginPath();
                ctx.arc(e.x + TILE*0.35, e.y + TILE*0.35, TILE * 0.35, 0, Math.PI * 2);
                ctx.fill();
                ctx.fillStyle = '#000';
                ctx.beginPath();
                ctx.arc(e.x + TILE*0.25, e.y + TILE*0.25, 3, 0, Math.PI * 2);
                ctx.fill();
                ctx.beginPath();
                ctx.arc(e.x + TILE*0.45, e.y + TILE*0.25, 3, 0, Math.PI * 2);
                ctx.fill();
            });

            // Boss
            if (boss && boss.hp > 0) {
                const bx = boss.x, by = boss.y;
                ctx.fillStyle = '#8b0000';
                ctx.fillRect(bx, by, TILE * 2, TILE * 2);
                ctx.fillStyle = '#ff0000';
                ctx.beginPath();
                ctx.arc(bx + TILE, by + TILE * 0.7, TILE * 0.6, 0, Math.PI * 2);
                ctx.fill();
                ctx.fillStyle = '#fff';
                ctx.font = `${TILE}px Arial`;
                ctx.textAlign = 'center';
                ctx.fillText('👿', bx + TILE, by + TILE * 1.2);
                ctx.fillStyle = '#ff4444';
                ctx.fillRect(bx + 5, by - 10, TILE * 2 - 10, 8);
                ctx.fillStyle = '#0f0';
                ctx.fillRect(bx + 5, by - 10, (TILE * 2 - 10) * (boss.hp / 3), 8);
            }

            // Flag
            if (flag && !flag.reached) {
                ctx.fillStyle = '#fff';
                ctx.fillRect(flag.x - 2, flag.y, 4, TILE * 5);
                ctx.fillStyle = '#ff4444';
                ctx.beginPath();
                ctx.moveTo(flag.x, flag.y);
                ctx.lineTo(flag.x + TILE, flag.y + TILE * 0.5);
                ctx.lineTo(flag.x, flag.y + TILE);
                ctx.fill();
            }

            // Player
            const px = player.x, py = player.y, pw = player.w, ph = player.h;
            ctx.fillStyle = '#ff2222';
            ctx.fillRect(px, py, pw, ph);
            ctx.fillStyle = '#ffaa88';
            ctx.fillRect(px + pw*0.25, py + 2, pw*0.5, ph*0.4);
            ctx.fillStyle = '#000';
            ctx.fillRect(px + (player.facing > 0 ? pw*0.6 : pw*0.2), py + ph*0.15, 4, 4);
            ctx.fillStyle = '#0066cc';
            ctx.fillRect(px + pw*0.1, py + ph*0.55, pw*0.8, ph*0.35);
            ctx.fillStyle = '#8B4513';
            ctx.fillRect(px + pw*0.1, py + ph*0.9, pw*0.8, ph*0.1);

            // Particles
            particles.forEach(p => {
                ctx.fillStyle = p.color.replace(')', `,${p.life})`).replace('rgb', 'rgba');
                ctx.beginPath();
                ctx.arc(p.x - cameraX, p.y, 3, 0, Math.PI * 2);
                ctx.fill();
            });

            ctx.restore();

            updateHUD();
        }

        // ==================== GAME LOOP ====================
        function gameLoop() {
            if (gameState === 'playing') {
                update();
                draw();
            }
            requestAnimationFrame(gameLoop);
        }

        // ==================== INIT ====================
        initLevel(0);
        draw();
        gameLoop();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  👑 Mario X - Legendary Platform       ║")
    print("║  🍄 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🎮 المميزات الأسطورية:")
    print("  🌿 المرحلة 1: العالم الأخضر (سهل)")
    print("  🏔️ المرحلة 2: الجبال (متوسط)")
    print("  🌌 المرحلة 3: الفضاء (صعب)")
    print("  🌋 المرحلة 4: البركان (صعب جداً)")
    print("  🏰 المرحلة 5: قلعة الزعيم (BOSS)")
    print("  👿 زعيم بآخر مرحلة مع شريط حياة")
    print("  🪙 عملات ذهبية")
    print("  👾 أعداء متحركة")
    print("  🚩 علم النهاية")
    print("  🎵 مؤثرات صوتية")
    print("  💀 نظام حياة (3 قلوب)")
    print("  🏆 شاشة فوز نهائية")
    print("  🎮 أزرار تحكم كاملة")
    print("  ⌨️ دعم الكيبورد")

if __name__ == "__main__":
    create_website_files()

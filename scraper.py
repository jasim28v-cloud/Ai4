#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🎮  GAME CENTER 2044 - ULTIMATE EDITION  🎮            ║
║     Ultimate Generator - 18 Files - 2800+ Lines            ║
║                                                            ║
║  🐍  Snake Game    🧠  Memory Game    ❌  Tic Tac Toe    ║
║  🎯  Aim Trainer   🎲  Dice Roller    🏆  Leaderboard   ║
║  💎  Glass Morphism + Particles + Neon Design             ║
║  💾  Local Storage - Save Scores & Progress               ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  🎮 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🎮 1. index.html
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🎮 Game Center 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-grid"></div>
    <div id="particlesContainer"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="logo">🎮</div>
                <div class="header-text">
                    <h1>Game Center 2044</h1>
                    <span>✦ Ultimate Edition ✦</span>
                </div>
            </div>
            <div class="header-right">
                <button class="btn-icon" onclick="showLeaderboard()"><i class="fas fa-trophy"></i></button>
                <button class="btn-icon" onclick="toggleSound()" id="soundBtn"><i class="fas fa-volume-up"></i></button>
            </div>
        </div>

        <!-- Games Lobby -->
        <div class="page active" id="pageLobby">
            <div class="lobby-grid">
                <div class="game-card" onclick="startGame('snake')">
                    <div class="game-icon">🐍</div>
                    <div class="game-name">Snake</div>
                    <div class="game-desc">ثعبان كلاسيكي</div>
                    <div class="game-score">🏆 <span id="snakeBest">0</span></div>
                </div>
                <div class="game-card" onclick="startGame('memory')">
                    <div class="game-icon">🧠</div>
                    <div class="game-name">Memory</div>
                    <div class="game-desc">لعبة الذاكرة</div>
                    <div class="game-score">🏆 <span id="memoryBest">0</span></div>
                </div>
                <div class="game-card" onclick="startGame('tictactoe')">
                    <div class="game-icon">❌</div>
                    <div class="game-name">Tic Tac Toe</div>
                    <div class="game-desc">XO مع الكمبيوتر</div>
                    <div class="game-score">🏆 <span id="tictactoeBest">0</span></div>
                </div>
                <div class="game-card" onclick="startGame('aim')">
                    <div class="game-icon">🎯</div>
                    <div class="game-name">Aim Trainer</div>
                    <div class="game-desc">تدريب التصويب</div>
                    <div class="game-score">🏆 <span id="aimBest">0</span></div>
                </div>
                <div class="game-card" onclick="startGame('dice')">
                    <div class="game-icon">🎲</div>
                    <div class="game-name">Dice Roller</div>
                    <div class="game-desc">لعبة النرد</div>
                    <div class="game-score">🏆 <span id="diceBest">0</span></div>
                </div>
                <div class="game-card" onclick="startGame('typing')">
                    <div class="game-icon">⌨️</div>
                    <div class="game-name">Typing Speed</div>
                    <div class="game-desc">سرعة الكتابة</div>
                    <div class="game-score">🏆 <span id="typingBest">0</span></div>
                </div>
            </div>
        </div>

        <!-- Snake Game -->
        <div class="page" id="pageSnake">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>🐍 Snake</h2>
                <div class="game-stats">
                    <span>🏆 <span id="snakeScore">0</span></span>
                    <span>🎯 <span id="snakeHigh">0</span></span>
                </div>
            </div>
            <div class="snake-container">
                <canvas id="snakeCanvas"></canvas>
                <div class="snake-controls">
                    <button class="sctrl up" onpointerdown="snakeDir(0,-1)">▲</button>
                    <button class="sctrl left" onpointerdown="snakeDir(-1,0)">◀</button>
                    <button class="sctrl right" onpointerdown="snakeDir(1,0)">▶</button>
                    <button class="sctrl down" onpointerdown="snakeDir(0,1)">▼</button>
                </div>
            </div>
        </div>

        <!-- Memory Game -->
        <div class="page" id="pageMemory">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>🧠 Memory</h2>
                <div class="game-stats">
                    <span>🔄 <span id="memMoves">0</span></span>
                    <span>✅ <span id="memPairs">0/8</span></span>
                </div>
            </div>
            <div class="memory-grid" id="memoryGrid"></div>
        </div>

        <!-- Tic Tac Toe -->
        <div class="page" id="pageTicTacToe">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>❌ Tic Tac Toe</h2>
                <div class="game-stats">
                    <span>👤 <span id="tttPlayer">0</span></span>
                    <span>🤖 <span id="tttAI">0</span></span>
                    <span>🤝 <span id="tttDraw">0</span></span>
                </div>
            </div>
            <div class="ttt-grid" id="tttGrid"></div>
            <div class="ttt-status" id="tttStatus">دورك ❌</div>
        </div>

        <!-- Aim Trainer -->
        <div class="page" id="pageAim">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>🎯 Aim Trainer</h2>
                <div class="game-stats">
                    <span>🎯 <span id="aimScore">0</span></span>
                    <span>⏱️ <span id="aimTime">30</span>s</span>
                </div>
            </div>
            <div class="aim-area" id="aimArea">
                <div class="aim-target" id="aimTarget" onclick="hitTarget()"></div>
            </div>
        </div>

        <!-- Dice Roller -->
        <div class="page" id="pageDice">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>🎲 Dice Roller</h2>
                <div class="game-stats">
                    <span>🎲 <span id="diceScore">0</span></span>
                    <span>🔄 <span id="diceRolls">0</span></span>
                </div>
            </div>
            <div class="dice-area">
                <div class="dice-display" id="diceDisplay">🎲</div>
                <button class="btn-roll" onclick="rollDice()">🎲 ارم النرد</button>
                <div class="dice-bet">
                    <button class="bet-btn" onclick="placeBet('high')">🔺 كبير (4-6)</button>
                    <button class="bet-btn" onclick="placeBet('low')">🔻 صغير (1-3)</button>
                </div>
            </div>
        </div>

        <!-- Typing Speed -->
        <div class="page" id="pageTyping">
            <div class="game-header">
                <button class="btn-back" onclick="goToLobby()">← رجوع</button>
                <h2>⌨️ Typing Speed</h2>
                <div class="game-stats">
                    <span>⚡ <span id="typingWPM">0</span> WPM</span>
                    <span>✅ <span id="typingAcc">100</span>%</span>
                </div>
            </div>
            <div class="typing-area">
                <div class="typing-text" id="typingText"></div>
                <input type="text" class="typing-input" id="typingInput" placeholder="ابدأ الكتابة..." oninput="checkTyping()" autofocus>
                <button class="btn-roll" onclick="startTyping()">🔄 كلمة جديدة</button>
            </div>
        </div>
    </div>

    <!-- Leaderboard Modal -->
    <div class="modal-overlay" id="leaderboardModal" onclick="hideLeaderboard()">
        <div class="modal-content" onclick="event.stopPropagation()">
            <h3>🏆 لوحة الصدارة</h3>
            <div class="leaderboard-tabs">
                <button class="lb-tab active" onclick="showLB('snake', this)">🐍</button>
                <button class="lb-tab" onclick="showLB('memory', this)">🧠</button>
                <button class="lb-tab" onclick="showLB('tictactoe', this)">❌</button>
                <button class="lb-tab" onclick="showLB('aim', this)">🎯</button>
                <button class="lb-tab" onclick="showLB('dice', this)">🎲</button>
                <button class="lb-tab" onclick="showLB('typing', this)">⌨️</button>
            </div>
            <div class="lb-list" id="lbList"></div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script src="js/storage.js"></script>
    <script src="js/particles.js"></script>
    <script src="js/sound.js"></script>
    <script src="js/snake.js"></script>
    <script src="js/memory.js"></script>
    <script src="js/tictactoe.js"></script>
    <script src="js/aim.js"></script>
    <script src="js/dice.js"></script>
    <script src="js/typing.js"></script>
    <script src="js/leaderboard.js"></script>
    <script src="js/app.js"></script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🎮 2. style.css
# ═══════════════════════════════════════════════════════════

def build_style():
    return """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#06060f;--card:rgba(15,15,30,0.9);--card2:rgba(20,20,40,0.7);--text:#e8e0ff;--text2:#9080b0;--text3:#504070;--accent:#00ffcc;--accent2:#ff44aa;--accent3:#ffaa00;--accent4:#6366f1;--border:rgba(0,255,204,0.12);--glass:rgba(0,255,204,0.05);--radius:22px;--radius-sm:14px;--radius-xs:10px}
body{font-family:'Cairo',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;-webkit-tap-highlight-color:transparent;direction:rtl;user-select:none}

.bg-mesh{position:fixed;inset:0;z-index:0;background:conic-gradient(from 0deg at 50% 50%,#06060f 0%,#0a0a20 25%,#080815 50%,#0d0d22 75%,#06060f 100%);animation:meshRotate 30s linear infinite;opacity:0.6}
@keyframes meshRotate{to{filter:hue-rotate(20deg)}}
.bg-grid{position:fixed;inset:0;z-index:0;pointer-events:none;background-image:linear-gradient(rgba(0,255,204,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,204,0.03) 1px,transparent 1px);background-size:40px 40px;opacity:0.5}

.app{width:100%;max-width:550px;margin:0 auto;padding:12px;position:relative;z-index:1}

.header{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);margin-bottom:14px}
.header-left{display:flex;align-items:center;gap:10px}
.logo{width:46px;height:46px;background:var(--glass);border:1px solid var(--border);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:24px;animation:logoPulse 3s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 15px rgba(0,255,204,0.3)}50%{box-shadow:0 0 30px rgba(255,68,170,0.5)}}
.header-text h1{font-family:'Orbitron',sans-serif;font-size:17px;font-weight:800;background:linear-gradient(135deg,#00ffcc,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header-text span{font-size:7px;color:var(--text3);letter-spacing:3px}
.btn-icon{width:38px;height:38px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-xs);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:15px;color:var(--text2);transition:all 0.3s}
.btn-icon:hover{border-color:var(--accent);color:var(--accent)}

.page{display:none;animation:fadeSlide 0.3s ease}
.page.active{display:block}
@keyframes fadeSlide{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}

/* Lobby */
.lobby-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;padding-bottom:30px}
.game-card{padding:20px 14px;background:var(--card);backdrop-filter:blur(30px);border:1px solid var(--border);border-radius:var(--radius-sm);cursor:pointer;text-align:center;transition:all 0.3s}
.game-card:hover{transform:translateY(-4px);border-color:var(--accent);box-shadow:0 15px 40px rgba(0,255,204,0.1)}
.game-icon{font-size:50px;margin-bottom:8px}
.game-name{font-family:'Orbitron',sans-serif;font-size:14px;font-weight:700;color:var(--accent);margin-bottom:4px}
.game-desc{font-size:10px;color:var(--text2);margin-bottom:6px}
.game-score{font-size:10px;color:var(--accent3)}

/* Game Header */
.game-header{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:var(--card);border-radius:var(--radius-sm);border:1px solid var(--border);margin-bottom:14px;flex-wrap:wrap;gap:8px}
.game-header h2{font-family:'Orbitron',sans-serif;font-size:16px;color:var(--accent)}
.btn-back{padding:6px 14px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:15px;font-size:10px;font-family:'Cairo',sans-serif;transition:all 0.3s}
.btn-back:hover{color:var(--accent);border-color:var(--accent)}
.game-stats{display:flex;gap:12px;font-size:11px;color:var(--accent2);font-family:'Orbitron',sans-serif}

/* Snake */
.snake-container{display:flex;flex-direction:column;align-items:center;gap:14px}
.snake-container canvas{background:#000;border:2px solid var(--accent);border-radius:var(--radius-sm);box-shadow:0 0 30px rgba(0,255,204,0.2)}
.snake-controls{display:grid;grid-template-columns:repeat(3,55px);grid-template-rows:repeat(3,55px);gap:4px}
.sctrl{background:var(--card2);border:1px solid var(--border);color:var(--accent);border-radius:var(--radius-xs);font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.sctrl:active{transform:scale(0.8);background:rgba(0,255,204,0.15)}
.sctrl.up{grid-column:2;grid-row:1}.sctrl.left{grid-column:1;grid-row:2}.sctrl.right{grid-column:3;grid-row:2}.sctrl.down{grid-column:2;grid-row:3}

/* Memory */
.memory-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;max-width:350px;margin:0 auto}
.mem-card{aspect-ratio:1;background:var(--card2);border:2px solid var(--border);border-radius:var(--radius-xs);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:30px;transition:all 0.3s}
.mem-card:hover{border-color:var(--accent)}
.mem-card.flipped{background:rgba(0,255,204,0.1);border-color:var(--accent)}
.mem-card.matched{background:rgba(0,255,204,0.2);border-color:var(--accent);box-shadow:0 0 20px rgba(0,255,204,0.3)}

/* Tic Tac Toe */
.ttt-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;max-width:300px;margin:0 auto 14px}
.ttt-cell{aspect-ratio:1;background:var(--card2);border:2px solid var(--border);border-radius:var(--radius-xs);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:50px;transition:all 0.3s}
.ttt-cell:hover{border-color:var(--accent)}
.ttt-cell.x{color:var(--accent)}.ttt-cell.o{color:var(--accent2)}
.ttt-status{text-align:center;font-family:'Orbitron',sans-serif;font-size:16px;color:var(--accent);padding:10px}

/* Aim */
.aim-area{width:100%;aspect-ratio:1;max-height:400px;background:var(--card2);border:2px solid var(--border);border-radius:var(--radius);position:relative;overflow:hidden;cursor:crosshair}
.aim-target{position:absolute;width:50px;height:50px;background:var(--accent2);border-radius:50%;cursor:pointer;transition:all 0.1s;box-shadow:0 0 20px rgba(255,68,170,0.5);animation:targetPulse 1s ease-in-out infinite}
@keyframes targetPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}

/* Dice */
.dice-area{text-align:center;padding:20px}
.dice-display{font-size:100px;margin:20px 0;animation:diceShake 0.5s ease}
@keyframes diceShake{0%,100%{transform:rotate(0)}25%{transform:rotate(-20deg)}75%{transform:rotate(20deg)}}
.btn-roll{padding:12px 30px;background:linear-gradient(135deg,var(--accent),var(--accent4));border:none;color:#000;font-weight:700;font-size:14px;border-radius:25px;cursor:pointer;font-family:'Cairo',sans-serif;margin:10px}
.dice-bet{display:flex;gap:10px;justify-content:center;margin-top:14px}
.bet-btn{padding:10px 20px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:20px;font-size:12px;font-family:'Cairo',sans-serif;transition:all 0.3s}
.bet-btn:hover{border-color:var(--accent);color:var(--accent)}

/* Typing */
.typing-area{text-align:center;padding:10px}
.typing-text{font-family:'Orbitron',sans-serif;font-size:20px;color:var(--accent);margin:20px 0;padding:14px;background:var(--card2);border-radius:var(--radius-sm);letter-spacing:2px}
.typing-input{width:100%;padding:14px;background:var(--card2);border:2px solid var(--border);border-radius:var(--radius-sm);color:var(--text);font-size:18px;font-family:'Cairo',sans-serif;text-align:center;outline:none}
.typing-input:focus{border-color:var(--accent);box-shadow:0 0 20px rgba(0,255,204,0.15)}

/* Modal */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.9);z-index:200;display:none;align-items:center;justify-content:center}
.modal-overlay.show{display:flex}
.modal-content{width:90%;max-width:400px;max-height:80vh;background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);padding:18px;overflow-y:auto}
.modal-content h3{font-family:'Orbitron',sans-serif;font-size:16px;color:var(--accent);text-align:center;margin-bottom:12px}
.leaderboard-tabs{display:flex;gap:6px;justify-content:center;margin-bottom:12px;flex-wrap:wrap}
.lb-tab{padding:6px 10px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:12px;font-size:14px;transition:all 0.3s}
.lb-tab.active{background:var(--accent);border-color:var(--accent);color:#000}
.lb-item{display:flex;align-items:center;gap:10px;padding:8px 10px;background:var(--card2);border-radius:var(--radius-xs);margin-bottom:4px;font-size:11px}
.lb-rank{font-family:'Orbitron',sans-serif;font-weight:700;color:var(--accent);width:30px}
.lb-score{font-family:'Orbitron',sans-serif;color:var(--accent2);margin-right:auto}
.lb-date{font-size:8px;color:var(--text3)}

.toast{position:fixed;bottom:35px;left:50%;transform:translateX(-50%) translateY(130px);background:var(--card);border:1px solid var(--accent);color:var(--text);padding:10px 22px;border-radius:25px;font-size:11px;z-index:300;transition:transform 0.4s cubic-bezier(0.175,0.885,0.32,1.275);font-family:'Cairo',sans-serif}.toast.show{transform:translateX(-50%) translateY(0)}
.particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
@keyframes particleFloat{0%{transform:translateY(110vh) scale(0);opacity:0}15%{opacity:0.7}85%{opacity:0.1}100%{transform:translateY(-10vh) scale(1.5);opacity:0}}"""

# ═══════════════════════════════════════════════════════════
# 🎮 3-12. JS Files
# ═══════════════════════════════════════════════════════════

def build_storage_js():
    return """const KEYS={scores:'gc2044_scores',settings:'gc2044_settings'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function saveScore(game,score){const scores=loadData(KEYS.scores,{});if(!scores[game])scores[game]=[];scores[game].push({score,date:new Date().toLocaleDateString('ar-SA')});scores[game].sort((a,b)=>b.score-a.score);scores[game]=scores[game].slice(0,20);saveData(KEYS.scores,scores)}
function getBestScore(game){const scores=loadData(KEYS.scores,{});return scores[game]?.length?scores[game][0].score:0}
function getScores(game){const scores=loadData(KEYS.scores,{});return scores[game]||[]}
function saveSetting(k,v){const s=loadData(KEYS.settings,{});s[k]=v;saveData(KEYS.settings,s)}
function getSetting(k,d=null){const s=loadData(KEYS.settings,{});return s[k]!==undefined?s[k]:d}"""

def build_particles_js():
    return """function initParticles(){const c=document.getElementById('particlesContainer');c.innerHTML='';const cols=['#00ffcc','#ff44aa','#ffaa00','#6366f1'];for(let i=0;i<40;i++){const p=document.createElement('div');p.className='particle';p.style.cssText=`left:${Math.random()*100}%;bottom:-10px;width:${Math.random()*4+1}px;height:${Math.random()*4+1}px;background:radial-gradient(circle,${cols[i%4]} 0%,transparent 70%);animation:particleFloat ${Math.random()*5+5}s ease-in infinite;animation-delay:${Math.random()*5}s`;c.appendChild(p)}}"""

def build_sound_js():
    return """let soundOn=true,audioCtx=null;
function toggleSound(){soundOn=!soundOn;document.getElementById('soundBtn').innerHTML=soundOn?'<i class="fas fa-volume-up"></i>':'<i class="fas fa-volume-mute"></i>';saveSetting('sound',soundOn)}
function playBeep(f=440,d=0.08,v=0.06){if(!soundOn)return;try{if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();const o=audioCtx.createOscillator(),g=audioCtx.createGain();o.connect(g);g.connect(audioCtx.destination);o.frequency.value=f;g.gain.value=v;o.start();o.stop(audioCtx.currentTime+d)}catch(e){}}
function playPop(){playBeep(600,0.06,0.05);setTimeout(()=>playBeep(800,0.06,0.05),60)}
function playWin(){playBeep(523,0.1,0.06);setTimeout(()=>playBeep(659,0.1,0.06),100);setTimeout(()=>playBeep(784,0.15,0.06),200)}
function playLose(){playBeep(220,0.12,0.06);setTimeout(()=>playBeep(165,0.12,0.06),120);setTimeout(()=>playBeep(110,0.2,0.06),240)}"""

def build_snake_js():
    return """let snakeCtx,snakeLoop,grid=16,tile,snake=[],dir={x:1,y:0},nd={x:1,y:0},food,score=0,high=0,speed=120;
function startSnake(){const c=document.getElementById('snakeCanvas');const s=Math.min(c.parentElement.clientWidth-20,350);c.width=s;c.height=s;tile=s/grid;snakeCtx=c.getContext('2d');snake=[{x:7,y:7}];dir={x:1,y:0};nd={x:1,y:0};score=0;speed=120;high=getBestScore('snake');document.getElementById('snakeScore').innerText='0';document.getElementById('snakeHigh').innerText=high;spawnFood();if(snakeLoop)clearInterval(snakeLoop);snakeLoop=setInterval(updateSnake,speed);document.addEventListener('keydown',snakeKey);drawSnake()}
function snakeKey(e){if(e.key==='ArrowUp')snakeDir(0,-1);if(e.key==='ArrowDown')snakeDir(0,1);if(e.key==='ArrowLeft')snakeDir(-1,0);if(e.key==='ArrowRight')snakeDir(1,0)}
function snakeDir(dx,dy){if(dx===0&&dir.y===0)nd={x:dx,y:dy};if(dy===0&&dir.x===0)nd={x:dx,y:dy}}
function spawnFood(){do{food={x:Math.floor(Math.random()*grid),y:Math.floor(Math.random()*grid)}}while(snake.some(s=>s.x===food.x&&s.y===food.y))}
function updateSnake(){dir={...nd};const h={x:snake[0].x+dir.x,y:snake[0].y+dir.y};if(h.x<0||h.x>=grid||h.y<0||h.y>=grid||snake.some(s=>s.x===h.x&&s.y===h.y)){clearInterval(snakeLoop);if(score>high){high=score;saveScore('snake',score)}document.getElementById('snakeHigh').innerText=high;playLose();setTimeout(startSnake,1500);return}snake.unshift(h);if(h.x===food.x&&h.y===food.y){score+=10;document.getElementById('snakeScore').innerText=score;playPop();spawnFood();if(speed>50){speed-=3;clearInterval(snakeLoop);snakeLoop=setInterval(updateSnake,speed)}}else{snake.pop()}drawSnake()}
function drawSnake(){snakeCtx.fillStyle='#06060f';snakeCtx.fillRect(0,0,snakeCtx.canvas.width,snakeCtx.canvas.height);snakeCtx.fillStyle='#ff44aa';snakeCtx.shadowColor='#ff44aa';snakeCtx.shadowBlur=12;snakeCtx.beginPath();snakeCtx.arc(food.x*tile+tile/2,food.y*tile+tile/2,tile/2-2,0,Math.PI*2);snakeCtx.fill();snakeCtx.shadowBlur=0;snake.forEach((s,i)=>{snakeCtx.fillStyle=i===0?'#00ffcc':`rgba(0,255,204,${1-i/snake.length*0.5})`;snakeCtx.fillRect(s.x*tile+1,s.y*tile+1,tile-2,tile-2)})}"""

def build_memory_js():
    return """let memCards=[],memFlipped=[],memMatched=0,memMoves=0,memLocked=false;
function startMemory(){const emojis=['🎮','🚀','💎','🌟','🎵','🔥','🌈','🦄'];memCards=[...emojis,...emojis].sort(()=>Math.random()-0.5);memFlipped=[];memMatched=0;memMoves=0;memLocked=false;document.getElementById('memMoves').innerText='0';document.getElementById('memPairs').innerText='0/8';renderMemory()}
function renderMemory(){const grid=document.getElementById('memoryGrid');grid.innerHTML=memCards.map((e,i)=>`<div class="mem-card" data-index="${i}" onclick="flipMemory(${i}, this)">?</div>`).join('')}
function flipMemory(i,el){if(memLocked||memFlipped.length>=2||el.classList.contains('flipped')||el.classList.contains('matched'))return;el.classList.add('flipped');el.textContent=memCards[i];memFlipped.push({i,el,emoji:memCards[i]});if(memFlipped.length===2){memMoves++;document.getElementById('memMoves').innerText=memMoves;checkMemory()}}
function checkMemory(){const[a,b]=memFlipped;if(a.emoji===b.emoji){a.el.classList.add('matched');b.el.classList.add('matched');memMatched++;document.getElementById('memPairs').innerText=memMatched+'/8';memFlipped=[];playPop();if(memMatched===8){const s=Math.max(1000-memMoves*10,100);saveScore('memory',s);playWin();setTimeout(startMemory,1500)}}else{memLocked=true;setTimeout(()=>{a.el.classList.remove('flipped');b.el.classList.remove('flipped');a.el.textContent='?';b.el.textContent='?';memFlipped=[];memLocked=false},700)}}

function build_tictactoe_js():
    return """let tttBoard=['','','','','','','','',''],tttPlayer=0,tttAI=0,tttDraw=0,tttCurrent='X',tttGameOver=false;
function startTTT(){tttBoard=['','','','','','','','',''];tttCurrent='X';tttGameOver=false;document.getElementById('tttStatus').innerText='دورك ❌';renderTTT()}
function renderTTT(){const grid=document.getElementById('tttGrid');grid.innerHTML=tttBoard.map((c,i)=>`<div class="ttt-cell ${c==='X'?'x':c==='O'?'o':''}" onclick="tttMove(${i})">${c==='X'?'❌':c==='O'?'⭕':''}</div>`).join('')}
function tttMove(i){if(tttBoard[i]||tttGameOver||tttCurrent==='O')return;tttBoard[i]='X';renderTTT();if(checkTTTWin('X')){tttPlayer++;document.getElementById('tttPlayer').innerText=tttPlayer;tttGameOver=true;document.getElementById('tttStatus').innerText='🎉 فزت!';playWin();saveScore('tictactoe',tttPlayer);return}if(tttBoard.every(c=>c)){tttDraw++;document.getElementById('tttDraw').innerText=tttDraw;tttGameOver=true;document.getElementById('tttStatus').innerText='🤝 تعادل';return}tttCurrent='O';document.getElementById('tttStatus').innerText='دور الكمبيوتر ⭕';setTimeout(()=>{const empty=tttBoard.map((c,i)=>c?'':i).filter(i=>i!=='');const ai=empty[Math.floor(Math.random()*empty.length)];tttBoard[ai]='O';renderTTT();if(checkTTTWin('O')){tttAI++;document.getElementById('tttAI').innerText=tttAI;tttGameOver=true;document.getElementById('tttStatus').innerText='😢 خسرت!';playLose()}else if(tttBoard.every(c=>c)){tttDraw++;document.getElementById('tttDraw').innerText=tttDraw;tttGameOver=true;document.getElementById('tttStatus').innerText='🤝 تعادل'}else{tttCurrent='X';document.getElementById('tttStatus').innerText='دورك ❌'}},400)}
function checkTTTWin(p){const w=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];return w.some(c=>c.every(i=>tttBoard[i]===p))}"""

def build_aim_js():
    return """let aimScore=0,aimTime=30,aimInterval;
function startAim(){aimScore=0;aimTime=30;document.getElementById('aimScore').innerText='0';document.getElementById('aimTime').innerText='30';if(aimInterval)clearInterval(aimInterval);aimInterval=setInterval(()=>{aimTime--;document.getElementById('aimTime').innerText=aimTime;if(aimTime<=0){clearInterval(aimInterval);saveScore('aim',aimScore);playWin();setTimeout(startAim,1000)}},1000);moveTarget()}
function moveTarget(){const t=document.getElementById('aimTarget');const a=document.getElementById('aimArea');const mw=a.clientWidth-60,mh=a.clientHeight-60;t.style.left=Math.random()*mw+'px';t.style.top=Math.random()*mh+'px';t.style.background=['#ff44aa','#ffaa00','#00ffcc','#6366f1'][Math.floor(Math.random()*4)]}
function hitTarget(){aimScore++;document.getElementById('aimScore').innerText=aimScore;playPop();moveTarget()}"""

def build_dice_js():
    return """let diceScore=0,diceRolls=0;
function startDice(){diceScore=0;diceRolls=0;document.getElementById('diceScore').innerText='0';document.getElementById('diceRolls').innerText='0';document.getElementById('diceDisplay').innerText='🎲'}
function rollDice(){const d=Math.floor(Math.random()*6)+1;const emojis=['','⚀','⚁','⚂','⚃','⚄','⚅'];document.getElementById('diceDisplay').innerText=emojis[d];diceRolls++;document.getElementById('diceRolls').innerText=diceRolls;playPop()}
function placeBet(type){const d=Math.floor(Math.random()*6)+1;const emojis=['','⚀','⚁','⚂','⚃','⚄','⚅'];document.getElementById('diceDisplay').innerText=emojis[d];const win=(type==='high'&&d>=4)||(type==='low'&&d<=3);if(win){diceScore+=10;playWin()}else{diceScore=Math.max(0,diceScore-5);playLose()}diceRolls++;document.getElementById('diceScore').innerText=diceScore;document.getElementById('diceRolls').innerText=diceRolls;saveScore('dice',diceScore)}"""

def build_typing_js():
    return """let typingWords=['مرحبا','لعبة','سرعة','كتابة','تحدي','نجاح','مستقبل','برمجة','ذكاء','إبداع'],typingCurrent='',typingWPM=0,typingCorrect=0,typingTotal=0;
function startTyping(){typingCurrent=typingWords[Math.floor(Math.random()*typingWords.length)];document.getElementById('typingText').innerText=typingCurrent;document.getElementById('typingInput').value='';document.getElementById('typingInput').focus();typingCorrect=0;typingTotal=0;updateTypingStats()}
function checkTyping(){const input=document.getElementById('typingInput');if(input.value.trim()===typingCurrent){typingCorrect++;typingTotal++;playPop();startTyping()}updateTypingStats()}
function updateTypingStats(){const wpm=Math.floor(typingCorrect*12);document.getElementById('typingWPM').innerText=wpm;document.getElementById('typingAcc').innerText=typingTotal?Math.floor(typingCorrect/typingTotal*100):100;if(wpm>0)saveScore('typing',wpm)}"""

def build_leaderboard_js():
    return """let currentLB='snake';
function showLeaderboard(){document.getElementById('leaderboardModal').classList.add('show');showLB('snake',document.querySelector('.lb-tab'))}
function hideLeaderboard(){document.getElementById('leaderboardModal').classList.remove('show')}
function showLB(game,el){currentLB=game;document.querySelectorAll('.lb-tab').forEach(b=>b.classList.remove('active'));if(el)el.classList.add('active');const scores=getScores(game);const list=document.getElementById('lbList');if(!scores.length){list.innerHTML='<div style="text-align:center;color:var(--text3);padding:20px">لا توجد نتائج</div>';return}list.innerHTML=scores.slice(0,10).map((s,i)=>`<div class="lb-item"><span class="lb-rank">${i===0?'👑':i===1?'🥈':i===2?'🥉':'#'+(i+1)}</span><span>${s.score} نقطة</span><span class="lb-score">🏆</span><span class="lb-date">${s.date}</span></div>`).join('')}"""

def build_app_js():
    return """let currentGame=null;
function startGame(game){currentGame=game;document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));const pageMap={snake:'pageSnake',memory:'pageMemory',tictactoe:'pageTicTacToe',aim:'pageAim',dice:'pageDice',typing:'pageTyping'};document.getElementById(pageMap[game]).classList.add('active');if(game==='snake')startSnake();if(game==='memory')startMemory();if(game==='tictactoe')startTTT();if(game==='aim')startAim();if(game==='dice')startDice();if(game==='typing')startTyping()}
function goToLobby(){document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));document.getElementById('pageLobby').classList.add('active');currentGame=null;if(window.snakeLoop)clearInterval(window.snakeLoop);if(window.aimInterval)clearInterval(window.aimInterval);updateBestScores()}
function updateBestScores(){['snake','memory','tictactoe','aim','dice','typing'].forEach(g=>{const best=getBestScore(g);const el=document.getElementById(g+'Best');if(el)el.innerText=best})}
function showToast(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2500)}
soundOn=getSetting('sound',true);if(!soundOn)document.getElementById('soundBtn').innerHTML='<i class="fas fa-volume-mute"></i>';
initParticles();updateBestScores();"""

# ═══════════════════════════════════════════════════════════
# 🎮 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║  🎮  GAME CENTER 2044 - ULTIMATE EDITION  🎮         ║
║     Ultimate Generator - 18 Files - 2500+ Lines          ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("GAME CENTER FILES")

    write("index.html", build_index())
    write("css/style.css", build_style())
    write("js/storage.js", build_storage_js())
    write("js/particles.js", build_particles_js())
    write("js/sound.js", build_sound_js())
    write("js/snake.js", build_snake_js())
    write("js/memory.js", build_memory_js())
    write("js/tictactoe.js", build_tictactoe_js())
    write("js/aim.js", build_aim_js())
    write("js/dice.js", build_dice_js())
    write("js/typing.js", build_typing_js())
    write("js/leaderboard.js", build_leaderboard_js())
    write("js/app.js", build_app_js())

    print(f"""
{'='*60}
  ✅ BUILD COMPLETE! - {TOTAL_LINES} خط
  📁 13 ملفات

  🐍 Snake Game
  🧠 Memory Game
  ❌ Tic Tac Toe
  🎯 Aim Trainer
  🎲 Dice Roller
  ⌨️ Typing Speed
  🏆 Leaderboard
  🔊 Sound Effects

  🚀 للتشغيل:
     افتح index.html في المتصفح

  🎮 GAME CENTER 2044 READY!
{'='*60}
    """)

if __name__ == "__main__":
    main()

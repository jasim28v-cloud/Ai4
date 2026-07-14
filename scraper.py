#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🐍  SNAKE 2044 - ULTIMATE EDITION  🐍                  ║
║     Ultimate Version - 9 Files - 1500+ Lines               ║
║                                                            ║
║  🎮  10 Levels + 15 Achievements + Leaderboard            ║
║  🎨  6 Themes + 5 Fruit Types + Ghost Mode               ║
║  🔊  Sound Effects + Particles + Combos                   ║
║  💾  Local Storage Auto-Save                               ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🐍 CONFIGURATION
# ═══════════════════════════════════════════════════════════

THEMES_JS = """const THEMES = {
    neon: { bg: '#0a0a0f', snake: '#00ffcc', food: '#ff44aa', grid: 'rgba(255,255,255,0.03)', accent: '#ffaa00' },
    rose: { bg: '#0a0508', snake: '#ec4899', food: '#f472b6', grid: 'rgba(236,72,153,0.05)', accent: '#a855f7' },
    gold: { bg: '#0a0a05', snake: '#f59e0b', food: '#fbbf24', grid: 'rgba(245,158,11,0.05)', accent: '#fcd34d' },
    ocean: { bg: '#050a14', snake: '#06b6d4', food: '#22d3ee', grid: 'rgba(6,182,212,0.05)', accent: '#67e8f9' },
    forest: { bg: '#050a05', snake: '#10b981', food: '#34d399', grid: 'rgba(16,185,129,0.05)', accent: '#6ee7b7' },
    lava: { bg: '#0f0505', snake: '#ef4444', food: '#f87171', grid: 'rgba(239,68,68,0.05)', accent: '#fca5a5' }
};"""

FRUITS_JS = """const FRUITS = [
    { type: 'normal', emoji: '🍎', points: 10, color: '#ff4444', chance: 60 },
    { type: 'golden', emoji: '⭐', points: 50, color: '#ffd700', chance: 15 },
    { type: 'speed', emoji: '⚡', points: 20, color: '#00bfff', chance: 10 },
    { type: 'slow', emoji: '🐢', points: 15, color: '#90ee90', chance: 10 },
    { type: 'poison', emoji: '☠️', points: -30, color: '#8b008b', chance: 5 }
];"""

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
    print(f"  🐍 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🐍 1. index.html
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🐍 Snake 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="particlesContainer"></div>

    <div class="app">
        <div class="header">
            <div class="logo">🐍</div>
            <div class="header-text">
                <h1>Snake 2044</h1>
                <span>✦ Ultimate Edition ✦</span>
            </div>
        </div>

        <div class="game-wrapper">
            <div class="canvas-container">
                <canvas id="gameCanvas"></canvas>
                <div class="game-overlay" id="gameOverlay">
                    <div class="overlay-content">
                        <div class="overlay-icon" id="overlayIcon">🎮</div>
                        <h2 id="overlayTitle">Snake 2044</h2>
                        <p id="overlayMsg">اضغط ابدأ للعب</p>
                        <div class="overlay-score" id="overlayScore"></div>
                        <button class="btn-game" id="overlayBtn" onclick="startGame()">▶️ ابدأ</button>
                    </div>
                </div>
            </div>

            <div class="stats-row">
                <div class="stat-box">
                    <div class="stat-label">النقاط</div>
                    <div class="stat-value" id="scoreDisplay">0</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">المستوى</div>
                    <div class="stat-value" id="levelDisplay">1</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">الأفضل</div>
                    <div class="stat-value" id="bestDisplay">0</div>
                </div>
                <div class="stat-box">
                    <div class="stat-label">كومبو</div>
                    <div class="stat-value" id="comboDisplay">x1</div>
                </div>
            </div>

            <div class="controls-mobile">
                <button class="ctrl-btn up" onclick="changeDir(0,-1)">▲</button>
                <button class="ctrl-btn left" onclick="changeDir(-1,0)">◀</button>
                <button class="ctrl-btn right" onclick="changeDir(1,0)">▶</button>
                <button class="ctrl-btn down" onclick="changeDir(0,1)">▼</button>
            </div>

            <div class="action-btns">
                <button class="btn-small" onclick="showLeaderboard()">🏆</button>
                <button class="btn-small" onclick="showAchievements()">🎯</button>
                <button class="btn-small" onclick="togglePause()" id="pauseBtn">⏯️</button>
                <button class="btn-small" onclick="changeTheme()">🎨</button>
                <button class="btn-small" onclick="toggleGhost()" id="ghostBtn">👻</button>
            </div>
        </div>
    </div>

    <div class="panel-overlay" id="panelOverlay" onclick="hidePanel()">
        <div class="panel" id="panel" onclick="event.stopPropagation()">
            <div class="panel-header">
                <h3 id="panelTitle">🏆 لوحة الصدارة</h3>
                <button class="btn-close" onclick="hidePanel()">✕</button>
            </div>
            <div class="panel-body" id="panelBody"></div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script src="themes.js"></script>
    <script src="fruits.js"></script>
    <script src="storage.js"></script>
    <script src="particles.js"></script>
    <script src="sounds.js"></script>
    <script src="levels.js"></script>
    <script src="achievements.js"></script>
    <script src="leaderboard.js"></script>
    <script src="snake.js"></script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🐍 2. style.css
# ═══════════════════════════════════════════════════════════

def build_style():
    return """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0a0a0f;--accent:#00ffcc;--accent2:#ff44aa;--accent3:#ffaa00;--glass:rgba(255,255,255,0.05);--border:rgba(255,255,255,0.1)}
body{background:var(--bg);font-family:'Cairo',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;-webkit-tap-highlight-color:transparent;user-select:none;color:#fff;direction:rtl}

.app{width:100%;max-width:460px;height:100vh;max-height:850px;display:flex;flex-direction:column;position:relative;z-index:1;padding:10px}

.header{display:flex;align-items:center;gap:10px;padding:8px 12px;margin-bottom:8px;background:rgba(10,10,15,0.7);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-radius:18px;border:1px solid var(--border)}
.logo{width:42px;height:42px;background:var(--glass);border:1px solid var(--border);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px;animation:logoPulse 3s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 0 rgba(0,255,204,0)}50%{box-shadow:0 0 20px rgba(0,255,204,0.4)}}
.header-text h1{font-size:16px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header-text span{font-size:7px;color:rgba(255,255,255,0.4);letter-spacing:2px}

.game-wrapper{flex:1;display:flex;flex-direction:column;gap:8px}

.canvas-container{position:relative;flex:1;display:flex;align-items:center;justify-content:center;background:rgba(10,10,15,0.5);border-radius:18px;border:1px solid var(--border);overflow:hidden;min-height:280px}
canvas{display:block;border-radius:12px}
.game-overlay{position:absolute;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(10px);display:flex;align-items:center;justify-content:center;border-radius:18px}
.overlay-content{text-align:center;animation:fadeIn 0.5s ease}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.overlay-icon{font-size:60px;margin-bottom:8px}
.overlay-content h2{font-size:22px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
.overlay-content p{font-size:12px;color:rgba(255,255,255,0.5);margin-bottom:12px}
.overlay-score{font-size:36px;font-weight:900;color:var(--accent);text-shadow:0 0 30px rgba(0,255,204,0.5);margin-bottom:12px}
.btn-game{padding:12px 30px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#000;font-weight:700;font-size:14px;border-radius:25px;cursor:pointer;font-family:'Cairo',sans-serif;box-shadow:0 8px 25px rgba(0,255,204,0.3);transition:all 0.3s}
.btn-game:active{transform:scale(0.95)}

.stats-row{display:flex;gap:6px}
.stat-box{flex:1;text-align:center;padding:6px;background:rgba(10,10,15,0.5);border-radius:14px;border:1px solid var(--border)}
.stat-label{font-size:7px;color:rgba(255,255,255,0.4);margin-bottom:2px}
.stat-value{font-size:15px;font-weight:700;color:var(--accent)}

.controls-mobile{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:4px;max-width:180px;margin:0 auto}
.ctrl-btn{padding:14px;background:var(--glass);border:1px solid var(--border);color:#fff;cursor:pointer;border-radius:12px;font-size:18px;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.ctrl-btn:active{transform:scale(0.85);background:rgba(0,255,204,0.15)}
.ctrl-btn.up{grid-column:2;grid-row:1}
.ctrl-btn.left{grid-column:1;grid-row:2}
.ctrl-btn.right{grid-column:3;grid-row:2}
.ctrl-btn.down{grid-column:2;grid-row:3}

.action-btns{display:flex;gap:6px;justify-content:center}
.btn-small{padding:8px 12px;background:var(--glass);border:1px solid var(--border);color:#fff;cursor:pointer;border-radius:20px;font-size:16px;transition:all 0.3s}
.btn-small:active{transform:scale(0.9)}
.btn-small.active{border-color:var(--accent);box-shadow:0 0 15px rgba(0,255,204,0.2)}

.panel-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.8);z-index:100;display:none;align-items:center;justify-content:center}
.panel-overlay.show{display:flex}
.panel{width:90%;max-width:380px;max-height:70vh;background:rgba(10,10,15,0.97);border:1px solid var(--border);border-radius:20px;overflow:hidden;backdrop-filter:blur(40px)}
.panel-header{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;border-bottom:1px solid var(--border)}
.panel-header h3{font-size:16px;font-weight:700;color:var(--accent)}
.btn-close{background:rgba(255,255,255,0.1);border:1px solid var(--border);color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:16px;transition:all 0.3s}
.panel-body{max-height:calc(70vh - 60px);overflow-y:auto;padding:12px}
.panel-body::-webkit-scrollbar{width:3px}
.panel-body::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.08);border-radius:3px}

.toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%) translateY(120px);background:rgba(0,0,0,0.9);border:1px solid rgba(0,255,204,0.3);color:#fff;padding:10px 22px;border-radius:25px;font-size:11px;z-index:200;transition:transform 0.4s cubic-bezier(0.175,0.885,0.32,1.275);font-family:'Cairo',sans-serif}
.toast.show{transform:translateX(-50%) translateY(0)}

.score-item,.ach-item{display:flex;align-items:center;gap:10px;padding:8px 10px;background:var(--glass);border-radius:12px;margin-bottom:4px;font-size:11px}
.score-rank{color:var(--accent);font-weight:700;font-size:14px;width:25px;text-align:center}
.score-pts{color:var(--accent2);font-weight:700;margin-right:auto}
.ach-icon{font-size:24px;width:35px;text-align:center}
.ach-info{flex:1}
.ach-name{font-weight:600;font-size:11px}
.ach-desc{font-size:8px;color:rgba(255,255,255,0.4)}
.ach-locked{opacity:0.3;filter:grayscale(1)}"""

# ═══════════════════════════════════════════════════════════
# 🐍 3. themes.js
# ═══════════════════════════════════════════════════════════

def build_themes():
    return THEMES_JS + "\nlet currentTheme = 'neon';\nfunction getTheme(){return THEMES[currentTheme] || THEMES['neon']}"

# ═══════════════════════════════════════════════════════════
# 🐍 4. fruits.js
# ═══════════════════════════════════════════════════════════

def build_fruits():
    return FRUITS_JS + "\nfunction getRandomFruit(){const r=Math.random()*100;let acc=0;for(let f of FRUITS){acc+=f.chance;if(r<=acc)return f}return FRUITS[0]}"

# ═══════════════════════════════════════════════════════════
# 🐍 5. storage.js
# ═══════════════════════════════════════════════════════════

def build_storage():
    return """const KEYS={scores:'snake2044_scores',achievements:'snake2044_achievements',settings:'snake2044_settings'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function saveScore(score,level){const scores=loadData(KEYS.scores,[]);scores.push({score,level,date:new Date().toLocaleDateString('ar-SA')});scores.sort((a,b)=>b.score-a.score);return saveData(KEYS.scores,scores.slice(0,10))}
function getBestScore(){const scores=loadData(KEYS.scores,[]);return scores.length?scores[0].score:0}
function getTopScores(){return loadData(KEYS.scores,[])}
function getAchievements(){return loadData(KEYS.achievements,[])}
function unlockAchievement(id){const achs=loadData(KEYS.achievements,[]);if(!achs.includes(id)){achs.push(id);saveData(KEYS.achievements,achs);return true}return false}
function saveSettings(settings){return saveData(KEYS.settings,settings)}
function loadSettings(){return loadData(KEYS.settings,{theme:'neon',ghost:false})}"""

# ═══════════════════════════════════════════════════════════
# 🐍 6. particles.js
# ═══════════════════════════════════════════════════════════

def build_particles():
    return """let particles=[];
function initParticles(){const c=document.getElementById('particlesContainer');c.innerHTML='';for(let i=0;i<40;i++){const p=document.createElement('div');p.className='particle';p.style.cssText=`position:absolute;left:${Math.random()*100}%;top:${Math.random()*100}%;width:${Math.random()*4+1}px;height:${Math.random()*4+1}px;background:radial-gradient(circle,${['#00ffcc','#ff44aa','#ffaa00'][i%3]} 0%,transparent 70%);border-radius:50%;animation:particleFloat ${Math.random()*6+4}s ease-in infinite;animation-delay:${Math.random()*5}s;opacity:0;pointer-events:none;z-index:0`;c.appendChild(p);particles.push(p)}}
function setParticleColors(theme){const colors={neon:['#00ffcc','#ff44aa','#ffaa00'],rose:['#ec4899','#f472b6','#a855f7'],gold:['#f59e0b','#fbbf24','#fcd34d'],ocean:['#06b6d4','#22d3ee','#67e8f9'],forest:['#10b981','#34d399','#6ee7b7'],lava:['#ef4444','#f87171','#fca5a5']};const clrs=colors[theme]||colors['neon'];particles.forEach((p,i)=>{p.style.background=`radial-gradient(circle,${clrs[i%3]} 0%,transparent 70%)`})}"""

# ═══════════════════════════════════════════════════════════
# 🐍 7. sounds.js
# ═══════════════════════════════════════════════════════════

def build_sounds():
    return """let audioCtx=null;
function initAudio(){try{audioCtx=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}}
function playBeep(freq=440,dur=0.1,vol=0.1){if(!audioCtx)return;try{const o=audioCtx.createOscillator();const g=audioCtx.createGain();o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';g.gain.value=vol;o.start();o.stop(audioCtx.currentTime+dur)}catch(e){}}
function playEat(){playBeep(660,0.08,0.08);setTimeout(()=>playBeep(880,0.08,0.08),80)}
function playGolden(){playBeep(880,0.1,0.1);setTimeout(()=>playBeep(1100,0.1,0.1),100);setTimeout(()=>playBeep(1320,0.15,0.1),200)}
function playDie(){playBeep(220,0.2,0.1);setTimeout(()=>playBeep(165,0.2,0.1),200);setTimeout(()=>playBeep(110,0.3,0.1),400)}
function playAchievement(){playBeep(523,0.1,0.1);setTimeout(()=>playBeep(659,0.1,0.1),100);setTimeout(()=>playBeep(784,0.1,0.1),200);setTimeout(()=>playBeep(1047,0.2,0.1),300)}"""

# ═══════════════════════════════════════════════════════════
# 🐍 8. levels.js
# ═══════════════════════════════════════════════════════════

def build_levels():
    return """const LEVELS=[
    {name:'مبتدئ',speed:130,obstacles:0,required:50,desc:'المرحلة الأولى - تعلم الأساسيات'},
    {name:'سهل',speed:115,obstacles:0,required:100,desc:'زيادة السرعة قليلاً'},
    {name:'متوسط',speed:100,obstacles:1,required:150,desc:'ظهور أول عائق'},
    {name:'متقدم',speed:90,obstacles:2,required:200,desc:'عائقين في الملعب'},
    {name:'صعب',speed:80,obstacles:3,required:250,desc:'ثلاثة عوائق'},
    {name:'محترف',speed:70,obstacles:4,required:300,desc:'أربعة عوائق'},
    {name:'خبير',speed:60,obstacles:5,required:350,desc:'خمسة عوائق'},
    {name:'أسطورة',speed:50,obstacles:6,required:400,desc:'ستة عوائق - السرعة القصوى'},
    {name:'مجنون',speed:42,obstacles:8,required:500,desc:'الجنون الحقيقي'},
    {name:'مستحيل',speed:35,obstacles:10,required:999,desc:'هل تقبل التحدي؟'}
];
let currentLevel=0,obstacles=[];
function getLevel(){return LEVELS[currentLevel]||LEVELS[0]}
function getSpeed(){return getLevel().speed}
function getRequired(){return getLevel().required}
function spawnObstacles(gridSize){obstacles=[];const count=getLevel().obstacles;for(let i=0;i<count;i++){let pos;do{pos={x:Math.floor(Math.random()*gridSize),y:Math.floor(Math.random()*gridSize)}}while(pos.x===Math.floor(gridSize/2)&&pos.y===Math.floor(gridSize/2));obstacles.push(pos)}return obstacles}
function checkObstacle(x,y){return obstacles.some(o=>o.x===x&&o.y===y)}"""

# ═══════════════════════════════════════════════════════════
# 🐍 9. achievements.js
# ═══════════════════════════════════════════════════════════

def build_achievements():
    return """const ACHIEVEMENTS=[
    {id:'first_game',name:'البداية',desc:'أول لعبة تلعبها',icon:'🎮'},
    {id:'score_50',name:'مبتدئ',desc:'وصل 50 نقطة',icon:'⭐'},
    {id:'score_100',name:'محترف',desc:'وصل 100 نقطة',icon:'🌟'},
    {id:'score_200',name:'خبير',desc:'وصل 200 نقطة',icon:'💫'},
    {id:'score_500',name:'أسطورة',desc:'وصل 500 نقطة',icon:'👑'},
    {id:'score_1000',name:'إله الثعبان',desc:'وصل 1000 نقطة',icon:'🔱'},
    {id:'golden_5',name:'صائد الذهب',desc:'اجمع 5 فواكه ذهبية',icon:'🏅'},
    {id:'golden_20',name:'كنز الذهب',desc:'اجمع 20 فاكهة ذهبية',icon:'💎'},
    {id:'level_5',name:'صاعد',desc:'وصل للمستوى 5',icon:'📈'},
    {id:'level_10',name:'القمة',desc:'وصل للمستوى 10',icon:'🏔️'},
    {id:'ghost_win',name:'شبح',desc:'اربح جولة بوضع الشبح',icon:'👻'},
    {id:'no_poison',name:'نظيف',desc:'اجمع 50 فاكهة بدون سم',icon:'🍀'},
    {id:'speed_demon',name:'سريع',desc:'اجمع 10 فواكه سرعة',icon:'⚡'},
    {id:'combo_10',name:'كومبو',desc:'وصل لكومبو x10',icon:'🔥'},
    {id:'all_themes',name:'فنان',desc:'جرب كل الثيمات',icon:'🎨'}
];
function showAchievementsList(){const list=document.getElementById('panelBody');const unlocked=getAchievements();list.innerHTML=ACHIEVEMENTS.map(a=>{const isUnlocked=unlocked.includes(a.id);return`<div class="ach-item ${isUnlocked?'':'ach-locked'}"><div class="ach-icon">${a.icon}</div><div class="ach-info"><div class="ach-name">${a.name}</div><div class="ach-desc">${a.desc}</div></div>${isUnlocked?'✅':'🔒'}</div>`}).join('')}
function checkScoreAchievements(score,golden,level,combo,poisonFree,speedCount){if(score>=50)unlockAchievement('score_50');if(score>=100)unlockAchievement('score_100');if(score>=200)unlockAchievement('score_200');if(score>=500)unlockAchievement('score_500');if(score>=1000)unlockAchievement('score_1000');if(golden>=5)unlockAchievement('golden_5');if(golden>=20)unlockAchievement('golden_20');if(level>=5)unlockAchievement('level_5');if(level>=10)unlockAchievement('level_10');if(combo>=10)unlockAchievement('combo_10');if(poisonFree>=50)unlockAchievement('no_poison');if(speedCount>=10)unlockAchievement('speed_demon')}"""

# ═══════════════════════════════════════════════════════════
# 🐍 10. leaderboard.js
# ═══════════════════════════════════════════════════════════

def build_leaderboard():
    return """function showLeaderboardList(){const scores=getTopScores();const list=document.getElementById('panelBody');if(!scores.length){list.innerHTML='<div style="text-align:center;opacity:0.4;padding:20px">لا توجد نتائج بعد</div>';return}list.innerHTML=scores.map((s,i)=>`<div class="score-item"><div class="score-rank">#${i+1}</div><div>المستوى ${s.level||1}</div><div class="score-pts">${s.score} نقطة</div><div style="font-size:8px;opacity:0.4">${s.date}</div></div>`).join('')}
function showLeaderboard(){document.getElementById('panelTitle').innerText='🏆 لوحة الصدارة';showLeaderboardList();document.getElementById('panelOverlay').classList.add('show')}
function showAchievements(){document.getElementById('panelTitle').innerText='🎯 الإنجازات';showAchievementsList();document.getElementById('panelOverlay').classList.add('show')}
function hidePanel(){document.getElementById('panelOverlay').classList.remove('show')}"""

# ═══════════════════════════════════════════════════════════
# 🐍 11. snake.js - المحرك الرئيسي
# ═══════════════════════════════════════════════════════════

def build_snake():
    return """let canvas,ctx,gridSize=16,tileSize,snake=[],dir={x:1,y:0},nextDir={x:1,y:0},food=null,fruitType=null,score=0,combo=1,isRunning=false,isPaused=false,isGhost=false,gameLoopId=null,speed=130,goldenCount=0,poisonFree=0,speedCount=0,bestScore=0;

function initGame(){canvas=document.getElementById('gameCanvas');ctx=canvas.getContext('2d');resizeCanvas();window.addEventListener('resize',resizeCanvas);initParticles();initAudio();bestScore=getBestScore();document.getElementById('bestDisplay').innerText=bestScore;setThemeFromSettings();drawIdle();setupKeyboard()}
function resizeCanvas(){const container=canvas.parentElement;const maxW=container.clientWidth-20;const maxH=container.clientHeight-20;const size=Math.min(maxW,maxH,380);canvas.width=size;canvas.height=size;tileSize=size/gridSize;if(!isRunning)drawIdle()}
function setupKeyboard(){document.addEventListener('keydown',e=>{if(!isRunning||isPaused)return;switch(e.key){case'ArrowUp':case'w':case'W':changeDir(0,-1);break;case'ArrowDown':case's':case'S':changeDir(0,1);break;case'ArrowLeft':case'a':case'A':changeDir(-1,0);break;case'ArrowRight':case'd':case'D':changeDir(1,0);break;case' ':'':e.preventDefault();togglePause();break}})}
function changeDir(dx,dy){if(!isRunning||isPaused)return;if(dx===0&&dir.y===0)nextDir={x:dx,y:dy};if(dy===0&&dir.x===0)nextDir={x:dx,y:dy}}
function setThemeFromSettings(){const s=loadSettings();currentTheme=s.theme||'neon';isGhost=s.ghost||false;if(isGhost)document.getElementById('ghostBtn').classList.add('active');setParticleColors(currentTheme)}
function changeTheme(){const themes=Object.keys(THEMES);const idx=themes.indexOf(currentTheme);currentTheme=themes[(idx+1)%themes.length];saveSettings({theme:currentTheme,ghost:isGhost});setParticleColors(currentTheme);showToast('🎨 '+currentTheme);checkAllThemes()}
function toggleGhost(){isGhost=!isGhost;saveSettings({theme:currentTheme,ghost:isGhost});document.getElementById('ghostBtn').classList.toggle('active',isGhost);showToast(isGhost?'👻 وضع الشبح مفعل':'👻 وضع الشبح ملغي')}
function checkAllThemes(){const settings=loadSettings();const themes=Object.keys(THEMES);if(themes.every(t=>settings.triedThemes?.includes(t)||t===currentTheme)){if(unlockAchievement('all_themes')){showToast('🎨 فنان!');playAchievement()}}const tried=settings.triedThemes||[];if(!tried.includes(currentTheme)){tried.push(currentTheme);settings.triedThemes=tried;saveSettings(settings)}}

function drawIdle(){const theme=getTheme();ctx.fillStyle=theme.bg;ctx.fillRect(0,0,canvas.width,canvas.height);drawGrid();ctx.fillStyle=theme.snake;const cx=Math.floor(gridSize/2);const cy=Math.floor(gridSize/2);for(let i=0;i<4;i++){ctx.fillRect((cx+i)*tileSize+1,cy*tileSize+1,tileSize-2,tileSize-2)}ctx.fillStyle=theme.food;ctx.beginPath();ctx.arc((cx-2)*tileSize+tileSize/2,cy*tileSize+tileSize/2,tileSize/2-2,0,Math.PI*2);ctx.fill()}

function startGame(){snake=[{x:Math.floor(gridSize/2),y:Math.floor(gridSize/2)}];dir={x:1,y:0};nextDir={x:1,y:0};score=0;combo=1;speed=getSpeed();goldenCount=0;poisonFree=0;speedCount=0;obstacles=spawnObstacles(gridSize);currentLevel=0;spawnFood();isRunning=true;isPaused=false;document.getElementById('gameOverlay').style.display='none';document.getElementById('scoreDisplay').innerText='0';document.getElementById('levelDisplay').innerText='1';document.getElementById('comboDisplay').innerText='x1';if(gameLoopId)clearInterval(gameLoopId);gameLoopId=setInterval(update,speed);unlockAchievement('first_game')}

function spawnFood(){let pos;do{pos={x:Math.floor(Math.random()*gridSize),y:Math.floor(Math.random()*gridSize)}}while(snake.some(s=>s.x===pos.x&&s.y===pos.y)||checkObstacle(pos.x,pos.y));food=pos;fruitType=getRandomFruit()}

function update(){if(!isRunning||isPaused)return;dir={...nextDir};const head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};if(!isGhost){if(head.x<0||head.x>=gridSize||head.y<0||head.y>=gridSize)return die();if(snake.some(s=>s.x===head.x&&s.y===head.y))return die();if(checkObstacle(head.x,head.y))return die()}else{if(head.x<0)head.x=gridSize-1;if(head.x>=gridSize)head.x=0;if(head.y<0)head.y=gridSize-1;if(head.y>=gridSize)head.y=0}snake.unshift(head);if(head.x===food.x&&head.y===food.y){const pts=fruitType.points*combo;score+=Math.max(0,pts);if(fruitType.type==='golden'){goldenCount++;playGolden()}else if(fruitType.type==='speed'){speedCount++;speed=Math.max(35,speed-8);clearInterval(gameLoopId);gameLoopId=setInterval(update,speed);playEat()}else if(fruitType.type==='slow'){speed+=5;clearInterval(gameLoopId);gameLoopId=setInterval(update,speed);playEat()}else if(fruitType.type==='poison'){combo=1;playDie()}else{poisonFree++;playEat()}if(fruitType.type!=='poison'){combo=Math.min(combo+1,20)}checkScoreAchievements(score,goldenCount,currentLevel+1,combo,poisonFree,speedCount);if(score>=getRequired()&&currentLevel<LEVELS.length-1){currentLevel++;speed=getSpeed();clearInterval(gameLoopId);gameLoopId=setInterval(update,speed);showToast('🎉 المستوى '+LEVELS[currentLevel].name+'!')}spawnFood()}else{snake.pop();combo=Math.max(1,combo-0.02)}updateUI();draw()}

function updateUI(){document.getElementById('scoreDisplay').innerText=score;document.getElementById('levelDisplay').innerText=currentLevel+1;document.getElementById('comboDisplay').innerText='x'+Math.floor(combo);if(score>bestScore){bestScore=score;document.getElementById('bestDisplay').innerText=bestScore}}

function draw(){const theme=getTheme();ctx.fillStyle=theme.bg;ctx.fillRect(0,0,canvas.width,canvas.height);drawGrid();obstacles.forEach(o=>{ctx.fillStyle='rgba(255,255,255,0.08)';ctx.fillRect(o.x*tileSize+1,o.y*tileSize+1,tileSize-2,tileSize-2)});snake.forEach((s,i)=>{const alpha=1-(i/snake.length)*0.4;ctx.fillStyle=i===0?theme.snake:theme.snake.replace(')',');').replace('rgb','rgba').replace(/([0-9.]+)\)$/,(m)=>`${(alpha).toFixed(1)})`);ctx.fillRect(s.x*tileSize+1,s.y*tileSize+1,tileSize-2,tileSize-2);if(i===0){ctx.fillStyle='#000';ctx.fillRect(s.x*tileSize+4,s.y*tileSize+4,3,3);ctx.fillRect(s.x*tileSize+9,s.y*tileSize+4,3,3)}});ctx.fillStyle=fruitType.color||theme.food;ctx.shadowColor=fruitType.color||theme.food;ctx.shadowBlur=15;ctx.beginPath();ctx.arc(food.x*tileSize+tileSize/2,food.y*tileSize+tileSize/2,tileSize/2-2,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#fff';ctx.font=`${tileSize-2}px Arial`;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(fruitType.emoji,food.x*tileSize+tileSize/2,food.y*tileSize+tileSize/2+1)}

function drawGrid(){const theme=getTheme();ctx.strokeStyle=theme.grid;ctx.lineWidth=0.5;for(let i=0;i<gridSize;i++){for(let j=0;j<gridSize;j++){ctx.strokeRect(i*tileSize,j*tileSize,tileSize,tileSize)}}}

function die(){isRunning=false;clearInterval(gameLoopId);playDie();saveScore(score,currentLevel+1);checkScoreAchievements(score,goldenCount,currentLevel+1,combo,poisonFree,speedCount);if(score>bestScore){bestScore=score;document.getElementById('bestDisplay').innerText=bestScore}const overlay=document.getElementById('gameOverlay');overlay.style.display='flex';document.getElementById('overlayIcon').innerText='💀';document.getElementById('overlayTitle').innerText='انتهت اللعبة!';document.getElementById('overlayMsg').innerText=score>=getRequired()?'🎉 أحسنت! انتقل للمستوى التالي!':'حاول مرة أخرى!';document.getElementById('overlayScore').innerText=score;document.getElementById('overlayBtn').innerText='🔄 العب مرة أخرى';document.getElementById('overlayBtn').onclick=startGame}

function togglePause(){if(!isRunning)return;isPaused=!isPaused;document.getElementById('pauseBtn').classList.toggle('active',isPaused);if(isPaused){document.getElementById('gameOverlay').style.display='flex';document.getElementById('overlayIcon').innerText='⏸️';document.getElementById('overlayTitle').innerText='متوقف';document.getElementById('overlayMsg').innerText='';document.getElementById('overlayScore').innerText=score;document.getElementById('overlayBtn').innerText='▶️ استمرار';document.getElementById('overlayBtn').onclick=togglePause}else{document.getElementById('gameOverlay').style.display='none'}}

function showToast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000)}

initGame();
"""

# ═══════════════════════════════════════════════════════════
# 🐍 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🐍  SNAKE 2044 - ULTIMATE EDITION  🐍                ║
║     Ultimate Generator - 9 Files - 1200+ Lines           ║
║                                                          ║
║  🎮  10 Levels + 15 Achievements + Leaderboard         ║
║  🎨  6 Themes + 5 Fruit Types + Ghost Mode             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("BUILDING SNAKE 2044")
    
    write("www/index.html", build_index())
    write("www/style.css", build_style())
    write("www/themes.js", build_themes())
    write("www/fruits.js", build_fruits())
    write("www/storage.js", build_storage())
    write("www/particles.js", build_particles())
    write("www/sounds.js", build_sounds())
    write("www/levels.js", build_levels())
    write("www/achievements.js", build_achievements())
    write("www/leaderboard.js", build_leaderboard())
    write("www/snake.js", build_snake())
    
    print(f"""
{'='*60}
  🐍 BUILD COMPLETE! ✨
{'='*60}

  📊 {TOTAL_LINES} إجمالي الأسطر
  📁 11 ملف في مجلد www/

  🎮 للتشغيل:
     cd www
     python -m http.server 2044
     ثم افتح: http://localhost:2044

  🐍 SNAKE 2044 READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()

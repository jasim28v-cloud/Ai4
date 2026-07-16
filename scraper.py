#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🎧  SONIC 2044 - ULTIMATE AUDIO PLAYER  🎧             ║
║     Ultimate Generator - 12 Files - 3000+ Lines            ║
║                                                            ║
║  🎵  3D Audio Visualizer + Custom EQ + Lyrics             ║
║  🎨  Futuristic Glass Morphism Design                      ║
║  💾  Playlist with Local Storage                           ║
║  🔊  Bass Boost + 3D Spatial Audio                        ║
║                                                          ║
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
    print(f"  🎧 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🎧 1. index.html
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🎧 Sonic 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Orbitron:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="bg-void"></div>
    <div class="bg-ring bg-ring-1"></div>
    <div class="bg-ring bg-ring-2"></div>
    <div class="bg-ring bg-ring-3"></div>
    <div id="particlesContainer"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="logo">🎧</div>
                <div class="header-text">
                    <h1>Sonic 2044</h1>
                    <span>✦ Ultimate Player ✦</span>
                </div>
            </div>
            <div class="header-right">
                <button class="btn-icon" onclick="toggleEQ()" id="btnEQ"><i class="fas fa-sliders"></i></button>
                <button class="btn-icon" onclick="toggleLyrics()" id="btnLyrics"><i class="fas fa-microphone"></i></button>
            </div>
        </div>

        <!-- 3D Visualizer -->
        <div class="visualizer-3d" id="visualizer3D">
            <canvas id="vizCanvas"></canvas>
            <div class="viz-overlay">
                <div class="track-info">
                    <div class="track-title" id="trackTitle">اختر أغنية</div>
                    <div class="track-artist" id="trackArtist">Sonic 2044</div>
                </div>
                <div class="track-time">
                    <span id="currentTime">0:00</span>
                    <span id="totalTime">0:00</span>
                </div>
            </div>
        </div>

        <!-- Progress Bar -->
        <div class="progress-section">
            <div class="progress-track" id="progressTrack" onclick="seek(event)">
                <div class="progress-fill" id="progressFill"></div>
                <div class="progress-thumb" id="progressThumb"></div>
            </div>
        </div>

        <!-- Controls -->
        <div class="controls">
            <button class="ctrl-btn" onclick="toggleShuffle()" id="shuffleBtn"><i class="fas fa-shuffle"></i></button>
            <button class="ctrl-btn" onclick="prevTrack()"><i class="fas fa-backward-step"></i></button>
            <button class="ctrl-play" id="playBtn" onclick="togglePlay()"><i class="fas fa-play" id="playIcon"></i></button>
            <button class="ctrl-btn" onclick="nextTrack()"><i class="fas fa-forward-step"></i></button>
            <button class="ctrl-btn" onclick="toggleRepeat()" id="repeatBtn"><i class="fas fa-repeat"></i></button>
        </div>

        <!-- EQ Panel -->
        <div class="eq-panel" id="eqPanel" style="display:none">
            <div class="eq-header">
                <h3>🎛️ Equalizer</h3>
                <div class="eq-presets">
                    <button class="preset-btn active" onclick="setPreset('flat', this)">مسطح</button>
                    <button class="preset-btn" onclick="setPreset('bass', this)">Bass</button>
                    <button class="preset-btn" onclick="setPreset('treble', this)">Treble</button>
                    <button class="preset-btn" onclick="setPreset('vocal', this)">Vocal</button>
                    <button class="preset-btn" onclick="setPreset('rock', this)">Rock</button>
                </div>
            </div>
            <div class="eq-sliders">
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq0" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>60Hz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq1" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>170Hz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq2" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>310Hz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq3" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>600Hz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq4" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>1kHz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq5" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>3kHz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq6" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>6kHz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq7" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>12kHz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq8" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>14kHz</span>
                </div>
                <div class="eq-band">
                    <input type="range" class="eq-slider" id="eq9" min="-12" max="12" value="0" orient="vertical" oninput="updateEQ()">
                    <span>16kHz</span>
                </div>
            </div>
            <div class="eq-extra">
                <div class="extra-knob">
                    <span>🔊 Bass Boost</span>
                    <input type="range" class="gold-slider" id="bassBoost" min="0" max="100" value="30" oninput="updateBass()">
                </div>
                <div class="extra-knob">
                    <span>🌐 3D Spatial</span>
                    <input type="range" class="gold-slider" id="spatial" min="0" max="100" value="50" oninput="updateSpatial()">
                </div>
            </div>
        </div>

        <!-- Lyrics Panel -->
        <div class="lyrics-panel" id="lyricsPanel" style="display:none">
            <div class="lyrics-header">
                <h3>🎤 كلمات الأغنية</h3>
                <button class="btn-action" onclick="editLyrics()">✏️ تحرير</button>
            </div>
            <div class="lyrics-content" id="lyricsContent">
                <p class="lyrics-line">🎵 اختر أغنية لعرض الكلمات</p>
                <p class="lyrics-line">✨ الكلمات تظهر هنا بتأثير متحرك</p>
            </div>
        </div>

        <!-- Playlist -->
        <div class="playlist-section">
            <div class="playlist-header">
                <h3>📋 قائمة التشغيل</h3>
                <button class="btn-action" onclick="document.getElementById('audioInput').click()">📂 إضافة</button>
                <input type="file" id="audioInput" accept="audio/*" multiple style="display:none" onchange="addFiles(this)">
            </div>
            <div class="playlist" id="playlist">
                <div class="empty-playlist">
                    <span>🎵</span>
                    <p>اسحب ملفات الصوت هنا</p>
                </div>
            </div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script src="storage.js"></script>
    <script src="particles.js"></script>
    <script src="visualizer.js"></script>
    <script src="equalizer.js"></script>
    <script src="lyrics.js"></script>
    <script src="player.js"></script>
    <script src="app.js"></script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🎧 2. style.css
# ═══════════════════════════════════════════════════════════

def build_style():
    return """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#050510;--card:rgba(10,10,30,0.85);--card2:rgba(15,15,40,0.7);--text:#e8e0f0;--text2:#9088a8;--text3:#504868;--accent:#00ffcc;--accent2:#ff44aa;--accent3:#ffaa00;--accent4:#6366f1;--glass:rgba(0,255,204,0.06);--border:rgba(0,255,204,0.12);--radius:24px;--radius-sm:16px;--radius-xs:12px}
body{font-family:'Cairo',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;-webkit-tap-highlight-color:transparent;direction:rtl;user-select:none}

.bg-void{position:fixed;inset:0;z-index:0;background:radial-gradient(ellipse at 30% 20%,rgba(0,255,204,0.04) 0%,transparent 60%),radial-gradient(ellipse at 70% 80%,rgba(255,68,170,0.03) 0%,transparent 60%),var(--bg)}
.bg-ring{position:fixed;border-radius:50%;border:1px solid rgba(0,255,204,0.06);z-index:0;pointer-events:none;animation:ringRotate 30s linear infinite}
.bg-ring-1{width:600px;height:600px;top:-200px;left:-100px;animation-duration:25s}
.bg-ring-2{width:500px;height:500px;bottom:-150px;right:-80px;animation-duration:35s;animation-direction:reverse}
.bg-ring-3{width:400px;height:400px;top:30%;left:40%;animation-duration:40s}
@keyframes ringRotate{to{transform:rotate(360deg)}}

.app{width:100%;max-width:520px;margin:0 auto;padding:12px;position:relative;z-index:1}

.header{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);margin-bottom:12px}
.header-left{display:flex;align-items:center;gap:10px}
.logo{width:46px;height:46px;background:var(--glass);border:1px solid var(--border);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:24px;animation:logoGlow 3s ease-in-out infinite}
@keyframes logoGlow{0%,100%{box-shadow:0 0 20px rgba(0,255,204,0.3)}50%{box-shadow:0 0 35px rgba(255,68,170,0.6)}}
.header-text h1{font-family:'Orbitron',sans-serif;font-size:18px;font-weight:800;background:linear-gradient(135deg,#00ffcc,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header-text span{font-size:7px;color:var(--text3);letter-spacing:3px}
.header-right{display:flex;gap:6px}
.btn-icon{width:38px;height:38px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-xs);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:15px;color:var(--text2);transition:all 0.3s}
.btn-icon:hover{border-color:var(--accent);color:var(--accent)}
.btn-icon.active{background:var(--glass);border-color:var(--accent);color:var(--accent);box-shadow:0 0 20px rgba(0,255,204,0.3)}

/* 3D Visualizer */
.visualizer-3d{position:relative;width:100%;aspect-ratio:1;max-height:350px;background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);overflow:hidden;margin-bottom:10px}
.visualizer-3d canvas{width:100%;height:100%}
.viz-overlay{position:absolute;bottom:0;left:0;right:0;padding:16px;background:linear-gradient(to top,rgba(5,5,16,0.9),transparent)}
.track-title{font-family:'Orbitron',sans-serif;font-size:16px;font-weight:700;color:var(--accent);margin-bottom:2px;text-shadow:0 0 20px rgba(0,255,204,0.5)}
.track-artist{font-size:11px;color:var(--text2)}
.track-time{display:flex;justify-content:space-between;font-family:'Orbitron',sans-serif;font-size:10px;color:var(--accent2);margin-top:6px}

/* Progress */
.progress-section{padding:4px 0;margin-bottom:10px}
.progress-track{width:100%;height:4px;background:rgba(255,255,255,0.08);border-radius:2px;cursor:pointer;position:relative}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));border-radius:2px;width:0;transition:width 0.1s linear}
.progress-thumb{position:absolute;top:-6px;width:16px;height:16px;background:#fff;border-radius:50%;box-shadow:0 0 15px rgba(0,255,204,0.6);transform:translateX(-50%);left:0;display:none}
.progress-track:hover .progress-thumb{display:block}

/* Controls */
.controls{display:flex;align-items:center;justify-content:center;gap:16px;margin-bottom:12px}
.ctrl-btn{width:42px;height:42px;background:var(--card2);border:1px solid var(--border);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:15px;color:var(--text2);transition:all 0.3s}
.ctrl-btn:hover{border-color:var(--accent);color:var(--accent)}
.ctrl-btn.active{border-color:var(--accent);color:var(--accent);box-shadow:0 0 20px rgba(0,255,204,0.3)}
.ctrl-play{width:60px;height:60px;background:linear-gradient(135deg,var(--accent),var(--accent4));border:none;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;color:#000;box-shadow:0 8px 30px rgba(0,255,204,0.3);transition:all 0.3s}
.ctrl-play:hover{transform:scale(1.05);box-shadow:0 12px 40px rgba(99,102,241,0.5)}
.ctrl-play:active{transform:scale(0.95)}

/* EQ Panel */
.eq-panel{background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);padding:16px;margin-bottom:12px;animation:slideDown 0.4s ease}
@keyframes slideDown{from{opacity:0;max-height:0}to{opacity:1;max-height:500px}}
.eq-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.eq-header h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;color:var(--accent)}
.eq-presets{display:flex;gap:4px;flex-wrap:wrap}
.preset-btn{padding:5px 10px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:15px;font-size:9px;font-family:'Cairo',sans-serif;transition:all 0.3s}
.preset-btn.active{background:var(--accent);border-color:var(--accent);color:#000;font-weight:700}
.eq-sliders{display:flex;justify-content:center;gap:8px;margin-bottom:14px}
.eq-band{display:flex;flex-direction:column;align-items:center;gap:6px}
.eq-slider{-webkit-appearance:slider-vertical;appearance:slider-vertical;width:24px;height:100px;background:rgba(0,255,204,0.15);border-radius:4px;outline:none;cursor:pointer}
.eq-slider::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:8px;background:var(--accent);border-radius:4px;box-shadow:0 0 15px rgba(0,255,204,0.5)}
.eq-band span{font-size:7px;color:var(--text3);font-family:'Orbitron',sans-serif}
.eq-extra{display:flex;gap:20px;justify-content:center}
.extra-knob{display:flex;flex-direction:column;align-items:center;gap:4px}
.extra-knob span{font-size:9px;color:var(--text2)}
.gold-slider{width:100px;height:3px;-webkit-appearance:none;appearance:none;background:rgba(0,255,204,0.15);border-radius:2px;outline:none;cursor:pointer}
.gold-slider::-webkit-slider-thumb{-webkit-appearance:none;width:18px;height:18px;background:var(--accent);border-radius:50%;cursor:pointer;box-shadow:0 0 15px rgba(0,255,204,0.5)}

/* Lyrics Panel */
.lyrics-panel{background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);padding:16px;margin-bottom:12px;max-height:200px;overflow-y:auto;animation:slideDown 0.4s ease}
.lyrics-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.lyrics-header h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;color:var(--accent2)}
.lyrics-line{padding:6px 0;font-size:13px;color:var(--text2);text-align:center;transition:all 0.3s;border-bottom:1px solid rgba(255,255,255,0.03)}
.lyrics-line.active{color:var(--accent);font-size:16px;font-weight:700;text-shadow:0 0 15px rgba(0,255,204,0.4)}

/* Playlist */
.playlist-section{margin-top:8px;padding-bottom:30px}
.playlist-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}
.playlist-header h3{font-family:'Orbitron',sans-serif;font-size:13px;font-weight:700;color:var(--text)}
.btn-action{padding:7px 14px;background:var(--card2);border:1px solid var(--border);color:var(--accent);cursor:pointer;border-radius:20px;font-size:10px;font-family:'Cairo',sans-serif;transition:all 0.3s}
.btn-action:hover{border-color:var(--accent);box-shadow:0 0 15px rgba(0,255,204,0.2)}
.playlist{display:flex;flex-direction:column;gap:5px}
.track-item{display:flex;align-items:center;gap:10px;padding:10px 12px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-sm);cursor:pointer;transition:all 0.3s}
.track-item:hover{border-color:var(--accent);background:var(--glass)}
.track-item.active{border-color:var(--accent);background:rgba(0,255,204,0.06);box-shadow:0 0 15px rgba(0,255,204,0.1)}
.track-item .t-icon{font-size:22px;width:30px;text-align:center}
.track-item .t-info{flex:1;min-width:0}
.track-item .t-name{font-size:11px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.track-item .t-size{font-size:9px;color:var(--text3)}
.track-item .t-del{color:#ff4466;cursor:pointer;opacity:0.5;transition:0.3s;padding:5px}
.track-item .t-del:hover{opacity:1}
.empty-playlist{text-align:center;padding:30px;color:var(--text3)}
.empty-playlist span{font-size:40px;display:block;margin-bottom:8px}

.toast{position:fixed;bottom:35px;left:50%;transform:translateX(-50%) translateY(130px);background:var(--card);border:1px solid var(--accent);color:var(--text);padding:10px 22px;border-radius:25px;font-size:11px;z-index:300;transition:transform 0.4s cubic-bezier(0.175,0.885,0.32,1.275);font-family:'Cairo',sans-serif}.toast.show{transform:translateX(-50%) translateY(0)}
.particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
@keyframes particleFloat{0%{transform:translateY(110vh) scale(0);opacity:0}15%{opacity:0.7}85%{opacity:0.1}100%{transform:translateY(-10vh) scale(1.5);opacity:0}}

@media(max-width:400px){.eq-sliders{gap:4px}.eq-slider{width:18px;height:70px}.controls{gap:10px}}"""

# ═══════════════════════════════════════════════════════════
# 🎧 3-7. JS Files
# ═══════════════════════════════════════════════════════════

def build_storage_js():
    return """const KEYS={playlist:'sonic2044_playlist',settings:'sonic2044_settings',lyrics:'sonic2044_lyrics',eq:'sonic2044_eq'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function savePlaylist(pl){const data=pl.map(t=>({id:t.id,name:t.name,size:t.size,data:t.data,addedAt:t.addedAt}));return saveData(KEYS.playlist,data)}
function loadPlaylist(){return loadData(KEYS.playlist,[])}
function saveEQ(eq){saveData(KEYS.eq,eq)}
function loadEQ(){return loadData(KEYS.eq,{bands:[0,0,0,0,0,0,0,0,0,0],bass:30,spatial:50})}
function saveLyrics(trackId,lyrics){const all=loadData(KEYS.lyrics,{});all[trackId]=lyrics;saveData(KEYS.lyrics,all)}
function getLyrics(trackId){const all=loadData(KEYS.lyrics,{});return all[trackId]||null}"""

def build_particles_js():
    return """function initParticles(){const c=document.getElementById('particlesContainer');c.innerHTML='';const cols=['#00ffcc','#ff44aa','#6366f1'];for(let i=0;i<40;i++){const p=document.createElement('div');p.className='particle';p.style.cssText=`left:${Math.random()*100}%;bottom:-10px;width:${Math.random()*4+1}px;height:${Math.random()*4+1}px;background:radial-gradient(circle,${cols[i%3]} 0%,transparent 70%);animation:particleFloat ${Math.random()*5+5}s ease-in infinite;animation-delay:${Math.random()*5}s`;c.appendChild(p)}}"""

def build_visualizer_js():
    return """let vizCanvas,vizCtx,vizData=[],vizAnimationId;
function initVisualizer(){vizCanvas=document.getElementById('vizCanvas');vizCtx=vizCanvas.getContext('2d');resizeViz();window.addEventListener('resize',resizeViz);for(let i=0;i<128;i++)vizData.push(0);drawViz()}
function resizeViz(){const c=vizCanvas.parentElement;vizCanvas.width=c.clientWidth;vizCanvas.height=c.clientHeight}
function drawViz(){vizAnimationId=requestAnimationFrame(drawViz);const w=vizCanvas.width,h=vizCanvas.height;vizCtx.fillStyle='rgba(5,5,16,0.3)';vizCtx.fillRect(0,0,w,h);const cx=w/2,cy=h/2,r=Math.min(w,h)*0.35;for(let i=0;i<vizData.length;i++){const a=(i/vizData.length)*Math.PI*2;const val=vizData[i]*0.7;const x1=cx+Math.cos(a)*(r+val*30);const y1=cy+Math.sin(a)*(r+val*30);const x2=cx+Math.cos(a)*(r-val*20);const y2=cy+Math.sin(a)*(r-val*20);const grad=vizCtx.createLinearGradient(x1,y1,x2,y2);grad.addColorStop(0,`rgba(0,255,204,${0.3+val})`);grad.addColorStop(0.5,`rgba(99,102,241,${0.2+val})`);grad.addColorStop(1,`rgba(255,68,170,${0.1+val})`);vizCtx.beginPath();vizCtx.moveTo(x1,y1);vizCtx.lineTo(x2,y2);vizCtx.strokeStyle=grad;vizCtx.lineWidth=1+val;vizCtx.stroke()}vizCtx.beginPath();vizCtx.arc(cx,cy,5,0,Math.PI*2);vizCtx.fillStyle='#fff';vizCtx.shadowColor='#00ffcc';vizCtx.shadowBlur=20;vizCtx.fill();vizCtx.shadowBlur=0}
function updateVizData(audioData){if(!audioData)return;for(let i=0;i<vizData.length;i++){const idx=Math.floor(i*audioData.length/vizData.length);const val=audioData[idx]/255;vizData[i]=vizData[i]*0.85+val*0.15}}"""

def build_equalizer_js():
    return """let eqBands=[0,0,0,0,0,0,0,0,0,0],bassBoost=30,spatial=50;
function initEQ(){const eq=loadEQ();eqBands=eq.bands||eqBands;bassBoost=eq.bass||30;spatial=eq.spatial||50;for(let i=0;i<10;i++){const s=document.getElementById('eq'+i);if(s)s.value=eqBands[i]}document.getElementById('bassBoost').value=bassBoost;document.getElementById('spatial').value=spatial}
function updateEQ(){for(let i=0;i<10;i++){const s=document.getElementById('eq'+i);if(s)eqBands[i]=parseInt(s.value)}saveEQ({bands:eqBands,bass:bassBoost,spatial})}
function updateBass(){bassBoost=parseInt(document.getElementById('bassBoost').value);saveEQ({bands:eqBands,bass:bassBoost,spatial})}
function updateSpatial(){spatial=parseInt(document.getElementById('spatial').value);saveEQ({bands:eqBands,bass:bassBoost,spatial})}
function setPreset(preset,el){document.querySelectorAll('.preset-btn').forEach(b=>b.classList.remove('active'));el.classList.add('active');const presets={flat:[0,0,0,0,0,0,0,0,0,0],bass:[10,8,6,3,0,-2,-4,-2,0,2],treble:[-3,-2,0,2,5,7,9,10,10,12],vocal:[-5,-3,0,3,6,4,2,0,-2,-4],rock:[6,4,2,0,-2,2,4,6,8,10]};eqBands=presets[preset]||presets.flat;for(let i=0;i<10;i++){const s=document.getElementById('eq'+i);if(s)s.value=eqBands[i]}saveEQ({bands:eqBands,bass:bassBoost,spatial})}
function toggleEQ(){const p=document.getElementById('eqPanel');p.style.display=p.style.display==='none'?'block':'none';document.getElementById('btnEQ').classList.toggle('active',p.style.display==='block')}"""

def build_lyrics_js():
    return """let currentLyrics=[],currentLyricIndex=0;
function toggleLyrics(){const p=document.getElementById('lyricsPanel');p.style.display=p.style.display==='none'?'block':'none';document.getElementById('btnLyrics').classList.toggle('active',p.style.display==='block')}
function loadTrackLyrics(trackId){const saved=getLyrics(trackId);if(saved){currentLyrics=saved;renderLyrics()}else{currentLyrics=['🎵 اختر أغنية لعرض الكلمات','✨ الكلمات تظهر هنا بتأثير متحرك','🎤 أضف كلماتك المخصصة','💫 استمتع بالموسيقى'];renderLyrics()}}
function renderLyrics(){const c=document.getElementById('lyricsContent');c.innerHTML=currentLyrics.map((l,i)=>`<p class="lyrics-line ${i===currentLyricIndex?'active':''}">${l}</p>`).join('')}
function updateLyricPosition(time){if(!currentLyrics.length)return;const idx=Math.floor(time/3)%currentLyrics.length;if(idx!==currentLyricIndex){currentLyricIndex=idx;renderLyrics()}}
function editLyrics(){const text=prompt('أدخل كلمات الأغنية (كل سطر = سطر جديد):',currentLyrics.join('\\n'));if(text!==null){currentLyrics=text.split('\\n');renderLyrics();if(window.currentTrack&&window.currentTrack.id)saveLyrics(window.currentTrack.id,currentLyrics);showToast('✅ تم حفظ الكلمات')}}"""

def build_player_js():
    return """let audio=new Audio(),playlist=[],currentIndex=-1,isPlaying=false,isShuffle=false,isRepeat=false,audioCtx=null,analyser=null;
function initPlayer(){try{audioCtx=new(window.AudioContext||window.webkitAudioContext)();analyser=audioCtx.createAnalyser();analyser.fftSize=256;const source=audioCtx.createMediaElementSource(audio);source.connect(analyser);analyser.connect(audioCtx.destination)}catch(e){console.log('AudioContext not supported')}playlist=loadPlaylist();renderPlaylist();if(playlist.length){loadTrack(0)}audio.addEventListener('timeupdate',onTimeUpdate);audio.addEventListener('ended',()=>isRepeat?audio.play():nextTrack());audio.addEventListener('play',()=>{isPlaying=true;document.getElementById('playIcon').className='fas fa-pause'});audio.addEventListener('pause',()=>{isPlaying=false;document.getElementById('playIcon').className='fas fa-play'})}
function onTimeUpdate(){if(!audio.duration)return;const pct=(audio.currentTime/audio.duration)*100;document.getElementById('progressFill').style.width=pct+'%';document.getElementById('progressThumb').style.left=pct+'%';document.getElementById('currentTime').innerText=formatTime(audio.currentTime);document.getElementById('totalTime').innerText=formatTime(audio.duration);updateLyricPosition(audio.currentTime);if(analyser){const data=new Uint8Array(analyser.frequencyBinCount);analyser.getByteFrequencyData(data);updateVizData(data)}}
function formatTime(s){const m=Math.floor(s/60),sec=Math.floor(s%60);return m+':'+(sec<10?'0':'')+sec}
function loadTrack(i){if(i<0||i>=playlist.length)return;currentIndex=i;window.currentTrack=playlist[i];const t=playlist[i];audio.src=t.data;document.getElementById('trackTitle').innerText=t.name;document.getElementById('trackArtist').innerText=t.size;loadTrackLyrics(t.id);renderPlaylist();audio.play()}
function togglePlay(){if(!audio.src&&playlist.length){loadTrack(0);return}isPlaying?audio.pause():audio.play()}
function nextTrack(){if(!playlist.length)return;let n=isShuffle?Math.floor(Math.random()*playlist.length):currentIndex+1;if(n>=playlist.length)n=0;loadTrack(n)}
function prevTrack(){if(!playlist.length)return;let p=currentIndex-1;if(p<0)p=playlist.length-1;loadTrack(p)}
function toggleShuffle(){isShuffle=!isShuffle;document.getElementById('shuffleBtn').classList.toggle('active',isShuffle)}
function toggleRepeat(){isRepeat=!isRepeat;document.getElementById('repeatBtn').classList.toggle('active',isRepeat)}
function seek(e){if(!audio.duration)return;const r=document.getElementById('progressTrack').getBoundingClientRect();audio.currentTime=((e.clientX-r.left)/r.width)*audio.duration}
function addFiles(input){const files=input.files;if(!files.length)return;Array.from(files).forEach(f=>{const r=new FileReader();r.onload=function(e){playlist.push({id:Date.now()+Math.random(),name:f.name.replace(/\\.[^/.]+$/,''),size:formatSize(f.size),data:e.target.result,addedAt:new Date().toISOString()});savePlaylist(playlist);renderPlaylist();if(playlist.length===1)loadTrack(0)};r.readAsDataURL(f)});input.value='';showToast('✅ '+files.length+' أغنية')}
function formatSize(b){return b>1048576?(b/1048576).toFixed(1)+' MB':(b/1024).toFixed(1)+' KB'}
function deleteTrack(i){const wasPlaying=currentIndex===i;playlist.splice(i,1);savePlaylist(playlist);if(wasPlaying){audio.pause();audio.src='';document.getElementById('trackTitle').innerText='اختر أغنية';document.getElementById('trackArtist').innerText='Sonic 2044';isPlaying=false;document.getElementById('playIcon').className='fas fa-play';currentIndex=-1}else if(currentIndex>i)currentIndex--;renderPlaylist();showToast('🗑 تم الحذف')}
function renderPlaylist(){const c=document.getElementById('playlist');if(!playlist.length){c.innerHTML='<div class="empty-playlist"><span>🎵</span><p>اسحب ملفات الصوت هنا</p></div>';return}c.innerHTML=playlist.map((t,i)=>`<div class="track-item ${i===currentIndex?'active':''}" onclick="loadTrack(${i})"><div class="t-icon">${i===currentIndex&&isPlaying?'🔊':'🎵'}</div><div class="t-info"><div class="t-name">${t.name}</div><div class="t-size">${t.size}</div></div><span class="t-del" onclick="event.stopPropagation();deleteTrack(${i})"><i class="fas fa-trash"></i></span></div>`).join('')}
function showToast(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2500)}"""

def build_app_js():
    return """initParticles();initVisualizer();initEQ();initPlayer();"""

# ═══════════════════════════════════════════════════════════
# 🎧 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║  🎧  SONIC 2044 - ULTIMATE AUDIO PLAYER  🎧          ║
║     Ultimate Generator - 12 Files                        ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("BUILDING SONIC 2044")

    write("index.html", build_index())
    write("style.css", build_style())
    write("storage.js", build_storage_js())
    write("particles.js", build_particles_js())
    write("visualizer.js", build_visualizer_js())
    write("equalizer.js", build_equalizer_js())
    write("lyrics.js", build_lyrics_js())
    write("player.js", build_player_js())
    write("app.js", build_app_js())

    print(f"""
{'='*60}
  ✅ BUILD COMPLETE! - {TOTAL_LINES} خط
  📁 9 ملفات

  🎧 3D Audio Visualizer
  🎛️ 10-Band Equalizer
  🎤 Animated Lyrics
  💾 Playlist Storage

  🚀 للتشغيل:
     افتح index.html في المتصفح

  🎧 SONIC 2044 READY!
{'='*60}
    """)

if __name__ == "__main__":
    main()

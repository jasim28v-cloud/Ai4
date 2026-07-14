import os

def create_website_files():
    """Spotify X - Persistent Storage Edition"""
    
    os.makedirs("www", exist_ok=True)
    os.makedirs("www/css", exist_ok=True)
    os.makedirs("www/js", exist_ok=True)
    
    # ==================== CSS ====================
    css_content = r'''/* Spotify X - Styles */
:root {
    --bg: #121212; --surface: #1a1a1a; --surface2: #222222;
    --border: #282828; --green: #1DB954; --green-light: #1ed760;
    --text: #ffffff; --text2: #b3b3b3; --text3: #727272;
    --radius: 8px; --radius-lg: 12px;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: #000; color: var(--text);
    font-family: 'Cairo', sans-serif;
    min-height: 100vh; display: flex; align-items: center; justify-content: center;
    -webkit-tap-highlight-color: transparent; direction: rtl;
}

.app {
    width: 100%; max-width: 440px; height: 100vh; max-height: 860px;
    display: flex; flex-direction: column;
    background: var(--bg); overflow: hidden;
    box-shadow: 0 0 60px rgba(0,0,0,0.8);
}

/* Top Bar */
.topbar { padding: 16px 16px 8px; display: flex; align-items: center; justify-content: space-between; }
.topbar-time { font-size: 11px; color: var(--text2); }
.topbar-icons { display: flex; gap: 12px; font-size: 14px; }

/* Storage Info */
.storage-info {
    padding: 4px 16px; font-size: 8px; color: var(--text3);
    display: flex; align-items: center; gap: 4px;
}
.storage-dot { width: 6px; height: 6px; background: var(--green); border-radius: 50%; }

/* Nav */
.nav-tabs { display: flex; gap: 4px; padding: 8px 16px; }
.nav-tab {
    padding: 8px 18px; border-radius: 20px;
    font-size: 11px; font-weight: 700; cursor: pointer;
    color: var(--text2); background: var(--surface2);
    border: none; font-family: 'Cairo', sans-serif; transition: all 0.3s;
}
.nav-tab.active { background: var(--green); color: #000; }

/* Content */
.content-area { flex: 1; overflow-y: auto; padding: 0 16px; }
.content-area::-webkit-scrollbar { width: 3px; }
.content-area::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
.section { margin-bottom: 20px; }
.section-title { font-size: 14px; font-weight: 800; margin-bottom: 10px; color: var(--text); }

/* Song List */
.song-list { display: flex; flex-direction: column; gap: 4px; }
.song-row {
    display: flex; align-items: center; gap: 12px; padding: 8px;
    border-radius: var(--radius); cursor: pointer; transition: all 0.2s;
}
.song-row:hover { background: var(--surface); }
.song-row.active { background: var(--surface); }
.song-img {
    width: 48px; height: 48px; border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; flex-shrink: 0;
}
.song-info { flex: 1; min-width: 0; }
.song-name { font-size: 12px; font-weight: 700; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.song-name.playing { color: var(--green); }
.song-artist { font-size: 10px; color: var(--text2); }
.song-actions { display: flex; gap: 8px; align-items: center; }
.song-del {
    background: none; border: none; color: #ff4466; cursor: pointer;
    font-size: 14px; opacity: 0.5; transition: 0.3s; padding: 4px;
}
.song-del:hover { opacity: 1; }

/* Now Playing Bar */
.now-playing-bar {
    background: #000; border-top: 1px solid var(--border);
    padding: 8px 12px; display: none; align-items: center; gap: 10px; cursor: pointer;
}
.now-playing-bar.show { display: flex; }
.np-img {
    width: 44px; height: 44px; border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
}
.np-info { flex: 1; min-width: 0; }
.np-name { font-size: 11px; font-weight: 700; color: var(--text); }
.np-name.playing { color: var(--green); }
.np-artist { font-size: 9px; color: var(--text2); }
.np-actions { display: flex; gap: 12px; }
.np-btn { background: none; border: none; color: var(--text); font-size: 18px; cursor: pointer; }
.np-btn.play-btn { font-size: 24px; color: var(--green); }

/* Full Player */
.player-overlay {
    display: none; position: fixed; inset: 0;
    background: var(--bg); z-index: 100; flex-direction: column;
}
.player-overlay.show { display: flex; }
.player-top { padding: 16px; display: flex; align-items: center; justify-content: space-between; }
.player-close { background: none; border: none; color: var(--text); font-size: 24px; cursor: pointer; }
.player-artwork { flex: 1; display: flex; align-items: center; justify-content: center; padding: 20px; }
.player-art {
    width: 260px; height: 260px; border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 80px; box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    animation: discSpin 4s linear infinite paused;
}
.player-art.playing { animation-play-state: running; }
@keyframes discSpin { to { transform: rotate(360deg); } }
.player-info { padding: 20px 24px; }
.player-name { font-size: 20px; font-weight: 800; margin-bottom: 6px; }
.player-artist { font-size: 13px; color: var(--text2); }
.player-progress { padding: 0 24px; }
.progress-bar { width: 100%; height: 4px; background: var(--surface2); border-radius: 2px; cursor: pointer; }
.progress-fill { height: 100%; background: var(--green); border-radius: 2px; width: 0%; }
.progress-time { display: flex; justify-content: space-between; font-size: 10px; color: var(--text2); margin-top: 6px; }
.player-controls { display: flex; align-items: center; justify-content: center; gap: 24px; padding: 16px 24px 24px; }
.player-ctrl { background: none; border: none; color: var(--text); font-size: 20px; cursor: pointer; }
.player-ctrl:active { transform: scale(0.9); }
.player-ctrl.active { color: var(--green); }
.player-ctrl.play-main {
    width: 64px; height: 64px; background: var(--green); border-radius: 50%;
    font-size: 24px; color: #000; display: flex; align-items: center; justify-content: center;
}
.player-extra { display: flex; justify-content: space-between; padding: 0 24px 16px; font-size: 16px; }

/* Upload */
.upload-section { padding: 20px; text-align: center; }
.upload-btn {
    padding: 14px 28px; background: var(--green); color: #000;
    border: none; cursor: pointer; border-radius: 25px;
    font-size: 13px; font-weight: 800; font-family: 'Cairo', sans-serif;
}
.upload-status { font-size: 10px; color: var(--text2); margin-top: 8px; }
input[type="file"] { display: none; }
.empty-state { text-align: center; padding: 30px; color: var(--text3); }
.empty-state .icon { font-size: 40px; display: block; margin-bottom: 8px; }
.toast {
    position: fixed; bottom: 80px; left: 50%;
    transform: translateX(-50%) translateY(120px);
    background: #333; color: #fff; padding: 10px 20px;
    border-radius: 20px; font-size: 10px; font-weight: 600;
    z-index: 300; transition: transform 0.4s; font-family: 'Cairo', sans-serif;
}
.toast.show { transform: translateX(-50%) translateY(0); }
'''

    # ==================== JS ====================
    js_content = r'''// Spotify X - Main Script
let playlist = [];
let favorites = [];
let currentIndex = -1;
let audio = new Audio();
let isPlaying = false, isShuffle = false, isRepeat = false;

// ==================== INDEXEDDB STORAGE ====================
const DB_NAME = 'SpotifyX_DB';
const DB_VERSION = 2;
let db = null;

function openDB() {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open(DB_NAME, DB_VERSION);
        request.onupgradeneeded = function(e) {
            const db = e.target.result;
            if (!db.objectStoreNames.contains('songs')) {
                db.createObjectStore('songs', { keyPath: 'id' });
            }
            if (!db.objectStoreNames.contains('favorites')) {
                db.createObjectStore('favorites', { keyPath: 'id' });
            }
        };
        request.onsuccess = function(e) { db = e.target.result; resolve(db); };
        request.onerror = function(e) { reject(e.target.error); };
    });
}

async function saveSong(song) {
    if (!db) await openDB();
    return new Promise((resolve) => {
        const tx = db.transaction('songs', 'readwrite');
        const store = tx.objectStore('songs');
        store.put(song);
        tx.oncomplete = resolve;
    });
}

async function deleteSongFromDB(id) {
    if (!db) await openDB();
    return new Promise((resolve) => {
        const tx = db.transaction('songs', 'readwrite');
        tx.objectStore('songs').delete(id);
        tx.oncomplete = resolve;
    });
}

async function loadAllSongs() {
    if (!db) await openDB();
    return new Promise((resolve) => {
        const tx = db.transaction('songs', 'readonly');
        const request = tx.objectStore('songs').getAll();
        request.onsuccess = () => resolve(request.result || []);
        request.onerror = () => resolve([]);
    });
}

async function saveFavorites() {
    if (!db) await openDB();
    return new Promise((resolve) => {
        const tx = db.transaction('favorites', 'readwrite');
        const store = tx.objectStore('favorites');
        store.clear();
        favorites.forEach(id => store.put({ id }));
        tx.oncomplete = resolve;
    });
}

async function loadFavorites() {
    if (!db) await openDB();
    return new Promise((resolve) => {
        const tx = db.transaction('favorites', 'readonly');
        const request = tx.objectStore('favorites').getAll();
        request.onsuccess = () => resolve((request.result || []).map(f => f.id));
        request.onerror = () => resolve([]);
    });
}

// ==================== AUDIO EVENTS ====================
audio.addEventListener('timeupdate', updateProgress);
audio.addEventListener('loadedmetadata', () => {
    document.getElementById('totalTime').textContent = formatTime(audio.duration);
});
audio.addEventListener('ended', () => { isRepeat ? audio.play() : nextSong(); });
audio.addEventListener('play', onPlay);
audio.addEventListener('pause', onPause);

function updateProgress() {
    if (audio.duration) {
        document.getElementById('progressFill').style.width = (audio.currentTime/audio.duration*100)+'%';
        document.getElementById('currentTime').textContent = formatTime(audio.currentTime);
    }
}

function onPlay() {
    isPlaying = true;
    document.getElementById('playBtn').textContent = '⏸';
    document.getElementById('miniPlayBtn').textContent = '⏸';
    document.getElementById('playerArt').classList.add('playing');
    updateNowPlayingBar();
    renderAll();
}

function onPause() {
    isPlaying = false;
    document.getElementById('playBtn').textContent = '▶';
    document.getElementById('miniPlayBtn').textContent = '▶';
    document.getElementById('playerArt').classList.remove('playing');
    updateNowPlayingBar();
}

function formatTime(s) { const m=Math.floor(s/60), sec=Math.floor(s%60); return m+':'+(sec<10?'0':'')+sec; }

// ==================== PLAYBACK ====================
function loadSong(index) {
    if (index<0 || index>=playlist.length) return;
    currentIndex = index;
    const s = playlist[index];
    audio.src = s.data;
    audio.play();
    document.getElementById('playerName').textContent = s.name;
    document.getElementById('playerArtist').textContent = s.size;
    document.getElementById('playerArt').textContent = '🎵';
    document.getElementById('playerArt').style.background = 'linear-gradient(135deg, #1DB954, #191414)';
    updateNowPlayingBar();
    updateLikeButton();
    renderAll();
}

function updateNowPlayingBar() {
    const bar = document.getElementById('nowPlayingBar');
    if (currentIndex >= 0 && currentIndex < playlist.length) {
        const s = playlist[currentIndex];
        bar.classList.add('show');
        document.getElementById('npName').textContent = s.name;
        document.getElementById('npName').classList.toggle('playing', isPlaying);
        document.getElementById('npArtist').textContent = s.size;
    } else {
        bar.classList.remove('show');
    }
}

function togglePlay() { 
    if (!audio.src && playlist.length>0) { loadSong(0); return; }
    isPlaying ? audio.pause() : audio.play(); 
}
function nextSong() { if(!playlist.length)return; let n=isShuffle?Math.floor(Math.random()*playlist.length):currentIndex+1; if(n>=playlist.length)n=0; loadSong(n); }
function prevSong() { if(!playlist.length)return; let p=currentIndex-1; if(p<0)p=playlist.length-1; loadSong(p); }
function toggleShuffle() { isShuffle=!isShuffle; document.getElementById('shuffleBtn').classList.toggle('active',isShuffle); }
function toggleRepeat() { isRepeat=!isRepeat; document.getElementById('repeatBtn').classList.toggle('active',isRepeat); }
function seek(e) { if(!audio.duration)return; const r=document.getElementById('progressBar').getBoundingClientRect(); audio.currentTime=((e.clientX-r.left)/r.width)*audio.duration; }

// ==================== FAVORITES ====================
function toggleLike() {
    if (currentIndex<0) return;
    const id = playlist[currentIndex].id;
    favorites = favorites.includes(id) ? favorites.filter(f=>f!==id) : [...favorites, id];
    saveFavorites();
    updateLikeButton();
    renderAll();
}
function updateLikeButton() {
    if (currentIndex<0) return;
    document.getElementById('likeBtn').textContent = favorites.includes(playlist[currentIndex].id) ? '❤️' : '🤍';
}

// ==================== FILES ====================
async function addFiles() {
    const files = document.getElementById('fileInput').files;
    if (!files.length) return;
    
    document.getElementById('uploadStatus').textContent = '⏳ جاري الحفظ...';
    
    for (const f of files) {
        const reader = new FileReader();
        await new Promise(resolve => {
            reader.onload = async function(e) {
                const song = {
                    name: f.name.replace(/\.[^/.]+$/, ""),
                    size: formatSize(f.size),
                    data: e.target.result,
                    id: Date.now() + Math.random()
                };
                playlist.push(song);
                await saveSong(song);
                resolve();
            };
            reader.readAsDataURL(f);
        });
    }
    
    document.getElementById('fileInput').value = '';
    document.getElementById('uploadStatus').textContent = '✅ ' + files.length + ' أغنية محفوظة';
    updateStorageInfo();
    renderAll();
    if (playlist.length === files.length) loadSong(0);
    showToast('✅ الأغاني محفوظة ولن تختفي');
}

function formatSize(b) { return b>1048576?(b/1048576).toFixed(1)+' MB':(b/1024).toFixed(1)+' KB'; }

async function deleteSong(index) {
    const song = playlist[index];
    const wasPlaying = currentIndex === index;
    
    if (wasPlaying) {
        audio.pause();
        audio.src = '';
        currentIndex = -1;
    }
    
    playlist.splice(index, 1);
    await deleteSongFromDB(song.id);
    
    if (wasPlaying) {
        document.getElementById('playerName').textContent = 'اختر أغنية';
        document.getElementById('playerArtist').textContent = '';
        document.getElementById('playBtn').textContent = '▶';
        document.getElementById('miniPlayBtn').textContent = '▶';
        document.getElementById('playerArt').classList.remove('playing');
    } else if (currentIndex > index) {
        currentIndex--;
    }
    
    updateNowPlayingBar();
    updateStorageInfo();
    renderAll();
    showToast('🗑 تم الحذف');
}

function updateStorageInfo() {
    document.getElementById('storageCount').textContent = playlist.length + ' أغنية';
    const totalSize = playlist.reduce((s, song) => {
        return s + (song.data ? song.data.length * 0.75 : 0);
    }, 0);
    document.getElementById('storageSize').textContent = formatSize(totalSize);
}

// ==================== RENDER ====================
function renderAll() {
    const favSongs = playlist.filter(s => favorites.includes(s.id));
    
    document.getElementById('favoritesList').innerHTML = favSongs.length ? favSongs.map(s => {
        const i = playlist.indexOf(s);
        return `<div class="song-row ${i===currentIndex?'active':''}" onclick="loadSong(${i})">
            <div class="song-img" style="background:linear-gradient(135deg,#1DB954,#191414)">❤️</div>
            <div class="song-info"><div class="song-name ${i===currentIndex&&isPlaying?'playing':''}">${s.name}</div><div class="song-artist">${s.size}</div></div>
            <div class="song-actions"><button class="song-del" onclick="event.stopPropagation();deleteSong(${i})">🗑</button></div>
        </div>`;
    }).join('') : '<div class="empty-state"><span class="icon">❤️</span><span>لا توجد مفضلة</span></div>';

    document.getElementById('allSongsList').innerHTML = playlist.length ? playlist.map((s,i) => 
        `<div class="song-row ${i===currentIndex?'active':''}" onclick="loadSong(${i})">
            <div class="song-img" style="background:linear-gradient(135deg,#1DB954,#191414)">🎵</div>
            <div class="song-info"><div class="song-name ${i===currentIndex&&isPlaying?'playing':''}">${s.name}</div><div class="song-artist">${s.size}</div></div>
            <div class="song-actions"><button class="song-del" onclick="event.stopPropagation();deleteSong(${i})">🗑</button></div>
        </div>`
    ).join('') : '<div class="empty-state"><span class="icon">🎵</span><span>لا توجد أغاني</span></div>';

    updateLikeButton();
    updateStorageInfo();
}

// ==================== TABS ====================
function switchTab(tab, btn) {
    document.getElementById('libraryTab').style.display = tab==='library'?'block':'none';
    document.getElementById('uploadTab').style.display = tab==='upload'?'block':'none';
    document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
}

// ==================== PLAYER MODAL ====================
function openPlayer() { document.getElementById('playerOverlay').classList.add('show'); }
function closePlayer() { document.getElementById('playerOverlay').classList.remove('show'); }

function showToast(msg) { const t=document.getElementById('toast'); t.textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),2000); }

// ==================== INIT ====================
async function init() {
    await openDB();
    playlist = await loadAllSongs();
    favorites = await loadFavorites();
    updateStorageInfo();
    renderAll();
    if (playlist.length > 0) {
        updateNowPlayingBar();
    }
}

setInterval(() => {
    document.getElementById('currentTime2').textContent = new Date().toLocaleTimeString('ar-SA', {hour:'2-digit',minute:'2-digit'});
}, 1000);

init();
'''

    # ==================== HTML ====================
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Spotify X</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="app">
        <div class="topbar">
            <span class="topbar-time" id="currentTime2">10:30</span>
            <div class="topbar-icons"><span>📶</span><span>📡</span><span>🔋</span></div>
        </div>
        <div class="storage-info">
            <span class="storage-dot"></span>
            <span id="storageCount">0 أغنية</span>
            <span style="margin:0 8px">•</span>
            <span id="storageSize">0 KB</span>
            <span style="margin-right:auto;color:var(--green)">💾 محفوظة</span>
        </div>

        <div class="nav-tabs">
            <button class="nav-tab active" onclick="switchTab('library', this)">📚 المكتبة</button>
            <button class="nav-tab" onclick="switchTab('upload', this)">📂 رفع</button>
        </div>

        <div class="content-area">
            <div id="libraryTab">
                <div class="section">
                    <div class="section-title">❤️ المفضلة</div>
                    <div class="song-list" id="favoritesList"></div>
                </div>
                <div class="section">
                    <div class="section-title">📋 كل الأغاني</div>
                    <div class="song-list" id="allSongsList"></div>
                </div>
            </div>
            <div id="uploadTab" style="display:none;">
                <div class="upload-section">
                    <button class="upload-btn" onclick="document.getElementById('fileInput').click()">📂 رفع موسيقى</button>
                    <input type="file" id="fileInput" accept="audio/*" multiple onchange="addFiles()">
                    <p class="upload-status" id="uploadStatus">MP3, WAV, OGG, FLAC - سيتم الحفظ تلقائياً</p>
                </div>
            </div>
        </div>

        <div class="now-playing-bar" id="nowPlayingBar" onclick="openPlayer()">
            <div class="np-img">🎵</div>
            <div class="np-info">
                <div class="np-name" id="npName">اختر أغنية</div>
                <div class="np-artist" id="npArtist"></div>
            </div>
            <div class="np-actions">
                <button class="np-btn play-btn" id="miniPlayBtn" onclick="event.stopPropagation();togglePlay()">▶</button>
                <button class="np-btn" onclick="event.stopPropagation();nextSong()">⏭</button>
            </div>
        </div>
    </div>

    <div class="player-overlay" id="playerOverlay">
        <div class="player-top">
            <button class="player-close" onclick="closePlayer()">▼</button>
            <span style="font-size:10px;color:var(--text2)">NOW PLAYING</span>
            <span style="font-size:16px">⋮</span>
        </div>
        <div class="player-artwork">
            <div class="player-art" id="playerArt">🎵</div>
        </div>
        <div class="player-info">
            <div class="player-name" id="playerName">اختر أغنية</div>
            <div class="player-artist" id="playerArtist"></div>
        </div>
        <div class="player-progress">
            <div class="progress-bar" id="progressBar" onclick="seek(event)">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="progress-time">
                <span id="currentTime">0:00</span>
                <span id="totalTime">0:00</span>
            </div>
        </div>
        <div class="player-controls">
            <button class="player-ctrl" id="shuffleBtn" onclick="toggleShuffle()">🔀</button>
            <button class="player-ctrl" onclick="prevSong()">⏮</button>
            <button class="player-ctrl play-main" id="playBtn" onclick="togglePlay()">▶</button>
            <button class="player-ctrl" onclick="nextSong()">⏭</button>
            <button class="player-ctrl" id="repeatBtn" onclick="toggleRepeat()">🔁</button>
        </div>
        <div class="player-extra">
            <span id="likeBtn" onclick="toggleLike()">🤍</span>
            <span>📤</span>
        </div>
    </div>

    <div class="toast" id="toast"></div>
    <script src="js/app.js"></script>
</body>
</html>'''

    # ==================== WRITE FILES ====================
    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    with open("www/css/style.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    
    with open("www/js/app.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    total_size = 0
    for root, dirs, files in os.walk("www"):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))

    print("🟢 Spotify X - Persistent Storage Edition!")
    print(f"📁 www/index.html")
    print(f"📁 www/css/style.css")
    print(f"📁 www/js/app.js")
    print(f"💾 الحجم الإجمالي: {total_size/1024:.1f} KB")
    print("")
    print("✅ المميزات:")
    print("  💾 IndexedDB - الأغاني محفوظة للأبد")
    print("  📂 4 ملفات منفصلة (HTML + CSS + JS)")
    print("  ❤️ مفضلة محفوظة")
    print("  📊 معلومات التخزين")
    print("  🔄 الخروج والعودة = الأغاني موجودة")

if __name__ == "__main__":
    create_website_files()

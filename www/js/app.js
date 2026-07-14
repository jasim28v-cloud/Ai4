// Spotify X - Main Script
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

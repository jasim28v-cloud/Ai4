import os

def create_website_files():
    """Music Player Pro - Ultimate Edition"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Music Player Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #faf8fc; --surface: #ffffff; --border: #eee8f4;
            --purple: #9b59b6; --purple-light: #f8f5fb; --purple-dark: #6c3483;
            --gold: #c9a84c; --red: #e74c3c; --text: #1a1a1a; --text2: #555; --text3: #999;
            --shadow: 0 2px 10px rgba(0,0,0,0.05);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.08);
            --radius: 14px; --radius-lg: 18px; --radius-xl: 24px;
            --transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #f0edf4; color: var(--text);
            font-family: 'Cairo', sans-serif; min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            -webkit-tap-highlight-color: transparent; direction: rtl;
        }

        .app {
            width: 100%; max-width: 480px; height: 100vh; max-height: 900px;
            display: flex; flex-direction: column; background: var(--bg);
            box-shadow: 0 20px 60px rgba(0,0,0,0.12); overflow: hidden;
        }

        .header {
            padding: 12px 16px; background: #fff; border-bottom: 1px solid var(--border);
            display: flex; align-items: center; justify-content: space-between; z-index: 10;
        }
        .brand { display: flex; align-items: center; gap: 10px; }
        .logo-icon {
            width: 40px; height: 40px; background: linear-gradient(135deg, var(--purple), #8e44ad);
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 18px; box-shadow: 0 3px 10px rgba(155,89,182,0.25);
        }
        .brand-text h1 { font-size: 16px; font-weight: 800; }
        .brand-text span { font-size: 8px; color: #999; }

        /* Now Playing */
        .now-playing {
            padding: 20px; text-align: center; background: #fff; border-bottom: 1px solid var(--border);
        }
        .album-art {
            width: 180px; height: 180px; margin: 0 auto 15px;
            background: linear-gradient(135deg, #9b59b6, #6c3483);
            border-radius: var(--radius-xl); display: flex; align-items: center; justify-content: center;
            font-size: 60px; box-shadow: 0 10px 30px rgba(155,89,182,0.3);
            animation: albumFloat 3s ease-in-out infinite;
        }
        @keyframes albumFloat { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)} }

        .song-title { font-size: 17px; font-weight: 800; color: #1a1a1a; margin-bottom: 4px; }
        .song-artist { font-size: 11px; color: #999; font-weight: 600; }

        /* Progress */
        .progress-container { padding: 0 20px 15px; background: #fff; border-bottom: 1px solid var(--border); }
        .progress-bar {
            width: 100%; height: 5px; background: #f0e8f4; border-radius: 3px;
            cursor: pointer; position: relative; margin-bottom: 6px;
        }
        .progress-fill {
            height: 100%; background: linear-gradient(90deg, #9b59b6, #6c3483);
            border-radius: 3px; width: 0%; transition: width 0.1s linear;
            position: relative;
        }
        .progress-thumb {
            position: absolute; right: -8px; top: -5px;
            width: 15px; height: 15px; background: #fff;
            border: 3px solid #9b59b6; border-radius: 50%;
        }
        .time-row { display: flex; justify-content: space-between; font-size: 9px; color: #999; }

        /* Controls */
        .controls-row {
            display: flex; align-items: center; justify-content: center;
            gap: 20px; padding: 12px 20px; background: #fff; border-bottom: 1px solid var(--border);
        }
        .ctrl-btn {
            width: 40px; height: 40px; background: #f8f6fa; border: 1px solid var(--border);
            color: #888; cursor: pointer; border-radius: 50%; font-size: 16px;
            display: flex; align-items: center; justify-content: center; transition: var(--transition);
        }
        .ctrl-btn:hover { background: #f0e8f4; color: var(--purple); }
        .ctrl-btn.active { background: var(--purple-light); border-color: var(--purple); color: var(--purple); }
        .btn-play-main {
            width: 60px; height: 60px; background: linear-gradient(135deg, #9b59b6, #6c3483);
            color: #fff; font-size: 22px; box-shadow: 0 6px 20px rgba(155,89,182,0.4);
        }
        .btn-play-main:hover { transform: scale(1.05); }

        /* Visualizer */
        .visualizer {
            display: flex; align-items: flex-end; justify-content: center;
            gap: 3px; height: 50px; padding: 10px 20px; background: #fff; border-bottom: 1px solid var(--border);
        }
        .vis-bar {
            width: 4px; border-radius: 2px;
            background: linear-gradient(to top, #9b59b6, #c39bd3);
            transition: height 0.1s ease;
            animation: visDance 0.5s ease-in-out infinite alternate;
        }
        @keyframes visDance { from{transform:scaleY(0.3)} to{transform:scaleY(1)} }

        /* Playlist */
        .playlist-header {
            padding: 10px 16px; font-size: 12px; font-weight: 700;
            color: #1a1a1a; display: flex; justify-content: space-between; align-items: center;
        }
        .btn-upload {
            padding: 6px 14px; background: var(--purple-light); border: 1px solid var(--purple);
            color: var(--purple); cursor: pointer; border-radius: 20px;
            font-size: 9px; font-weight: 700; font-family: 'Cairo', sans-serif;
        }
        .playlist {
            flex: 1; overflow-y: auto; padding: 0 12px 10px;
        }
        .playlist::-webkit-scrollbar { width: 3px; }
        .playlist::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        .song-item {
            display: flex; align-items: center; gap: 10px; padding: 10px 12px;
            background: #fff; border: 1px solid var(--border); border-radius: var(--radius);
            margin-bottom: 6px; cursor: pointer; transition: var(--transition);
        }
        .song-item:hover { border-color: #d5c8e0; background: #fdfbff; }
        .song-item.active { border-color: var(--purple); background: var(--purple-light); }
        .song-item .s-icon { font-size: 24px; flex-shrink: 0; }
        .song-item .s-info { flex: 1; min-width: 0; }
        .song-item .s-name { font-size: 11px; font-weight: 700; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .song-item .s-dur { font-size: 9px; color: #999; }
        .song-item .s-del { color: #e74c3c; cursor: pointer; font-size: 16px; opacity: 0.5; transition: 0.3s; }
        .song-item .s-del:hover { opacity: 1; }

        .empty-playlist { text-align: center; padding: 30px; color: #ccc; }
        .empty-playlist .icon { font-size: 40px; display: block; margin-bottom: 8px; }

        input[type="file"] { display: none; }

        .toast {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #1a1a1a; color: #fff; padding: 10px 20px;
            border-radius: 25px; font-size: 10px; font-weight: 600;
            z-index: 300; transition: transform 0.4s; font-family: 'Cairo', sans-serif;
        }
        .toast.show { transform: translateX(-50%) translateY(0); }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <div class="brand">
                <div class="logo-icon">🎵</div>
                <div class="brand-text"><h1>Music Player Pro</h1><span>مشغل صوت احترافي</span></div>
            </div>
        </div>

        <div class="now-playing">
            <div class="album-art" id="albumArt">🎵</div>
            <div class="song-title" id="songTitle">اختر أغنية</div>
            <div class="song-artist" id="songArtist">قائمة التشغيل</div>
        </div>

        <div class="progress-container">
            <div class="progress-bar" id="progressBar" onclick="seek(event)">
                <div class="progress-fill" id="progressFill"><div class="progress-thumb"></div></div>
            </div>
            <div class="time-row">
                <span id="currentTime">0:00</span>
                <span id="totalTime">0:00</span>
            </div>
        </div>

        <div class="controls-row">
            <button class="ctrl-btn" id="shuffleBtn" onclick="toggleShuffle()">🔀</button>
            <button class="ctrl-btn" onclick="prevSong()">⏮</button>
            <button class="ctrl-btn btn-play-main" id="playBtn" onclick="togglePlay()">▶</button>
            <button class="ctrl-btn" onclick="nextSong()">⏭</button>
            <button class="ctrl-btn" id="repeatBtn" onclick="toggleRepeat()">🔁</button>
        </div>

        <div class="visualizer" id="visualizer"></div>

        <div class="playlist-header">
            <span>📋 قائمة التشغيل</span>
            <button class="btn-upload" onclick="document.getElementById('fileInput').click()">📂 رفع ملفات</button>
            <input type="file" id="fileInput" accept="audio/*" multiple onchange="addFiles()">
        </div>

        <div class="playlist" id="playlist">
            <div class="empty-playlist"><span class="icon">🎵</span><span>لا توجد أغاني</span></div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script>
        // ==================== STATE ====================
        let playlist = [];
        let currentIndex = -1;
        let audio = new Audio();
        let isPlaying = false;
        let isShuffle = false;
        let isRepeat = false;

        // ==================== VISUALIZER ====================
        function createVisualizer() {
            const vis = document.getElementById('visualizer');
            vis.innerHTML = '';
            for (let i = 0; i < 30; i++) {
                const bar = document.createElement('div');
                bar.className = 'vis-bar';
                bar.style.height = (Math.random() * 40 + 5) + 'px';
                bar.style.animationDelay = (i * 0.03) + 's';
                vis.appendChild(bar);
            }
        }
        createVisualizer();

        // ==================== AUDIO EVENTS ====================
        audio.addEventListener('timeupdate', () => {
            if (audio.duration) {
                const pct = (audio.currentTime / audio.duration) * 100;
                document.getElementById('progressFill').style.width = pct + '%';
                document.getElementById('currentTime').textContent = formatTime(audio.currentTime);
            }
            updateVisualizer();
        });

        audio.addEventListener('loadedmetadata', () => {
            document.getElementById('totalTime').textContent = formatTime(audio.duration);
        });

        audio.addEventListener('ended', () => {
            if (isRepeat) { audio.play(); return; }
            nextSong();
        });

        audio.addEventListener('play', () => {
            isPlaying = true;
            document.getElementById('playBtn').textContent = '⏸';
        });

        audio.addEventListener('pause', () => {
            isPlaying = false;
            document.getElementById('playBtn').textContent = '▶';
        });

        function updateVisualizer() {
            const bars = document.querySelectorAll('.vis-bar');
            bars.forEach(bar => {
                const h = Math.random() * 40 + 5;
                bar.style.height = h + 'px';
            });
        }

        function formatTime(s) {
            const m = Math.floor(s / 60);
            const sec = Math.floor(s % 60);
            return m + ':' + (sec < 10 ? '0' : '') + sec;
        }

        // ==================== PLAYBACK ====================
        function loadSong(index) {
            if (index < 0 || index >= playlist.length) return;
            currentIndex = index;
            const song = playlist[index];
            audio.src = song.data;
            document.getElementById('songTitle').textContent = song.name;
            document.getElementById('songArtist').textContent = song.size;
            document.getElementById('albumArt').textContent = '🎵';
            document.getElementById('albumArt').style.background = 'linear-gradient(135deg, #9b59b6, #6c3483)';
            renderPlaylist();
            audio.play();
        }

        function togglePlay() {
            if (!audio.src && playlist.length > 0) { loadSong(0); return; }
            if (isPlaying) audio.pause();
            else audio.play();
        }

        function nextSong() {
            if (!playlist.length) return;
            let next = isShuffle ? Math.floor(Math.random() * playlist.length) : currentIndex + 1;
            if (next >= playlist.length) next = 0;
            loadSong(next);
        }

        function prevSong() {
            if (!playlist.length) return;
            let prev = currentIndex - 1;
            if (prev < 0) prev = playlist.length - 1;
            loadSong(prev);
        }

        function toggleShuffle() {
            isShuffle = !isShuffle;
            document.getElementById('shuffleBtn').classList.toggle('active', isShuffle);
            showToast(isShuffle ? '🔀 عشوائي' : '🔀 ترتيب');
        }

        function toggleRepeat() {
            isRepeat = !isRepeat;
            document.getElementById('repeatBtn').classList.toggle('active', isRepeat);
            showToast(isRepeat ? '🔁 تكرار' : '🔁 عادي');
        }

        function seek(e) {
            if (!audio.duration) return;
            const rect = document.getElementById('progressBar').getBoundingClientRect();
            const pct = (e.clientX - rect.left) / rect.width;
            audio.currentTime = pct * audio.duration;
        }

        // ==================== PLAYLIST ====================
        function addFiles() {
            const files = document.getElementById('fileInput').files;
            if (!files.length) return;

            Array.from(files).forEach(file => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    playlist.push({
                        name: file.name.replace(/\.[^/.]+$/, ""),
                        size: formatSize(file.size),
                        data: e.target.result,
                        id: Date.now() + Math.random()
                    });
                    renderPlaylist();
                    if (playlist.length === 1) loadSong(0);
                };
                reader.readAsDataURL(file);
            });
            document.getElementById('fileInput').value = '';
            showToast('✅ ' + files.length + ' أغنية مضافة');
        }

        function formatSize(bytes) {
            return bytes > 1048576 ? (bytes/1048576).toFixed(1) + ' MB' : (bytes/1024).toFixed(1) + ' KB';
        }

        function deleteSong(index) {
            const wasPlaying = currentIndex === index;
            playlist.splice(index, 1);
            if (wasPlaying) {
                audio.pause();
                audio.src = '';
                document.getElementById('songTitle').textContent = 'اختر أغنية';
                document.getElementById('songArtist').textContent = 'قائمة التشغيل';
                currentIndex = -1;
                isPlaying = false;
                document.getElementById('playBtn').textContent = '▶';
            } else if (currentIndex > index) {
                currentIndex--;
            }
            renderPlaylist();
            showToast('🗑 تم الحذف');
        }

        function renderPlaylist() {
            const area = document.getElementById('playlist');
            if (!playlist.length) {
                area.innerHTML = '<div class="empty-playlist"><span class="icon">🎵</span><span>لا توجد أغاني</span></div>';
                return;
            }

            area.innerHTML = playlist.map((s, i) => `
                <div class="song-item ${i === currentIndex ? 'active' : ''}" onclick="loadSong(${i})">
                    <span class="s-icon">${i === currentIndex && isPlaying ? '🔊' : '🎵'}</span>
                    <div class="s-info">
                        <div class="s-name">${s.name}</div>
                        <div class="s-dur">${s.size}</div>
                    </div>
                    <span class="s-del" onclick="event.stopPropagation();deleteSong(${i})">🗑</span>
                </div>
            `).join('');
        }

        function showToast(msg) {
            const t = document.getElementById('toast');
            t.textContent = msg; t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2000);
        }

        // ==================== INIT ====================
        renderPlaylist();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("🎵 Music Player Pro جاهز!")
    print(f"📁 www/index.html - {os.path.getsize('www/index.html')/1024:.1f} KB")

if __name__ == "__main__":
    create_website_files()

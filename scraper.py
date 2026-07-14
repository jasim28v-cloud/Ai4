import os

def create_website_files():
    """Music Player 2044 - Future Edition"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Music Player 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --glass: rgba(255,255,255,0.08);
            --glass-border: rgba(255,255,255,0.15);
            --text: #ffffff;
            --text2: rgba(255,255,255,0.6);
            --accent: #00ffcc;
            --accent2: #ff44aa;
            --accent3: #ffaa00;
            --shadow: 0 8px 32px rgba(0,0,0,0.2);
            --neumorph: 8px 8px 16px rgba(0,0,0,0.3), -4px -4px 12px rgba(255,255,255,0.05);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #0a0a0f;
            font-family: 'Cairo', sans-serif;
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            -webkit-tap-highlight-color: transparent;
            overflow: hidden;
            direction: rtl;
        }

        /* Mesh Gradient Background */
        .bg-mesh {
            position: fixed; inset: 0; z-index: 0;
            background: conic-gradient(from 0deg at 50% 50%, 
                #0a0a2e 0%, #1a0a2e 25%, #0a1a2e 50%, #1a0a0a 75%, #0a0a2e 100%);
            animation: meshRotate 20s linear infinite;
        }
        @keyframes meshRotate { to { filter: hue-rotate(360deg); } }

        .bg-orb {
            position: fixed; border-radius: 50%; filter: blur(80px); opacity: 0.4;
            animation: orbFloat 8s ease-in-out infinite;
        }
        .bg-orb:nth-child(1) { width: 300px; height: 300px; background: #ff44aa; top: -10%; left: -20%; animation-delay: 0s; }
        .bg-orb:nth-child(2) { width: 250px; height: 250px; background: #00ffcc; bottom: -10%; right: -15%; animation-delay: -4s; }
        .bg-orb:nth-child(3) { width: 200px; height: 200px; background: #ffaa00; top: 50%; left: 40%; animation-delay: -2s; }

        @keyframes orbFloat {
            0%, 100% { transform: translate(0, 0) scale(1); }
            33% { transform: translate(30px, -30px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }

        .app {
            width: 100%; max-width: 440px; height: 100vh; max-height: 850px;
            display: flex; flex-direction: column;
            position: relative; z-index: 1; padding: 12px;
        }

        /* ==================== HEADER ==================== */
        .header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 8px 4px; margin-bottom: 8px;
        }
        .header-brand {
            display: flex; align-items: center; gap: 10px;
        }
        .logo {
            width: 44px; height: 44px;
            background: var(--glass); border: 1px solid var(--glass-border);
            border-radius: 16px; display: flex; align-items: center; justify-content: center;
            font-size: 20px; backdrop-filter: blur(20px);
            box-shadow: var(--neumorph);
        }
        .header-text h1 {
            font-size: 18px; font-weight: 800;
            background: linear-gradient(135deg, #00ffcc, #ff44aa);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .header-text span { font-size: 8px; color: var(--text2); letter-spacing: 2px; }

        .btn-glass {
            width: 40px; height: 40px;
            background: var(--glass); border: 1px solid var(--glass-border);
            color: var(--text); cursor: pointer; border-radius: 14px;
            font-size: 16px; display: flex; align-items: center; justify-content: center;
            backdrop-filter: blur(20px); box-shadow: var(--neumorph);
            transition: all 0.3s;
        }
        .btn-glass:active { transform: scale(0.9); box-shadow: inset 4px 4px 8px rgba(0,0,0,0.4); }

        /* ==================== NOW PLAYING ==================== */
        .now-playing {
            text-align: center; padding: 20px 0;
            position: relative;
        }
        .disc-container {
            width: 200px; height: 200px; margin: 0 auto 20px; position: relative;
        }
        .disc-outer-ring {
            position: absolute; inset: -12px;
            border: 2px solid rgba(255,255,255,0.1); border-radius: 50%;
            animation: ringSpin 8s linear infinite;
        }
        .disc-outer-ring:nth-child(2) { inset: -6px; border-style: dashed; animation-duration: 6s; animation-direction: reverse; }
        @keyframes ringSpin { to { transform: rotate(360deg); } }

        .disc {
            width: 100%; height: 100%;
            background: linear-gradient(135deg, rgba(255,68,170,0.3), rgba(0,255,204,0.3));
            border: 2px solid rgba(255,255,255,0.2); border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 70px; backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 0 40px rgba(255,255,255,0.05);
            animation: discSpin 4s linear infinite paused;
        }
        .disc.playing { animation-play-state: running; }
        @keyframes discSpin { to { transform: rotate(360deg); } }

        .disc-center {
            width: 30px; height: 30px; background: #0a0a0f;
            border: 3px solid rgba(255,255,255,0.3); border-radius: 50%;
            position: absolute;
        }

        .song-name {
            font-size: 18px; font-weight: 800; color: var(--text);
            margin-bottom: 4px; text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }
        .song-artist {
            font-size: 11px; color: var(--text2); font-weight: 500;
            letter-spacing: 1px;
        }

        /* ==================== PROGRESS ==================== */
        .progress-section { padding: 0 8px 12px; }
        .progress-track {
            width: 100%; height: 4px;
            background: rgba(255,255,255,0.1); border-radius: 2px;
            cursor: pointer; position: relative;
        }
        .progress-fill {
            height: 100%; background: linear-gradient(90deg, #00ffcc, #ff44aa);
            border-radius: 2px; width: 0%; transition: width 0.1s linear;
            box-shadow: 0 0 10px rgba(0,255,204,0.5);
        }
        .time-row {
            display: flex; justify-content: space-between;
            font-size: 9px; color: var(--text2); margin-top: 6px;
        }

        /* ==================== CONTROLS ==================== */
        .controls-section {
            display: flex; align-items: center; justify-content: center;
            gap: 16px; padding: 8px 0;
        }
        .ctrl-glass {
            width: 44px; height: 44px;
            background: var(--glass); border: 1px solid var(--glass-border);
            color: var(--text); cursor: pointer; border-radius: 16px;
            font-size: 15px; display: flex; align-items: center; justify-content: center;
            backdrop-filter: blur(20px); box-shadow: var(--neumorph);
            transition: all 0.3s;
        }
        .ctrl-glass:active { transform: scale(0.9); box-shadow: inset 4px 4px 8px rgba(0,0,0,0.4); }
        .ctrl-glass.active { border-color: #00ffcc; color: #00ffcc; box-shadow: 0 0 20px rgba(0,255,204,0.3); }

        .btn-play-big {
            width: 64px; height: 64px;
            background: linear-gradient(135deg, #00ffcc, #ff44aa);
            border: none; color: #000; cursor: pointer; border-radius: 20px;
            font-size: 24px; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 10px 30px rgba(0,255,204,0.3), 0 0 40px rgba(255,68,170,0.2);
            transition: all 0.3s;
        }
        .btn-play-big:active { transform: scale(0.9); }

        /* ==================== VISUALIZER ==================== */
        .viz-container {
            display: flex; align-items: center; justify-content: center;
            gap: 4px; height: 60px; padding: 10px 0;
        }
        .viz-ring {
            width: 50px; height: 50px; border-radius: 50%;
            border: 2px solid rgba(255,255,255,0.2);
            position: relative; animation: vizPulse 1s ease-in-out infinite;
        }
        @keyframes vizPulse {
            0%, 100% { transform: scale(0.8); opacity: 0.5; }
            50% { transform: scale(1.2); opacity: 1; }
        }
        .viz-ring:nth-child(1) { animation-delay: 0s; border-color: #ff44aa; }
        .viz-ring:nth-child(2) { animation-delay: 0.2s; border-color: #ffaa00; }
        .viz-ring:nth-child(3) { animation-delay: 0.4s; border-color: #00ffcc; }
        .viz-ring:nth-child(4) { animation-delay: 0.6s; border-color: #ff44aa; }
        .viz-ring:nth-child(5) { animation-delay: 0.8s; border-color: #ffaa00; }

        /* ==================== PLAYLIST ==================== */
        .playlist-header {
            display: flex; justify-content: space-between; align-items: center;
            padding: 8px 4px; margin-top: 4px;
        }
        .playlist-title {
            font-size: 11px; font-weight: 700; color: var(--text);
            letter-spacing: 1px;
        }
        .btn-upload-glass {
            padding: 7px 14px;
            background: var(--glass); border: 1px solid var(--glass-border);
            color: var(--text); cursor: pointer; border-radius: 20px;
            font-size: 9px; font-family: 'Cairo', sans-serif; font-weight: 600;
            backdrop-filter: blur(20px);
        }

        .playlist {
            flex: 1; overflow-y: auto; padding: 0 2px;
        }
        .playlist::-webkit-scrollbar { width: 3px; }
        .playlist::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }

        .song-card {
            display: flex; align-items: center; gap: 10px; padding: 10px 12px;
            background: var(--glass); border: 1px solid var(--glass-border);
            border-radius: 16px; margin-bottom: 6px; cursor: pointer;
            backdrop-filter: blur(20px); transition: all 0.3s;
        }
        .song-card:hover { border-color: rgba(255,255,255,0.3); }
        .song-card.active { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0,255,204,0.2); }
        .song-card .s-icon { font-size: 20px; }
        .song-card .s-info { flex: 1; min-width: 0; }
        .song-card .s-name { font-size: 11px; font-weight: 600; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .song-card .s-dur { font-size: 9px; color: var(--text2); }
        .song-card .s-del { color: #ff4466; cursor: pointer; opacity: 0.5; transition: 0.3s; }
        .song-card .s-del:hover { opacity: 1; }

        .empty-state { text-align: center; padding: 30px; color: rgba(255,255,255,0.2); }
        .empty-state .icon { font-size: 40px; display: block; margin-bottom: 8px; }

        input[type="file"] { display: none; }

        .toast {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: rgba(0,0,0,0.8); backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2); color: #fff;
            padding: 12px 24px; border-radius: 30px; font-size: 10px;
            z-index: 300; transition: transform 0.4s; font-family: 'Cairo', sans-serif;
        }
        .toast.show { transform: translateX(-50%) translateY(0); }
    </style>
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <div class="app">
        <div class="header">
            <div class="header-brand">
                <div class="logo">🎵</div>
                <div class="header-text">
                    <h1>Music 2044</h1>
                    <span>✦ Future Edition ✦</span>
                </div>
            </div>
            <button class="btn-glass">⚡</button>
        </div>

        <div class="now-playing">
            <div class="disc-container">
                <div class="disc-outer-ring"></div>
                <div class="disc-outer-ring"></div>
                <div class="disc" id="disc">
                    <div class="disc-center"></div>
                </div>
            </div>
            <div class="song-name" id="songTitle">اختر أغنية</div>
            <div class="song-artist" id="songArtist">Music Player 2044</div>
        </div>

        <div class="progress-section">
            <div class="progress-track" id="progressTrack" onclick="seek(event)">
                <div class="progress-fill" id="progressFill"></div>
            </div>
            <div class="time-row">
                <span id="currentTime">0:00</span>
                <span id="totalTime">0:00</span>
            </div>
        </div>

        <div class="controls-section">
            <button class="ctrl-glass" id="shuffleBtn" onclick="toggleShuffle()">🔀</button>
            <button class="ctrl-glass" onclick="prevSong()">⏮</button>
            <button class="btn-play-big" id="playBtn" onclick="togglePlay()">▶</button>
            <button class="ctrl-glass" onclick="nextSong()">⏭</button>
            <button class="ctrl-glass" id="repeatBtn" onclick="toggleRepeat()">🔁</button>
        </div>

        <div class="viz-container" id="visualizer">
            <div class="viz-ring"></div><div class="viz-ring"></div><div class="viz-ring"></div>
            <div class="viz-ring"></div><div class="viz-ring"></div>
        </div>

        <div class="playlist-header">
            <span class="playlist-title">📋 قائمة التشغيل</span>
            <button class="btn-upload-glass" onclick="document.getElementById('fileInput').click()">📂 رفع</button>
            <input type="file" id="fileInput" accept="audio/*" multiple onchange="addFiles()">
        </div>

        <div class="playlist" id="playlist">
            <div class="empty-state"><span class="icon">🎵</span><span>اسحب الملفات هنا</span></div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script>
        let playlist = [], currentIndex = -1;
        let audio = new Audio();
        let isPlaying = false, isShuffle = false, isRepeat = false;

        audio.addEventListener('timeupdate', () => {
            if (audio.duration) {
                document.getElementById('progressFill').style.width = (audio.currentTime/audio.duration*100) + '%';
                document.getElementById('currentTime').textContent = formatTime(audio.currentTime);
            }
        });
        audio.addEventListener('loadedmetadata', () => {
            document.getElementById('totalTime').textContent = formatTime(audio.duration);
        });
        audio.addEventListener('ended', () => { isRepeat ? audio.play() : nextSong(); });
        audio.addEventListener('play', () => {
            isPlaying = true;
            document.getElementById('playBtn').textContent = '⏸';
            document.getElementById('disc').classList.add('playing');
        });
        audio.addEventListener('pause', () => {
            isPlaying = false;
            document.getElementById('playBtn').textContent = '▶';
            document.getElementById('disc').classList.remove('playing');
        });

        function formatTime(s) { const m=Math.floor(s/60), sec=Math.floor(s%60); return m+':'+(sec<10?'0':'')+sec; }

        function loadSong(index) {
            if (index<0||index>=playlist.length) return;
            currentIndex=index;
            const s=playlist[index];
            audio.src=s.data;
            document.getElementById('songTitle').textContent=s.name;
            document.getElementById('songArtist').textContent=s.size;
            document.getElementById('disc').style.background='linear-gradient(135deg, rgba(255,68,170,0.3), rgba(0,255,204,0.3))';
            document.getElementById('disc').innerHTML='<div class="disc-center"></div>';
            renderPlaylist();
            audio.play();
        }

        function togglePlay() { if(!audio.src&&playlist.length>0){loadSong(0);return;} isPlaying?audio.pause():audio.play(); }
        function nextSong() { if(!playlist.length)return; let n=isShuffle?Math.floor(Math.random()*playlist.length):currentIndex+1; if(n>=playlist.length)n=0; loadSong(n); }
        function prevSong() { if(!playlist.length)return; let p=currentIndex-1; if(p<0)p=playlist.length-1; loadSong(p); }
        function toggleShuffle() { isShuffle=!isShuffle; document.getElementById('shuffleBtn').classList.toggle('active',isShuffle); showToast(isShuffle?'🔀 عشوائي':'🔀 ترتيب'); }
        function toggleRepeat() { isRepeat=!isRepeat; document.getElementById('repeatBtn').classList.toggle('active',isRepeat); showToast(isRepeat?'🔁 تكرار':'🔁 عادي'); }
        function seek(e) { if(!audio.duration)return; const r=document.getElementById('progressTrack').getBoundingClientRect(); audio.currentTime=((e.clientX-r.left)/r.width)*audio.duration; }

        function addFiles() {
            const files=document.getElementById('fileInput').files;
            if(!files.length)return;
            Array.from(files).forEach(f=>{
                const r=new FileReader();
                r.onload=function(e){
                    playlist.push({name:f.name.replace(/\.[^/.]+$/,""),size:formatSize(f.size),data:e.target.result,id:Date.now()+Math.random()});
                    renderPlaylist();
                    if(playlist.length===1)loadSong(0);
                };
                r.readAsDataURL(f);
            });
            document.getElementById('fileInput').value='';
            showToast('✅ '+files.length+' أغنية');
        }

        function formatSize(b) { return b>1048576?(b/1048576).toFixed(1)+' MB':(b/1024).toFixed(1)+' KB'; }

        function deleteSong(index) {
            const wasPlaying=currentIndex===index;
            playlist.splice(index,1);
            if(wasPlaying){audio.pause();audio.src='';document.getElementById('songTitle').textContent='اختر أغنية';document.getElementById('songArtist').textContent='Music Player 2044';currentIndex=-1;isPlaying=false;document.getElementById('playBtn').textContent='▶';document.getElementById('disc').classList.remove('playing');}
            else if(currentIndex>index)currentIndex--;
            renderPlaylist();
            showToast('🗑 تم الحذف');
        }

        function renderPlaylist() {
            const area=document.getElementById('playlist');
            if(!playlist.length){area.innerHTML='<div class="empty-state"><span class="icon">🎵</span><span>اسحب الملفات هنا</span></div>';return;}
            area.innerHTML=playlist.map((s,i)=>`
                <div class="song-card ${i===currentIndex?'active':''}" onclick="loadSong(${i})">
                    <span class="s-icon">${i===currentIndex&&isPlaying?'🔊':'🎵'}</span>
                    <div class="s-info"><div class="s-name">${s.name}</div><div class="s-dur">${s.size}</div></div>
                    <span class="s-del" onclick="event.stopPropagation();deleteSong(${i})">🗑</span>
                </div>
            `).join('');
        }

        function showToast(msg) { const t=document.getElementById('toast'); t.textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),2000); }

        renderPlaylist();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("🎵 Music Player 2044 - Future Edition جاهز!")
    print(f"📁 www/index.html - {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("🚀 تصميم 2044: Glass Morphism + Mesh Gradient + Neumorphism + Holographic")

if __name__ == "__main__":
    create_website_files()

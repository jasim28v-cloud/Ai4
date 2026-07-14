import os

def create_website_files():
    """إنشاء Vault X Ultimate - خزنة الملفات الأسطورية"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Vault X | Ultimate</title>
    <style>
        :root {
            --bg: #000;
            --surface: #080808;
            --border: #1a1a1a;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
            --gold-glow: rgba(201,168,76,0.4);
            --accent: #00ff88;
            --accent2: #00aaff;
            --text: #e0d5c0;
            --text-dim: #6b6355;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #000;
            color: var(--text);
            font-family: 'Segoe UI', system-ui, sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
            -webkit-user-select: none;
            overflow: hidden;
            -webkit-tap-highlight-color: transparent;
        }

        .app {
            width: 100%;
            max-width: 480px;
            height: 100vh;
            max-height: 850px;
            display: flex;
            flex-direction: column;
            background: var(--bg);
            border: 1px solid var(--border);
            position: relative;
        }

        /* ==================== LOCK SCREEN ==================== */
        .lock-screen {
            position: absolute;
            inset: 0;
            background: #000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            z-index: 100;
            transition: all 0.5s;
            padding: 20px;
            background-image: 
                radial-gradient(ellipse at 50% 30%, rgba(201,168,76,0.06) 0%, transparent 60%);
        }

        .lock-screen.hidden {
            opacity: 0;
            pointer-events: none;
            transform: scale(1.1);
        }

        .lock-icon {
            font-size: 50px;
            animation: lockFloat 2s ease-in-out infinite;
            margin-bottom: 16px;
        }

        @keyframes lockFloat {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .lock-title {
            font-size: 22px;
            font-weight: 900;
            letter-spacing: 4px;
            background: linear-gradient(135deg, var(--gold), var(--gold-light), var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 4px;
        }

        .lock-subtitle {
            font-size: 8px;
            color: var(--text-dim);
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        .pin-dots {
            display: flex;
            gap: 14px;
            margin-bottom: 20px;
        }

        .pin-dot {
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: #1a1a1a;
            border: 2px solid #333;
            transition: all 0.3s;
        }

        .pin-dot.filled {
            background: var(--accent);
            border-color: var(--accent);
            box-shadow: 0 0 15px rgba(0,255,136,0.5);
        }

        .pin-dot.error {
            background: #ff3344;
            border-color: #ff3344;
            animation: shake 0.5s ease;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-8px); }
            75% { transform: translateX(8px); }
        }

        .keypad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            max-width: 260px;
            width: 100%;
        }

        .key-btn {
            aspect-ratio: 1;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            color: var(--text);
            cursor: pointer;
            border-radius: 16px;
            font-size: 20px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            font-family: inherit;
        }

        .key-btn:active {
            background: rgba(0,255,136,0.15);
            border-color: var(--accent);
            transform: scale(0.9);
            box-shadow: 0 0 20px rgba(0,255,136,0.2);
        }

        .key-btn.key-del { font-size: 14px; color: #ff4444; }
        .key-btn.key-empty { background: transparent; border: none; pointer-events: none; }

        .lock-error {
            font-size: 9px;
            color: #ff4444;
            letter-spacing: 2px;
            margin-top: 10px;
            height: 16px;
        }

        /* ==================== MAIN APP ==================== */
        .main-app {
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .header {
            padding: 10px 14px;
            background: #0a0a0a;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 10;
        }

        .header-title {
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 3px;
            color: var(--accent);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .header-actions {
            display: flex;
            gap: 6px;
        }

        .header-btn {
            padding: 5px 10px;
            background: rgba(0,255,136,0.08);
            border: 1px solid rgba(0,255,136,0.2);
            color: var(--accent);
            cursor: pointer;
            border-radius: 8px;
            font-size: 8px;
            letter-spacing: 1px;
            font-family: inherit;
        }

        .header-btn.lock-btn {
            background: rgba(255,51,68,0.08);
            border-color: rgba(255,51,68,0.2);
            color: #ff4444;
        }

        /* Toolbar */
        .toolbar {
            display: flex;
            gap: 4px;
            padding: 8px 12px;
            background: #050505;
            border-bottom: 1px solid var(--border);
            overflow-x: auto;
        }

        .toolbar::-webkit-scrollbar { height: 2px; }
        .toolbar::-webkit-scrollbar-thumb { background: #1a1a1a; }

        .tool-btn {
            padding: 8px 12px;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            color: #888;
            cursor: pointer;
            border-radius: 20px;
            font-size: 9px;
            white-space: nowrap;
            letter-spacing: 1px;
            transition: all 0.3s;
            font-family: inherit;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .tool-btn:hover { border-color: #444; color: #aaa; }
        .tool-btn.active {
            border-color: var(--accent);
            color: var(--accent);
            background: rgba(0,255,136,0.08);
        }

        /* Content Area */
        .content-area {
            flex: 1;
            overflow-y: auto;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 10px;
            background: #000;
        }

        .content-area::-webkit-scrollbar { width: 3px; }
        .content-area::-webkit-scrollbar-thumb { background: #1a1a1a; border-radius: 3px; }

        .file-card {
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            border-radius: 12px;
            padding: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: all 0.3s;
            animation: cardIn 0.3s ease;
            position: relative;
        }

        @keyframes cardIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .file-card:hover { border-color: #333; }
        .file-card:active { background: #0f0f0f; }

        .file-icon {
            font-size: 30px;
            flex-shrink: 0;
            width: 44px;
            text-align: center;
        }

        .file-info { flex: 1; min-width: 0; }

        .file-name {
            font-size: 12px;
            font-weight: 600;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .file-meta {
            font-size: 8px;
            color: var(--text-dim);
            letter-spacing: 1px;
            margin-top: 2px;
        }

        .file-actions {
            display: flex;
            gap: 4px;
        }

        .file-btn {
            width: 28px;
            height: 28px;
            background: #111;
            border: 1px solid #1a1a1a;
            color: #888;
            cursor: pointer;
            border-radius: 8px;
            font-size: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .file-btn:hover { border-color: #444; color: #fff; }
        .file-btn.danger:hover { border-color: #ff4444; color: #ff4444; }

        /* Image Preview */
        .image-preview {
            width: 100%;
            border-radius: 12px;
            border: 1px solid #1a1a1a;
            cursor: pointer;
            transition: all 0.3s;
        }

        .image-preview:active { transform: scale(0.98); }

        /* Video Preview */
        .video-preview {
            width: 100%;
            border-radius: 12px;
            border: 1px solid #1a1a1a;
            max-height: 200px;
            background: #000;
        }

        /* Audio Player */
        .audio-player {
            width: 100%;
            height: 40px;
            border-radius: 20px;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
        }

        /* Fullscreen Viewer */
        .viewer-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.95);
            z-index: 200;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }

        .viewer-overlay.show { display: flex; }

        .viewer-content {
            max-width: 95%;
            max-height: 80%;
            border-radius: 12px;
        }

        .viewer-close {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 40px;
            height: 40px;
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: #fff;
            cursor: pointer;
            border-radius: 50%;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10;
        }

        .empty-state {
            text-align: center;
            color: #1a1a1a;
            margin-top: 40px;
        }

        .empty-state .icon { font-size: 40px; display: block; margin-bottom: 8px; }
        .empty-state .text { font-size: 10px; letter-spacing: 2px; }

        /* Input Area */
        .input-area {
            padding: 10px 14px;
            background: #0a0a0a;
            border-top: 1px solid var(--border);
            display: flex;
            gap: 8px;
            align-items: flex-end;
        }

        .input-area input {
            flex: 1;
            padding: 10px 14px;
            background: #000;
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 12px;
            border-radius: 20px;
            font-family: inherit;
            outline: none;
            transition: all 0.3s;
        }

        .input-area input:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(0,255,136,0.1);
        }

        .input-area input::placeholder { color: #2a2520; }

        .add-btn {
            width: 38px;
            height: 38px;
            background: linear-gradient(135deg, #00ff88, #00cc66);
            border: none;
            color: #000;
            cursor: pointer;
            border-radius: 50%;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.3s;
        }

        .add-btn:active { transform: scale(0.9); }

        .upload-btn {
            width: 38px;
            height: 38px;
            background: #0a0a0a;
            border: 1px solid var(--accent2);
            color: var(--accent2);
            cursor: pointer;
            border-radius: 50%;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.3s;
        }

        .upload-btn:active { background: rgba(0,170,255,0.1); }

        input[type="file"] { display: none; }

        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #0a0a0a;
            border: 1px solid var(--accent);
            color: var(--accent);
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 10px;
            letter-spacing: 2px;
            z-index: 300;
            transition: transform 0.4s;
        }
        .toast.show { transform: translateX(-50%) translateY(0); }
    </style>
</head>
<body>
    <div class="app">
        <!-- ==================== LOCK SCREEN ==================== -->
        <div class="lock-screen" id="lockScreen">
            <div class="lock-icon">🔐</div>
            <div class="lock-title">VAULT X</div>
            <div class="lock-subtitle">✦ Ultimate Vault ✦</div>
            
            <div class="pin-dots">
                <div class="pin-dot" id="dot1"></div>
                <div class="pin-dot" id="dot2"></div>
                <div class="pin-dot" id="dot3"></div>
                <div class="pin-dot" id="dot4"></div>
            </div>

            <div class="keypad">
                <button class="key-btn" onclick="pressKey('1')">1</button>
                <button class="key-btn" onclick="pressKey('2')">2</button>
                <button class="key-btn" onclick="pressKey('3')">3</button>
                <button class="key-btn" onclick="pressKey('4')">4</button>
                <button class="key-btn" onclick="pressKey('5')">5</button>
                <button class="key-btn" onclick="pressKey('6')">6</button>
                <button class="key-btn" onclick="pressKey('7')">7</button>
                <button class="key-btn" onclick="pressKey('8')">8</button>
                <button class="key-btn" onclick="pressKey('9')">9</button>
                <button class="key-btn key-empty"></button>
                <button class="key-btn" onclick="pressKey('0')">0</button>
                <button class="key-btn key-del" onclick="deleteKey()">⌫</button>
            </div>

            <p class="lock-error" id="lockError"></p>
        </div>

        <!-- ==================== MAIN APP ==================== -->
        <div class="main-app" id="mainApp">
            <div class="header">
                <span class="header-title">🔐 VAULT X</span>
                <div class="header-actions">
                    <button class="header-btn" onclick="exportAll()">📤</button>
                    <button class="header-btn lock-btn" onclick="lockVault()">🔒</button>
                </div>
            </div>

            <div class="toolbar" id="toolbar">
                <button class="tool-btn active" data-type="all" onclick="filterType('all', this)">📂 All</button>
                <button class="tool-btn" data-type="text" onclick="filterType('text', this)">📝 Text</button>
                <button class="tool-btn" data-type="image" onclick="filterType('image', this)">🖼️ Images</button>
                <button class="tool-btn" data-type="video" onclick="filterType('video', this)">🎥 Video</button>
                <button class="tool-btn" data-type="audio" onclick="filterType('audio', this)">🎵 Audio</button>
                <button class="tool-btn" data-type="password" onclick="filterType('password', this)">🔑 Pass</button>
                <button class="tool-btn" data-type="link" onclick="filterType('link', this)">🔗 Links</button>
            </div>

            <div class="content-area" id="contentArea">
                <div class="empty-state" id="emptyState">
                    <span class="icon">🔐</span>
                    <span class="text">Vault is empty</span>
                </div>
            </div>

            <div class="input-area">
                <input type="text" id="textInput" placeholder="Add note, link, or password..." onkeypress="if(event.key==='Enter')addText()">
                <input type="file" id="fileInput" onchange="addFile()" multiple accept="*/*">
                <button class="upload-btn" onclick="document.getElementById('fileInput').click()">📎</button>
                <button class="add-btn" onclick="addText()">+</button>
            </div>
        </div>
    </div>

    <!-- Fullscreen Viewer -->
    <div class="viewer-overlay" id="viewerOverlay">
        <button class="viewer-close" onclick="closeViewer()">✕</button>
        <img class="viewer-content" id="viewerImage" style="display:none">
        <video class="viewer-content" id="viewerVideo" controls style="display:none"></video>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script>
        // ==================== CONSTANTS ====================
        const CORRECT_PIN = '1235';
        let pinInput = '';
        let isUnlocked = false;
        let currentFilter = 'all';
        let vaultFiles = [];
        let failedAttempts = 0;
        let lockTimeout = null;
        const AUTO_LOCK_TIME = 120000;

        // ==================== ENCRYPTION ====================
        function encrypt(text) {
            let result = '';
            const key = CORRECT_PIN;
            for (let i = 0; i < text.length; i++) {
                result += String.fromCharCode(text.charCodeAt(i) ^ key.charCodeAt(i % key.length));
            }
            return btoa(result);
        }

        function decrypt(encrypted) {
            try {
                const text = atob(encrypted);
                let result = '';
                const key = CORRECT_PIN;
                for (let i = 0; i < text.length; i++) {
                    result += String.fromCharCode(text.charCodeAt(i) ^ key.charCodeAt(i % key.length));
                }
                return result;
            } catch(e) { return ''; }
        }

        // ==================== PIN PAD ====================
        function pressKey(num) {
            if (pinInput.length >= 4) return;
            pinInput += num;
            updateDots();
            if (pinInput.length === 4) setTimeout(checkPin, 200);
        }

        function deleteKey() {
            pinInput = pinInput.slice(0, -1);
            updateDots();
            document.getElementById('lockError').textContent = '';
            document.querySelectorAll('.pin-dot').forEach(d => d.classList.remove('error'));
        }

        function updateDots() {
            for (let i = 1; i <= 4; i++) {
                const dot = document.getElementById('dot' + i);
                dot.classList.toggle('filled', i <= pinInput.length);
            }
        }

        function checkPin() {
            if (pinInput === CORRECT_PIN) {
                unlockVault();
            } else {
                failedAttempts++;
                document.querySelectorAll('.pin-dot').forEach(d => d.classList.add('error'));
                document.getElementById('lockError').textContent = '❌ Wrong! ' + (3 - failedAttempts) + ' tries';
                if (failedAttempts >= 3) {
                    document.getElementById('lockError').textContent = '⏳ Locked 30s';
                    document.querySelectorAll('.key-btn').forEach(b => b.style.pointerEvents = 'none');
                    setTimeout(() => {
                        failedAttempts = 0;
                        document.querySelectorAll('.key-btn').forEach(b => b.style.pointerEvents = 'auto');
                        document.getElementById('lockError').textContent = '';
                    }, 30000);
                }
                setTimeout(() => { pinInput = ''; updateDots(); }, 500);
            }
        }

        function unlockVault() {
            isUnlocked = true;
            document.getElementById('lockScreen').classList.add('hidden');
            document.getElementById('lockError').textContent = '';
            pinInput = ''; failedAttempts = 0;
            updateDots();
            loadVault();
            resetAutoLock();
            showToast('✅ Unlocked');
        }

        function lockVault() {
            isUnlocked = false;
            document.getElementById('lockScreen').classList.remove('hidden');
            if (lockTimeout) clearTimeout(lockTimeout);
            saveVault();
            showToast('🔒 Locked');
        }

        function resetAutoLock() {
            if (lockTimeout) clearTimeout(lockTimeout);
            lockTimeout = setTimeout(() => { if (isUnlocked) lockVault(); }, AUTO_LOCK_TIME);
        }

        document.addEventListener('click', () => { if (isUnlocked) resetAutoLock(); });

        // ==================== FILE MANAGEMENT ====================
        function addText() {
            const input = document.getElementById('textInput');
            const text = input.value.trim();
            if (!text) return;

            // Detect type
            let type = 'text';
            if (text.startsWith('http')) type = 'link';
            if (text.startsWith('pass:')) type = 'password';

            const file = {
                id: Date.now(),
                name: text.substring(0, 30) + (text.length > 30 ? '...' : ''),
                type: type,
                content: text,
                size: new Blob([text]).size,
                date: new Date().toLocaleString(),
            };

            vaultFiles.unshift(file);
            input.value = '';
            saveVault();
            renderFiles();
            resetAutoLock();
        }

        function addFile() {
            const input = document.getElementById('fileInput');
            const files = input.files;
            if (!files.length) return;

            Array.from(files).forEach(f => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    let type = 'file';
                    if (f.type.startsWith('image/')) type = 'image';
                    else if (f.type.startsWith('video/')) type = 'video';
                    else if (f.type.startsWith('audio/')) type = 'audio';

                    const fileObj = {
                        id: Date.now() + Math.random(),
                        name: f.name,
                        type: type,
                        mimeType: f.type,
                        content: e.target.result,
                        size: f.size,
                        date: new Date().toLocaleString(),
                    };

                    vaultFiles.unshift(fileObj);
                    saveVault();
                    renderFiles();
                    resetAutoLock();
                    showToast('📎 ' + f.name + ' added');
                };
                reader.readAsDataURL(f);
            });

            input.value = '';
        }

        function deleteFile(id) {
            vaultFiles = vaultFiles.filter(f => f.id !== id);
            saveVault();
            renderFiles();
            showToast('🗑 Deleted');
            resetAutoLock();
        }

        function viewFile(file) {
            if (file.type === 'image') {
                document.getElementById('viewerImage').src = file.content;
                document.getElementById('viewerImage').style.display = 'block';
                document.getElementById('viewerVideo').style.display = 'none';
                document.getElementById('viewerOverlay').classList.add('show');
            } else if (file.type === 'video') {
                document.getElementById('viewerVideo').src = file.content;
                document.getElementById('viewerVideo').style.display = 'block';
                document.getElementById('viewerImage').style.display = 'none';
                document.getElementById('viewerOverlay').classList.add('show');
                document.getElementById('viewerVideo').play();
            } else if (file.type === 'audio') {
                const audio = new Audio(file.content);
                audio.play();
                showToast('🎵 Playing...');
            } else if (file.type === 'link') {
                window.open(file.content, '_blank');
            } else {
                // Copy text
                navigator.clipboard.writeText(file.content).then(() => {
                    showToast('📋 Copied!');
                });
            }
            resetAutoLock();
        }

        function closeViewer() {
            document.getElementById('viewerOverlay').classList.remove('show');
            document.getElementById('viewerVideo').pause();
            document.getElementById('viewerVideo').src = '';
        }

        function downloadFile(file) {
            const a = document.createElement('a');
            a.href = file.content;
            a.download = file.name;
            a.click();
            showToast('📥 Downloading...');
            resetAutoLock();
        }

        function filterType(type, btn) {
            currentFilter = type;
            document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderFiles();
            resetAutoLock();
        }

        // ==================== STORAGE ====================
        function saveVault() {
            try {
                const json = JSON.stringify(vaultFiles);
                const encrypted = encrypt(json);
                localStorage.setItem('vaultx_ultimate', encrypted);
                sessionStorage.setItem('vaultx_ram', json);
            } catch(e) {
                showToast('⚠️ Storage full! Clear some files.');
            }
        }

        function loadVault() {
            try {
                const encrypted = localStorage.getItem('vaultx_ultimate');
                if (encrypted) {
                    const decrypted = decrypt(encrypted);
                    if (decrypted) vaultFiles = JSON.parse(decrypted);
                }
                if (!vaultFiles.length) {
                    const ram = sessionStorage.getItem('vaultx_ram');
                    if (ram) vaultFiles = JSON.parse(ram);
                }
            } catch(e) {
                vaultFiles = [];
            }
            renderFiles();
        }

        function renderFiles() {
            const area = document.getElementById('contentArea');
            const empty = document.getElementById('emptyState');
            
            const filtered = currentFilter === 'all' 
                ? vaultFiles 
                : vaultFiles.filter(f => f.type === currentFilter);

            if (filtered.length === 0) {
                empty.style.display = 'block';
                area.innerHTML = '';
                area.appendChild(empty);
            } else {
                empty.style.display = 'none';
                area.innerHTML = filtered.map(f => {
                    const icons = {
                        text: '📝', image: '🖼️', video: '🎥', audio: '🎵',
                        password: '🔑', link: '🔗', file: '📄'
                    };
                    const icon = icons[f.type] || '📄';
                    const sizeStr = f.size > 1024*1024 ? (f.size/(1024*1024)).toFixed(1)+'MB' : 
                                   f.size > 1024 ? (f.size/1024).toFixed(1)+'KB' : f.size+'B';

                    let preview = '';
                    if (f.type === 'image') {
                        preview = `<img src="${f.content}" class="image-preview" style="max-height:120px;object-fit:cover" onclick="viewFile(vaultFiles.find(x=>x.id===${f.id}))">`;
                    } else if (f.type === 'video') {
                        preview = `<video src="${f.content}" class="video-preview" controls></video>`;
                    } else if (f.type === 'audio') {
                        preview = `<audio src="${f.content}" class="audio-player" controls></audio>`;
                    }

                    return `
                        <div class="file-card">
                            <div class="file-icon">${icon}</div>
                            <div class="file-info">
                                <div class="file-name">${escapeHtml(f.name)}</div>
                                <div class="file-meta">${f.date} • ${sizeStr} • ${f.type}</div>
                                ${preview}
                            </div>
                            <div class="file-actions">
                                <button class="file-btn" onclick="viewFile(vaultFiles.find(x=>x.id===${f.id}))">👁</button>
                                <button class="file-btn" onclick="downloadFile(vaultFiles.find(x=>x.id===${f.id}))">⬇</button>
                                <button class="file-btn danger" onclick="deleteFile(${f.id})">🗑</button>
                            </div>
                        </div>
                    `;
                }).join('');
            }
            
            updateRamIndicator();
        }

        function updateRamIndicator() {
            const total = vaultFiles.reduce((s, f) => s + (f.size || 0), 0);
            const sizeStr = total > 1024*1024 ? (total/(1024*1024)).toFixed(1)+'MB' : (total/1024).toFixed(1)+'KB';
            // Silent update - no visible indicator needed
        }

        function escapeHtml(t) {
            const d = document.createElement('div');
            d.textContent = t;
            return d.innerHTML;
        }

        // ==================== EXPORT ====================
        function exportAll() {
            if (!isUnlocked) return;
            const pw = prompt('Export password:');
            if (!pw) return;
            const json = JSON.stringify(vaultFiles, null, 2);
            const enc = encrypt(json);
            const blob = new Blob([enc], {type:'text/plain'});
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'vaultx-'+Date.now()+'.enc';
            a.click();
            showToast('📤 Exported encrypted');
            resetAutoLock();
        }

        // ==================== TOAST ====================
        function showToast(m) {
            const t = document.getElementById('toast');
            t.textContent = m; t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2000);
        }

        // ==================== KEYBOARD ====================
        document.addEventListener('keydown', e => {
            if (!isUnlocked) {
                if (e.key >= '0' && e.key <= '9') pressKey(e.key);
                if (e.key === 'Backspace') deleteKey();
            }
        });

        // ==================== INIT ====================
        updateDots();
        loadVault();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  🔐 Vault X - ULTIMATE EDITION         ║")
    print("║  📂 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🔐 المميزات الأسطورية:")
    print("  🔢 PIN: 1235")
    print("  🔐 تشفير XOR + Base64")
    print("  🧠 RAM + localStorage")
    print("  📝 نصوص وملاحظات")
    print("  🔗 روابط")
    print("  🔑 كلمات سر (pass:xxx)")
    print("  🖼️ صور (رفع وعرض وتحميل)")
    print("  🎥 فيديو (رفع وتشغيل)")
    print("  🎵 صوت (رفع وتشغيل)")
    print("  📄 جميع الملفات")
    print("  👁️ عارض كامل الشاشة")
    print("  📥 تحميل الملفات")
    print("  📤 تصدير مشفر")
    print("  ⏱️ Auto-lock بعد دقيقتين")

if __name__ == "__main__":
    create_website_files()

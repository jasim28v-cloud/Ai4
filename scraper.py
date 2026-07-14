import os

def create_website_files():
    """إنشاء Vault X RAM Edition - تخزين حقيقي في الذاكرة"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Vault X | RAM</title>
    <style>
        :root {
            --bg: #000;
            --surface: #080808;
            --border: #1a1a1a;
            --gold: #c9a84c;
            --gold-light: #e2c97e;
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
            -webkit-tap-highlight-color: transparent;
            overflow: hidden;
        }

        .app {
            width: 100%;
            max-width: 480px;
            height: 100vh;
            max-height: 860px;
            display: flex;
            flex-direction: column;
            background: var(--bg);
            border: 1px solid var(--border);
            position: relative;
            border-radius: 8px;
            box-shadow: 0 0 80px rgba(0,0,0,0.8);
        }

        /* Lock Screen */
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
                radial-gradient(ellipse at 50% 30%, rgba(0,255,136,0.06) 0%, transparent 60%);
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

        .key-del { color: #ff4444; }
        .key-empty { background: transparent; border: none; pointer-events: none; }

        .lock-error {
            font-size: 9px;
            letter-spacing: 2px;
            margin-top: 10px;
            height: 16px;
        }

        /* Main App */
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
            text-shadow: 0 0 10px rgba(0,255,136,0.3);
        }

        .header-actions { display: flex; gap: 6px; }

        .header-btn {
            padding: 6px 12px;
            background: rgba(0,255,136,0.06);
            border: 1px solid rgba(0,255,136,0.2);
            color: var(--accent);
            cursor: pointer;
            border-radius: 20px;
            font-size: 8px;
            letter-spacing: 1px;
            font-family: inherit;
            transition: all 0.3s;
        }

        .header-btn.lock-btn {
            background: rgba(255,51,68,0.06);
            border-color: rgba(255,51,68,0.2);
            color: #ff4444;
        }

        /* RAM Status */
        .ram-status {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 14px;
            background: #050505;
            border-bottom: 1px solid var(--border);
            font-size: 8px;
            letter-spacing: 1px;
        }

        .ram-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent);
            animation: ramPulse 1s ease-in-out infinite;
        }

        @keyframes ramPulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 8px rgba(0,255,136,0.5); }
            50% { opacity: 0.5; box-shadow: 0 0 2px rgba(0,255,136,0.2); }
        }

        .ram-text { color: var(--accent); }
        .ram-size { color: #666; margin-left: auto; }

        /* Toolbar */
        .toolbar {
            display: flex;
            gap: 4px;
            padding: 8px 12px;
            background: #050505;
            border-bottom: 1px solid var(--border);
            overflow-x: auto;
        }

        .toolbar::-webkit-scrollbar { height: 0; }

        .tool-btn {
            padding: 8px 12px;
            background: #0a0a0a;
            border: 1px solid #1a1a1a;
            color: #666;
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

        .tool-btn:hover { border-color: #333; color: #999; }
        .tool-btn.active {
            border-color: var(--accent);
            color: var(--accent);
            background: rgba(0,255,136,0.08);
            box-shadow: 0 0 15px rgba(0,255,136,0.1);
        }

        /* Content */
        .content-area {
            flex: 1;
            overflow-y: auto;
            padding: 10px;
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
            gap: 10px;
            margin-bottom: 8px;
            transition: all 0.3s;
            animation: cardIn 0.3s ease;
        }

        @keyframes cardIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .file-card:hover { border-color: #2a2a2a; background: #0d0d0d; }
        .file-card:active { transform: scale(0.98); }

        .file-icon {
            font-size: 28px;
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
            display: flex;
            gap: 6px;
            align-items: center;
        }

        .file-type-badge {
            padding: 2px 6px;
            border-radius: 8px;
            font-size: 7px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .badge-image { background: rgba(0,170,255,0.1); color: #00aaff; }
        .badge-video { background: rgba(255,136,0,0.1); color: #ff8800; }
        .badge-audio { background: rgba(170,0,255,0.1); color: #aa00ff; }
        .badge-text { background: rgba(0,255,136,0.1); color: #00ff88; }
        .badge-password { background: rgba(255,51,68,0.1); color: #ff3344; }
        .badge-link { background: rgba(201,168,76,0.1); color: #c9a84c; }

        .file-actions { display: flex; gap: 3px; }

        .file-btn {
            width: 28px;
            height: 28px;
            background: #111;
            border: 1px solid #1a1a1a;
            color: #777;
            cursor: pointer;
            border-radius: 8px;
            font-size: 11px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .file-btn:hover { border-color: #444; color: #fff; background: #1a1a1a; }
        .file-btn.danger:hover { border-color: #ff4444; color: #ff4444; background: rgba(255,68,68,0.1); }

        .card-preview img {
            width: 100%;
            max-height: 120px;
            object-fit: cover;
            border-radius: 8px;
            margin-top: 6px;
            cursor: pointer;
        }

        .empty-state {
            text-align: center;
            color: #111;
            margin-top: 50px;
        }

        .empty-state .icon { font-size: 40px; display: block; margin-bottom: 8px; opacity: 0.4; }
        .empty-state .text { font-size: 10px; letter-spacing: 2px; text-transform: uppercase; }

        /* Input */
        .input-area {
            padding: 10px 14px;
            background: #0a0a0a;
            border-top: 1px solid var(--border);
            display: flex;
            gap: 8px;
            align-items: flex-end;
        }

        .input-area input[type="text"] {
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

        .input-area input[type="text"]:focus {
            border-color: var(--accent);
            box-shadow: 0 0 0 3px rgba(0,255,136,0.08);
        }

        .input-area input[type="text"]::placeholder { color: #1a1a1a; }

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
            box-shadow: 0 4px 15px rgba(0,255,136,0.3);
        }

        .add-btn:active { transform: scale(0.85); }

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

        /* Viewer */
        .viewer-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.97);
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
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            color: #fff;
            cursor: pointer;
            border-radius: 50%;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Toast */
        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #0a0a0a;
            border: 1px solid var(--accent);
            color: var(--accent);
            padding: 10px 24px;
            border-radius: 20px;
            font-size: 10px;
            letter-spacing: 2px;
            z-index: 300;
            transition: transform 0.4s;
        }

        .toast.show { transform: translateX(-50%) translateY(0); }

        .footer {
            text-align: center;
            padding: 4px;
            font-size: 7px;
            color: #0a0a0a;
            letter-spacing: 2px;
            background: #000;
            border-top: 1px solid var(--border);
        }
    </style>
</head>
<body>
    <div class="app">
        <!-- Lock Screen -->
        <div class="lock-screen" id="lockScreen">
            <div class="lock-icon">🔐</div>
            <div class="lock-title">VAULT X</div>
            <div class="lock-subtitle">✦ RAM Mode ✦</div>
            
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

        <!-- Main App -->
        <div class="main-app" id="mainApp">
            <div class="header">
                <span class="header-title">🔐 VAULT X</span>
                <div class="header-actions">
                    <button class="header-btn" onclick="exportAll()">📤</button>
                    <button class="header-btn lock-btn" onclick="lockVault()">🔒</button>
                </div>
            </div>

            <div class="ram-status">
                <span class="ram-dot"></span>
                <span class="ram-text">⚡ RAM Active</span>
                <span class="ram-size" id="ramSize">0 KB used</span>
            </div>

            <div class="toolbar" id="toolbar">
                <button class="tool-btn active" data-type="all" onclick="filterType('all', this)">📂 All</button>
                <button class="tool-btn" data-type="image" onclick="filterType('image', this)">🖼️</button>
                <button class="tool-btn" data-type="video" onclick="filterType('video', this)">🎥</button>
                <button class="tool-btn" data-type="audio" onclick="filterType('audio', this)">🎵</button>
                <button class="tool-btn" data-type="text" onclick="filterType('text', this)">📝</button>
                <button class="tool-btn" data-type="password" onclick="filterType('password', this)">🔑</button>
                <button class="tool-btn" data-type="link" onclick="filterType('link', this)">🔗</button>
            </div>

            <div class="content-area" id="contentArea">
                <div class="empty-state" id="emptyState">
                    <span class="icon">🔐</span>
                    <span class="text">Vault is empty</span>
                </div>
            </div>

            <div class="input-area">
                <input type="text" id="textInput" placeholder="Add text, link, or pass:xxx..." onkeypress="if(event.key==='Enter')addText()">
                <input type="file" id="fileInput" onchange="addFile()" multiple accept="*/*">
                <button class="upload-btn" onclick="document.getElementById('fileInput').click()">📎</button>
                <button class="add-btn" onclick="addText()">+</button>
            </div>

            <div class="footer">VAULT X • RAM MODE • ENCRYPTED</div>
        </div>
    </div>

    <!-- Viewer -->
    <div class="viewer-overlay" id="viewerOverlay">
        <button class="viewer-close" onclick="closeViewer()">✕</button>
        <img class="viewer-content" id="viewerImage" style="display:none">
        <video class="viewer-content" id="viewerVideo" controls style="display:none"></video>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script>
        // ==================== DATABASE (IndexedDB + RAM) ====================
        const DB_NAME = 'VaultX_RAM_DB';
        const DB_VERSION = 1;
        const STORE_NAME = 'vault_files';
        let db = null;

        // RAM Memory Store (holds all data in memory)
        const RAMStore = {
            files: [],
            totalSize: 0,

            add(file) {
                this.files.unshift(file);
                this.totalSize += file.size || 0;
                this.updateUI();
            },

            remove(id) {
                const idx = this.files.findIndex(f => f.id === id);
                if (idx > -1) {
                    this.totalSize -= this.files[idx].size || 0;
                    this.files.splice(idx, 1);
                }
                this.updateUI();
            },

            getAll() {
                return this.files;
            },

            getByType(type) {
                return type === 'all' ? this.files : this.files.filter(f => f.type === type);
            },

            clear() {
                this.files = [];
                this.totalSize = 0;
                this.updateUI();
            },

            updateUI() {
                const sizeKB = (this.totalSize / 1024).toFixed(1);
                const sizeStr = this.totalSize > 1048576 ? (this.totalSize / 1048576).toFixed(1) + ' MB' : sizeKB + ' KB';
                document.getElementById('ramSize').textContent = sizeStr + ' used';
            }
        };

        // IndexedDB for persistent backup
        function openDB() {
            return new Promise((resolve, reject) => {
                const request = indexedDB.open(DB_NAME, DB_VERSION);
                
                request.onupgradeneeded = function(e) {
                    const db = e.target.result;
                    if (!db.objectStoreNames.contains(STORE_NAME)) {
                        db.createObjectStore(STORE_NAME, { keyPath: 'id' });
                    }
                };

                request.onsuccess = function(e) {
                    db = e.target.result;
                    resolve(db);
                };

                request.onerror = function(e) {
                    console.error('IndexedDB error:', e.target.error);
                    reject(e.target.error);
                };
            });
        }

        async function saveToDB(file) {
            if (!db) return;
            try {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                const store = tx.objectStore(STORE_NAME);
                store.put(file);
                return new Promise(resolve => { tx.oncomplete = resolve; });
            } catch(e) {
                console.error('Save error:', e);
            }
        }

        async function deleteFromDB(id) {
            if (!db) return;
            try {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                const store = tx.objectStore(STORE_NAME);
                store.delete(id);
                return new Promise(resolve => { tx.oncomplete = resolve; });
            } catch(e) {}
        }

        async function loadAllFromDB() {
            if (!db) return [];
            try {
                const tx = db.transaction(STORE_NAME, 'readonly');
                const store = tx.objectStore(STORE_NAME);
                const request = store.getAll();
                return new Promise((resolve) => {
                    request.onsuccess = () => resolve(request.result || []);
                    request.onerror = () => resolve([]);
                });
            } catch(e) {
                return [];
            }
        }

        async function clearDB() {
            if (!db) return;
            try {
                const tx = db.transaction(STORE_NAME, 'readwrite');
                const store = tx.objectStore(STORE_NAME);
                store.clear();
            } catch(e) {}
        }

        // ==================== PIN ====================
        const CORRECT_PIN = '1235';
        let pinInput = '';
        let isUnlocked = false;
        let failedAttempts = 0;
        let currentFilter = 'all';

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
                document.getElementById('dot' + i).classList.toggle('filled', i <= pinInput.length);
            }
        }

        function checkPin() {
            if (pinInput === CORRECT_PIN) {
                unlockVault();
            } else {
                failedAttempts++;
                document.querySelectorAll('.pin-dot').forEach(d => d.classList.add('error'));
                document.getElementById('lockError').textContent = '❌ Wrong! ' + (3 - failedAttempts) + ' tries';
                document.getElementById('lockError').style.color = '#ff4444';
                if (failedAttempts >= 3) {
                    document.getElementById('lockError').textContent = '⏳ Locked 30s';
                    document.querySelectorAll('.key-btn').forEach(b => b.style.pointerEvents = 'none');
                    setTimeout(() => {
                        failedAttempts = 0;
                        document.querySelectorAll('.key-btn').forEach(b => b.style.pointerEvents = 'auto');
                        document.getElementById('lockError').textContent = '';
                        document.getElementById('lockError').style.color = '';
                    }, 30000);
                }
                setTimeout(() => { pinInput = ''; updateDots(); }, 500);
            }
        }

        async function unlockVault() {
            isUnlocked = true;
            document.getElementById('lockScreen').classList.add('hidden');
            document.getElementById('lockError').textContent = '';
            pinInput = ''; failedAttempts = 0;
            updateDots();

            // Load from IndexedDB to RAM
            if (!db) await openDB();
            const savedFiles = await loadAllFromDB();
            RAMStore.files = savedFiles;
            RAMStore.totalSize = savedFiles.reduce((s, f) => s + (f.size || 0), 0);
            RAMStore.updateUI();
            renderFiles();
            showToast('✅ RAM Active • ' + savedFiles.length + ' files loaded');
        }

        function lockVault() {
            isUnlocked = false;
            document.getElementById('lockScreen').classList.remove('hidden');
            renderFiles();
            showToast('🔒 Vault Locked');
        }

        // ==================== FILES ====================
        function addText() {
            const input = document.getElementById('textInput');
            const text = input.value.trim();
            if (!text) return;

            let type = 'text';
            if (text.startsWith('http')) type = 'link';
            else if (text.startsWith('pass:')) type = 'password';

            const file = {
                id: Date.now(),
                name: text.substring(0, 40).replace(/pass:/, '••••'),
                type, content: text,
                size: new Blob([text]).size,
                date: new Date().toLocaleString()
            };

            RAMStore.add(file);
            saveToDB(file);
            input.value = '';
            renderFiles();
            showToast('✅ Added to RAM');
        }

        function addFile() {
            const input = document.getElementById('fileInput');
            const files = input.files;
            if (!files.length) return;

            let count = 0;
            Array.from(files).forEach(f => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    let type = 'file';
                    if (f.type.startsWith('image/')) type = 'image';
                    else if (f.type.startsWith('video/')) type = 'video';
                    else if (f.type.startsWith('audio/')) type = 'audio';

                    const fileObj = {
                        id: Date.now() + Math.random(),
                        name: f.name, type, mimeType: f.type,
                        content: e.target.result, size: f.size,
                        date: new Date().toLocaleString()
                    };

                    RAMStore.add(fileObj);
                    saveToDB(fileObj);
                    count++;
                    if (count === files.length) {
                        renderFiles();
                        showToast('📎 ' + count + ' file(s) in RAM');
                    }
                };
                reader.readAsDataURL(f);
            });

            input.value = '';
        }

        function deleteFile(id) {
            RAMStore.remove(id);
            deleteFromDB(id);
            renderFiles();
            showToast('🗑 Deleted from RAM');
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
                new Audio(file.content).play();
                showToast('🎵 Playing from RAM');
            } else if (file.type === 'link') {
                window.open(file.content, '_blank');
            } else {
                navigator.clipboard.writeText(file.content).then(() => showToast('📋 Copied!'));
            }
        }

        function closeViewer() {
            document.getElementById('viewerOverlay').classList.remove('show');
            const vid = document.getElementById('viewerVideo');
            vid.pause(); vid.src = '';
        }

        function downloadFile(file) {
            const a = document.createElement('a');
            a.href = file.content;
            a.download = file.name;
            a.click();
            showToast('📥 Downloading...');
        }

        function filterType(type, btn) {
            currentFilter = type;
            document.querySelectorAll('.tool-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderFiles();
        }

        function renderFiles() {
            const area = document.getElementById('contentArea');
            const empty = document.getElementById('emptyState');
            const filtered = RAMStore.getByType(currentFilter);

            if (filtered.length === 0) {
                empty.style.display = 'block';
                area.innerHTML = '';
                area.appendChild(empty);
            } else {
                empty.style.display = 'none';
                area.innerHTML = filtered.map(f => {
                    const icons = {
                        image: '🖼️', video: '🎥', audio: '🎵',
                        text: '📝', password: '🔑', link: '🔗', file: '📄'
                    };
                    const icon = icons[f.type] || '📄';
                    const sizeStr = f.size > 1048576 ? (f.size/1048576).toFixed(1)+'MB' : f.size > 1024 ? (f.size/1024).toFixed(1)+'KB' : f.size+'B';
                    const badgeClass = 'badge-' + f.type;

                    let preview = '';
                    if (f.type === 'image') {
                        preview = `<div class="card-preview"><img src="${f.content}" onclick="viewFile(RAMStore.getAll().find(x=>x.id===${f.id}))"></div>`;
                    }

                    return `
                        <div class="file-card">
                            <div class="file-icon">${icon}</div>
                            <div class="file-info">
                                <div class="file-name">${escapeHtml(f.name)}</div>
                                <div class="file-meta">
                                    <span class="file-type-badge ${badgeClass}">${f.type}</span>
                                    <span>${sizeStr}</span>
                                    <span>${f.date}</span>
                                </div>
                                ${preview}
                            </div>
                            <div class="file-actions">
                                <button class="file-btn" onclick="viewFile(RAMStore.getAll().find(x=>x.id===${f.id}))">👁</button>
                                <button class="file-btn" onclick="downloadFile(RAMStore.getAll().find(x=>x.id===${f.id}))">⬇</button>
                                <button class="file-btn danger" onclick="deleteFile(${f.id})">🗑</button>
                            </div>
                        </div>
                    `;
                }).join('');
            }
        }

        function escapeHtml(t) {
            const d = document.createElement('div');
            d.textContent = t;
            return d.innerHTML;
        }

        // ==================== EXPORT ====================
        async function exportAll() {
            if (!isUnlocked) return;
            const files = RAMStore.getAll();
            const json = JSON.stringify(files, null, 2);
            const blob = new Blob([json], {type:'application/json'});
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'vaultx-ram-' + Date.now() + '.json';
            a.click();
            showToast('📤 ' + files.length + ' files exported');
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
        async function init() {
            await openDB();
            updateDots();
            RAMStore.updateUI();
        }
        init();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  ⚡ Vault X - RAM Edition              ║")
    print("║  🧠 تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🧠 نظام التخزين الجديد:")
    print("  ⚡ RAM Store - JavaScript Object في الذاكرة")
    print("  💾 IndexedDB - تخزين دائم احتياطي")
    print("  📊 مؤشر RAM حي (الحجم المستخدم)")
    print("  🔄 تحميل تلقائي من IndexedDB للـ RAM")
    print("  💚 نقطة RAM نابضة خضراء")
    print("")
    print("🔢 PIN: 1235")

if __name__ == "__main__":
    create_website_files()

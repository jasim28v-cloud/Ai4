import os

def create_website_files():
    """Wallpaper Hub - God Mode Edition"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Wallpaper Hub | God Mode</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fafaf8; --surface: #ffffff; --border: #eeece8;
            --gold: #c9a84c; --gold-light: #faf5e8; --gold-dark: #8b7300;
            --red: #e74c3c; --red-light: #fef5f5;
            --blue: #3498db; --blue-light: #f0f7fc;
            --text: #1a1a1a; --text2: #555; --text3: #999;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.03);
            --shadow: 0 2px 10px rgba(0,0,0,0.05);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.08);
            --radius-sm: 10px; --radius: 14px; --radius-lg: 18px;
            --transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #f0ede6; color: var(--text);
            font-family: 'Cairo', sans-serif; min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            -webkit-tap-highlight-color: transparent;
            -webkit-font-smoothing: antialiased; direction: rtl; overflow: hidden;
        }

        .particles-bg {
            position: fixed; inset: 0; pointer-events: none; z-index: 0;
        }
        .particle {
            position: absolute; background: var(--gold); border-radius: 50%; opacity: 0;
            animation: floatUp 6s ease-in infinite;
        }
        @keyframes floatUp {
            0% { transform: translateY(105vh) scale(0); opacity: 0; }
            15% { opacity: 0.5; } 85% { opacity: 0.1; }
            100% { transform: translateY(-5vh) scale(2); opacity: 0; }
        }

        .app {
            width: 100%; max-width: 480px; height: 100vh; max-height: 900px;
            display: flex; flex-direction: column; background: var(--bg);
            box-shadow: 0 20px 60px rgba(0,0,0,0.12); position: relative; z-index: 1; overflow: hidden;
        }

        /* ==================== SPLASH ==================== */
        .splash-screen {
            position: absolute; inset: 0; background: #fff;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 200; transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .splash-screen.hidden { opacity: 0; pointer-events: none; transform: scale(1.1); filter: blur(8px); }

        .splash-logo {
            width: 80px; height: 80px; position: relative; margin-bottom: 20px;
        }
        .splash-ring1 {
            position: absolute; inset: -10px; border: 2px solid rgba(52,152,219,0.2); border-radius: 50%;
            animation: ringSpin 3s linear infinite;
        }
        .splash-ring2 {
            position: absolute; inset: -5px; border: 1px dashed rgba(52,152,219,0.3); border-radius: 50%;
            animation: ringSpin 4s linear infinite reverse;
        }
        @keyframes ringSpin { to { transform: rotate(360deg); } }

        .splash-core {
            width: 100%; height: 100%; background: linear-gradient(135deg, var(--blue), #2980b9);
            border-radius: 22px; display: flex; align-items: center; justify-content: center;
            font-size: 35px; box-shadow: 0 8px 30px rgba(52,152,219,0.3);
            animation: logoBounce 1s ease-in-out infinite; position: relative; z-index: 2;
        }
        @keyframes logoBounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }

        .splash-spark {
            position: absolute; width: 4px; height: 4px; background: #f39c12;
            border-radius: 50%; animation: sparkOrbit 2s ease-in-out infinite; z-index: 3;
        }
        .splash-spark:nth-child(1){top:5px;left:10px;animation-delay:0s}
        .splash-spark:nth-child(2){top:10px;right:8px;animation-delay:.6s}
        .splash-spark:nth-child(3){bottom:8px;left:12px;animation-delay:1.2s}
        @keyframes sparkOrbit { 0%,100%{opacity:.3;transform:scale(1)} 50%{opacity:1;transform:scale(2.5)} }

        .splash-title {
            font-size: 26px; font-weight: 900; letter-spacing: 3px;
            background: linear-gradient(135deg, var(--gold), #e2c97e, var(--gold));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text; animation: titleShine 2s ease-in-out infinite;
        }
        @keyframes titleShine { 0%,100%{filter:brightness(1)} 50%{filter:brightness(1.3)} }

        .splash-sub { font-size: 9px; color: #999; letter-spacing: 4px; margin-top: 4px; }
        .splash-loader {
            width: 50px; height: 3px; background: #f0ede8; border-radius: 2px;
            margin-top: 20px; overflow: hidden;
        }
        .splash-loader-fill { height: 100%; background: var(--gold); border-radius: 2px; animation: loadFill 1.5s ease-in-out; width: 100%; }
        @keyframes loadFill { from{width:0} to{width:100%} }

        /* ==================== HEADER ==================== */
        .header {
            padding: 12px 16px; background: #fff; border-bottom: 1px solid var(--border);
            display: flex; align-items: center; justify-content: space-between; z-index: 10;
        }
        .brand { display: flex; align-items: center; gap: 10px; }
        .logo-icon {
            width: 42px; height: 42px; background: linear-gradient(135deg, var(--blue), #2980b9);
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 19px; box-shadow: 0 3px 12px rgba(52,152,219,0.25); position: relative;
        }
        .logo-dot {
            position: absolute; top: -3px; right: -3px; width: 7px; height: 7px;
            background: #f39c12; border-radius: 50%; animation: dotPulse 2s ease-in-out infinite;
        }
        @keyframes dotPulse { 0%,100%{transform:scale(1);opacity:.7} 50%{transform:scale(1.8);opacity:1} }

        .brand-text h1 { font-size: 16px; font-weight: 800; color: #1a1a1a; line-height: 1; }
        .brand-text span { font-size: 8px; color: #999; font-weight: 600; }

        .header-actions { display: flex; gap: 6px; }
        .btn-icon {
            width: 38px; height: 38px; background: #f8f7f4; border: 1px solid var(--border);
            color: #888; cursor: pointer; border-radius: 12px; font-size: 15px;
            display: flex; align-items: center; justify-content: center;
            transition: var(--transition); position: relative;
        }
        .btn-icon:hover { background: #f0ede8; color: #555; }
        .btn-icon.active { background: var(--red-light); border-color: var(--red); color: var(--red); }

        .badge {
            position: absolute; top: -6px; right: -6px; width: 20px; height: 20px;
            background: var(--red); color: #fff; font-size: 9px; font-weight: 700;
            border-radius: 50%; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 2px 8px rgba(231,76,60,0.3); display: none;
        }
        .badge.show { display: flex; animation: badgePop 0.3s ease; }
        @keyframes badgePop { from{transform:scale(0)} to{transform:scale(1)} }

        /* ==================== STATS ==================== */
        .stats-row {
            display: flex; gap: 6px; padding: 8px 14px; background: #fff; border-bottom: 1px solid var(--border);
        }
        .stat-box { flex: 1; padding: 9px 6px; border-radius: var(--radius-sm); text-align: center; transition: var(--transition); }
        .stat-box:hover { transform: translateY(-2px); }
        .stat-box:nth-child(1) { background: #f0f7fc; border: 1px solid #d6eaf8; }
        .stat-box:nth-child(2) { background: #fef5f5; border: 1px solid #fce4e4; }
        .stat-box:nth-child(3) { background: #fdfaf3; border: 1px solid #f5eed8; }
        .stat-num { font-size: 16px; font-weight: 800; display: block; }
        .stat-box:nth-child(1) .stat-num { color: #2980b9; }
        .stat-box:nth-child(2) .stat-num { color: #e74c3c; }
        .stat-box:nth-child(3) .stat-num { color: #b8860b; }
        .stat-lbl { font-size: 7px; color: #999; letter-spacing: 0.5px; margin-top: 2px; }

        /* ==================== SEARCH ==================== */
        .search-bar {
            padding: 10px 14px; background: #fff; border-bottom: 1px solid var(--border);
            display: flex; gap: 8px;
        }
        .search-input {
            flex: 1; padding: 11px 14px; background: #f8f7f4;
            border: 1.5px solid var(--border); color: var(--text);
            font-size: 11px; border-radius: 14px; font-family: 'Cairo', sans-serif; outline: none;
            transition: var(--transition);
        }
        .search-input:focus { border-color: var(--gold); background: #fff; box-shadow: 0 0 0 4px rgba(201,168,76,0.06); }
        .search-input::placeholder { color: #ccc; }
        .search-btn {
            padding: 11px 18px; background: var(--gold); color: #fff; border: none;
            cursor: pointer; border-radius: 14px; font-size: 11px;
            font-family: 'Cairo', sans-serif; font-weight: 700; white-space: nowrap;
            box-shadow: 0 3px 10px rgba(201,168,76,0.2); transition: var(--transition);
        }
        .search-btn:hover { background: var(--gold-dark); }

        /* ==================== SUGGESTIONS ==================== */
        .suggestions-row {
            display: flex; gap: 5px; padding: 8px 14px; background: #fff;
            border-bottom: 1px solid var(--border); overflow-x: auto;
        }
        .suggestions-row::-webkit-scrollbar { height: 0; }
        .sug-chip {
            padding: 6px 10px; background: #f8f6f2; border: 1px solid var(--border);
            color: #888; cursor: pointer; border-radius: 15px;
            font-size: 8px; font-weight: 600; white-space: nowrap;
            font-family: 'Cairo', sans-serif; transition: var(--transition);
        }
        .sug-chip:hover { background: #f0ede8; color: #555; }

        /* ==================== CATEGORIES ==================== */
        .cat-scroll {
            display: flex; gap: 5px; padding: 0 14px 10px; background: #fff;
            overflow-x: auto; border-bottom: 1px solid var(--border);
        }
        .cat-scroll::-webkit-scrollbar { height: 0; }
        .cat-chip {
            padding: 8px 13px; background: #f8f6f2; border: 1.5px solid var(--border);
            color: #888; cursor: pointer; border-radius: 22px;
            font-size: 9px; font-weight: 700; white-space: nowrap;
            font-family: 'Cairo', sans-serif; transition: var(--transition);
            display: flex; align-items: center; gap: 4px;
        }
        .cat-chip:hover { background: #f0ede8; }
        .cat-chip.active {
            background: #fff; border-color: var(--gold); color: var(--gold-dark);
            font-weight: 800; box-shadow: 0 2px 8px rgba(201,168,76,0.15); transform: translateY(-1px);
        }
        .cat-chip .cat-emoji { font-size: 14px; }

        /* ==================== CONTENT ==================== */
        .content {
            flex: 1; overflow-y: auto; padding: 10px 12px;
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; align-content: start;
        }
        .content::-webkit-scrollbar { width: 3px; }
        .content::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        /* ==================== CARD ==================== */
        .wall-card {
            background: #fff; border: 1px solid var(--border);
            border-radius: var(--radius-lg); overflow: hidden; cursor: pointer;
            transition: var(--transition); box-shadow: var(--shadow-sm);
            animation: cardIn 0.5s ease; position: relative;
        }
        @keyframes cardIn { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }

        .wall-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
        .wall-card:active { transform: scale(0.97); }

        .wall-img {
            width: 100%; aspect-ratio: 0.75;
            background: #f0ede8; display: flex; align-items: center;
            justify-content: center; position: relative; overflow: hidden;
        }
        .wall-img img {
            width: 100%; height: 100%; object-fit: cover; display: block;
            transition: transform 0.5s;
        }
        .wall-card:hover .wall-img img { transform: scale(1.06); }
        .wall-img .placeholder-img { font-size: 35px; position: absolute; color: #ddd; }

        .wall-overlay {
            position: absolute; inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.2), transparent 50%);
            opacity: 0; transition: opacity 0.3s;
        }
        .wall-card:hover .wall-overlay { opacity: 1; }

        .wall-fav {
            position: absolute; top: 10px; left: 10px;
            width: 30px; height: 30px; background: rgba(255,255,255,0.95);
            border: none; color: #ccc; cursor: pointer; border-radius: 50%;
            font-size: 13px; display: flex; align-items: center; justify-content: center;
            z-index: 2; box-shadow: var(--shadow-sm); transition: var(--transition);
        }
        .wall-fav:hover { transform: scale(1.15); }
        .wall-fav.liked { color: var(--red); }

        .wall-dl-btn {
            position: absolute; bottom: 10px; right: 10px;
            padding: 6px 12px; background: rgba(0,0,0,0.65); color: #fff;
            border: none; cursor: pointer; border-radius: 20px;
            font-size: 9px; font-family: 'Cairo', sans-serif; z-index: 2;
            transition: var(--transition); display: flex; align-items: center; gap: 4px;
        }
        .wall-dl-btn:hover { background: rgba(0,0,0,0.85); }

        /* ==================== VIEWER ==================== */
        .viewer-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,0.96); z-index: 100;
            align-items: center; justify-content: center; flex-direction: column;
            backdrop-filter: blur(10px);
        }
        .viewer-overlay.show { display: flex; }

        .viewer-img {
            max-width: 95%; max-height: 72%; border-radius: 16px;
            object-fit: contain; box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            animation: viewerIn 0.4s ease;
        }
        @keyframes viewerIn { from{opacity:0;transform:scale(0.9)} to{opacity:1;transform:scale(1)} }

        .viewer-close {
            position: absolute; top: 20px; right: 20px;
            width: 44px; height: 44px; background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2); color: #fff;
            cursor: pointer; border-radius: 50%; font-size: 20px;
            display: flex; align-items: center; justify-content: center;
            transition: var(--transition);
        }
        .viewer-close:hover { background: rgba(255,255,255,0.2); }

        .viewer-info {
            color: #aaa; font-size: 10px; margin-top: 12px; letter-spacing: 1px;
        }

        .viewer-actions {
            display: flex; gap: 10px; margin-top: 14px;
        }
        .viewer-btn {
            padding: 12px 22px; border-radius: 25px; border: none;
            font-size: 11px; font-family: 'Cairo', sans-serif; font-weight: 700;
            cursor: pointer; color: #fff; transition: var(--transition);
            display: flex; align-items: center; gap: 6px;
        }
        .viewer-btn:active { transform: scale(0.95); }
        .btn-dl { background: #27ae60; }
        .btn-dl:hover { background: #2ecc71; }
        .btn-fav-v { background: #e74c3c; }
        .btn-fav-v:hover { background: #c0392b; }
        .btn-share { background: #3498db; }
        .btn-share:hover { background: #2980b9; }

        /* ==================== STATES ==================== */
        .loading-state {
            grid-column: 1 / -1; text-align: center; padding: 50px 20px; color: #bbb;
        }
        .loading-ring {
            width: 42px; height: 42px; border: 3px solid #f0ede8;
            border-top-color: var(--gold); border-radius: 50%;
            animation: spin 0.8s linear infinite; margin: 0 auto 12px;
        }
        @keyframes spin { to{transform:rotate(360deg)} }

        .empty-state { grid-column: 1 / -1; text-align: center; padding: 50px 20px; }
        .empty-icon { font-size: 50px; display: block; margin-bottom: 10px; opacity: 0.4; animation: emptyBounce 3s ease-in-out infinite; }
        @keyframes emptyBounce { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
        .empty-title { font-size: 13px; font-weight: 700; color: #999; margin-bottom: 4px; }

        /* ==================== TOAST ==================== */
        .toast {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #1a1a1a; color: #fff; padding: 12px 24px;
            border-radius: 30px; font-size: 10px; font-weight: 600;
            z-index: 300; transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
            font-family: 'Cairo', sans-serif; white-space: nowrap;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            display: flex; align-items: center; gap: 6px;
        }
        .toast.show { transform: translateX(-50%) translateY(0); }
        .toast-dot { width: 8px; height: 8px; background: #27ae60; border-radius: 50%; animation: dotPulse 1s ease-in-out infinite; }

        .refresh-bar {
            text-align: center; padding: 7px; background: #fdfaf3;
            color: var(--gold-dark); font-size: 9px; font-weight: 700;
            cursor: pointer; border-bottom: 1px solid var(--border);
            font-family: 'Cairo', sans-serif; transition: var(--transition);
        }
        .refresh-bar:hover { background: #faf5e6; }
    </style>
</head>
<body>
    <!-- Particles -->
    <div class="particles-bg" id="particlesBg"></div>

    <div class="app">
        <!-- ==================== SPLASH ==================== -->
        <div class="splash-screen" id="splashScreen">
            <div class="splash-logo">
                <div class="splash-ring1"></div>
                <div class="splash-ring2"></div>
                <div class="splash-core">
                    🖼️
                    <span class="splash-spark"></span>
                    <span class="splash-spark"></span>
                    <span class="splash-spark"></span>
                </div>
            </div>
            <div class="splash-title">Wallpaper Hub</div>
            <div class="splash-sub">✦ God Mode ✦</div>
            <div class="splash-loader"><div class="splash-loader-fill"></div></div>
        </div>

        <!-- ==================== HEADER ==================== -->
        <div class="header">
            <div class="brand">
                <div class="logo-icon">
                    🖼️
                    <span class="logo-dot"></span>
                </div>
                <div class="brand-text">
                    <h1>Wallpaper Hub</h1>
                    <span>خلفيات عالية الدقة</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn-icon" id="favFilterBtn" onclick="toggleFavFilter()">
                    ❤️
                    <span class="badge" id="favBadge">0</span>
                </button>
            </div>
        </div>

        <!-- ==================== STATS ==================== -->
        <div class="stats-row">
            <div class="stat-box"><span class="stat-num" id="statTotal">-</span><span class="stat-lbl">خلفية</span></div>
            <div class="stat-box"><span class="stat-num" id="statFavs">0</span><span class="stat-lbl">مفضلة</span></div>
            <div class="stat-box"><span class="stat-num">🌐</span><span class="stat-lbl">مباشر</span></div>
        </div>

        <!-- ==================== REFRESH ==================== -->
        <div class="refresh-bar" onclick="fetchWallpapers('nature')">🔄 اسحب للتحديث وجلب المزيد من الخلفيات</div>

        <!-- ==================== SEARCH ==================== -->
        <div class="search-bar">
            <input type="text" class="search-input" placeholder="ابحث عن خلفيات... (طبيعة، سيارات، فضاء...)" id="searchInput" onkeypress="if(event.key==='Enter')searchWallpapers()">
            <button class="search-btn" onclick="searchWallpapers()">🔍 بحث</button>
        </div>

        <!-- ==================== SUGGESTIONS ==================== -->
        <div class="suggestions-row">
            <span class="sug-chip" onclick="setSearch('مناظر طبيعية')">🏔️ مناظر طبيعية</span>
            <span class="sug-chip" onclick="setSearch('سيارات فاخرة')">🏎️ سيارات فاخرة</span>
            <span class="sug-chip" onclick="setSearch('غروب الشمس')">🌅 غروب الشمس</span>
            <span class="sug-chip" onclick="setSearch('جبال')">⛰️ جبال</span>
            <span class="sug-chip" onclick="setSearch('بحر')">🌊 بحر</span>
        </div>

        <!-- ==================== CATEGORIES ==================== -->
        <div class="cat-scroll" id="catFilter">
            <button class="cat-chip active" data-cat="nature" onclick="fetchWallpapers('nature', this)">
                <span class="cat-emoji">🌿</span> طبيعة
            </button>
            <button class="cat-chip" data-cat="cars" onclick="fetchWallpapers('cars', this)">
                <span class="cat-emoji">🏎️</span> سيارات
            </button>
            <button class="cat-chip" data-cat="space" onclick="fetchWallpapers('space', this)">
                <span class="cat-emoji">🌌</span> فضاء
            </button>
            <button class="cat-chip" data-cat="city" onclick="fetchWallpapers('city', this)">
                <span class="cat-emoji">🏙️</span> مدن
            </button>
            <button class="cat-chip" data-cat="animals" onclick="fetchWallpapers('animals', this)">
                <span class="cat-emoji">🐾</span> حيوانات
            </button>
            <button class="cat-chip" data-cat="abstract" onclick="fetchWallpapers('abstract', this)">
                <span class="cat-emoji">🎨</span> تجريدي
            </button>
        </div>

        <!-- ==================== CONTENT ==================== -->
        <div class="content" id="contentArea">
            <div class="loading-state"><div class="loading-ring"></div><div>جاري تحميل الخلفيات...</div></div>
        </div>
    </div>

    <!-- ==================== VIEWER ==================== -->
    <div class="viewer-overlay" id="viewerOverlay">
        <button class="viewer-close" onclick="closeViewer()">✕</button>
        <img class="viewer-img" id="viewerImg">
        <div class="viewer-info" id="viewerInfo"></div>
        <div class="viewer-actions">
            <button class="viewer-btn btn-dl" onclick="downloadCurrent()">📥 تحميل HD</button>
            <button class="viewer-btn btn-fav-v" id="viewerFavBtn" onclick="toggleFavViewer()">🤍 مفضلة</button>
            <button class="viewer-btn btn-share" onclick="shareCurrent()">📤 مشاركة</button>
        </div>
    </div>

    <!-- ==================== TOAST ==================== -->
    <div class="toast" id="toast">
        <span class="toast-dot"></span>
        <span id="toastText"></span>
    </div>

    <script>
        // ==================== PARTICLES ====================
        (function() {
            const c = document.getElementById('particlesBg');
            for (let i = 0; i < 25; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                const s = Math.random() * 3 + 1;
                p.style.width = s + 'px'; p.style.height = s + 'px';
                p.style.animationDuration = (Math.random() * 8 + 4) + 's';
                p.style.animationDelay = (Math.random() * 6) + 's';
                c.appendChild(p);
            }
        })();

        // ==================== SPLASH ====================
        setTimeout(() => document.getElementById('splashScreen').classList.add('hidden'), 1800);

        // ==================== STATE ====================
        let wallpapers = [];
        let favorites = JSON.parse(localStorage.getItem('wallpaper_god_favs') || '[]');
        let showFavs = false;
        let currentViewerUrl = null;
        let currentViewerId = null;

        function setSearch(text) {
            document.getElementById('searchInput').value = text;
            searchWallpapers();
        }

        async function fetchWallpapers(query, btn) {
            if (btn) {
                document.querySelectorAll('.cat-chip').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            }
            document.getElementById('contentArea').innerHTML = '<div class="loading-state"><div class="loading-ring"></div><div>جاري التحميل...</div></div>';

            try {
                const res = await fetch(`https://api.unsplash.com/search/photos?query=${encodeURIComponent(query)}&per_page=30&orientation=portrait&client_id=DemoApp123`);
                const data = await res.json();
                wallpapers = (data.results || []).map(img => ({
                    id: img.id, url: img.urls.regular, full: img.urls.full,
                    thumb: img.urls.thumb, author: img.user.name,
                    likes: img.likes
                }));
            } catch(e) { wallpapers = []; }
            render(); updateStats();
        }

        async function searchWallpapers() {
            const q = document.getElementById('searchInput').value.trim();
            if (!q) return showToast('⚠️ اكتب كلمة البحث');
            await fetchWallpapers(q);
        }

        function render() {
            const area = document.getElementById('contentArea');
            let list = showFavs ? wallpapers.filter(w => favorites.includes(w.id)) : wallpapers;

            if (!list.length) {
                area.innerHTML = '<div class="empty-state"><span class="empty-icon">🖼️</span><div class="empty-title">لا توجد خلفيات</div></div>';
                return;
            }

            area.innerHTML = list.map(w => {
                const isFav = favorites.includes(w.id);
                return `
                    <div class="wall-card" onclick="openViewer('${w.id}')">
                        <div class="wall-img">
                            <img src="${w.thumb}" alt="wallpaper" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
                            <span class="placeholder-img" style="display:none">🖼️</span>
                            <div class="wall-overlay"></div>
                            <button class="wall-fav ${isFav?'liked':''}" onclick="event.stopPropagation();toggleFav('${w.id}')">${isFav?'❤️':'🤍'}</button>
                            <button class="wall-dl-btn" onclick="event.stopPropagation();downloadImg('${w.full}')">📥 تحميل</button>
                        </div>
                    </div>`;
            }).join('');
            updateBadge();
        }

        function updateStats() {
            document.getElementById('statTotal').textContent = wallpapers.length;
            document.getElementById('statFavs').textContent = favorites.length;
        }

        function updateBadge() {
            const b = document.getElementById('favBadge');
            b.textContent = favorites.length;
            b.classList.toggle('show', favorites.length > 0);
        }

        // ==================== VIEWER ====================
        function openViewer(id) {
            const w = wallpapers.find(x => x.id === id);
            if (!w) return;
            currentViewerUrl = w.full;
            currentViewerId = w.id;
            document.getElementById('viewerImg').src = w.url;
            document.getElementById('viewerInfo').textContent = '📸 ' + w.author + ' • ❤️ ' + (w.likes || 0);
            document.getElementById('viewerFavBtn').textContent = favorites.includes(w.id) ? '❤️ مفضلة' : '🤍 مفضلة';
            document.getElementById('viewerOverlay').classList.add('show');
        }

        function closeViewer() { document.getElementById('viewerOverlay').classList.remove('show'); }

        function downloadCurrent() { if (currentViewerUrl) downloadImg(currentViewerUrl); }

        function downloadImg(url) {
            showToast('⏳ جاري التحميل...');
            fetch(url).then(r => r.blob()).then(blob => {
                const a = document.createElement('a');
                a.href = URL.createObjectURL(blob);
                a.download = 'wallpaper-' + Date.now() + '.jpg';
                a.click();
                showToast('✅ تم تحميل الخلفية');
            }).catch(() => showToast('❌ فشل التحميل'));
        }

        function toggleFav(id) {
            favorites = favorites.includes(id) ? favorites.filter(f => f !== id) : [...favorites, id];
            localStorage.setItem('wallpaper_god_favs', JSON.stringify(favorites));
            render(); updateStats(); updateBadge();
        }

        function toggleFavViewer() {
            if (currentViewerId) toggleFav(currentViewerId);
            document.getElementById('viewerFavBtn').textContent = favorites.includes(currentViewerId) ? '❤️ مفضلة' : '🤍 مفضلة';
        }

        async function shareCurrent() {
            if (!currentViewerUrl) return;
            if (navigator.share) {
                try { await navigator.share({ title: 'خلفية رائعة', url: currentViewerUrl }); } catch(e) {}
            } else {
                window.open(currentViewerUrl, '_blank');
            }
        }

        function toggleFavFilter() {
            showFavs = !showFavs;
            document.getElementById('favFilterBtn').classList.toggle('active', showFavs);
            render();
            showToast(showFavs ? '❤️ عرض المفضلة' : '🌍 عرض الكل');
        }

        // ==================== TOAST ====================
        function showToast(msg) {
            document.getElementById('toastText').textContent = msg;
            document.getElementById('toast').classList.add('show');
            setTimeout(() => document.getElementById('toast').classList.remove('show'), 2200);
        }

        // ==================== PULL TO REFRESH ====================
        let tsY = 0;
        document.addEventListener('touchstart', e => { tsY = e.touches[0].clientY; });
        document.addEventListener('touchend', e => {
            if (e.changedTouches[0].clientY - tsY > 100) fetchWallpapers('nature');
        });

        // ==================== INIT ====================
        updateStats(); fetchWallpapers('nature', document.querySelector('.cat-chip'));
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  🖼️ Wallpaper Hub - God Mode           ║")
    print("║  ✨ تم الإنشاء بنجاح                   ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html - {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("👑 المميزات الأسطورية:")
    print("  🎬 Splash Screen متحرك")
    print("  ✨ 25 جسيم ذهبي في الخلفية")
    print("  💫 حلقات وبريق حول الشعار")
    print("  🖼️ Unsplash API - آلاف الخلفيات HD")
    print("  🔍 بحث مع اقتراحات سريعة")
    print("  🎨 6 أقسام مع أيقونات")
    print("  📊 3 إحصائيات")
    print("  👁️ عارض Fullscreen مع blur")
    print("  📥 تحميل HD مباشر")
    print("  📤 مشاركة")
    print("  ❤️ مفضلة مع شارة وعداد")
    print("  🔄 Pull-to-Refresh")
    print("  💳 بطاقات بتأثيرات hover وتكبير الصورة")
    print("  🔔 Toast بنبض أخضر")

if __name__ == "__main__":
    create_website_files()

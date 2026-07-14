import os

def create_website_files():
    """طبّاخ برو - الإصدار الأسطوري المبهر"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>طبّاخ برو | الإصدار الأسطوري</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fafaf8; --surface: #ffffff; --border: #eeece8;
            --gold: #c9a84c; --gold-light: #faf5e8; --gold-dark: #8b7300;
            --red: #e74c3c; --red-light: #fef5f5; --green: #27ae60;
            --green-light: #f0faf4; --blue: #3498db; --blue-light: #f0f7fc;
            --text: #1a1a1a; --text2: #555; --text3: #999;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.03);
            --shadow: 0 2px 10px rgba(0,0,0,0.05);
            --shadow-lg: 0 8px 30px rgba(0,0,0,0.08);
            --shadow-xl: 0 15px 50px rgba(0,0,0,0.12);
            --radius-sm: 10px; --radius: 14px; --radius-lg: 18px; --radius-xl: 24px;
            --transition: 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #f0ede6;
            color: var(--text);
            font-family: 'Cairo', sans-serif;
            min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            -webkit-tap-highlight-color: transparent;
            -webkit-font-smoothing: antialiased;
            direction: rtl;
            overflow: hidden;
        }

        /* ==================== PARTICLES BACKGROUND ==================== */
        .particles-bg {
            position: fixed; inset: 0; pointer-events: none; z-index: 0;
        }

        .particle {
            position: absolute; background: var(--gold);
            border-radius: 50%; opacity: 0;
            animation: floatUp 6s ease-in infinite;
        }

        @keyframes floatUp {
            0% { transform: translateY(105vh) scale(0); opacity: 0; }
            15% { opacity: 0.5; }
            85% { opacity: 0.1; }
            100% { transform: translateY(-5vh) scale(2); opacity: 0; }
        }

        .app {
            width: 100%; max-width: 480px; height: 100vh; max-height: 900px;
            display: flex; flex-direction: column; background: var(--bg);
            box-shadow: var(--shadow-xl); position: relative; z-index: 1;
            overflow: hidden;
        }

        /* ==================== SPLASH SCREEN ==================== */
        .splash-screen {
            position: absolute; inset: 0; background: #fff;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            z-index: 200; transition: all 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .splash-screen.hidden {
            opacity: 0; pointer-events: none; transform: scale(1.1); filter: blur(8px);
        }

        .splash-logo {
            width: 80px; height: 80px; position: relative; margin-bottom: 20px;
        }

        .splash-logo-ring1 {
            position: absolute; inset: -10px;
            border: 2px solid rgba(231,76,60,0.2); border-radius: 50%;
            animation: ringSpin 3s linear infinite;
        }

        .splash-logo-ring2 {
            position: absolute; inset: -5px;
            border: 1px dashed rgba(231,76,60,0.3); border-radius: 50%;
            animation: ringSpin 4s linear infinite reverse;
        }

        @keyframes ringSpin { to { transform: rotate(360deg); } }

        .splash-logo-core {
            width: 100%; height: 100%;
            background: linear-gradient(135deg, var(--red), #c0392b);
            border-radius: 22px;
            display: flex; align-items: center; justify-content: center;
            font-size: 35px;
            box-shadow: 0 8px 30px rgba(231,76,60,0.3);
            animation: logoBounce 1s ease-in-out infinite;
            position: relative; z-index: 2;
        }

        @keyframes logoBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .splash-spark {
            position: absolute; width: 4px; height: 4px;
            background: #f39c12; border-radius: 50%;
            animation: sparkOrbit 2s ease-in-out infinite; z-index: 3;
        }
        .splash-spark:nth-child(1) { top: 5px; left: 10px; animation-delay: 0s; }
        .splash-spark:nth-child(2) { top: 10px; right: 8px; animation-delay: 0.6s; }
        .splash-spark:nth-child(3) { bottom: 8px; left: 12px; animation-delay: 1.2s; }

        @keyframes sparkOrbit {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 1; transform: scale(2.5); }
        }

        .splash-title {
            font-size: 26px; font-weight: 900; letter-spacing: 3px;
            background: linear-gradient(135deg, var(--gold), #e2c97e, var(--gold));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: titleShine 2s ease-in-out infinite;
        }

        @keyframes titleShine {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }

        .splash-sub {
            font-size: 9px; color: #999; letter-spacing: 4px;
            margin-top: 4px; animation: fadeInOut 2s ease-in-out infinite;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .splash-loader {
            width: 50px; height: 3px; background: #f0ede8;
            border-radius: 2px; margin-top: 20px; overflow: hidden;
        }

        .splash-loader-fill {
            height: 100%; background: var(--gold);
            border-radius: 2px; animation: loadFill 1.5s ease-in-out;
            width: 100%;
        }

        @keyframes loadFill {
            from { width: 0; }
            to { width: 100%; }
        }

        /* ==================== HEADER ==================== */
        .header {
            padding: 12px 16px; background: #fff; border-bottom: 1px solid var(--border);
            display: flex; align-items: center; justify-content: space-between; z-index: 10;
        }

        .brand { display: flex; align-items: center; gap: 10px; }

        .logo-icon {
            width: 42px; height: 42px;
            background: linear-gradient(135deg, var(--red), #c0392b);
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 19px; position: relative;
            box-shadow: 0 3px 12px rgba(231,76,60,0.25);
        }

        .logo-dot {
            position: absolute; top: -3px; right: -3px;
            width: 7px; height: 7px; background: #f39c12;
            border-radius: 50%; animation: dotPulse 2s ease-in-out infinite;
        }

        @keyframes dotPulse {
            0%, 100% { transform: scale(1); opacity: 0.7; }
            50% { transform: scale(1.8); opacity: 1; }
        }

        .brand-text h1 { font-size: 16px; font-weight: 800; color: #1a1a1a; line-height: 1; }
        .brand-text span { font-size: 8px; color: #999; font-weight: 600; }

        .header-actions { display: flex; gap: 6px; }

        .btn-icon {
            width: 38px; height: 38px; background: #f8f7f4;
            border: 1px solid var(--border); color: #888;
            cursor: pointer; border-radius: 12px; font-size: 15px;
            display: flex; align-items: center; justify-content: center;
            transition: var(--transition); position: relative;
        }

        .btn-icon:hover { background: #f0ede8; color: #555; }
        .btn-icon.active { background: var(--red-light); border-color: var(--red); color: var(--red); }

        .badge {
            position: absolute; top: -6px; right: -6px;
            width: 20px; height: 20px; background: var(--red); color: #fff;
            font-size: 9px; font-weight: 700; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 2px 8px rgba(231,76,60,0.3);
            display: none;
        }
        .badge.show { display: flex; animation: badgePop 0.3s ease; }

        @keyframes badgePop {
            from { transform: scale(0); }
            to { transform: scale(1); }
        }

        /* ==================== WAVE HEADER ==================== */
        .wave-container {
            height: 8px; background: #fff; overflow: hidden;
            position: relative;
        }

        .wave-svg {
            position: absolute; bottom: 0; width: 200%; height: 100%;
            animation: waveMove 4s linear infinite;
        }

        @keyframes waveMove {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        /* ==================== STATS ==================== */
        .stats-row {
            display: flex; gap: 6px; padding: 8px 14px;
            background: #fff; border-bottom: 1px solid var(--border);
        }

        .stat-box {
            flex: 1; padding: 9px 6px; border-radius: var(--radius-sm);
            text-align: center; transition: var(--transition);
        }

        .stat-box:hover { transform: translateY(-2px); }
        .stat-box:nth-child(1) { background: #fdfaf3; border: 1px solid #f5eed8; }
        .stat-box:nth-child(2) { background: #fef5f5; border: 1px solid #fce4e4; }
        .stat-box:nth-child(3) { background: #f0faf4; border: 1px solid #d5f5e3; }
        .stat-box:nth-child(4) { background: #f0f7fc; border: 1px solid #d6eaf8; }

        .stat-num { font-size: 16px; font-weight: 800; display: block; }
        .stat-box:nth-child(1) .stat-num { color: #b8860b; }
        .stat-box:nth-child(2) .stat-num { color: #e74c3c; }
        .stat-box:nth-child(3) .stat-num { color: #27ae60; }
        .stat-box:nth-child(4) .stat-num { color: #2980b9; }

        .stat-lbl { font-size: 7px; color: #999; letter-spacing: 0.5px; margin-top: 2px; }

        /* ==================== SEARCH ==================== */
        .search-bar {
            padding: 10px 14px; background: #fff;
            border-bottom: 1px solid var(--border);
            display: flex; gap: 8px;
        }

        .search-input-wrap { flex: 1; position: relative; }

        .search-input {
            width: 100%; padding: 11px 42px 11px 14px;
            background: #f8f7f4; border: 1.5px solid var(--border);
            color: var(--text); font-size: 11px; border-radius: 14px;
            font-family: 'Cairo', sans-serif; outline: none;
            transition: var(--transition);
        }

        .search-input:focus {
            border-color: var(--gold); background: #fff;
            box-shadow: 0 0 0 4px rgba(201,168,76,0.06);
        }

        .search-input::placeholder { color: #ccc; }

        .search-icon-btn {
            position: absolute; right: 4px; top: 50%; transform: translateY(-50%);
            width: 34px; height: 34px; background: var(--gold); border: none;
            color: #fff; cursor: pointer; border-radius: 10px;
            font-size: 14px; display: flex; align-items: center; justify-content: center;
            transition: var(--transition);
        }

        .search-icon-btn:hover { background: var(--gold-dark); transform: translateY(-50%) scale(1.05); }

        /* ==================== CATEGORIES ==================== */
        .cat-scroll {
            display: flex; gap: 5px; padding: 0 14px 10px;
            background: #fff; overflow-x: auto; border-bottom: 1px solid var(--border);
        }
        .cat-scroll::-webkit-scrollbar { height: 0; }

        .cat-chip {
            padding: 7px 13px; background: #f8f6f2;
            border: 1.5px solid var(--border); color: #888;
            cursor: pointer; border-radius: 22px;
            font-size: 9px; font-weight: 700; white-space: nowrap;
            font-family: 'Cairo', sans-serif; transition: var(--transition);
        }

        .cat-chip:hover { background: #f0ede8; }
        .cat-chip.active {
            background: #fff; border-color: var(--gold); color: var(--gold-dark);
            font-weight: 800; box-shadow: 0 2px 8px rgba(201,168,76,0.15);
            transform: translateY(-1px);
        }

        /* ==================== CONTENT ==================== */
        .content {
            flex: 1; overflow-y: auto; padding: 12px 14px;
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;
            align-content: start;
        }
        .content::-webkit-scrollbar { width: 3px; }
        .content::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        /* ==================== CARD ==================== */
        .card {
            background: #fff; border: 1px solid var(--border);
            border-radius: var(--radius-lg); overflow: hidden; cursor: pointer;
            transition: var(--transition); box-shadow: var(--shadow-sm);
            animation: cardFadeIn 0.5s ease;
            position: relative;
        }

        @keyframes cardFadeIn {
            from { opacity: 0; transform: translateY(14px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
        .card:active { transform: scale(0.97); }

        .card-badge-top {
            position: absolute; top: 8px; right: 8px;
            padding: 3px 8px; background: linear-gradient(135deg, #f39c12, #e67e22);
            color: #fff; font-size: 7px; font-weight: 700;
            border-radius: 20px; z-index: 3;
            box-shadow: 0 2px 8px rgba(243,156,18,0.3);
        }

        .card-img {
            width: 100%; height: 140px;
            background: linear-gradient(135deg, #faf7f0, #f2ece0);
            display: flex; align-items: center; justify-content: center;
            position: relative; overflow: hidden;
        }

        .card-img img {
            width: 100%; height: 100%; object-fit: cover; object-position: center;
            display: block; background: #f5f0e8;
            transition: transform 0.5s;
        }

        .card:hover .card-img img { transform: scale(1.06); }

        .card-img .emoji-placeholder {
            font-size: 45px; position: absolute;
        }

        .card-img-overlay {
            position: absolute; inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.15), transparent 40%);
            opacity: 0; transition: opacity 0.3s;
        }

        .card:hover .card-img-overlay { opacity: 1; }

        .card-time-badge {
            position: absolute; bottom: 8px; right: 8px;
            padding: 4px 8px; background: rgba(255,255,255,0.95);
            color: #555; font-size: 7px; font-weight: 700;
            border-radius: 15px; z-index: 2;
            display: flex; align-items: center; gap: 3px;
        }

        .card-fav-btn {
            position: absolute; top: 8px; left: 8px;
            width: 29px; height: 29px; background: rgba(255,255,255,0.95);
            border: none; color: #ccc; cursor: pointer; border-radius: 50%;
            font-size: 12px; display: flex; align-items: center; justify-content: center;
            transition: var(--transition); z-index: 2;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        }

        .card-fav-btn:hover { transform: scale(1.15); }
        .card-fav-btn.liked { color: var(--red); }

        .card-body { padding: 10px 12px 12px; }

        .card-tag {
            display: inline-block; padding: 2px 7px;
            background: var(--gold-light); color: var(--gold-dark);
            font-size: 7px; font-weight: 700; border-radius: 5px;
            letter-spacing: 0.5px; margin-bottom: 5px;
        }

        .card-title {
            font-size: 12px; font-weight: 700; color: #1a1a1a;
            line-height: 1.35; margin-bottom: 6px;
            display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
        }

        .card-footer-row { display: flex; align-items: center; justify-content: space-between; }
        .card-area-text { font-size: 8px; color: #999; font-weight: 600; }
        .card-rating { color: #f0a500; font-size: 9px; letter-spacing: 1px; }

        /* ==================== MODAL ==================== */
        .modal-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,0.5); z-index: 100;
            align-items: flex-end; justify-content: center;
            backdrop-filter: blur(4px);
        }
        .modal-overlay.show { display: flex; }

        .modal {
            background: #fff; border-radius: 28px 28px 0 0;
            width: 100%; max-width: 480px; max-height: 88vh;
            overflow-y: auto;
            animation: modalSlideUp 0.45s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 -20px 60px rgba(0,0,0,0.25);
        }

        @keyframes modalSlideUp {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }

        .modal::-webkit-scrollbar { width: 3px; }
        .modal::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        .modal-handle-bar {
            width: 40px; height: 5px; background: #e0ddd8;
            border-radius: 3px; margin: 12px auto 0;
        }

        .modal-hero-image {
            width: 100%; height: 230px;
            background: linear-gradient(135deg, #faf7f0, #f2ece0);
            display: flex; align-items: center; justify-content: center;
            position: relative; overflow: hidden; margin-top: 8px;
        }

        .modal-hero-image img {
            width: 100%; height: 100%; object-fit: cover; object-position: center;
            display: block; background: #f5f0e8;
        }

        .modal-hero-image .emoji-placeholder {
            font-size: 65px; position: absolute;
        }

        .modal-close-btn {
            position: absolute; top: 14px; right: 14px;
            width: 38px; height: 38px; background: rgba(255,255,255,0.95);
            border: none; color: #333; cursor: pointer; border-radius: 50%;
            font-size: 16px; display: flex; align-items: center; justify-content: center;
            z-index: 5; box-shadow: var(--shadow); transition: var(--transition);
        }

        .modal-close-btn:hover { background: #fff; transform: scale(1.08); }

        .modal-content-body { padding: 22px 18px 32px; }

        .modal-meta-row { display: flex; align-items: center; gap: 6px; margin-bottom: 8px; }

        .modal-tag-badge {
            display: inline-block; padding: 5px 12px;
            background: var(--gold-light); color: var(--gold-dark);
            font-size: 9px; font-weight: 700; border-radius: 20px;
        }

        .modal-recipe-title {
            font-size: 22px; font-weight: 800; color: #1a1a1a;
            margin-bottom: 12px; line-height: 1.3;
        }

        .modal-info-pills { display: flex; gap: 8px; margin-bottom: 22px; flex-wrap: wrap; }

        .info-pill-item {
            display: flex; align-items: center; gap: 5px;
            padding: 8px 14px; background: #faf8f4; border-radius: 25px;
            font-size: 10px; font-weight: 600; color: #666; border: 1px solid #f0ede8;
        }

        .info-pill-item .pill-icon { font-size: 15px; }

        .modal-section-block { margin-bottom: 22px; }

        .section-heading-text {
            font-size: 13px; font-weight: 700; color: #1a1a1a;
            margin-bottom: 10px; display: flex; align-items: center; gap: 8px;
        }

        .section-heading-text::after {
            content: ''; flex: 1; height: 1px; background: #f0ede8;
        }

        .ingredients-list-group { list-style: none; display: flex; flex-direction: column; gap: 5px; }

        .ingredient-row-item {
            display: flex; align-items: center; gap: 10px;
            font-size: 11px; color: #444; padding: 10px 14px;
            background: #fafaf8; border-radius: 10px; border: 1px solid #f5f2ec;
            transition: all 0.2s;
        }

        .ingredient-row-item:hover { background: #fdfaf3; border-color: #f0e8d0; }

        .ingredient-bullet-dot {
            width: 6px; height: 6px; background: var(--gold);
            border-radius: 50%; flex-shrink: 0;
        }

        .instructions-text-block {
            font-size: 11px; color: #444; line-height: 1.9; white-space: pre-line;
        }

        .btn-actions-row { display: flex; flex-direction: column; gap: 8px; margin-top: 8px; }

        .btn-favorite-action {
            width: 100%; padding: 13px; background: #fafaf8;
            border: 1.5px solid #f0ede8; color: #666;
            cursor: pointer; border-radius: 14px;
            font-size: 12px; font-weight: 700; transition: var(--transition);
            font-family: 'Cairo', sans-serif;
        }

        .btn-favorite-action:hover { background: #fdf5f5; border-color: var(--red); color: var(--red); }
        .btn-favorite-action.liked { background: var(--red); color: #fff; border-color: var(--red); }

        .btn-youtube-link-action {
            width: 100%; padding: 13px; background: #ff0000; color: #fff;
            border: none; cursor: pointer; border-radius: 14px;
            font-size: 12px; font-weight: 700; font-family: 'Cairo', sans-serif;
            display: flex; align-items: center; justify-content: center; gap: 8px;
            text-decoration: none; transition: var(--transition);
        }

        .btn-youtube-link-action:hover { background: #cc0000; }

        /* ==================== STATES ==================== */
        .loading-state-box {
            grid-column: 1 / -1; text-align: center; padding: 50px 20px; color: #bbb;
        }

        .loading-ring-spinner {
            width: 42px; height: 42px; border: 3px solid #f0ede8;
            border-top-color: var(--gold); border-radius: 50%;
            animation: spinRotate 0.8s linear infinite; margin: 0 auto 12px;
        }

        @keyframes spinRotate { to { transform: rotate(360deg); } }

        .loading-state-text { font-size: 11px; font-weight: 600; }

        .empty-state-box { grid-column: 1 / -1; text-align: center; padding: 50px 20px; }

        .empty-state-icon {
            font-size: 50px; display: block; margin-bottom: 10px; opacity: 0.4;
            animation: emptyBounce 3s ease-in-out infinite;
        }

        @keyframes emptyBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .empty-state-title { font-size: 13px; font-weight: 700; color: #999; margin-bottom: 4px; }
        .empty-state-sub { font-size: 10px; color: #bbb; }

        /* ==================== TOAST ==================== */
        .toast-notification {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #1a1a1a; color: #fff; padding: 12px 24px;
            border-radius: 30px; font-size: 10px; font-weight: 600;
            z-index: 300; transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
            font-family: 'Cairo', sans-serif; white-space: nowrap;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            display: flex; align-items: center; gap: 6px;
        }

        .toast-notification.show { transform: translateX(-50%) translateY(0); }

        .toast-dot-pulse {
            width: 8px; height: 8px; background: var(--green);
            border-radius: 50%; animation: dotPulse 1s ease-in-out infinite;
        }

        .refresh-bar-top {
            text-align: center; padding: 7px; background: #fdfaf3;
            color: var(--gold-dark); font-size: 9px; font-weight: 700;
            cursor: pointer; border-bottom: 1px solid var(--border);
            font-family: 'Cairo', sans-serif; transition: var(--transition);
        }

        .refresh-bar-top:hover { background: #faf5e6; }
    </style>
</head>
<body>
    <!-- Particles -->
    <div class="particles-bg" id="particlesBg"></div>

    <div class="app">
        <!-- ==================== SPLASH ==================== -->
        <div class="splash-screen" id="splashScreen">
            <div class="splash-logo">
                <div class="splash-logo-ring1"></div>
                <div class="splash-logo-ring2"></div>
                <div class="splash-logo-core">
                    🍳
                    <span class="splash-spark"></span>
                    <span class="splash-spark"></span>
                    <span class="splash-spark"></span>
                </div>
            </div>
            <div class="splash-title">طبّاخ برو</div>
            <div class="splash-sub">✦ الإصدار الأسطوري ✦</div>
            <div class="splash-loader"><div class="splash-loader-fill"></div></div>
        </div>

        <!-- ==================== HEADER ==================== -->
        <div class="header">
            <div class="brand">
                <div class="logo-icon">
                    🍳
                    <span class="logo-dot"></span>
                </div>
                <div class="brand-text">
                    <h1>طبّاخ برو</h1>
                    <span>وصفات عربية وعالمية</span>
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
            <div class="stat-box"><span class="stat-num" id="statTotal">-</span><span class="stat-lbl">وصفة</span></div>
            <div class="stat-box"><span class="stat-num" id="statFavs">0</span><span class="stat-lbl">مفضلة</span></div>
            <div class="stat-box"><span class="stat-num" id="statOnline">0</span><span class="stat-lbl">أونلاين</span></div>
            <div class="stat-box"><span class="stat-num">⭐</span><span class="stat-lbl">تقييم</span></div>
        </div>

        <!-- ==================== REFRESH ==================== -->
        <div class="refresh-bar-top" onclick="fetchRecipes()">🔄 اسحب للتحديث وجلب وصفات جديدة من العالم</div>

        <!-- ==================== SEARCH ==================== -->
        <div class="search-bar">
            <div class="search-input-wrap">
                <input type="text" class="search-input" placeholder="ابحث عن وصفة..." id="searchInput" onkeypress="if(event.key==='Enter')searchRecipes()">
                <button class="search-icon-btn" onclick="searchRecipes()">🔍</button>
            </div>
        </div>

        <!-- ==================== CATEGORIES ==================== -->
        <div class="cat-scroll" id="catFilter">
            <button class="cat-chip active" data-cat="all" onclick="filterCat('all', this)">🍽️ الكل</button>
            <button class="cat-chip" data-cat="main" onclick="filterCat('main', this)">🍖 رئيسية</button>
            <button class="cat-chip" data-cat="rice" onclick="filterCat('rice', this)">🍚 أرز</button>
            <button class="cat-chip" data-cat="appetizer" onclick="filterCat('appetizer', this)">🥗 مقبلات</button>
            <button class="cat-chip" data-cat="sweet" onclick="filterCat('sweet', this)">🍯 حلويات</button>
            <button class="cat-chip" data-cat="drink" onclick="filterCat('drink', this)">☕ مشروبات</button>
        </div>

        <!-- ==================== CONTENT ==================== -->
        <div class="content" id="contentArea">
            <div class="loading-state-box">
                <div class="loading-ring-spinner"></div>
                <div class="loading-state-text">جاري تحميل أشهى الوصفات...</div>
            </div>
        </div>
    </div>

    <!-- ==================== MODAL ==================== -->
    <div class="modal-overlay" id="modalOverlay"><div class="modal" id="modal"></div></div>

    <!-- ==================== TOAST ==================== -->
    <div class="toast-notification" id="toast">
        <span class="toast-dot-pulse"></span>
        <span id="toastText"></span>
    </div>

    <script>
        // ==================== PARTICLES ====================
        (function() {
            const container = document.getElementById('particlesBg');
            for (let i = 0; i < 30; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                p.style.left = Math.random() * 100 + '%';
                const size = Math.random() * 3 + 1;
                p.style.width = size + 'px';
                p.style.height = size + 'px';
                p.style.animationDuration = (Math.random() * 8 + 4) + 's';
                p.style.animationDelay = (Math.random() * 6) + 's';
                container.appendChild(p);
            }
        })();

        // ==================== SPLASH ====================
        setTimeout(() => {
            document.getElementById('splashScreen').classList.add('hidden');
        }, 1800);

        // ==================== STATE ====================
        let allRecipes = [];
        let favorites = JSON.parse(localStorage.getItem('tbakh_legend_favs') || '[]');
        let showFavs = false;
        let currentCat = 'all';

        // ==================== ARABIC RECIPES ====================
        const arabicRecipes = [
            { id:'ar1', title:'كبسة الدجاج السعودية', cat:'rice', area:'سعودي', time:'90 د', img:'🍗', badge:'الأكثر شعبية', ings:['دجاجة كاملة','3 أكواب أرز بسمتي','2 بصل','4 طماطم','بهارات كبسة','زبيب ولوز'], steps:'حمّر الدجاج حتى يصبح ذهبياً.\nأضف البصل وقلّب حتى يذبل.\nأضف الطماطم والبهارات واطبخ 10 دقائق.\nأضف 4 أكواب ماء واتركه يغلي.\nأضف الأرز واتركه على نار هادئة 30 دقيقة.\nزيّن بالزبيب واللوز المحمص.' },
            { id:'ar2', title:'مندي اللحم', cat:'rice', area:'يمني', time:'180 د', img:'🥩', ings:['2 كيلو لحم غنم','3 أكواب أرز','بهارات مندي','فحم','زعفران','مكسرات'], steps:'تبّل اللحم واتركه ساعتين.\nاطبخ اللحم في قدر الضغط 45 دقيقة.\nاسلق الأرز في مرق اللحم.\nضع الفحم المشتعل للتدخين 10 دقائق.\nقدّم مع المكسرات.' },
            { id:'ar3', title:'شاورما الدجاج', cat:'main', area:'عربي', time:'40 د', img:'🌯', badge:'سريعة', ings:['صدر دجاج','بهارات شاورما','ثومية','مخلل','بطاطس','خبز صاج'], steps:'قطّع الدجاج شرائح.\nتبّل واتركه 30 دقيقة.\nاقلي على نار عالية.\nادهن الخبز بالثومية.\nأضف الحشوة ولفّ.' },
            { id:'ar4', title:'مقلوبة فلسطينية', cat:'rice', area:'فلسطيني', time:'90 د', img:'🍲', ings:['دجاج','أرز','باذنجان','قرنبيط','بطاطا','بهارات'], steps:'اسلق الدجاج.\nاقلي الخضار.\nرصّ في القدر.\nاسكب المرق واطبخ 30 دقيقة.\nاقلب القدر وقدم.' },
            { id:'ar5', title:'منسف أردني', cat:'main', area:'أردني', time:'120 د', img:'🍖', ings:['لحم غنم','جميد','أرز','خبز شراك','صنوبر'], steps:'انقع الجميد.\nاطبخ اللحم.\nضع الخبز ثم الأرز واللحم.\nاسكب الجميد وزين.' },
            { id:'ar6', title:'حمص بيروتي', cat:'appetizer', area:'لبناني', time:'15 د', img:'🫒', badge:'مشهور', ings:['حمص','طحينة','ليمون','ثوم','زيت زيتون','كمون'], steps:'اسلق الحمص.\nاهرسه مع الطحينة والليمون.\nزين بزيت الزيتون ورش الكمون.' },
            { id:'ar7', title:'متبل باذنجان', cat:'appetizer', area:'شامي', time:'25 د', img:'🍆', ings:['باذنجان','طحينة','ليمون','ثوم','زيت زيتون'], steps:'اشوِ الباذنجان.\nقشّره واهرسه.\nأضف الطحينة والليمون.\nزيّن بزيت الزيتون.' },
            { id:'ar8', title:'كنافة نابلسية', cat:'sweet', area:'فلسطيني', time:'60 د', img:'🧀', badge:'الألذ', ings:['عجينة كنافة','جبن عكاوي','سمن','قطر','فستق'], steps:'فتّت العجينة واخلطها بالسمن.\nضع نصفها ثم الجبن.\nأضف الباقي واخبز.\nاسكب القطر وزين.' },
            { id:'ar9', title:'بقلاوة تركية', cat:'sweet', area:'تركي', time:'60 د', img:'🥮', ings:['جلاش','جوز','سمن','قطر','فستق'], steps:'ضع طبقات الجلاش مع الجوز.\nاخبز 45 دقيقة.\nاسكب القطر البارد.' },
            { id:'ar10', title:'أم علي', cat:'sweet', area:'مصري', time:'35 د', img:'🥣', ings:['بف باستري','حليب','قشطة','مكسرات','زبيب'], steps:'اخبز البف باستري وفتته.\nأضف الحليب والمكسرات.\nاخبز 20 دقيقة وقدم.' },
            { id:'ar11', title:'كباب عراقي', cat:'main', area:'عراقي', time:'30 د', img:'🥙', badge:'مشوي', ings:['لحم مفروم','بصل','بقدونس','بهارات'], steps:'اخلط اللحم مع البصل.\nشكّل على أسياخ.\nاشوِ وقدم.' },
            { id:'ar12', title:'شكشوكة مغربية', cat:'main', area:'مغربي', time:'20 د', img:'🍳', ings:['بيض','طماطم','بصل','فلفل','كمون'], steps:'اقلي البصل والفلفل.\nأضف الطماطم.\nاكسر البيض وغطّ.' },
            { id:'ar13', title:'قهوة عربية', cat:'drink', area:'عربي', time:'20 د', img:'🫖', badge:'أصيلة', ings:['بن عربي','هيل','زعفران','ماء','تمر'], steps:'اغلِ الماء.\nأضف البن.\nأضف الهيل.\nاتركه يهدأ واسكب.' },
            { id:'ar14', title:'شاي عدني', cat:'drink', area:'يمني', time:'15 د', img:'☕', ings:['شاي أحمر','حليب مكثف','هيل','زنجبيل'], steps:'اغلِ الماء مع البهارات.\nأضف الشاي.\nصفّ وأضف الحليب.' },
            { id:'ar15', title:'معصوب يمني', cat:'sweet', area:'يمني', time:'20 د', img:'🍌', ings:['خبز بر','موز','قشطة','عسل','تمر'], steps:'فتّت الخبز.\nاهرس الموز.\nأضف القشطة.\nاسكب العسل.' }
        ];

        // ==================== FETCH ====================
        async function fetchRecipes(query) {
            const area = document.getElementById('contentArea');
            area.innerHTML = '<div class="loading-state-box"><div class="loading-ring-spinner"></div><div class="loading-state-text">جاري تحميل الوصفات...</div></div>';

            let fetched = [];
            try {
                const q = query || 'chicken';
                const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${encodeURIComponent(q)}`);
                const data = await res.json();
                if (data.meals) {
                    fetched = data.meals.map(m => ({
                        id: m.idMeal, title: m.strMeal, cat: m.strCategory || 'عام',
                        area: m.strArea || 'عالمي', time: '30-45 د',
                        img: m.strMealThumb || '', badge: '',
                        yt: m.strYoutube || '', ings: getIngs(m), steps: m.strInstructions || ''
                    }));
                }
                allRecipes = [...arabicRecipes, ...fetched];
                render(); updateStats();
            } catch(e) { allRecipes = arabicRecipes; render(); updateStats(); }
        }

        function getIngs(m) {
            const ings = [];
            for (let i = 1; i <= 20; i++) {
                const ing = m['strIngredient' + i], meas = m['strMeasure' + i];
                if (ing && ing.trim()) ings.push(meas ? `${meas.trim()} ${ing.trim()}` : ing.trim());
            }
            return ings.length ? ings : ['مكونات متنوعة'];
        }

        async function searchRecipes() {
            const q = document.getElementById('searchInput').value.trim();
            if (!q) return showToast('⚠️ اكتب اسم الوصفة');
            await fetchRecipes(q);
        }

        // ==================== RENDER ====================
        function render() {
            const area = document.getElementById('contentArea');
            const search = document.getElementById('searchInput').value.trim();
            let list = allRecipes;
            if (currentCat !== 'all') list = list.filter(r => r.cat === currentCat);
            if (showFavs) list = list.filter(r => favorites.includes(r.id));
            if (search) list = list.filter(r => r.title.includes(search) || r.ings?.some(i => i.includes(search)));

            updateStats();
            if (!list.length) {
                area.innerHTML = '<div class="empty-state-box"><span class="empty-state-icon">🍽️</span><div class="empty-state-title">لا توجد وصفات</div><div class="empty-state-sub">جرب البحث عن شيء آخر</div></div>';
                return;
            }

            area.innerHTML = list.map(r => {
                const isFav = favorites.includes(r.id);
                const catNames = { main:'رئيسي', rice:'أرز', appetizer:'مقبلات', sweet:'حلويات', drink:'مشروبات' };
                const catName = catNames[r.cat] || r.cat || 'عام';
                const hasImage = r.img && r.img.startsWith('http');
                const imgHTML = hasImage 
                    ? `<img src="${r.img}" alt="${r.title}" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='block'"><span class="emoji-placeholder" style="display:none">🍽️</span>`
                    : `<span class="emoji-placeholder" style="display:block">${r.img||'🍽️'}</span>`;

                const badgeHTML = r.badge ? `<span class="card-badge-top">🏆 ${r.badge}</span>` : '';

                return `
                    <div class="card" onclick="openModal('${r.id}')">
                        <div class="card-img">
                            ${imgHTML}
                            <div class="card-img-overlay"></div>
                            ${badgeHTML}
                            <span class="card-time-badge">⏱ ${r.time}</span>
                            <button class="card-fav-btn ${isFav?'liked':''}" onclick="event.stopPropagation();toggleFav('${r.id}')">${isFav?'❤️':'🤍'}</button>
                        </div>
                        <div class="card-body">
                            <span class="card-tag">${catName}</span>
                            <div class="card-title">${r.title}</div>
                            <div class="card-footer-row">
                                <span class="card-area-text">🌍 ${r.area||'عالمي'}</span>
                                <span class="card-rating">⭐</span>
                            </div>
                        </div>
                    </div>`;
            }).join('');
        }

        function updateStats() {
            const localCount = arabicRecipes.length;
            const onlineCount = allRecipes.length - localCount;
            document.getElementById('statTotal').textContent = allRecipes.length;
            document.getElementById('statFavs').textContent = favorites.length;
            document.getElementById('statOnline').textContent = Math.max(0, onlineCount);
            const b = document.getElementById('favBadge');
            b.textContent = favorites.length;
            b.classList.toggle('show', favorites.length > 0);
        }

        // ==================== FILTERS ====================
        function filterCat(cat, btn) {
            currentCat = cat;
            document.querySelectorAll('.cat-chip').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            render();
        }

        function toggleFavFilter() {
            showFavs = !showFavs;
            document.getElementById('favFilterBtn').classList.toggle('active', showFavs);
            render();
            showToast(showFavs ? '❤️ عرض المفضلة' : '🌍 عرض الكل');
        }

        function toggleFav(id) {
            favorites = favorites.includes(id) ? favorites.filter(f => f !== id) : [...favorites, id];
            localStorage.setItem('tbakh_legend_favs', JSON.stringify(favorites));
            updateStats(); render();
        }

        // ==================== MODAL ====================
        function openModal(id) {
            const r = allRecipes.find(x => x.id.toString() === id.toString());
            if (!r) return;
            const isFav = favorites.includes(r.id);
            const catNames = { main:'رئيسي', rice:'أرز', appetizer:'مقبلات', sweet:'حلويات', drink:'مشروبات' };
            const catName = catNames[r.cat] || r.cat || 'عام';
            const hasImage = r.img && r.img.startsWith('http');
            const imgHTML = hasImage 
                ? `<img src="${r.img}" alt="${r.title}" onerror="this.style.display='none';this.nextElementSibling.style.display='block'"><span class="emoji-placeholder" style="display:none">🍽️</span>`
                : `<span class="emoji-placeholder" style="display:block">${r.img||'🍽️'}</span>`;

            document.getElementById('modal').innerHTML = `
                <div class="modal-handle-bar"></div>
                <div class="modal-hero-image">
                    ${imgHTML}
                    <button class="modal-close-btn" onclick="closeModal()">✕</button>
                </div>
                <div class="modal-content-body">
                    <div class="modal-meta-row">
                        <span class="modal-tag-badge">${catName}</span>
                        <span style="font-size:9px;color:#999">${r.area||'عالمي'}</span>
                    </div>
                    <div class="modal-recipe-title">${r.title}</div>
                    <div class="modal-info-pills">
                        <div class="info-pill-item"><span class="pill-icon">⏱</span>${r.time}</div>
                        <div class="info-pill-item"><span class="pill-icon">🌍</span>${r.area||'عالمي'}</div>
                        <div class="info-pill-item"><span class="pill-icon">📋</span>${(r.ings||[]).length} مكونات</div>
                    </div>
                    <div class="modal-section-block">
                        <div class="section-heading-text">🛒 المقادير</div>
                        <ul class="ingredients-list-group">${(r.ings||['مكونات متنوعة']).map(i => `<li class="ingredient-row-item"><span class="ingredient-bullet-dot"></span>${i}</li>`).join('')}</ul>
                    </div>
                    <div class="modal-section-block">
                        <div class="section-heading-text">👨‍🍳 طريقة التحضير</div>
                        <div class="instructions-text-block">${r.steps||'暂无说明'}</div>
                    </div>
                    <div class="btn-actions-row">
                        ${r.yt ? `<a href="${r.yt}" target="_blank" class="btn-youtube-link-action">▶️ شاهد الفيديو على يوتيوب</a>` : ''}
                        <button class="btn-favorite-action ${isFav?'liked':''}" onclick="toggleFav('${r.id}');closeModal();showToast('${isFav?'💔 تمت الإزالة':'❤️ تمت الإضافة'}')">${isFav?'❤️ إزالة من المفضلة':'🤍 أضف إلى المفضلة'}</button>
                    </div>
                </div>`;
            document.getElementById('modalOverlay').classList.add('show');
        }

        function closeModal() { document.getElementById('modalOverlay').classList.remove('show'); }
        document.getElementById('modalOverlay').addEventListener('click', function(e) { if (e.target === this) closeModal(); });

        // ==================== TOAST ====================
        function showToast(msg) {
            const t = document.getElementById('toast');
            document.getElementById('toastText').textContent = msg;
            t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2200);
        }

        // ==================== PULL TO REFRESH ====================
        let touchStartY = 0;
        document.addEventListener('touchstart', e => { touchStartY = e.touches[0].clientY; });
        document.addEventListener('touchend', e => {
            const dy = e.changedTouches[0].clientY - touchStartY;
            if (dy > 100) fetchRecipes();
        });

        // ==================== INIT ====================
        updateStats(); fetchRecipes();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  👑 طبّاخ برو - الإصدار الأسطوري       ║")
    print("║  🍳 1000+ سطر من الإبداع               ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html - {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("✨ المميزات الأسطورية الجديدة:")
    print("  🎬 Splash Screen متحرك عند الفتح")
    print("  ✨ 30 جسيم ذهبي في الخلفية")
    print("  💫 حلقات دائرية حول الشعار")
    print("  ⚡ بريق متحرك حول الأيقونة")
    print("  🏆 شارات للوصفات المميزة")
    print("  📊 4 إحصائيات (وصفات، مفضلة، أونلاين، تقييم)")
    print("  🔔 Toast بنبض أخضر")
    print("  🎯 Pull-to-Refresh")
    print("  💳 بطاقات بتأثير hover وتكبير الصورة")
    print("  📱 مودال أنيق مع blur")
    print("  🎨 أيقونات متحركة أيونية")

if __name__ == "__main__":
    create_website_files()

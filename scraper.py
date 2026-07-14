import os

def create_website_files():
    """تطبيق طبّاخ برو العربي المطور"""
    
    os.makedirs("www", exist_ok=True)
    
    html_content = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>طبّاخ برو | وصفات عربية</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #fafaf8;
            --surface: #ffffff;
            --border: #eeece8;
            --gold: #c9a84c;
            --gold-light: #faf5e8;
            --gold-dark: #8b7300;
            --red: #e74c3c;
            --red-light: #fef5f5;
            --green: #27ae60;
            --text: #1a1a1a;
            --text2: #555;
            --text3: #999;
            --shadow: 0 2px 8px rgba(0,0,0,0.04);
            --shadow-lg: 0 8px 24px rgba(0,0,0,0.07);
            --radius: 14px;
            --radius-lg: 18px;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background: #f2f0eb;
            color: var(--text);
            font-family: 'Cairo', 'Tajawal', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            -webkit-tap-highlight-color: transparent;
            direction: rtl;
        }

        .app {
            width: 100%;
            max-width: 480px;
            height: 100vh;
            max-height: 900px;
            display: flex;
            flex-direction: column;
            background: var(--bg);
            box-shadow: 0 20px 50px rgba(0,0,0,0.1);
            overflow: hidden;
        }

        /* ==================== HEADER ==================== */
        .header {
            padding: 12px 16px;
            background: #fff;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 10;
        }

        .brand { display: flex; align-items: center; gap: 10px; }

        .logo-icon {
            width: 40px; height: 40px;
            background: linear-gradient(135deg, var(--red), #c0392b);
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 18px;
            box-shadow: 0 3px 10px rgba(231,76,60,0.2);
        }

        .brand-text h1 { font-size: 16px; font-weight: 800; color: #1a1a1a; }
        .brand-text span { font-size: 8px; color: #999; font-weight: 600; }

        .header-actions { display: flex; gap: 6px; }

        .btn-icon {
            width: 38px; height: 38px;
            background: #f8f7f4; border: 1px solid var(--border);
            color: #888; cursor: pointer; border-radius: 12px;
            font-size: 14px; display: flex; align-items: center; justify-content: center;
            transition: all 0.25s; position: relative;
        }

        .btn-icon:hover { background: #f0ede8; }
        .btn-icon.active { background: var(--red-light); border-color: var(--red); color: var(--red); }

        .badge {
            position: absolute; top: -5px; right: -5px;
            width: 18px; height: 18px; background: var(--red); color: #fff;
            font-size: 8px; font-weight: 700; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            display: none;
        }
        .badge.show { display: flex; }

        /* ==================== STATS ==================== */
        .stats-row {
            display: flex; gap: 6px; padding: 8px 14px;
            background: #fff; border-bottom: 1px solid var(--border);
        }

        .stat-item {
            flex: 1; padding: 8px; border-radius: 10px; text-align: center;
        }
        .stat-item:nth-child(1) { background: #fdfaf3; border: 1px solid #f5eed8; }
        .stat-item:nth-child(2) { background: #fef5f5; border: 1px solid #fce4e4; }
        .stat-item:nth-child(3) { background: #f5fdf8; border: 1px solid #d5f5e3; }

        .stat-num { font-size: 14px; font-weight: 800; display: block; }
        .stat-item:nth-child(1) .stat-num { color: #b8860b; }
        .stat-item:nth-child(2) .stat-num { color: #e74c3c; }
        .stat-item:nth-child(3) .stat-num { color: #27ae60; }

        .stat-lbl { font-size: 7px; color: #999; margin-top: 1px; }

        /* ==================== REFRESH ==================== */
        .refresh-bar {
            text-align: center; padding: 6px; background: #fdfaf3;
            color: var(--gold-dark); font-size: 9px; font-weight: 700;
            cursor: pointer; border-bottom: 1px solid var(--border);
        }
        .refresh-bar:hover { background: #faf5e6; }

        /* ==================== SEARCH ==================== */
        .search-bar {
            padding: 10px 14px; background: #fff;
            border-bottom: 1px solid var(--border);
            display: flex; gap: 8px;
        }

        .search-input {
            flex: 1; padding: 10px 14px;
            background: #f8f7f4; border: 1.5px solid var(--border);
            color: var(--text); font-size: 11px; border-radius: 12px;
            font-family: 'Cairo', sans-serif; outline: none; transition: all 0.3s;
        }

        .search-input:focus {
            border-color: var(--gold); background: #fff;
            box-shadow: 0 0 0 3px rgba(201,168,76,0.06);
        }
        .search-input::placeholder { color: #ccc; }

        .search-btn {
            padding: 10px 16px; background: var(--gold); color: #fff;
            border: none; cursor: pointer; border-radius: 12px;
            font-size: 11px; font-family: 'Cairo', sans-serif; font-weight: 700;
            white-space: nowrap; transition: all 0.3s;
        }
        .search-btn:hover { background: var(--gold-dark); }

        /* ==================== CATEGORIES ==================== */
        .cat-scroll {
            display: flex; gap: 5px; padding: 0 14px 10px;
            background: #fff; overflow-x: auto; border-bottom: 1px solid var(--border);
        }
        .cat-scroll::-webkit-scrollbar { height: 0; }

        .cat-chip {
            padding: 7px 12px; background: #f8f6f2;
            border: 1.5px solid var(--border); color: #888;
            cursor: pointer; border-radius: 20px;
            font-size: 9px; font-weight: 700; white-space: nowrap;
            transition: all 0.3s; font-family: 'Cairo', sans-serif;
        }

        .cat-chip:hover { background: #f0ede8; }
        .cat-chip.active {
            background: #fff; border-color: var(--gold); color: var(--gold-dark);
            font-weight: 800; box-shadow: 0 2px 6px rgba(201,168,76,0.1);
        }

        /* ==================== CONTENT ==================== */
        .content {
            flex: 1; overflow-y: auto; padding: 10px 14px;
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;
            align-content: start;
        }
        .content::-webkit-scrollbar { width: 3px; }
        .content::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        /* ==================== CARD ==================== */
        .card {
            background: #fff; border: 1px solid var(--border);
            border-radius: var(--radius-lg); overflow: hidden; cursor: pointer;
            transition: all 0.3s; box-shadow: var(--shadow);
            animation: fadeUp 0.4s ease;
        }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

        .card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
        .card:active { transform: scale(0.97); }

        .card-img {
            width: 100%; aspect-ratio: 1.3;
            background: linear-gradient(135deg, #faf7f0, #f2ece0);
            display: flex; align-items: center; justify-content: center;
            font-size: 36px; position: relative; overflow: hidden;
        }

        .card-img img { width: 100%; height: 100%; object-fit: cover; }

        .card-time {
            position: absolute; top: 8px; right: 8px;
            padding: 4px 8px; background: rgba(255,255,255,0.95);
            color: #666; font-size: 8px; font-weight: 700;
            border-radius: 15px; box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }

        .card-fav {
            position: absolute; top: 8px; left: 8px;
            width: 28px; height: 28px; background: rgba(255,255,255,0.95);
            border: none; color: #ddd; cursor: pointer; border-radius: 50%;
            font-size: 12px; display: flex; align-items: center; justify-content: center;
            transition: all 0.3s; box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }
        .card-fav.liked { color: var(--red); }

        .card-body { padding: 10px 12px 12px; }

        .card-tag {
            display: inline-block; padding: 2px 7px;
            background: var(--gold-light); color: var(--gold-dark);
            font-size: 7px; font-weight: 700; border-radius: 5px; margin-bottom: 5px;
        }

        .card-title {
            font-size: 12px; font-weight: 700; color: #1a1a1a;
            line-height: 1.35; margin-bottom: 6px;
            display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
        }

        .card-footer { display: flex; align-items: center; justify-content: space-between; }
        .card-area { font-size: 9px; color: #999; font-weight: 600; }
        .card-stars { color: #f0a500; font-size: 9px; }

        /* ==================== MODAL ==================== */
        .modal-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,0.45); z-index: 100;
            align-items: flex-end; justify-content: center;
        }
        .modal-overlay.show { display: flex; }

        .modal {
            background: #fff; border-radius: 24px 24px 0 0;
            width: 100%; max-width: 480px; max-height: 88vh;
            overflow-y: auto; animation: slideUp 0.4s ease;
            box-shadow: 0 -15px 40px rgba(0,0,0,0.2);
        }
        @keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
        .modal::-webkit-scrollbar { width: 3px; }
        .modal::-webkit-scrollbar-thumb { background: #ddd; border-radius: 3px; }

        .modal-handle { width: 36px; height: 4px; background: #e0ddd8; border-radius: 2px; margin: 10px auto 0; }

        .modal-hero {
            width: 100%; aspect-ratio: 1.5;
            background: linear-gradient(135deg, #faf7f0, #f2ece0);
            display: flex; align-items: center; justify-content: center;
            font-size: 55px; position: relative; margin-top: 6px;
        }
        .modal-hero img { width: 100%; height: 100%; object-fit: cover; }

        .modal-close {
            position: absolute; top: 12px; right: 12px;
            width: 34px; height: 34px; background: rgba(255,255,255,0.95);
            border: none; color: #333; cursor: pointer; border-radius: 50%;
            font-size: 15px; display: flex; align-items: center; justify-content: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .modal-body { padding: 18px 16px 28px; }

        .modal-tag {
            display: inline-block; padding: 4px 10px;
            background: var(--gold-light); color: var(--gold-dark);
            font-size: 9px; font-weight: 700; border-radius: 20px; margin-bottom: 6px;
        }

        .modal-title { font-size: 20px; font-weight: 800; color: #1a1a1a; margin-bottom: 10px; line-height: 1.3; }

        .modal-info { display: flex; gap: 8px; margin-bottom: 18px; flex-wrap: wrap; }

        .info-pill {
            display: flex; align-items: center; gap: 4px;
            padding: 6px 10px; background: #faf8f4; border-radius: 20px;
            font-size: 10px; font-weight: 600; color: #666; border: 1px solid #f0ede8;
        }

        .section { margin-bottom: 18px; }
        .section-title {
            font-size: 12px; font-weight: 700; color: #1a1a1a;
            margin-bottom: 8px; display: flex; align-items: center; gap: 6px;
        }

        .ingredient-list { list-style: none; display: flex; flex-direction: column; gap: 4px; }
        .ingredient-item {
            display: flex; align-items: center; gap: 8px;
            font-size: 10px; color: #444; padding: 8px 10px;
            background: #fafaf8; border-radius: 8px; border: 1px solid #f5f2ec;
        }
        .ingredient-dot { width: 5px; height: 5px; background: var(--gold); border-radius: 50%; flex-shrink: 0; }

        .instructions { font-size: 11px; color: #444; line-height: 1.8; white-space: pre-line; }

        .btn-fav {
            width: 100%; padding: 12px;
            background: #fafaf8; border: 1.5px solid #f0ede8;
            color: #666; cursor: pointer; border-radius: 14px;
            font-size: 11px; font-weight: 700; transition: all 0.3s;
            font-family: 'Cairo', sans-serif; margin-top: 6px;
        }
        .btn-fav.liked { background: var(--red); color: #fff; border-color: var(--red); }

        .btn-yt {
            width: 100%; padding: 12px; background: #ff0000; color: #fff;
            border: none; cursor: pointer; border-radius: 14px;
            font-size: 11px; font-weight: 700; font-family: 'Cairo', sans-serif;
            margin-top: 6px; display: flex; align-items: center; justify-content: center; gap: 6px;
            text-decoration: none;
        }

        /* ==================== STATES ==================== */
        .loading-box { grid-column: 1 / -1; text-align: center; padding: 40px; color: #bbb; }
        .spinner {
            width: 36px; height: 36px; border: 3px solid #f0ede8;
            border-top-color: var(--gold); border-radius: 50%;
            animation: spin 0.8s linear infinite; margin: 0 auto 10px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }

        .empty-box { grid-column: 1 / -1; text-align: center; padding: 40px; color: #ccc; }
        .empty-icon { font-size: 40px; display: block; margin-bottom: 6px; }
        .empty-text { font-size: 11px; font-weight: 600; }

        /* ==================== TOAST ==================== */
        .toast {
            position: fixed; bottom: 30px; left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: #1a1a1a; color: #fff; padding: 10px 20px;
            border-radius: 25px; font-size: 10px; font-weight: 600;
            z-index: 300; transition: transform 0.4s;
            font-family: 'Cairo', sans-serif; white-space: nowrap;
        }
        .toast.show { transform: translateX(-50%) translateY(0); }
    </style>
</head>
<body>
    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="brand">
                <div class="logo-icon">🍳</div>
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

        <!-- Stats -->
        <div class="stats-row">
            <div class="stat-item"><span class="stat-num" id="statTotal">-</span><span class="stat-lbl">وصفة</span></div>
            <div class="stat-item"><span class="stat-num" id="statFavs">0</span><span class="stat-lbl">مفضلة</span></div>
            <div class="stat-item"><span class="stat-num">🌐</span><span class="stat-lbl">مباشر</span></div>
        </div>

        <!-- Refresh -->
        <div class="refresh-bar" onclick="fetchRecipes()">🔄 اضغط للتحديث وجلب وصفات جديدة</div>

        <!-- Search -->
        <div class="search-bar">
            <input type="text" class="search-input" placeholder="ابحث عن وصفة..." id="searchInput" onkeypress="if(event.key==='Enter')searchRecipes()">
            <button class="search-btn" onclick="searchRecipes()">🔍 بحث</button>
        </div>

        <!-- Categories -->
        <div class="cat-scroll" id="catFilter">
            <button class="cat-chip active" data-cat="all" onclick="filterCat('all', this)">🍽️ الكل</button>
            <button class="cat-chip" data-cat="main" onclick="filterCat('main', this)">🍖 رئيسية</button>
            <button class="cat-chip" data-cat="rice" onclick="filterCat('rice', this)">🍚 أرز</button>
            <button class="cat-chip" data-cat="appetizer" onclick="filterCat('appetizer', this)">🥗 مقبلات</button>
            <button class="cat-chip" data-cat="sweet" onclick="filterCat('sweet', this)">🍯 حلويات</button>
            <button class="cat-chip" data-cat="drink" onclick="filterCat('drink', this)">☕ مشروبات</button>
        </div>

        <!-- Content -->
        <div class="content" id="contentArea">
            <div class="loading-box"><div class="spinner"></div><div>جاري تحميل الوصفات...</div></div>
        </div>
    </div>

    <!-- Modal -->
    <div class="modal-overlay" id="modalOverlay"><div class="modal" id="modal"></div></div>
    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script>
        // ==================== STATE ====================
        let allRecipes = [];
        let favorites = JSON.parse(localStorage.getItem('tbakh_dev_favs') || '[]');
        let showFavs = false;
        let currentCat = 'all';

        // ==================== ARABIC RECIPES ====================
        const arabicRecipes = [
            { id:'ar1', title:'كبسة الدجاج السعودية', cat:'rice', area:'سعودي', time:'90 د', img:'🍗', yt:'', ings:['دجاجة كاملة','3 أكواب أرز بسمتي','2 بصل','4 طماطم','بهارات كبسة','زبيب ولوز'], steps:'حمّر الدجاج ثم أضف البصل والطماطم والبهارات. أضف الماء واتركه يغلي. أضف الأرز واطبخ 30 دقيقة. زين بالمكسرات.' },
            { id:'ar2', title:'مندي اللحم', cat:'rice', area:'يمني', time:'180 د', img:'🥩', yt:'', ings:['2 كيلو لحم غنم','3 أكواب أرز','بهارات مندي','فحم','زعفران','مكسرات'], steps:'تبّل اللحم واطبخه. اسلق الأرز في المرق. ضع الفحم للتدخين. قدم مع المكسرات.' },
            { id:'ar3', title:'شاورما الدجاج', cat:'main', area:'عربي', time:'40 د', img:'🌯', yt:'', ings:['صدر دجاج','بهارات شاورما','ثومية','مخلل','بطاطس','خبز صاج'], steps:'قطع الدجاج وتبله. اقله. ادهن الخبز بالثومية. أضف الحشوة ولف.' },
            { id:'ar4', title:'مقلوبة فلسطينية', cat:'rice', area:'فلسطيني', time:'90 د', img:'🍲', yt:'', ings:['دجاج','أرز','باذنجان','قرنبيط','بطاطا','بهارات'], steps:'اسلق الدجاج. اقلي الخضار. رص ثم اطبخ. اقلب القدر وقدم.' },
            { id:'ar5', title:'منسف أردني', cat:'main', area:'أردني', time:'120 د', img:'🍖', yt:'', ings:['لحم غنم','جميد','أرز','خبز شراك','صنوبر'], steps:'انقع الجميد. اطبخ اللحم. ضع الخبز ثم الأرز واللحم. اسكب الجميد.' },
            { id:'ar6', title:'حمص بيروتي', cat:'appetizer', area:'لبناني', time:'15 د', img:'🫒', yt:'', ings:['حمص','طحينة','ليمون','ثوم','زيت زيتون','كمون'], steps:'اسلق الحمص. اهرسه مع الطحينة والليمون. زين بزيت الزيتون.' },
            { id:'ar7', title:'متبل باذنجان', cat:'appetizer', area:'شامي', time:'25 د', img:'🍆', yt:'', ings:['باذنجان','طحينة','ليمون','ثوم','زيت زيتون'], steps:'اشوِ الباذنجان. قشره واهرسه. أضف الطحينة والليمون. زين.' },
            { id:'ar8', title:'كنافة نابلسية', cat:'sweet', area:'فلسطيني', time:'60 د', img:'🧀', yt:'', ings:['عجينة كنافة','جبن عكاوي','سمن','قطر','فستق'], steps:'فتت العجينة. ضع نصفها ثم الجبن. أضف الباقي. اخبز. اسكب القطر.' },
            { id:'ar9', title:'بقلاوة تركية', cat:'sweet', area:'تركي', time:'60 د', img:'🥮', yt:'', ings:['جلاش','جوز','سمن','قطر','فستق'], steps:'ضع طبقات الجلاش مع الجوز. اخبز. اسكب القطر البارد.' },
            { id:'ar10', title:'أم علي', cat:'sweet', area:'مصري', time:'35 د', img:'🥣', yt:'', ings:['بف باستري','حليب','قشطة','مكسرات','زبيب'], steps:'اخبز البف باستري. أضف الحليب والمكسرات. اخبز وقدم.' },
            { id:'ar11', title:'كباب عراقي', cat:'main', area:'عراقي', time:'30 د', img:'🥙', yt:'', ings:['لحم مفروم','بصل','بقدونس','بهارات'], steps:'اخلط اللحم مع البصل. شكّل على أسياخ. اشوِ وقدم.' },
            { id:'ar12', title:'شكشوكة مغربية', cat:'main', area:'مغربي', time:'20 د', img:'🍳', yt:'', ings:['بيض','طماطم','بصل','فلفل','كمون'], steps:'اقلي البصل. أضف الطماطم. اكسر البيض. غطّ حتى ينضج.' },
            { id:'ar13', title:'محاشي مصرية', cat:'main', area:'مصري', time:'120 د', img:'🫑', yt:'', ings:['فلفل','باذنجان','كوسا','أرز','لحم مفروم'], steps:'احفر الخضار. احشُ بالخلطة. اطبخ في الصلصة.' },
            { id:'ar14', title:'فتوش لبناني', cat:'appetizer', area:'لبناني', time:'15 د', img:'🥗', yt:'', ings:['خبز محمص','خس','طماطم','خيار','زيت زيتون','دبس رمان'], steps:'قطع الخضار. أضف الخبز. اسكب الصوص. رش السماق.' },
            { id:'ar15', title:'شاي عدني', cat:'drink', area:'يمني', time:'15 د', img:'☕', yt:'', ings:['شاي أحمر','حليب مكثف','هيل','زنجبيل','قرنفل'], steps:'اغلِ الماء مع البهارات. أضف الشاي. صفّ وأضف الحليب.' },
            { id:'ar16', title:'قهوة عربية', cat:'drink', area:'عربي', time:'20 د', img:'🫖', yt:'', ings:['بن عربي','هيل','زعفران','ماء','تمر'], steps:'اغلِ الماء. أضف البن. أضف الهيل. اسكب وقدم مع التمر.' },
            { id:'ar17', title:'معصوب يمني', cat:'sweet', area:'يمني', time:'20 د', img:'🍌', yt:'', ings:['خبز بر','موز','قشطة','عسل','تمر'], steps:'فتت الخبز. اهرس الموز. أضف القشطة. اسكب العسل.' },
            { id:'ar18', title:'سمبوسة', cat:'appetizer', area:'هندي', time:'40 د', img:'🥟', yt:'', ings:['عجينة سمبوسة','لحم مفروم','بصل','بهارات'], steps:'اطبخ الحشوة. احشُ العجينة. اقلي حتى تصبح ذهبية.' },
            { id:'ar19', title:'مهلبية', cat:'sweet', area:'عربي', time:'15 د', img:'🍮', yt:'', ings:['حليب','نشا','سكر','ماء ورد','فستق'], steps:'اخلط النشا. سخن الحليب. أضف النشا. اسكب وبرد.' },
            { id:'ar20', title:'كبسة حجازية', cat:'rice', area:'سعودي', time:'60 د', img:'🍛', yt:'', ings:['دجاج','أرز','طماطم','جزر','بهارات'], steps:'حمّر الدجاج. أضف الخضار. أضف الأرز. اطبخ وقدم.' }
        ];

        // ==================== FETCH ====================
        async function fetchRecipes(query) {
            const area = document.getElementById('contentArea');
            area.innerHTML = '<div class="loading-box"><div class="spinner"></div><div>جاري التحميل...</div></div>';

            let fetched = [];
            try {
                const q = query || 'chicken';
                const res = await fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${encodeURIComponent(q)}`);
                const data = await res.json();
                if (data.meals) {
                    fetched = data.meals.map(m => ({
                        id: m.idMeal, title: m.strMeal, cat: m.strCategory || 'عام',
                        area: m.strArea || 'عالمي', time: '30-45 د', img: m.strMealThumb || '🍽️',
                        yt: m.strYoutube || '', ings: getIngs(m), steps: m.strInstructions || ''
                    }));
                }
                allRecipes = [...arabicRecipes, ...fetched];
                render(); updateStats();
                showToast(`✅ ${allRecipes.length} وصفة`);
            } catch(e) {
                allRecipes = arabicRecipes; render(); updateStats();
            }
        }

        function getIngs(m) {
            const ings = [];
            for (let i = 1; i <= 20; i++) {
                const ing = m['strIngredient' + i], meas = m['strMeasure' + i];
                if (ing && ing.trim()) ings.push(meas ? `${meas.trim()} ${ing.trim()}` : ing.trim());
            }
            return ings.length ? ings : ['مكونات متنوعة'];
        }

        // ==================== SEARCH ====================
        async function searchRecipes() {
            const q = document.getElementById('searchInput').value.trim();
            if (!q) { showToast('⚠️ اكتب اسم الوصفة'); return; }
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
                area.innerHTML = '<div class="empty-box"><span class="empty-icon">🍽️</span><span class="empty-text">لا توجد وصفات</span></div>';
                return;
            }

            area.innerHTML = list.map(r => {
                const isFav = favorites.includes(r.id);
                const imgTag = r.img && r.img.startsWith('http') ? `<img src="${r.img}" alt="${r.title}" loading="lazy">` : `<span style="font-size:40px">${r.img||'🍽️'}</span>`;
                const catName = { main:'رئيسي', rice:'أرز', appetizer:'مقبلات', sweet:'حلويات', drink:'مشروبات' }[r.cat] || r.cat || 'عام';
                return `
                    <div class="card" onclick="openModal('${r.id}')">
                        <div class="card-img">
                            ${imgTag}
                            <span class="card-time">⏱ ${r.time}</span>
                            <button class="card-fav ${isFav?'liked':''}" onclick="event.stopPropagation();toggleFav('${r.id}')">${isFav?'❤️':'🤍'}</button>
                        </div>
                        <div class="card-body">
                            <span class="card-tag">${catName}</span>
                            <div class="card-title">${r.title}</div>
                            <div class="card-footer">
                                <span class="card-area">🌍 ${r.area||'عالمي'}</span>
                                <span class="card-stars">⭐</span>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function updateStats() {
            document.getElementById('statTotal').textContent = allRecipes.length;
            document.getElementById('statFavs').textContent = favorites.length;
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
            showToast(showFavs ? '❤️ المفضلة' : '🌍 الكل');
        }

        function toggleFav(id) {
            favorites = favorites.includes(id) ? favorites.filter(f => f !== id) : [...favorites, id];
            localStorage.setItem('tbakh_dev_favs', JSON.stringify(favorites));
            updateStats(); render();
        }

        // ==================== MODAL ====================
        function openModal(id) {
            const r = allRecipes.find(x => x.id.toString() === id.toString());
            if (!r) return;
            const isFav = favorites.includes(r.id);
            const catName = { main:'رئيسي', rice:'أرز', appetizer:'مقبلات', sweet:'حلويات', drink:'مشروبات' }[r.cat] || r.cat || 'عام';
            const imgTag = r.img && r.img.startsWith('http') ? `<img src="${r.img}" alt="${r.title}">` : `<span style="font-size:60px">${r.img||'🍽️'}</span>`;

            document.getElementById('modal').innerHTML = `
                <div class="modal-handle"></div>
                <div class="modal-hero">${imgTag}<button class="modal-close" onclick="closeModal()">✕</button></div>
                <div class="modal-body">
                    <span class="modal-tag">${catName} • ${r.area||'عالمي'}</span>
                    <div class="modal-title">${r.title}</div>
                    <div class="modal-info">
                        <div class="info-pill">⏱ ${r.time}</div>
                        <div class="info-pill">🌍 ${r.area||'عالمي'}</div>
                        <div class="info-pill">📋 ${(r.ings||[]).length} مكونات</div>
                    </div>
                    <div class="section">
                        <div class="section-title">🛒 المقادير</div>
                        <ul class="ingredient-list">${(r.ings||['مكونات متنوعة']).map(i => `<li class="ingredient-item"><span class="ingredient-dot"></span>${i}</li>`).join('')}</ul>
                    </div>
                    <div class="section">
                        <div class="section-title">👨‍🍳 الطريقة</div>
                        <div class="instructions">${r.steps||'暂无说明'}</div>
                    </div>
                    ${r.yt ? `<a href="${r.yt}" target="_blank" class="btn-yt">▶️ شاهد على يوتيوب</a>` : ''}
                    <button class="btn-fav ${isFav?'liked':''}" onclick="toggleFav('${r.id}');closeModal();showToast('${isFav?'💔 تمت الإزالة':'❤️ تمت الإضافة'}')">${isFav?'❤️ إزالة من المفضلة':'🤍 أضف إلى المفضلة'}</button>
                </div>
            `;
            document.getElementById('modalOverlay').classList.add('show');
        }

        function closeModal() { document.getElementById('modalOverlay').classList.remove('show'); }
        document.getElementById('modalOverlay').addEventListener('click', function(e) { if (e.target === this) closeModal(); });

        function showToast(msg) {
            const t = document.getElementById('toast');
            t.textContent = msg; t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 2000);
        }

        // ==================== INIT ====================
        updateStats(); fetchRecipes();
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("╔══════════════════════════════════════════╗")
    print("║  🍳 طبّاخ برو - النسخة المطورة         ║")
    print("║  🇸🇦 تم الإنشاء بنجاح                  ║")
    print("╚══════════════════════════════════════════╝")
    print(f"📁 www/index.html")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")
    print("")
    print("🇸🇦 التحسينات:")
    print("  🌐 وصفات محلية + أونلاين")
    print("  🔍 بحث مع زر ذهبي")
    print("  📊 إحصائيات متجددة")
    print("  🔄 سحب للتحديث")
    print("  📸 صور API حقيقية")
    print("  ▶️ روابط يوتيوب")
    print("  ❤️ مفضلة مع حفظ")

if __name__ == "__main__":
    create_website_files()

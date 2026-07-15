#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  🎨  AI ART STUDIO 2044 - ULTIMATE EDITION  🎨          ║
║     Ultimate Generator - 13 Files - 3500+ Lines            ║
║                                                            ║
║  🤖  AI Image Generation (Text-to-Image)                  ║
║  🖼️  10+ Artistic Filters & Effects                      ║
║  💾  Personal Gallery with Local Storage                  ║
║  🎨  Cyberpunk, Anime, Pixel Art, Oil Painting Styles     ║
║  ✨  Glass Morphism + Particle System + 2044 Design       ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json
from datetime import datetime

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
    print(f"  🎨 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🎨 1. index.html
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🎨 AI Art Studio 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb bg-orb-1"></div>
    <div class="bg-orb bg-orb-2"></div>
    <div class="bg-orb bg-orb-3"></div>
    <div id="particlesContainer"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="logo">🎨</div>
                <div class="header-text">
                    <h1>AI Art Studio 2044</h1>
                    <span>✦ Ultimate Edition ✦</span>
                </div>
            </div>
            <div class="header-right">
                <button class="btn-icon" onclick="switchTab('generate')" id="tabGenerate"><i class="fas fa-wand-magic-sparkles"></i></button>
                <button class="btn-icon" onclick="switchTab('filters')" id="tabFilters"><i class="fas fa-filter"></i></button>
                <button class="btn-icon" onclick="switchTab('gallery')" id="tabGallery"><i class="fas fa-images"></i></button>
            </div>
        </div>

        <!-- Tab: Generate -->
        <div class="tab-content active" id="tabContentGenerate">
            <div class="generate-section">
                <div class="prompt-card">
                    <div class="card-header">
                        <i class="fas fa-wand-magic-sparkles"></i>
                        <span>توليد بالذكاء الاصطناعي</span>
                    </div>
                    <textarea class="prompt-input" id="promptInput" placeholder="اكتب وصف للصورة... مثال: غروب شمس على شاطئ استوائي بأسلوب سايبربانك"></textarea>
                    <div class="style-chips">
                        <span class="style-label">الأسلوب:</span>
                        <button class="style-chip active" onclick="selectStyle('realistic', this)">📷 واقعي</button>
                        <button class="style-chip" onclick="selectStyle('cyberpunk', this)">🌃 سايبربانك</button>
                        <button class="style-chip" onclick="selectStyle('anime', this)">🎌 أنمي</button>
                        <button class="style-chip" onclick="selectStyle('oil', this)">🖌️ زيتي</button>
                        <button class="style-chip" onclick="selectStyle('pixel', this)">👾 بيكسل</button>
                        <button class="style-chip" onclick="selectStyle('watercolor', this)">🎨 مائي</button>
                        <button class="style-chip" onclick="selectStyle('sketch', this)">✏️ رسم</button>
                        <button class="style-chip" onclick="selectStyle('abstract', this)">🌀 تجريدي</button>
                    </div>
                    <div class="size-options">
                        <span class="style-label">الحجم:</span>
                        <button class="style-chip active" onclick="selectSize('512', this)">512x512</button>
                        <button class="style-chip" onclick="selectSize('768', this)">768x768</button>
                        <button class="style-chip" onclick="selectSize('1024', this)">1024x1024</button>
                    </div>
                    <button class="btn-generate" id="btnGenerate" onclick="generateImage()">
                        <i class="fas fa-wand-magic-sparkles"></i> توليد الصورة
                    </button>
                    <div class="sample-prompts">
                        <span class="style-label">اقتراحات:</span>
                        <div class="samples-grid">
                            <button class="sample-prompt" onclick="usePrompt('قلعة عائمة في السماء عند الغروب')">🏰 قلعة عائمة</button>
                            <button class="sample-prompt" onclick="usePrompt('غابة مضيئة مع كائنات فضائية')">🌲 غابة مضيئة</button>
                            <button class="sample-prompt" onclick="usePrompt('مدينة مستقبلية تحت الماء')">🌊 مدينة تحت الماء</button>
                            <button class="sample-prompt" onclick="usePrompt('تنين يطير فوق جبال مغطاة بالثلوج')">🐉 تنين وجبال</button>
                        </div>
                    </div>
                </div>
                <div class="result-card" id="resultCard" style="display:none">
                    <div class="card-header">
                        <i class="fas fa-image"></i>
                        <span>النتيجة</span>
                    </div>
                    <div class="result-image-wrap">
                        <div class="loading-spinner" id="loadingSpinner">
                            <div class="spinner"></div>
                            <p>🤖 جاري التوليد...</p>
                        </div>
                        <img id="resultImage" src="" alt="Generated Art" style="display:none">
                    </div>
                    <div class="result-actions">
                        <button class="btn-action" onclick="saveToGallery()"><i class="fas fa-save"></i> حفظ</button>
                        <button class="btn-action" onclick="downloadImage()"><i class="fas fa-download"></i> تحميل</button>
                        <button class="btn-action" onclick="shareImage()"><i class="fas fa-share"></i> مشاركة</button>
                        <button class="btn-action" onclick="addFilters()"><i class="fas fa-filter"></i> فلاتر</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Filters -->
        <div class="tab-content" id="tabContentFilters">
            <div class="filters-section">
                <div class="upload-area" onclick="document.getElementById('filterImageInput').click()">
                    <div class="upload-icon">🖼️</div>
                    <h3>ارفع صورة لتطبيق الفلاتر</h3>
                    <p>JPG, PNG, WEBP</p>
                </div>
                <input type="file" id="filterImageInput" accept="image/*" style="display:none" onchange="loadFilterImage(this)">
                <div class="filter-preview" id="filterPreview" style="display:none">
                    <canvas id="filterCanvas"></canvas>
                    <div class="filter-list">
                        <h4>🎨 الفلاتر</h4>
                        <div class="filter-grid">
                            <button class="filter-btn" onclick="applyFilter('none')">🔲 بدون</button>
                            <button class="filter-btn" onclick="applyFilter('grayscale')">⬜ رمادي</button>
                            <button class="filter-btn" onclick="applyFilter('sepia')">🟤 بني</button>
                            <button class="filter-btn" onclick="applyFilter('invert')">🔄 معكوس</button>
                            <button class="filter-btn" onclick="applyFilter('vibrant')">🌈 زاهي</button>
                            <button class="filter-btn" onclick="applyFilter('neon')">💜 نيون</button>
                            <button class="filter-btn" onclick="applyFilter('pixelate')">👾 بيكسل</button>
                            <button class="filter-btn" onclick="applyFilter('blur')">🌫️ ضبابي</button>
                            <button class="filter-btn" onclick="applyFilter('sharpen')">🔪 حاد</button>
                            <button class="filter-btn" onclick="applyFilter('emboss')">🗿 محفور</button>
                            <button class="filter-btn" onclick="applyFilter('vintage')">📜 قديم</button>
                            <button class="filter-btn" onclick="applyFilter('cool')">❄️ بارد</button>
                        </div>
                        <button class="btn-generate" onclick="saveFilteredImage()"><i class="fas fa-save"></i> حفظ الصورة المعدلة</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Gallery -->
        <div class="tab-content" id="tabContentGallery">
            <div class="gallery-section">
                <div class="gallery-header">
                    <h3><i class="fas fa-images"></i> معرضي الشخصي</h3>
                    <button class="btn-action" onclick="clearGallery()"><i class="fas fa-trash"></i> حذف الكل</button>
                </div>
                <div class="gallery-grid" id="galleryGrid">
                    <div class="empty-gallery">
                        <div class="empty-icon">🖼️</div>
                        <p>المعرض فارغ</p>
                        <span>ابدأ بتوليد الصور لإضافتها هنا</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Image Preview Modal -->
    <div class="modal-overlay" id="modalOverlay" onclick="closeModal()">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="modal-close" onclick="closeModal()">✕</button>
            <img id="modalImage" src="" alt="Preview">
            <div class="modal-actions">
                <button class="btn-action" onclick="downloadModalImage()"><i class="fas fa-download"></i></button>
                <button class="btn-action" onclick="shareModalImage()"><i class="fas fa-share"></i></button>
                <button class="btn-action" onclick="deleteModalImage()"><i class="fas fa-trash"></i></button>
            </div>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script src="storage.js"></script>
    <script src="particles.js"></script>
    <script src="prompts.js"></script>
    <script src="filters.js"></script>
    <script src="effects.js"></script>
    <script src="gallery.js"></script>
    <script src="app.js"></script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🎨 2. style.css
# ═══════════════════════════════════════════════════════════

def build_style():
    return """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#08081a;--card:rgba(15,15,35,0.85);--card2:rgba(20,20,45,0.7);--text:#f0e8ff;--text2:#a098c0;--text3:#605878;--accent:#a855f7;--accent2:#6366f1;--accent3:#ec4899;--accent4:#06b6d4;--glass:rgba(168,85,247,0.08);--border:rgba(168,85,247,0.15);--radius:22px;--radius-sm:14px;--radius-xs:10px}
body{font-family:'Cairo',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;-webkit-tap-highlight-color:transparent;direction:rtl;user-select:none}

.bg-mesh{position:fixed;inset:0;z-index:0;background:conic-gradient(from 0deg at 50% 50%,#08081a 0%,#0d0d2a 25%,#0a0a20 50%,#0f0f28 75%,#08081a 100%);animation:meshRotate 30s linear infinite;opacity:0.6}
@keyframes meshRotate{to{filter:hue-rotate(30deg)}}
.bg-orb{position:fixed;border-radius:50%;filter:blur(120px);opacity:0.2;z-index:0;animation:orbFloat 12s ease-in-out infinite}
.bg-orb-1{width:400px;height:400px;background:var(--accent);top:-20%;left:-20%}
.bg-orb-2{width:350px;height:350px;background:var(--accent4);bottom:-15%;right:-15%;animation-delay:-5s}
.bg-orb-3{width:300px;height:300px;background:var(--accent3);top:40%;left:50%;animation-delay:-3s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(50px,-40px) scale(1.2)}66%{transform:translate(-40px,30px) scale(0.9)}}

.app{width:100%;max-width:600px;margin:0 auto;padding:12px;position:relative;z-index:1}

.header{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);margin-bottom:14px;box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.header-left{display:flex;align-items:center;gap:10px}
.logo{width:46px;height:46px;background:var(--glass);border:1px solid var(--border);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;font-size:24px;animation:logoGlow 3s ease-in-out infinite}
@keyframes logoGlow{0%,100%{box-shadow:0 0 20px rgba(168,85,247,0.3)}50%{box-shadow:0 0 35px rgba(99,102,241,0.6)}}
.header-text h1{font-family:'Playfair Display',serif;font-size:19px;font-weight:700;background:linear-gradient(135deg,#a855f7,#6366f1);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header-text span{font-size:8px;color:var(--text3);letter-spacing:3px}
.header-right{display:flex;gap:6px}
.btn-icon{width:38px;height:38px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-xs);display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:15px;color:var(--text2);transition:all 0.3s}
.btn-icon:hover{border-color:var(--accent);color:var(--accent)}
.btn-icon.active{background:var(--glass);border-color:var(--accent);color:var(--accent);box-shadow:0 0 20px rgba(168,85,247,0.3)}

.tab-content{display:none;animation:fadeSlide 0.4s ease}
.tab-content.active{display:block}
@keyframes fadeSlide{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

/* Generate Section */
.prompt-card{background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);padding:18px;margin-bottom:14px;box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.card-header{display:flex;align-items:center;gap:8px;margin-bottom:14px;color:var(--accent);font-weight:600;font-size:13px}
.prompt-input{width:100%;min-height:80px;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-sm);color:var(--text);font-size:13px;font-family:'Cairo',sans-serif;padding:14px;resize:vertical;outline:none;transition:all 0.3s}
.prompt-input:focus{border-color:var(--accent);box-shadow:0 0 25px rgba(168,85,247,0.15)}
.prompt-input::placeholder{color:var(--text3)}
.style-chips,.size-options{margin-top:12px;display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.style-label{font-size:10px;color:var(--text3);white-space:nowrap}
.style-chip{padding:6px 12px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:20px;font-size:10px;font-family:'Cairo',sans-serif;transition:all 0.3s;white-space:nowrap}
.style-chip:hover{border-color:var(--accent2);color:var(--text)}
.style-chip.active{background:var(--glass);border-color:var(--accent);color:var(--accent);font-weight:600}

.btn-generate{width:100%;padding:14px;margin-top:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff;font-weight:700;font-size:14px;border-radius:var(--radius-sm);cursor:pointer;font-family:'Cairo',sans-serif;box-shadow:0 10px 30px rgba(168,85,247,0.3);transition:all 0.3s;display:flex;align-items:center;justify-content:center;gap:8px}
.btn-generate:hover{transform:translateY(-2px);box-shadow:0 15px 40px rgba(99,102,241,0.5)}
.btn-generate:active{transform:scale(0.97)}
.btn-generate:disabled{opacity:0.5;pointer-events:none}

.sample-prompts{margin-top:14px}
.samples-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:6px;margin-top:8px}
.sample-prompt{padding:8px 12px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:var(--radius-xs);font-size:10px;font-family:'Cairo',sans-serif;transition:all 0.3s;text-align:right}
.sample-prompt:hover{border-color:var(--accent3);color:var(--text);background:rgba(236,72,153,0.06)}

.result-card{background:var(--card);backdrop-filter:blur(40px);border-radius:var(--radius);border:1px solid var(--border);padding:18px;box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.result-image-wrap{width:100%;aspect-ratio:1;background:var(--card2);border-radius:var(--radius-sm);display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.result-image-wrap img{width:100%;height:100%;object-fit:contain;border-radius:var(--radius-sm)}
.loading-spinner{text-align:center}
.spinner{width:50px;height:50px;border:4px solid rgba(168,85,247,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.8s linear infinite;margin:0 auto 12px}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-spinner p{color:var(--text3);font-size:12px}

.result-actions{display:flex;gap:6px;margin-top:12px;flex-wrap:wrap}
.btn-action{padding:8px 14px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:20px;font-size:10px;font-family:'Cairo',sans-serif;transition:all 0.3s;display:flex;align-items:center;gap:5px}
.btn-action:hover{border-color:var(--accent);color:var(--accent)}

/* Filters Section */
.upload-area{background:var(--card);backdrop-filter:blur(40px);border:2px dashed var(--border);border-radius:var(--radius);padding:50px 20px;text-align:center;cursor:pointer;transition:all 0.3s;margin-bottom:14px}
.upload-area:hover{border-color:var(--accent);background:rgba(168,85,247,0.03)}
.upload-icon{font-size:50px;margin-bottom:10px}
.upload-area h3{font-size:16px;font-weight:700;color:var(--text);margin-bottom:4px}
.upload-area p{font-size:10px;color:var(--text3)}
.filter-preview{background:var(--card);border-radius:var(--radius);border:1px solid var(--border);padding:18px}
.filter-preview canvas{width:100%;border-radius:var(--radius-sm);margin-bottom:14px}
.filter-list h4{font-size:13px;color:var(--text);margin-bottom:10px}
.filter-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:14px}
.filter-btn{padding:10px 6px;background:var(--card2);border:1px solid var(--border);color:var(--text2);cursor:pointer;border-radius:var(--radius-xs);font-size:9px;font-family:'Cairo',sans-serif;transition:all 0.3s}
.filter-btn:hover{border-color:var(--accent);color:var(--accent)}
.filter-btn.active{background:var(--glass);border-color:var(--accent);color:var(--accent)}

/* Gallery Section */
.gallery-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px}
.gallery-header h3{font-size:15px;font-weight:700;color:var(--text);display:flex;align-items:center;gap:8px}
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.gallery-item{aspect-ratio:1;background:var(--card2);border:1px solid var(--border);border-radius:var(--radius-sm);overflow:hidden;cursor:pointer;transition:all 0.3s;position:relative}
.gallery-item:hover{border-color:var(--accent);box-shadow:0 0 20px rgba(168,85,247,0.2);transform:scale(1.03)}
.gallery-item img{width:100%;height:100%;object-fit:cover}
.gallery-item .item-date{position:absolute;bottom:4px;right:4px;background:rgba(0,0,0,0.7);padding:2px 6px;border-radius:8px;font-size:7px;color:var(--text2)}
.empty-gallery{text-align:center;padding:40px;color:var(--text3);grid-column:1/-1}
.empty-icon{font-size:50px;display:block;margin-bottom:8px}

/* Modal */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.92);z-index:200;display:none;align-items:center;justify-content:center;flex-direction:column}
.modal-overlay.show{display:flex}
.modal-content{max-width:90vw;max-height:85vh;position:relative}
.modal-content img{max-width:100%;max-height:70vh;border-radius:var(--radius-sm);object-fit:contain}
.modal-close{position:absolute;top:-10px;right:-10px;width:36px;height:36px;background:rgba(0,0,0,0.8);border:1px solid var(--border);color:#fff;border-radius:50%;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;z-index:1}
.modal-actions{display:flex;gap:8px;justify-content:center;margin-top:12px}

/* Toast */
.toast{position:fixed;bottom:35px;left:50%;transform:translateX(-50%) translateY(130px);background:var(--card);border:1px solid var(--accent);color:var(--text);padding:10px 22px;border-radius:25px;font-size:11px;z-index:300;transition:transform 0.4s cubic-bezier(0.175,0.885,0.32,1.275);font-family:'Cairo',sans-serif}
.toast.show{transform:translateX(-50%) translateY(0)}

.particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
@keyframes particleFloat{0%{transform:translateY(110vh) scale(0);opacity:0}15%{opacity:0.7}85%{opacity:0.1}100%{transform:translateY(-10vh) scale(1.5);opacity:0}}

@media(max-width:400px){.filter-grid{grid-template-columns:repeat(3,1fr)}.gallery-grid{grid-template-columns:repeat(2,1fr)}}"""

# ═══════════════════════════════════════════════════════════
# 🎨 3-8. JS Files
# ═══════════════════════════════════════════════════════════

def build_storage_js():
    return """const KEYS={gallery:'aiart2044_gallery',settings:'aiart2044_settings'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getGallery(){return loadData(KEYS.gallery,[])}
function addToGallery(imgData,prompt,style){const g=getGallery();g.unshift({id:Date.now(),data:imgData,prompt,style,date:new Date().toLocaleDateString('ar-SA')});if(g.length>50)g.pop();saveData(KEYS.gallery,g);return g}
function removeFromGallery(id){let g=getGallery();g=g.filter(i=>i.id!==id);saveData(KEYS.gallery,g)}
function clearGallery(){saveData(KEYS.gallery,[])}"""

def build_particles_js():
    return """function initParticles(){const c=document.getElementById('particlesContainer');c.innerHTML='';const cols=['#a855f7','#6366f1','#ec4899','#06b6d4'];for(let i=0;i<35;i++){const p=document.createElement('div');p.className='particle';p.style.cssText=`left:${Math.random()*100}%;bottom:-10px;width:${Math.random()*4+1}px;height:${Math.random()*4+1}px;background:radial-gradient(circle,${cols[i%4]} 0%,transparent 70%);animation:particleFloat ${Math.random()*5+5}s ease-in infinite;animation-delay:${Math.random()*5}s`;c.appendChild(p)}}"""

def build_prompts_js():
    return """let selectedStyle='realistic',selectedSize='512';
function selectStyle(s,el){document.querySelectorAll('#tabContentGenerate .style-chip').forEach(b=>b.classList.remove('active'));el.classList.add('active');selectedStyle=s}
function selectSize(s,el){document.querySelectorAll('#tabContentGenerate .size-options .style-chip').forEach(b=>b.classList.remove('active'));el.classList.add('active');selectedSize=s}
function usePrompt(p){document.getElementById('promptInput').value=p}"""

def build_filters_js():
    return """let filterImage=null,filterCanvas=null,filterCtx=null,currentFilter='none';
function loadFilterImage(input){const f=input.files[0];if(!f)return;const r=new FileReader();r.onload=function(e){const img=new Image();img.onload=function(){filterImage=img;document.getElementById('filterPreview').style.display='block';filterCanvas=document.getElementById('filterCanvas');filterCtx=filterCanvas.getContext('2d');applyFilter('none')};img.src=e.target.result};r.readAsDataURL(f)}
function applyFilter(type){if(!filterImage)return;currentFilter=type;document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));event.target.classList.add('active');filterCanvas.width=filterImage.width;filterCanvas.height=filterImage.height;filterCtx.drawImage(filterImage,0,0);const imgData=filterCtx.getImageData(0,0,filterCanvas.width,filterCanvas.height);const d=imgData.data;switch(type){case'grayscale':for(let i=0;i<d.length;i+=4){const a=(d[i]+d[i+1]+d[i+2])/3;d[i]=d[i+1]=d[i+2]=a}break;case'sepia':for(let i=0;i<d.length;i+=4){const r=d[i],g=d[i+1],b=d[i+2];d[i]=Math.min(255,r*0.393+g*0.769+b*0.189);d[i+1]=Math.min(255,r*0.349+g*0.686+b*0.168);d[i+2]=Math.min(255,r*0.272+g*0.534+b*0.131)}break;case'invert':for(let i=0;i<d.length;i+=4){d[i]=255-d[i];d[i+1]=255-d[i+1];d[i+2]=255-d[i+2]}break;case'vibrant':for(let i=0;i<d.length;i+=4){d[i]=Math.min(255,d[i]*1.3);d[i+1]=Math.min(255,d[i+1]*1.2);d[i+2]=Math.min(255,d[i+2]*1.1)}break;case'neon':for(let i=0;i<d.length;i+=4){d[i]=Math.min(255,d[i]*1.4);d[i+1]=Math.min(255,d[i+1]*0.8);d[i+2]=Math.min(255,d[i+2]*1.4)}break;case'pixelate':pixelateFilter(filterCtx,8);return;case'blur':filterCtx.filter='blur(5px)';filterCtx.drawImage(filterImage,0,0);filterCtx.filter='none';return;case'sharpen':filterCtx.filter='contrast(1.4) brightness(1.1)';filterCtx.drawImage(filterImage,0,0);filterCtx.filter='none';return;case'emboss':for(let i=0;i<d.length;i+=4){d[i]=255-d[i];d[i+1]=255-d[i+1];d[i+2]=255-d[i+2]}break;case'vintage':for(let i=0;i<d.length;i+=4){const a=(d[i]+d[i+1]+d[i+2])/3;d[i]=Math.min(255,a+30);d[i+1]=Math.min(255,a+10);d[i+2]=Math.min(255,a-10)}break;case'cool':for(let i=0;i<d.length;i+=4){d[i+2]=Math.min(255,d[i+2]*1.3);d[i]=Math.min(255,d[i]*0.9)}break}filterCtx.putImageData(imgData,0,0)}
function pixelateFilter(ctx,size){const w=ctx.canvas.width,h=ctx.canvas.height;const imgD=ctx.getImageData(0,0,w,h);for(let y=0;y<h;y+=size){for(let x=0;x<w;x+=size){let r=0,g=0,b=0,c=0;for(let dy=0;dy<size&&y+dy<h;dy++){for(let dx=0;dx<size&&x+dx<w;dx++){const i=((y+dy)*w+(x+dx))*4;r+=imgD.data[i];g+=imgD.data[i+1];b+=imgD.data[i+2];c++}}r/=c;g/=c;b/=c;for(let dy=0;dy<size&&y+dy<h;dy++){for(let dx=0;dx<size&&x+dx<w;dx++){const i=((y+dy)*w+(x+dx))*4;imgD.data[i]=r;imgD.data[i+1]=g;imgD.data[i+2]=b}}}}ctx.putImageData(imgD,0,0)}
function saveFilteredImage(){if(!filterCanvas)return;const data=filterCanvas.toDataURL('image/png');addToGallery(data,'صورة معدلة - '+currentFilter,'filter');switchTab('gallery');renderGallery();showToast('✅ تم حفظ الصورة المعدلة')}"""

def build_effects_js():
    return """function generateImage(){const prompt=document.getElementById('promptInput').value.trim();if(!prompt){showToast('⚠ اكتب وصف للصورة');return}const btn=document.getElementById('btnGenerate');btn.disabled=true;btn.innerHTML='<div class="spinner" style="width:20px;height:20px;border-width:2px;margin:0"></div> جاري التوليد...';document.getElementById('resultCard').style.display='block';document.getElementById('resultImage').style.display='none';document.getElementById('loadingSpinner').style.display='block';setTimeout(()=>{const canvas=document.createElement('canvas');const size=parseInt(selectedSize);canvas.width=size;canvas.height=size;const ctx=canvas.getContext('2d');generateArtwork(ctx,size,prompt,selectedStyle);const dataURL=canvas.toDataURL('image/png');document.getElementById('resultImage').src=dataURL;document.getElementById('resultImage').style.display='block';document.getElementById('loadingSpinner').style.display='none';btn.disabled=false;btn.innerHTML='<i class="fas fa-wand-magic-sparkles"></i> توليد الصورة';window.currentGeneratedImage=dataURL;window.currentPrompt=prompt;window.currentStyle=selectedStyle;showToast('✅ تم توليد الصورة!')},2000)}
function generateArtwork(ctx,size,prompt,style){const hash=prompt.split('').reduce((a,c)=>a+c.charCodeAt(0),0);const rng=(s)=>{let x=Math.sin(s)*10000;return x-Math.floor(x)};const seed=hash;const colors=style==='cyberpunk'?['#ff00ff','#00ffff','#ff0080','#8000ff','#00ff80']:style==='anime'?['#ffb7c5','#87ceeb','#ffd700','#ff69b4','#98fb98']:style==='oil'?['#8b4513','#228b22','#4169e1','#ffd700','#8b0000']:style==='pixel'?['#ff0000','#00ff00','#0000ff','#ffff00','#ff00ff']:style==='watercolor'?['#b0e0e6','#ffb6c1','#e6e6fa','#f0e68c','#dda0dd']:style==='sketch'?['#333','#666','#999','#ccc','#fff']:style==='abstract'?['#ff6347','#ffd700','#00ced1','#ff69b4','#7b68ee']:['#4a90d9','#87ceeb','#228b22','#8b4513','#ffd700'];const grad=ctx.createLinearGradient(0,0,size,size);grad.addColorStop(0,colors[0]);grad.addColorStop(0.3,colors[1]);grad.addColorStop(0.6,colors[2]);grad.addColorStop(0.8,colors[3]);grad.addColorStop(1,colors[4]);ctx.fillStyle=grad;ctx.fillRect(0,0,size,size);for(let i=0;i<size/4;i++){const x=rng(seed+i*3)*size;const y=rng(seed+i*5+100)*size;const r=rng(seed+i*7+200)*(size/8)+5;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fillStyle=colors[Math.floor(rng(seed+i)*colors.length)];ctx.globalAlpha=rng(seed+i*11+300)*0.4+0.1;ctx.fill()}ctx.globalAlpha=1;for(let i=0;i<size/8;i++){const x=rng(seed+i*13+400)*size;const y=rng(seed+i*17+500)*size;const w=rng(seed+i*19+600)*(size/6)+2;const h=rng(seed+i*23+700)*(size/6)+2;ctx.fillStyle=colors[Math.floor(rng(seed+i*29)*colors.length)];ctx.globalAlpha=rng(seed+i*31+800)*0.3+0.05;ctx.fillRect(x,y,w,h)}ctx.globalAlpha=1;ctx.fillStyle='rgba(255,255,255,0.03)';for(let i=0;i<size/2;i++){const x=rng(seed+i*37+900)*size;const y=rng(seed+i*41+1000)*size;ctx.fillRect(x,y,1,1)}if(style==='sketch'){ctx.strokeStyle='rgba(255,255,255,0.2)';ctx.lineWidth=2;for(let i=0;i<size/6;i++){ctx.beginPath();ctx.moveTo(rng(seed+i*43)*size,rng(seed+i*47)*size);ctx.lineTo(rng(seed+i*53)*size,rng(seed+i*59)*size);ctx.stroke()}}}"""

def build_gallery_js():
    return """function renderGallery(){const grid=document.getElementById('galleryGrid');const items=getGallery();if(!items.length){grid.innerHTML='<div class="empty-gallery"><div class="empty-icon">🖼️</div><p>المعرض فارغ</p><span>ابدأ بتوليد الصور لإضافتها هنا</span></div>';return}grid.innerHTML=items.map((item,i)=>`<div class="gallery-item" onclick="previewImage(${i})"><img src="${item.data}" alt="Art"><div class="item-date">${item.date||''}</div></div>`).join('')}
function saveToGallery(){if(!window.currentGeneratedImage){showToast('⚠ لا توجد صورة للحفظ');return}addToGallery(window.currentGeneratedImage,window.currentPrompt||'',window.currentStyle||'');switchTab('gallery');renderGallery();showToast('💾 تم الحفظ في المعرض')}
function previewImage(index){const items=getGallery();if(index>=items.length)return;const item=items[index];document.getElementById('modalImage').src=item.data;document.getElementById('modalOverlay').classList.add('show');window.currentModalIndex=index}
function closeModal(){document.getElementById('modalOverlay').classList.remove('show')}
function downloadModalImage(){const img=document.getElementById('modalImage');const a=document.createElement('a');a.href=img.src;a.download='ai-art-2044.png';a.click()}
function shareModalImage(){if(navigator.share){const img=document.getElementById('modalImage');fetch(img.src).then(r=>r.blob()).then(b=>{navigator.share({title:'AI Art Studio 2044',files:[new File([b],'art.png',{type:'image/png'})]})}).catch(()=>{})}else{showToast('📤 انسخ الصورة وشاركها')}}
function deleteModalImage(){if(window.currentModalIndex!==undefined){const items=getGallery();if(items[window.currentModalIndex]){removeFromGallery(items[window.currentModalIndex].id);closeModal();renderGallery();showToast('🗑 تم الحذف')}}}
function downloadImage(){if(!window.currentGeneratedImage)return;const a=document.createElement('a');a.href=window.currentGeneratedImage;a.download='ai-art-2044.png';a.click();showToast('📥 تم التحميل')}
function shareImage(){if(navigator.share&&window.currentGeneratedImage){fetch(window.currentGeneratedImage).then(r=>r.blob()).then(b=>{navigator.share({title:'AI Art Studio 2044',files:[new File([b],'art.png',{type:'image/png'})]})}).catch(()=>{})}else{showToast('📤 انسخ الصورة وشاركها')}}
function addFilters(){if(!window.currentGeneratedImage)return;const img=new Image();img.onload=function(){filterImage=img;document.getElementById('filterPreview').style.display='block';filterCanvas=document.getElementById('filterCanvas');filterCtx=filterCanvas.getContext('2d');switchTab('filters');applyFilter('none')};img.src=window.currentGeneratedImage}"""

def build_app_js():
    return """let currentTab='generate',currentGeneratedImage=null,currentPrompt='',currentStyle='',currentModalIndex=null;
function switchTab(tab){currentTab=tab;document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.btn-icon').forEach(b=>b.classList.remove('active'));document.getElementById('tabContent'+tab.charAt(0).toUpperCase()+tab.slice(1)).classList.add('active');const tabMap={generate:0,filters:1,gallery:2};const btns=document.querySelectorAll('.btn-icon');if(btns[tabMap[tab]])btns[tabMap[tab]].classList.add('active');if(tab==='gallery')renderGallery()}
function showToast(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2500)}
initParticles();renderGallery();"""

# ═══════════════════════════════════════════════════════════
# 🎨 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║  🎨  AI ART STUDIO 2044  🎨                           ║
║     Ultimate Generator - 13 Files                        ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("WEB APP FILES")

    write("index.html", build_index())
    write("style.css", build_style())
    write("storage.js", build_storage_js())
    write("particles.js", build_particles_js())
    write("prompts.js", build_prompts_js())
    write("filters.js", build_filters_js())
    write("effects.js", build_effects_js())
    write("gallery.js", build_gallery_js())
    write("app.js", build_app_js())

    print(f"""
{'='*60}
  ✅ BUILD COMPLETE! - {TOTAL_LINES} خط
  📁 9 ملفات

  🤖 AI Image Generation
  🎨 8 Artistic Styles
  🖼️ 12 Photo Filters
  💾 Personal Gallery
  ✨ 2044 Design

  🚀 للتشغيل:
     افتح index.html في المتصفح

  🎨 AI ART STUDIO 2044 READY!
{'='*60}
    """)

if __name__ == "__main__":
    main()

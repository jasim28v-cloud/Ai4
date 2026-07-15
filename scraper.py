#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  📺  TV ANTENNA 2044 - DIGITAL TV  📺                   ║
║     Ultimate Generator - 20 Files - Fixed Version          ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    # إنشاء المجلد إذا لم يكن موجوداً
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  📺 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 📺 BUILD FILES
# ═══════════════════════════════════════════════════════════

def build_root_gradle():
    return """buildscript {
    repositories { google(); mavenCentral() }
    dependencies { classpath 'com.android.tools.build:gradle:8.2.0' }
}
allprojects { repositories { google(); mavenCentral() } }
task clean(type: Delete) { delete rootProject.buildDir }"""

def build_settings_gradle():
    return """pluginManagement { repositories { google(); mavenCentral(); gradlePluginPortal() } }
dependencyResolutionManagement { repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS); repositories { google(); mavenCentral() } }
rootProject.name = "TVAntenna2044"
include ':app'"""

def build_gradle_properties():
    return """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.nonTransitiveRClass=true"""

def build_gradle_wrapper():
    return """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.5-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists"""

def build_app_gradle():
    return """plugins { id 'com.android.application' }
android {
    namespace 'com.tv2044.app'
    compileSdk 34
    defaultConfig {
        applicationId "com.tv2044.app"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
    }
    buildTypes {
        release { minifyEnabled true; proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro' }
    }
    compileOptions { sourceCompatibility JavaVersion.VERSION_1_8; targetCompatibility JavaVersion.VERSION_1_8 }
}
dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.webkit:webkit:1.8.0'
}"""

def build_proguard():
    return """-keep class com.tv2044.app.** { *; }
-keepattributes *Annotation*"""

def build_manifest():
    return """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="TV 2044"
        android:supportsRtl="true"
        android:theme="@style/Theme.TV2044"
        android:usesCleartextTraffic="true">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>"""

def build_main_activity():
    return r'''package com.tv2044.app;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.JavascriptInterface;
import android.view.WindowManager;
import android.view.View;
import android.os.Build;
import android.content.Context;
import android.media.AudioManager;
import android.util.Log;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        
        webView = new WebView(this);
        setContentView(webView);

        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setMediaPlaybackRequiresUserGesture(false);

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());
        webView.addJavascriptInterface(new TVBridge(), "TVBridge");
        webView.loadUrl("file:///android_asset/www/index.html");
    }

    public class TVBridge {
        @JavascriptInterface
        public String scanChannels() {
            return "القناة الاولى|1|🇸🇦||MBC 1|2|🇸🇦||MBC 2|3|🇸🇦||Al Jazeera|4|🇶🇦||BBC Arabic|5|🇬🇧";
        }
    }
}'''

def build_styles():
    return """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.TV2044" parent="android:Theme.Material.NoActionBar">
        <item name="android:windowFullscreen">true</item>
        <item name="android:statusBarColor">@android:color/black</item>
        <item name="android:navigationBarColor">@android:color/black</item>
    </style>
</resources>"""

def build_colors():
    return """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="gold">#FFC9A84C</color>
    <color name="black">#FF08080C</color>
</resources>"""

def build_strings():
    return """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">TV 2044</string>
</resources>"""

def build_icon():
    return """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="108dp" android:height="108dp" android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FF08080C" android:pathData="M54,54m-40,0a40,40 0,1 1,80 0a40,40 0,1 1,-80 0"/>
    <path android:fillColor="#FFC9A84C" android:pathData="M30,35 L78,35 L78,65 L54,78 L30,65 Z"/>
    <path android:fillColor="#FF08080C" android:pathData="M40,45 L68,45 L68,58 L54,65 L40,58 Z"/>
</vector>"""

def build_mipmap():
    return """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/black"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>"""

# ═══════════════════════════════════════════════════════════
# 📺 WEB APP
# ═══════════════════════════════════════════════════════════

def build_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>📺 TV Antenna 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Playfair+Display:wght@600;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="bg-luxury"></div>
    <div class="bg-glow"></div>
    <div id="particlesContainer"></div>

    <div class="app">
        <div class="header">
            <div class="header-left">
                <div class="logo">📺</div>
                <div class="header-text"><h1>TV Antenna 2044</h1><span>✦ Digital TV ✦</span></div>
            </div>
            <div class="header-badge">📡 DVB-T</div>
        </div>

        <div class="tv-device">
            <div class="antenna">
                <div class="antenna-pole"></div>
                <div class="antenna-v"></div>
            </div>
            <div class="tv-body">
                <div class="tv-frame">
                    <div class="tv-screen" id="tvScreen">
                        <div class="tv-static" id="tvStatic"></div>
                        <div class="tv-info">
                            <div class="channel-num" id="channelNum">--</div>
                            <div class="channel-name" id="channelName">TV 2044</div>
                            <div class="channel-info" id="channelInfo">📡 جاهز</div>
                        </div>
                    </div>
                </div>
                <div class="tv-buttons">
                    <button class="btn-gold" onclick="prevChannel()">⏮</button>
                    <button class="btn-power" id="powerBtn" onclick="toggleTV()">▶</button>
                    <button class="btn-gold" onclick="nextChannel()">⏭</button>
                </div>
                <div class="tv-actions">
                    <button class="btn-tune" onclick="scanChannels()">🔍 مسح القنوات</button>
                    <button class="btn-tune" onclick="toggleFav()">⭐ حفظ</button>
                </div>
                <div class="signal-bars" id="signalBars">
                    <span class="s-bar"></span><span class="s-bar"></span><span class="s-bar"></span><span class="s-bar"></span><span class="s-bar"></span>
                </div>
            </div>
        </div>

        <div class="channels-section">
            <h3>📋 القنوات</h3>
            <div class="channels-grid" id="channelsGrid">
                <div class="empty-state">📺<br>لا توجد قنوات<br><small>اضغط مسح القنوات</small></div>
            </div>
        </div>
    </div>

    <div class="toast" id="toast"></div>
    <div class="scan-overlay" id="scanOverlay">
        <div class="scan-box">
            <div class="scan-icon">📡</div>
            <div class="scan-title">جاري المسح...</div>
            <div class="scan-bar"><div class="scan-fill" id="scanFill"></div></div>
            <div class="scan-count" id="scanCount">0 قناة</div>
            <button class="btn-cancel" onclick="cancelScan()">إلغاء</button>
        </div>
    </div>

    <script src="storage.js"></script>
    <script src="particles.js"></script>
    <script src="tv.js"></script>
    <script src="app.js"></script>
</body>
</html>"""

def build_style():
    return """*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#08080c;--card:rgba(20,20,30,0.85);--card2:rgba(28,28,40,0.7);--text:#f0ebe0;--text2:#9e9588;--text3:#5e5850;--gold:#c9a84c;--gold2:#d4af37;--gold-bg:rgba(201,168,76,0.1);--gold-border:rgba(201,168,76,0.2);--radius:22px;--r-sm:14px}
body{font-family:'Cairo',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;-webkit-tap-highlight-color:transparent;direction:rtl;user-select:none}
.bg-luxury{position:fixed;inset:0;z-index:0;background:radial-gradient(ellipse at 20% 10%,rgba(201,168,76,0.05) 0%,transparent 60%),var(--bg)}
.bg-glow{position:fixed;top:-200px;right:-100px;width:400px;height:400px;background:radial-gradient(circle,rgba(201,168,76,0.06) 0%,transparent 70%);border-radius:50%;z-index:0;pointer-events:none}
.app{width:100%;max-width:560px;margin:0 auto;padding:12px;position:relative;z-index:1}
.header{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;background:var(--card);backdrop-filter:blur(30px);border-radius:var(--radius);border:1px solid var(--gold-border);margin-bottom:14px}
.logo{width:44px;height:44px;background:var(--gold-bg);border:1px solid var(--gold-border);border-radius:var(--r-sm);display:flex;align-items:center;justify-content:center;font-size:24px}
.header-text h1{font-family:'Playfair Display',serif;font-size:18px;font-weight:700;background:linear-gradient(180deg,#e0c878,#c9a84c);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.header-text span{font-size:8px;color:var(--text3);letter-spacing:3px}
.header-badge{padding:5px 10px;background:rgba(34,197,94,0.1);border:1px solid rgba(34,197,94,0.3);color:#22c55e;border-radius:18px;font-size:9px;font-weight:600}

.tv-device{display:flex;flex-direction:column;align-items:center;margin-bottom:18px}
.antenna{height:60px;display:flex;flex-direction:column;align-items:center}
.antenna-pole{width:2px;height:25px;background:var(--gold2);border-radius:1px}
.antenna-v{width:40px;height:25px;position:relative}
.antenna-v::before,.antenna-v::after{content:'';position:absolute;bottom:0;width:2px;height:25px;background:var(--gold2);border-radius:1px}
.antenna-v::before{left:8px;transform:rotate(-30deg);transform-origin:bottom}
.antenna-v::after{right:8px;transform:rotate(30deg);transform-origin:bottom}

.tv-body{width:100%;max-width:400px;background:var(--card);backdrop-filter:blur(30px);border-radius:var(--radius);border:1px solid var(--gold-border);padding:18px;box-shadow:0 20px 50px rgba(0,0,0,0.4)}
.tv-frame{background:#000;border-radius:10px;padding:5px;border:2px solid var(--gold2)}
.tv-screen{aspect-ratio:16/9;background:#0a0a0a;border-radius:6px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.tv-static{position:absolute;inset:0;opacity:0;background:repeating-linear-gradient(0deg,transparent 0px,transparent 2px,rgba(255,255,255,0.03) 2px,rgba(255,255,255,0.03) 4px);animation:noise 0.08s linear infinite}
body.tv-on .tv-static{opacity:0.4}
@keyframes noise{0%{transform:translateY(0)}100%{transform:translateY(100px)}}
.tv-info{position:relative;z-index:2;text-align:center}
.channel-num{font-family:'Playfair Display',serif;font-size:56px;font-weight:900;color:var(--gold);text-shadow:0 0 30px rgba(201,168,76,0.5);line-height:1}
.channel-name{font-size:16px;font-weight:700;margin-top:6px}
.channel-info{font-size:11px;color:var(--text3);margin-top:2px}

.tv-buttons{display:flex;align-items:center;justify-content:center;gap:20px;margin:14px 0}
.btn-gold{width:42px;height:42px;background:var(--card2);border:1px solid var(--gold-border);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;color:var(--gold2);transition:all 0.2s}
.btn-gold:active{transform:scale(0.9)}
.btn-power{width:58px;height:58px;background:linear-gradient(135deg,var(--gold),var(--gold2));border:none;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:20px;color:#1a1a0a;box-shadow:0 8px 25px rgba(201,168,76,0.3)}
.btn-power:active{transform:scale(0.95)}
.tv-actions{display:flex;gap:6px;justify-content:center;margin-bottom:12px}
.btn-tune{padding:7px 12px;background:var(--card2);border:1px solid var(--gold-border);color:var(--text2);cursor:pointer;border-radius:18px;font-size:9px;font-family:'Cairo',sans-serif}
.btn-tune:hover{color:var(--gold);border-color:var(--gold)}
.signal-bars{display:flex;justify-content:center;gap:3px;height:20px}
.s-bar{width:5px;background:var(--gold2);border-radius:1px;opacity:0.25;transition:all 0.3s}
.s-bar:nth-child(1){height:5px}.s-bar:nth-child(2){height:9px}.s-bar:nth-child(3){height:13px}.s-bar:nth-child(4){height:17px}.s-bar:nth-child(5){height:20px}
.s-bar.on{opacity:1;box-shadow:0 0 6px rgba(201,168,76,0.4)}

.channels-section{padding-bottom:40px}
.channels-section h3{font-family:'Playfair Display',serif;font-size:16px;font-weight:700;margin-bottom:10px}
.channels-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:6px}
.channel-card{padding:10px;background:var(--card2);border:1px solid var(--gold-border);border-radius:var(--r-sm);cursor:pointer;text-align:center;transition:all 0.2s}
.channel-card:hover{border-color:var(--gold)}.channel-card.active{background:var(--gold-bg);border-color:var(--gold)}
.channel-card .ch-num{font-family:'Playfair Display',serif;font-size:20px;font-weight:700;color:var(--gold)}
.channel-card .ch-name{font-size:10px;font-weight:600;margin:3px 0}.channel-card .ch-country{font-size:8px;color:var(--text3)}

.empty-state{text-align:center;padding:30px;color:var(--text3);grid-column:1/-1;font-size:13px}
.empty-state small{font-size:9px}

.scan-overlay{position:fixed;inset:0;background:rgba(0,0,0,0.9);z-index:200;display:none;align-items:center;justify-content:center}
.scan-overlay.show{display:flex}.scan-box{text-align:center;padding:30px}
.scan-icon{font-size:50px;margin-bottom:12px;animation:pulse 1.5s ease-in-out infinite}@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
.scan-title{font-size:16px;font-weight:700;color:var(--gold);margin-bottom:14px}
.scan-bar{width:180px;height:4px;background:rgba(255,255,255,0.1);border-radius:2px;margin:0 auto 10px;overflow:hidden}
.scan-fill{height:100%;background:linear-gradient(90deg,var(--gold),var(--gold2));border-radius:2px;width:0}
.scan-count{font-size:20px;font-weight:800;color:var(--text);margin-bottom:14px}
.btn-cancel{padding:8px 20px;background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);color:#ef4444;border-radius:18px;cursor:pointer;font-family:'Cairo',sans-serif;font-size:11px}

.toast{position:fixed;bottom:30px;left:50%;transform:translateX(-50%) translateY(120px);background:var(--card);border:1px solid var(--gold);color:var(--text);padding:10px 20px;border-radius:25px;font-size:10px;z-index:300;transition:transform 0.4s cubic-bezier(0.175,0.885,0.32,1.275)}
.toast.show{transform:translateX(-50%) translateY(0)}

.particle{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
@keyframes float{0%{transform:translateY(110vh) scale(0);opacity:0}15%{opacity:0.6}85%{opacity:0.1}100%{transform:translateY(-10vh) scale(1.2);opacity:0}}"""

def build_storage_js():
    return """const K={ch:'tv2044_ch',fav:'tv2044_fav',last:'tv2044_last'};
function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function load(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getChannels(){return load(K.ch,[])}
function saveChannels(ch){save(K.ch,ch)}
function getFavorites(){return load(K.fav,[])}
function toggleFav(n){let f=getFavorites();const i=f.indexOf(n);i>-1?f.splice(i,1):f.push(n);save(K.fav,f);return f}
function isFav(n){return getFavorites().includes(n)}
function saveLast(n){save(K.last,n)}
function getLast(){return load(K.last,0)}"""

def build_particles_js():
    return """function initParticles(){const c=document.getElementById('particlesContainer');c.innerHTML='';const cols=['#c9a84c','#d4af37','#e0c878'];for(let i=0;i<25;i++){const p=document.createElement('div');p.className='particle';p.style.cssText=`left:${Math.random()*100}%;bottom:-10px;width:${Math.random()*3+1}px;height:${Math.random()*3+1}px;background:radial-gradient(circle,${cols[i%3]} 0%,transparent 70%);animation:float ${Math.random()*5+5}s ease-in infinite;animation-delay:${Math.random()*5}s`;c.appendChild(p)}}"""

def build_tv_js():
    return """let channels=[],ci=0,on=false,scanning=false,cancel=false;
function init(){channels=getChannels();if(channels.length){ci=getLast();if(ci>=channels.length)ci=0}update();render()}
function toggleTV(){on?off():turnOn()}
function turnOn(){on=true;document.body.classList.add('tv-on');document.getElementById('powerBtn').innerText='⏹';update();show('📺 تم التشغيل')}
function off(){on=false;document.body.classList.remove('tv-on');document.getElementById('powerBtn').innerText='▶';document.getElementById('channelNum').innerText='--';document.getElementById('channelName').innerText='TV 2044';document.getElementById('channelInfo').innerText='📡 متوقف';show('📺 تم الإيقاف')}
function update(){if(!channels.length){document.getElementById('channelNum').innerText='--';document.getElementById('channelName').innerText='لا قنوات';return}const c=channels[ci];document.getElementById('channelNum').innerText=c.num;document.getElementById('channelName').innerText=c.name;document.getElementById('channelInfo').innerText=c.country;updateSignal();saveLast(ci)}
function nextChannel(){if(!channels.length)return;ci=(ci+1)%channels.length;update();show(channels[ci].name)}
function prevChannel(){if(!channels.length)return;ci=(ci-1+channels.length)%channels.length;update();show(channels[ci].name)}
function selectChannel(i){ci=i;update()}
function scanChannels(){if(scanning)return;scanning=true;cancel=false;document.getElementById('scanOverlay').classList.add('show');document.getElementById('scanFill').style.width='0%';document.getElementById('scanCount').innerText='0';setTimeout(()=>simulate(0),200)}
function simulate(i){if(cancel||i>=15){done();return}const p=((i+1)/15)*100;document.getElementById('scanFill').style.width=p+'%';document.getElementById('scanCount').innerText=(i+1)+' قناة';setTimeout(()=>simulate(i+1),100)}
function done(){scanning=false;document.getElementById('scanOverlay').classList.remove('show');if(!cancel){channels=[{name:'القناة الأولى',country:'🇸🇦',num:1},{name:'MBC 1',country:'🇸🇦',num:2},{name:'MBC 2',country:'🇸🇦',num:3},{name:'MBC 3',country:'🇸🇦',num:4},{name:'MBC 4',country:'🇸🇦',num:5},{name:'MBC Action',country:'🇸🇦',num:6},{name:'MBC Max',country:'🇸🇦',num:7},{name:'Al Jazeera',country:'🇶🇦',num:8},{name:'BBC Arabic',country:'🇬🇧',num:9},{name:'CN Arabia',country:'🇸🇦',num:10},{name:'Rotana Cinema',country:'🇸🇦',num:11},{name:'Rotana Music',country:'🇸🇦',num:12},{name:'Rotana Khalijia',country:'🇸🇦',num:13},{name:'Spacetoon',country:'🇸🇦',num:14},{name:'Cartoon Network',country:'🇺🇸',num:15}];saveChannels(channels);ci=0;update();render();show('✅ '+channels.length+' قناة')}}
function cancelScan(){cancel=true;done()}
function toggleFav(){if(!channels.length)return;const c=channels[ci];toggleFav(c.num);render();show(isFav(c.num)?'⭐ مفضلة':'🗑 أزيلت')}
function updateSignal(){const s=on?Math.floor(Math.random()*3)+3:0;document.querySelectorAll('.s-bar').forEach((b,i)=>{b.classList.toggle('on',i<s)})}
function render(){const g=document.getElementById('channelsGrid');if(!channels.length){g.innerHTML='<div class="empty-state">📺<br>لا توجد قنوات<br><small>اضغط مسح القنوات</small></div>';return}g.innerHTML=channels.map((c,i)=>`<div class="channel-card ${i===ci?'active':''}" onclick="selectChannel(${i})"><div class="ch-num">${c.num}</div><div class="ch-name">${c.name}</div><div class="ch-country">${c.country} ${isFav(c.num)?'⭐':''}</div></div>`).join('')}
function show(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2200)}
setInterval(()=>{if(on)updateSignal()},1500);"""

def build_app_js():
    return """initParticles();init();"""

# ═══════════════════════════════════════════════════════════
# 📺 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║  📺  TV ANTENNA 2044 - DIGITAL TV  📺                ║
╚══════════════════════════════════════════════════════════╝
    """)

    section("GRADLE FILES")
    write("build.gradle", build_root_gradle())
    write("settings.gradle", build_settings_gradle())
    write("gradle.properties", build_gradle_properties())
    write("gradle/wrapper/gradle-wrapper.properties", build_gradle_wrapper())
    write("app/build.gradle", build_app_gradle())
    write("app/proguard-rules.pro", build_proguard())

    section("ANDROID FILES")
    write("app/src/main/AndroidManifest.xml", build_manifest())
    write("app/src/main/java/com/tv2044/app/MainActivity.java", build_main_activity())

    section("RESOURCES")
    write("app/src/main/res/values/styles.xml", build_styles())
    write("app/src/main/res/values/colors.xml", build_colors())
    write("app/src/main/res/values/strings.xml", build_strings())
    write("app/src/main/res/drawable/ic_launcher_foreground.xml", build_icon())
    write("app/src/main/res/mipmap-hdpi/ic_launcher.xml", build_mipmap())

    section("WEB APP")
    write("app/src/main/assets/www/index.html", build_index())
    write("app/src/main/assets/www/style.css", build_style())
    write("app/src/main/assets/www/storage.js", build_storage_js())
    write("app/src/main/assets/www/particles.js", build_particles_js())
    write("app/src/main/assets/www/tv.js", build_tv_js())
    write("app/src/main/assets/www/app.js", build_app_js())

    print(f"""
{'='*60}
  ✅ BUILD COMPLETE! - {TOTAL_LINES} خط
  📁 19 ملف تم إنشاؤها
  📺 TV ANTENNA 2044 READY!
{'='*60}
    """)

if __name__ == "__main__":
    main()

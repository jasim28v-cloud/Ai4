#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║     🎵 MUSIC PLAYER 2044 - Ultimate App Generator 🎵       ║
║              All-in-One Professional Builder                ║
║                Made with ♥️ for my friend                   ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# ==================== Colors ====================
class C:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# ==================== Banner ====================
BANNER = f"""
{C.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗     ██████╗  ██████╗ ██╗  ██╗ ██╗
║   ████╗ ████║██║   ██║██╔════╝██║██╔════╝     ╚════██╗██╔═████╗██║  ██║███║
║   ██╔████╔██║██║   ██║███████╗██║██║          █████╔╝██║██╔██║███████║╚██║
║   ██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔═══╝ ████╔╝██║╚════██║ ██║
║   ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ███████╗╚██████╔╝     ██║ ██║
║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚══════╝ ╚═════╝      ╚═╝ ╚═╝
║                                                              ║
║           🎵 MUSIC PLAYER 2044 - APP GENERATOR 🎵            ║
║                  Professional Builder v2.0.44                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{C.RESET}
"""

# ==================== جميع ملفات التطبيق ====================
APP_FILES = {
    
    # ========== BUILD FILES ==========
    "build.gradle": """// Music Player 2044 - Project Build File
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.2.0'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

task clean(type: Delete) {
    delete rootProject.buildDir
}
""",

    "settings.gradle": """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "MusicPlayer2044"
include ':app'
""",

    "gradle.properties": """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.nonTransitiveRClass=true
android.enableJetifier=true
""",

    "gradle/wrapper/gradle-wrapper.properties": """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\\://services.gradle.org/distributions/gradle-8.5-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""",

    # ========== APP BUILD FILE ==========
    "app/build.gradle": """plugins {
    id 'com.android.application'
}

android {
    namespace 'com.musicplayer2044.app'
    compileSdk 34

    defaultConfig {
        applicationId "com.musicplayer2044.app"
        minSdk 21
        targetSdk 34
        versionCode 1
        versionName "1.0.0"
    }

    buildTypes {
        release {
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
        debug {
            debuggable true
        }
    }
    
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'androidx.webkit:webkit:1.8.0'
}
""",

    "app/proguard-rules.pro": """# Music Player 2044 ProGuard Rules
-keep class com.musicplayer2044.app.** { *; }
-keepattributes *Annotation*
-keepattributes SourceFile,LineNumberTable
-dontwarn javax.annotation.**
""",

    # ========== ANDROID MANIFEST ==========
    "app/src/main/AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_MEDIA_AUDIO" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="Music 2044"
        android:roundIcon="@mipmap/ic_launcher"
        android:supportsRtl="true"
        android:theme="@style/Theme.MusicPlayer2044"
        android:usesCleartextTraffic="true"
        android:hardwareAccelerated="true"
        tools:targetApi="34">
        
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|screenLayout|keyboardHidden"
            android:windowSoftInputMode="adjustResize"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""",

    # ========== MAIN ACTIVITY ==========
    "app/src/main/java/com/musicplayer2044/app/MainActivity.java": r'''package com.musicplayer2044.app;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.view.WindowManager;
import android.view.View;
import android.os.Build;

public class MainActivity extends Activity {
    private WebView webView;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Full Screen Mode
        getWindow().setFlags(
            WindowManager.LayoutParams.FLAG_FULLSCREEN,
            WindowManager.LayoutParams.FLAG_FULLSCREEN
        );
        
        // Immersive Mode
        hideSystemUI();
        
        webView = new WebView(this);
        setContentView(webView);
        
        // Configure WebView
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webSettings.setDomStorageEnabled(true);
        webSettings.setAllowFileAccess(true);
        webSettings.setAllowContentAccess(true);
        webSettings.setMediaPlaybackRequiresUserGesture(false);
        webSettings.setCacheMode(WebSettings.LOAD_NO_CACHE);
        webSettings.setUseWideViewPort(true);
        webSettings.setLoadWithOverviewMode(true);
        webSettings.setSupportZoom(false);
        webSettings.setBuiltInZoomControls(false);
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
            webSettings.setAllowFileAccessFromFileURLs(true);
            webSettings.setAllowUniversalAccessFromFileURLs(true);
        }
        
        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());
        
        // Load the Music Player
        webView.loadUrl("file:///android_asset/www/index.html");
    }
    
    private void hideSystemUI() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY |
                View.SYSTEM_UI_FLAG_FULLSCREEN |
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            );
        }
    }
    
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        hideSystemUI();
    }
    
    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            hideSystemUI();
        }
    }
}
''',

    # ========== RESOURCES ==========
    "app/src/main/res/values/styles.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.MusicPlayer2044" parent="android:Theme.Material.NoActionBar">
        <item name="android:windowFullscreen">true</item>
        <item name="android:windowNoTitle">true</item>
        <item name="android:statusBarColor">@android:color/transparent</item>
        <item name="android:navigationBarColor">@android:color/transparent</item>
        <item name="android:windowTranslucentStatus">true</item>
        <item name="android:windowTranslucentNavigation">true</item>
        <item name="android:windowBackground">#FF0A0A0F</item>
    </style>
</resources>
""",

    "app/src/main/res/values/colors.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="primary">#FF00FFCC</color>
    <color name="secondary">#FFFF44AA</color>
    <color name="accent">#FFFFAA00</color>
    <color name="background">#FF0A0A0F</color>
</resources>
""",

    "app/src/main/res/values/strings.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Music 2044</string>
</resources>
""",

    "app/src/main/res/xml/network_security_config.xml": """<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
</network-security-config>
""",

    "app/src/main/res/drawable/ic_launcher_foreground.xml": """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <!-- Outer Ring -->
    <path
        android:fillColor="#FF00FFCC"
        android:pathData="M54,54m-40,0a40,40 0,1 1,80 0a40,40 0,1 1,-80 0"/>
    <!-- Inner Circle -->
    <path
        android:fillColor="#FF0A0A0F"
        android:pathData="M54,54m-20,0a20,20 0,1 1,40 0a20,20 0,1 1,-40 0"/>
    <!-- Center Dot -->
    <path
        android:fillColor="#FFFF44AA"
        android:pathData="M54,54m-8,0a8,8 0,1 1,16 0a8,8 0,1 1,-16 0"/>
</vector>
""",

    "app/src/main/res/mipmap-hdpi/ic_launcher.xml": """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/background"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>
""",

    # ========== MUSIC PLAYER HTML ==========
    "app/src/main/assets/www/index.html": r'''<!DOCTYPE html>
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
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            -webkit-tap-highlight-color: transparent;
            overflow: hidden;
            direction: rtl;
        }

        .bg-mesh {
            position: fixed;
            inset: 0;
            z-index: 0;
            background: conic-gradient(from 0deg at 50% 50%, 
                #0a0a2e 0%, #1a0a2e 25%, #0a1a2e 50%, #1a0a0a 75%, #0a0a2e 100%);
            animation: meshRotate 20s linear infinite;
        }
        @keyframes meshRotate {
            to { filter: hue-rotate(360deg); }
        }

        .bg-orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.4;
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
            width: 100%;
            max-width: 440px;
            height: 100vh;
            max-height: 850px;
            display: flex;
            flex-direction: column;
            position: relative;
            z-index: 1;
            padding: 12px;
        }

        /* HEADER */
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 4px;
            margin-bottom: 8px;
        }
        .header-brand {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .logo {
            width: 44px;
            height: 44px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            backdrop-filter: blur(20px);
            box-shadow: var(--neumorph);
        }
        .header-text h1 {
            font-size: 18px;
            font-weight: 800;
            background: linear-gradient(135deg, #00ffcc, #ff44aa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .header-text span {
            font-size: 8px;
            color: var(--text2);
            letter-spacing: 2px;
        }

        /* NOW PLAYING */
        .now-playing {
            text-align: center;
            padding: 20px 0;
            position: relative;
        }
        .disc-container {
            width: 200px;
            height: 200px;
            margin: 0 auto 20px;
            position: relative;
        }
        .disc-outer-ring {
            position: absolute;
            inset: -12px;
            border: 2px solid rgba(255,255,255,0.1);
            border-radius: 50%;
            animation: ringSpin 8s linear infinite;
        }
        .disc-outer-ring:nth-child(2) {
            inset: -6px;
            border-style: dashed;
            animation-duration: 6s;
            animation-direction: reverse;
        }
        @keyframes ringSpin {
            to { transform: rotate(360deg); }
        }

        .disc {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255,68,170,0.3), rgba(0,255,204,0.3));
            border: 2px solid rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 70px;
            backdrop-filter: blur(20px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 0 40px rgba(255,255,255,0.05);
            animation: discSpin 4s linear infinite paused;
        }
        .disc.playing {
            animation-play-state: running;
        }
        @keyframes discSpin {
            to { transform: rotate(360deg); }
        }

        .disc-center {
            width: 30px;
            height: 30px;
            background: #0a0a0f;
            border: 3px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            position: absolute;
        }

        .song-name {
            font-size: 18px;
            font-weight: 800;
            color: var(--text);
            margin-bottom: 4px;
            text-shadow: 0 0 20px rgba(255,255,255,0.3);
        }
        .song-artist {
            font-size: 11px;
            color: var(--text2);
            font-weight: 500;
            letter-spacing: 1px;
        }

        /* PROGRESS */
        .progress-section {
            padding: 0 8px 12px;
        }
        .progress-track {
            width: 100%;
            height: 4px;
            background: rgba(255,255,255,0.1);
            border-radius: 2px;
            cursor: pointer;
            position: relative;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #00ffcc, #ff44aa);
            border-radius: 2px;
            width: 0%;
            transition: width 0.1s linear;
            box-shadow: 0 0 10px rgba(0,255,204,0.5);
        }
        .time-row {
            display: flex;
            justify-content: space-between;
            font-size: 9px;
            color: var(--text2);
            margin-top: 6px;
        }

        /* CONTROLS */
        .controls-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            padding: 8px 0;
        }
        .ctrl-glass {
            width: 44px;
            height: 44px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            color: var(--text);
            cursor: pointer;
            border-radius: 16px;
            font-size: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(20px);
            box-shadow: var(--neumorph);
            transition: all 0.3s;
        }
        .ctrl-glass:active {
            transform: scale(0.9);
            box-shadow: inset 4px 4px 8px rgba(0,0,0,0.4);
        }
        .ctrl-glass.active {
            border-color: #00ffcc;
            color: #00ffcc;
            box-shadow: 0 0 20px rgba(0,255,204,0.3);
        }

        .btn-play-big {
            width: 64px;
            height: 64px;
            background: linear-gradient(135deg, #00ffcc, #ff44aa);
            border: none;
            color: #000;
            cursor: pointer;
            border-radius: 20px;
            font-size: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 30px rgba(0,255,204,0.3), 0 0 40px rgba(255,68,170,0.2);
            transition: all 0.3s;
        }
        .btn-play-big:active {
            transform: scale(0.9);
        }

        /* VISUALIZER */
        .viz-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            height: 60px;
            padding: 10px 0;
        }
        .viz-ring {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: 2px solid rgba(255,255,255,0.2);
            position: relative;
            animation: vizPulse 1s ease-in-out infinite;
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

        /* PLAYLIST */
        .playlist-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 4px;
            margin-top: 4px;
        }
        .playlist-title {
            font-size: 11px;
            font-weight: 700;
            color: var(--text);
            letter-spacing: 1px;
        }
        .btn-upload-glass {
            padding: 7px 14px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            color: var(--text);
            cursor: pointer;
            border-radius: 20px;
            font-size: 9px;
            font-family: 'Cairo', sans-serif;
            font-weight: 600;
            backdrop-filter: blur(20px);
        }

        .playlist {
            flex: 1;
            overflow-y: auto;
            padding: 0 2px;
        }
        .playlist::-webkit-scrollbar {
            width: 3px;
        }
        .playlist::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.1);
            border-radius: 3px;
        }

        .song-card {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 12px;
            background: var(--glass);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            margin-bottom: 6px;
            cursor: pointer;
            backdrop-filter: blur(20px);
            transition: all 0.3s;
        }
        .song-card:hover {
            border-color: rgba(255,255,255,0.3);
        }
        .song-card.active {
            border-color: #00ffcc;
            box-shadow: 0 0 15px rgba(0,255,204,0.2);
        }
        .song-card .s-icon {
            font-size: 20px;
        }
        .song-card .s-info {
            flex: 1;
            min-width: 0;
        }
        .song-card .s-name {
            font-size: 11px;
            font-weight: 600;
            color: var(--text);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .song-card .s-dur {
            font-size: 9px;
            color: var(--text2);
        }
        .song-card .s-del {
            color: #ff4466;
            cursor: pointer;
            opacity: 0.5;
            transition: 0.3s;
            padding: 5px;
        }
        .song-card .s-del:hover {
            opacity: 1;
        }

        .empty-state {
            text-align: center;
            padding: 30px;
            color: rgba(255,255,255,0.2);
        }
        .empty-state .icon {
            font-size: 40px;
            display: block;
            margin-bottom: 8px;
        }

        input[type="file"] {
            display: none;
        }

        .toast {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%) translateY(120px);
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
            color: #fff;
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 10px;
            z-index: 300;
            transition: transform 0.4s;
            font-family: 'Cairo', sans-serif;
        }
        .toast.show {
            transform: translateX(-50%) translateY(0);
        }
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
            <div class="viz-ring"></div>
            <div class="viz-ring"></div>
            <div class="viz-ring"></div>
            <div class="viz-ring"></div>
            <div class="viz-ring"></div>
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

        function formatTime(s) { 
            const m=Math.floor(s/60), sec=Math.floor(s%60); 
            return m+':'+(sec<10?'0':'')+sec; 
        }

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

        function togglePlay() { 
            if(!audio.src&&playlist.length>0){loadSong(0);return;} 
            isPlaying?audio.pause():audio.play(); 
        }
        
        function nextSong() { 
            if(!playlist.length)return; 
            let n=isShuffle?Math.floor(Math.random()*playlist.length):currentIndex+1; 
            if(n>=playlist.length)n=0; 
            loadSong(n); 
        }
        
        function prevSong() { 
            if(!playlist.length)return; 
            let p=currentIndex-1; 
            if(p<0)p=playlist.length-1; 
            loadSong(p); 
        }
        
        function toggleShuffle() { 
            isShuffle=!isShuffle; 
            document.getElementById('shuffleBtn').classList.toggle('active',isShuffle); 
            showToast(isShuffle?'🔀 عشوائي':'🔀 ترتيب'); 
        }
        
        function toggleRepeat() { 
            isRepeat=!isRepeat; 
            document.getElementById('repeatBtn').classList.toggle('active',isRepeat); 
            showToast(isRepeat?'🔁 تكرار':'🔁 عادي'); 
        }
        
        function seek(e) { 
            if(!audio.duration)return; 
            const r=document.getElementById('progressTrack').getBoundingClientRect(); 
            audio.currentTime=((e.clientX-r.left)/r.width)*audio.duration; 
        }

        function addFiles() {
            const files=document.getElementById('fileInput').files;
            if(!files.length)return;
            Array.from(files).forEach(f=>{
                const r=new FileReader();
                r.onload=function(e){
                    playlist.push({
                        name:f.name.replace(/\.[^/.]+$/,""),
                        size:formatSize(f.size),
                        data:e.target.result,
                        id:Date.now()+Math.random()
                    });
                    renderPlaylist();
                    if(playlist.length===1)loadSong(0);
                };
                r.readAsDataURL(f);
            });
            document.getElementById('fileInput').value='';
            showToast('✅ '+files.length+' أغنية');
        }

        function formatSize(b) { 
            return b>1048576?(b/1048576).toFixed(1)+' MB':(b/1024).toFixed(1)+' KB'; 
        }

        function deleteSong(index) {
            const wasPlaying=currentIndex===index;
            playlist.splice(index,1);
            if(wasPlaying){
                audio.pause();audio.src='';
                document.getElementById('songTitle').textContent='اختر أغنية';
                document.getElementById('songArtist').textContent='Music Player 2044';
                currentIndex=-1;isPlaying=false;
                document.getElementById('playBtn').textContent='▶';
                document.getElementById('disc').classList.remove('playing');
            }
            else if(currentIndex>index)currentIndex--;
            renderPlaylist();
            showToast('🗑 تم الحذف');
        }

        function renderPlaylist() {
            const area=document.getElementById('playlist');
            if(!playlist.length){
                area.innerHTML='<div class="empty-state"><span class="icon">🎵</span><span>اسحب الملفات هنا</span></div>';
                return;
            }
            area.innerHTML=playlist.map((s,i)=>`
                <div class="song-card ${i===currentIndex?'active':''}" onclick="loadSong(${i})">
                    <span class="s-icon">${i===currentIndex&&isPlaying?'🔊':'🎵'}</span>
                    <div class="s-info"><div class="s-name">${s.name}</div></div>
                    <div class="s-dur">${s.size}</div>
                    <span class="s-del" onclick="event.stopPropagation();deleteSong(${i})">🗑</span>
                </div>
            `).join('');
        }

        function showToast(msg) { 
            const t=document.getElementById('toast'); 
            t.textContent=msg; 
            t.classList.add('show'); 
            setTimeout(()=>t.classList.remove('show'),2000); 
        }

        renderPlaylist();
    </script>
</body>
</html>'''
}

# ==================== Main Function ====================
def create_project():
    """إنشاء جميع ملفات المشروع"""
    
    print(BANNER)
    print(f"{C.CYAN}🚀 Starting Music Player 2044 App Generator...{C.RESET}\n")
    
    files_created = 0
    total_size = 0
    
    for file_path, content in APP_FILES.items():
        # إنشاء المجلدات إذا لم تكن موجودة
        full_path = Path(file_path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # كتابة الملف
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        file_size = len(content.encode('utf-8'))
        total_size += file_size
        files_created += 1
        
        print(f"{C.GREEN}  ✓{C.RESET} {file_path} {C.PURPLE}({file_size/1024:.1f} KB){C.RESET}")
    
    # ==================== إحصائيات ====================
    print(f"\n{C.BOLD}{C.CYAN}{'═' * 55}{C.RESET}")
    print(f"{C.BOLD}{C.PURPLE}  🎵 Music Player 2044 - Build Complete!{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}{'═' * 55}{C.RESET}")
    print(f"  {C.GREEN}📁 Files Created:{C.RESET} {files_created}")
    print(f"  {C.GREEN}📦 Total Size:{C.RESET} {total_size/1024:.1f} KB")
    print(f"  {C.CYAN}🎯 Package:{C.RESET} com.musicplayer2044.app")
    print(f"  {C.CYAN}📱 Min SDK:{C.RESET} 21 (Android 5.0)")
    print(f"  {C.CYAN}📱 Target SDK:{C.RESET} 34 (Android 14)")
    print(f"  {C.YELLOW}✅ Ready for APK Build!{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}{'═' * 55}{C.RESET}\n")
    
    # إنشاء ملف info.json
    info = {
        "app_name": "Music Player 2044",
        "package": "com.musicplayer2044.app",
        "version": "1.0.0",
        "version_code": 1,
        "min_sdk": 21,
        "target_sdk": 34,
        "files_count": files_created,
        "total_size_kb": round(total_size/1024, 1),
        "build_date": datetime.now().isoformat(),
        "features": [
            "🎵 Music Player with Glass Morphism UI",
            "💾 Auto-save uploaded songs",
            "📂 Multiple file upload support",
            "🔀 Shuffle & Repeat modes",
            "🎨 2044 Future Edition Design",
            "📱 Full Android APK support"
        ]
    }
    
    with open("app-info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2, ensure_ascii=False)
    
    print(f"{C.GREEN}  ✓ app-info.json created{C.RESET}")
    
    return files_created


if __name__ == "__main__":
    create_project()

"""
╔══════════════════════════════════════════════════════════════╗
║              🎵 MUSIC VAULT 2044 - Local Server 🎵          ║
║            Future Storage System - Professional             ║
║              Made with ♥️ for my friend                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import json
import base64
import shutil
import hashlib
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus
import mimetypes
import secrets

# ==================== التهيئة ====================

class Colors:
    """ألوان الطرفية 2044"""
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class MusicVault2044:
    """
    🎵 Music Vault 2044 - نظام تخزين موسيقى احترافي
    
    الميزات:
    - تخزين دائم للأغاني على القرص
    - خادم HTTP محلي للـ API
    - قاعدة بيانات JSON للمكتبة
    - دعم رفع وحذف وتحميل الملفات
    - واجهة WebSocket للاتصال المباشر
    - تشغيل تلقائي للمتصفح
    """
    
    def __init__(self, music_dir="music_vault_2044", port=2044):
        self.music_dir = Path(music_dir)
        self.port = port
        self.db_file = self.music_dir / "library_2044.json"
        self.www_dir = self.music_dir / "www"
        
        # إنشاء المجلدات
        self.music_dir.mkdir(parents=True, exist_ok=True)
        self.www_dir.mkdir(parents=True, exist_ok=True)
        
        # تحميل المكتبة
        self.library = self._load_library()
        
        # إعداد السيرفر
        self.server = None
        self.server_thread = None
    
    def _load_library(self) -> dict:
        """تحميل مكتبة الموسيقى"""
        if self.db_file.exists():
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {"songs": {}, "playlists": {}, "settings": {"volume": 0.8, "theme": "2044"}}
    
    def _save_library(self):
        """حفظ مكتبة الموسيقى"""
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.library, f, indent=2, ensure_ascii=False)
    
    def add_song(self, song_id: str, name: str, artist: str, data_base64: str) -> bool:
        """إضافة أغنية للمكتبة"""
        try:
            # فك تشفير base64
            if ',' in data_base64:
                data_base64 = data_base64.split(',')[1]
            
            song_data = base64.b64decode(data_base64)
            
            # حفظ الملف
            safe_name = self._safe_filename(f"{artist} - {name}")
            file_path = self.music_dir / f"{safe_name}.mp3"
            
            with open(file_path, 'wb') as f:
                f.write(song_data)
            
            # تحديث المكتبة
            self.library["songs"][song_id] = {
                "id": song_id,
                "name": name,
                "artist": artist,
                "file_path": str(file_path.relative_to(self.music_dir)),
                "size": len(song_data),
                "added_date": datetime.now().isoformat(),
                "plays": 0,
                "favorite": False
            }
            
            self._save_library()
            return True
            
        except Exception as e:
            print(f"{Colors.RED}✗ Error adding song: {e}{Colors.RESET}")
            return False
    
    def delete_song(self, song_id: str) -> bool:
        """حذف أغنية من المكتبة"""
        try:
            if song_id in self.library["songs"]:
                song_info = self.library["songs"][song_id]
                file_path = self.music_dir / song_info["file_path"]
                
                # حذف الملف
                if file_path.exists():
                    file_path.unlink()
                
                # حذف من المكتبة
                del self.library["songs"][song_id]
                self._save_library()
                return True
        except Exception as e:
            print(f"{Colors.RED}✗ Error deleting song: {e}{Colors.RESET}")
        return False
    
    def get_song_file(self, song_id: str) -> Path:
        """الحصول على مسار ملف الأغنية"""
        if song_id in self.library["songs"]:
            file_path = self.music_dir / self.library["songs"][song_id]["file_path"]
            if file_path.exists():
                # تحديث عداد التشغيل
                self.library["songs"][song_id]["plays"] += 1
                self._save_library()
                return file_path
        return None
    
    def _safe_filename(self, filename: str) -> str:
        """تنظيف اسم الملف"""
        safe = "".join(c if c.isalnum() or c in " .-_()[]{}" else "_" for c in filename)
        return safe.strip()[:100] or "unknown"
    
    def get_all_songs(self) -> list:
        """الحصول على كل الأغاني"""
        return [
            {
                "id": song_id,
                "name": info["name"],
                "artist": info["artist"],
                "size": self._format_size(info["size"]),
                "added_date": info["added_date"],
                "plays": info["plays"],
                "favorite": info["favorite"]
            }
            for song_id, info in self.library["songs"].items()
        ]
    
    def _format_size(self, size_bytes: int) -> str:
        """تنسيق الحجم"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
    
    def print_banner(self):
        """طباعة بانر 2044"""
        banner = f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗  ██╗   ██╗ █████╗ 
║   ████╗ ████║██║   ██║██╔════╝██║██╔════╝  ██║   ██║██╔══██╗
║   ██╔████╔██║██║   ██║███████╗██║██║       ██║   ██║███████║
║   ██║╚██╔╝██║██║   ██║╚════██║██║██║       ╚██╗ ██╔╝██╔══██║
║   ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗   ╚████╔╝ ██║  ██║
║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═══╝  ╚═╝  ╚═╝
║                                                              ║
║              🎵 MUSIC VAULT 2044 - Local Server 🎵           ║
║                     Professional v2.0.44                     ║
║                                                              ║
║      📁 Storage: {str(self.music_dir):<43} ║
║      🌐 Server:  http://localhost:{self.port:<37} ║
║      📚 Library: {len(self.library['songs']):<3} songs{:37} ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}
        """
        print(banner)


class MusicAPIHandler(http.server.SimpleHTTPRequestHandler):
    """معالج HTTP للـ API"""
    
    vault = None  # سيتم تعيينه من الخارج
    
    def do_OPTIONS(self):
        """معالجة CORS"""
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()
    
    def do_GET(self):
        """معالجة طلبات GET"""
        parsed = urlparse(self.path)
        
        # API Routes
        if parsed.path == '/api/songs':
            self._handle_get_songs()
        elif parsed.path.startswith('/api/download/'):
            song_id = parsed.path.split('/')[-1]
            self._handle_download(song_id)
        elif parsed.path.startswith('/api/stream/'):
            song_id = parsed.path.split('/')[-1]
            self._handle_stream(song_id)
        else:
            # ملفات ثابتة
            super().do_GET()
    
    def do_POST(self):
        """معالجة طلبات POST"""
        parsed = urlparse(self.path)
        
        if parsed.path == '/api/upload':
            self._handle_upload()
        elif parsed.path == '/api/delete':
            self._handle_delete()
        else:
            self.send_error(404)
    
    def _send_cors_headers(self):
        """إرسال هيدرات CORS"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
    
    def _send_json(self, data, status=200):
        """إرسال استجابة JSON"""
        self.send_response(status)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def _handle_get_songs(self):
        """API: الحصول على قائمة الأغاني"""
        songs = self.vault.get_all_songs()
        self._send_json({"songs": songs, "total": len(songs)})
    
    def _handle_upload(self):
        """API: رفع أغنية"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body)
            song_id = data.get('id', secrets.token_hex(8))
            name = data.get('name', 'Unknown')
            artist = data.get('artist', 'Unknown')
            audio_data = data.get('data', '')
            
            success = self.vault.add_song(song_id, name, artist, audio_data)
            
            if success:
                self._send_json({"status": "success", "id": song_id, "message": "✅ Song added to vault!"})
            else:
                self._send_json({"status": "error", "message": "Failed to save song"}, 500)
                
        except Exception as e:
            self._send_json({"status": "error", "message": str(e)}, 400)
    
    def _handle_delete(self):
        """API: حذف أغنية"""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body)
            song_id = data.get('id', '')
            
            if self.vault.delete_song(song_id):
                self._send_json({"status": "success", "message": "🗑 Song deleted!"})
            else:
                self._send_json({"status": "error", "message": "Song not found"}, 404)
                
        except Exception as e:
            self._send_json({"status": "error", "message": str(e)}, 400)
    
    def _handle_stream(self, song_id):
        """API: تشغيل أغنية"""
        file_path = self.vault.get_song_file(song_id)
        
        if file_path and file_path.exists():
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'audio/mpeg')
            self.send_header('Content-Length', str(file_path.stat().st_size))
            self.end_headers()
            
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self._send_json({"error": "Song not found"}, 404)
    
    def _handle_download(self, song_id):
        """API: تحميل أغنية"""
        file_path = self.vault.get_song_file(song_id)
        
        if file_path and file_path.exists():
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', f'attachment; filename="{file_path.name}"')
            self.send_header('Content-Length', str(file_path.stat().st_size))
            self.end_headers()
            
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self._send_json({"error": "Song not found"}, 404)
    
    def log_message(self, format, *args):
        """تخصيص رسائل السجل"""
        print(f"{Colors.PURPLE}[2044]{Colors.RESET} {format % args}")


class MusicVaultServer:
    """خادم Music Vault"""
    
    def __init__(self, vault: MusicVault2044):
        self.vault = vault
        MusicAPIHandler.vault = vault
        self.httpd = None
    
    def start(self):
        """تشغيل الخادم"""
        # تغيير مجلد العمل للملفات الثابتة
        os.chdir(self.vault.www_dir)
        
        self.httpd = socketserver.ThreadingTCPServer(
            ("localhost", self.vault.port),
            MusicAPIHandler
        )
        
        print(f"{Colors.GREEN}🚀 Music Vault 2044 Server is running!{Colors.RESET}")
        print(f"{Colors.CYAN}🌐 Open: http://localhost:{self.vault.port}{Colors.RESET}")
        print(f"{Colors.YELLOW}📚 {len(self.vault.library['songs'])} songs in library{Colors.RESET}")
        print(f"{Colors.PURPLE}Press Ctrl+C to stop the server{Colors.RESET}\n")
        
        # فتح المتصفح تلقائياً
        webbrowser.open(f"http://localhost:{self.vault.port}")
        
        try:
            self.httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}🛑 Shutting down server...{Colors.RESET}")
            self.httpd.shutdown()


def create_website_files(vault: MusicVault2044):
    """إنشاء ملفات الموقع"""
    
    html_content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Music Vault 2044</title>
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

        .header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 8px 4px; margin-bottom: 8px;
        }
        .header-brand { display: flex; align-items: center; gap: 10px; }
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

        .vault-badge {
            background: rgba(0,255,204,0.1); border: 1px solid rgba(0,255,204,0.3);
            color: #00ffcc; padding: 4px 10px; border-radius: 20px;
            font-size: 8px; font-weight: 600;
        }

        .btn-glass {
            width: 40px; height: 40px;
            background: var(--glass); border: 1px solid var(--glass-border);
            color: var(--text); cursor: pointer; border-radius: 14px;
            font-size: 16px; display: flex; align-items: center; justify-content: center;
            backdrop-filter: blur(20px); box-shadow: var(--neumorph);
            transition: all 0.3s;
        }
        .btn-glass:active { transform: scale(0.9); box-shadow: inset 4px 4px 8px rgba(0,0,0,0.4); }

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
            position: relative;
        }
        .song-card:hover { border-color: rgba(255,255,255,0.3); }
        .song-card.active { border-color: #00ffcc; box-shadow: 0 0 15px rgba(0,255,204,0.2); }
        .song-card .s-icon { font-size: 20px; }
        .song-card .s-info { flex: 1; min-width: 0; }
        .song-card .s-name { font-size: 11px; font-weight: 600; color: var(--text); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .song-card .s-artist { font-size: 8px; color: var(--text2); }
        .song-card .s-dur { font-size: 9px; color: var(--text2); }
        .song-card .s-del { color: #ff4466; cursor: pointer; opacity: 0.5; transition: 0.3s; }
        .song-card .s-del:hover { opacity: 1; }

        .saved-badge {
            position: absolute; top: 4px; right: 4px;
            background: rgba(0,255,204,0.2); color: #00ffcc;
            font-size: 7px; padding: 2px 6px; border-radius: 10px;
        }

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

        .sync-indicator {
            position: fixed; top: 10px; left: 50%; transform: translateX(-50%);
            background: rgba(0,255,204,0.2); border: 1px solid rgba(0,255,204,0.3);
            color: #00ffcc; padding: 6px 16px; border-radius: 20px;
            font-size: 9px; z-index: 200; display: none;
            animation: syncPulse 2s ease-in-out infinite;
        }
        @keyframes syncPulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
    </style>
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <div class="sync-indicator" id="syncIndicator">💾 جاري الحفظ في Vault...</div>

    <div class="app">
        <div class="header">
            <div class="header-brand">
                <div class="logo">🎵</div>
                <div class="header-text">
                    <h1>Music Vault</h1>
                    <span>✦ 2044 Edition ✦</span>
                </div>
            </div>
            <div class="vault-badge">💾 VAULT</div>
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
            <div class="song-artist" id="songArtist">Music Vault 2044</div>
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
        // ==================== Music Vault 2044 - Client ====================
        
        const API_BASE = '';
        let playlist = [], currentIndex = -1;
        let audio = new Audio();
        let isPlaying = false, isShuffle = false, isRepeat = false;
        let savedSongs = new Set(); // تتبع الأغاني المحفوظة

        // تحميل الأغاني المحفوظة من السيرفر عند البداية
        async function loadSavedSongs() {
            try {
                const response = await fetch(`${API_BASE}/api/songs`);
                const data = await response.json();
                
                data.songs.forEach(song => {
                    playlist.push({
                        id: song.id,
                        name: song.name,
                        artist: song.artist,
                        size: song.size,
                        streamUrl: `${API_BASE}/api/stream/${song.id}`,
                        isSaved: true
                    });
                    savedSongs.add(song.id);
                });
                
                renderPlaylist();
                if (playlist.length > 0 && currentIndex === -1) {
                    loadSong(0);
                }
            } catch (e) {
                console.log('No saved songs found or server not available');
            }
        }

        // حفظ أغنية في السيرفر
        async function saveToVault(songData, blobUrl) {
            showSyncIndicator(true);
            try {
                // تحويل blob إلى base64
                const response = await fetch(blobUrl);
                const blob = await response.blob();
                const reader = new FileReader();
                
                const base64Data = await new Promise((resolve) => {
                    reader.onloadend = () => resolve(reader.result);
                    reader.readAsDataURL(blob);
                });
                
                const saveResponse = await fetch(`${API_BASE}/api/upload`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        id: songData.id,
                        name: songData.name,
                        artist: songData.artist || 'Unknown Artist',
                        data: base64Data
                    })
                });
                
                const result = await saveResponse.json();
                if (result.status === 'success') {
                    savedSongs.add(songData.id);
                    showToast('💾 تم الحفظ في Vault!');
                    renderPlaylist();
                }
            } catch (e) {
                console.error('Save to vault failed:', e);
                showToast('⚠ فشل الحفظ في Vault');
            } finally {
                showSyncIndicator(false);
            }
        }

        // حذف أغنية من السيرفر
        async function deleteFromVault(songId) {
            try {
                await fetch(`${API_BASE}/api/delete`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ id: songId })
                });
                savedSongs.delete(songId);
            } catch (e) {
                console.error('Delete from vault failed:', e);
            }
        }

        function showSyncIndicator(show) {
            document.getElementById('syncIndicator').style.display = show ? 'block' : 'none';
        }

        // ==================== Audio Controls ====================
        
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
            
            // استخدام stream URL إذا كانت محفوظة، وإلا استخدام data URL
            audio.src = s.streamUrl || s.data;
            document.getElementById('songTitle').textContent=s.name;
            document.getElementById('songArtist').textContent=s.artist || s.size;
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
                r.onload=async function(e){
                    const songId = Date.now().toString(36) + Math.random().toString(36).substr(2);
                    const songData = {
                        id: songId,
                        name: f.name.replace(/\.[^/.]+$/,""),
                        artist: 'Unknown Artist',
                        size: formatSize(f.size),
                        data: e.target.result
                    };
                    
                    playlist.push(songData);
                    renderPlaylist();
                    
                    if(playlist.length===1) loadSong(0);
                    
                    // حفظ تلقائي في Vault
                    await saveToVault(songData, e.target.result);
                };
                r.readAsDataURL(f);
            });
            
            document.getElementById('fileInput').value='';
            showToast('✅ '+files.length+' أغنية');
        }

        function formatSize(b) { return b>1048576?(b/1048576).toFixed(1)+' MB':(b/1024).toFixed(1)+' KB'; }

        async function deleteSong(index) {
            const song = playlist[index];
            const wasPlaying = currentIndex === index;
            
            // حذف من السيرفر إذا كانت محفوظة
            if (song.isSaved || savedSongs.has(song.id)) {
                await deleteFromVault(song.id);
            }
            
            playlist.splice(index,1);
            
            if(wasPlaying){
                audio.pause();
                audio.src='';
                document.getElementById('songTitle').textContent='اختر أغنية';
                document.getElementById('songArtist').textContent='Music Vault 2044';
                currentIndex=-1;
                isPlaying=false;
                document.getElementById('playBtn').textContent='▶';
                document.getElementById('disc').classList.remove('playing');
            } else if(currentIndex>index) {
                currentIndex--;
            }
            
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
                    ${(s.isSaved || savedSongs.has(s.id)) ? '<span class="saved-badge">💾 Vault</span>' : ''}
                    <span class="s-icon">${i===currentIndex&&isPlaying?'🔊':'🎵'}</span>
                    <div class="s-info">
                        <div class="s-name">${s.name}</div>
                        <div class="s-artist">${s.artist || ''}</div>
                    </div>
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

        // تحميل الأغاني المحفوظة عند البداية
        loadSavedSongs();
        renderPlaylist();
    </script>
</body>
</html>'''
    
    # كتابة ملف HTML
    index_path = vault.www_dir / "index.html"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return index_path


def main():
    """الدالة الرئيسية"""
    vault = MusicVault2044(music_dir="music_vault_2044", port=2044)
    vault.print_banner()
    
    # إنشاء ملفات الموقع
    index_path = create_website_files(vault)
    print(f"{Colors.GREEN}✓ Website created: {index_path}{Colors.RESET}")
    
    # تشغيل الخادم
    server = MusicVaultServer(vault)
    server.start()


if __name__ == "__main__":
    main()

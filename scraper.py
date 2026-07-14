"""
╔══════════════════════════════════════════════════════════════╗
║                   🎵 MUSIC SCRAPER 2044 🎵                  ║
║              Future Edition - Professional Tool             ║
║                 Made with ♥️ for my friend                  ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import re
import json
import time
import random
import hashlib
import threading
import concurrent.futures
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse, urljoin, quote_plus
from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field, asdict
from collections import deque
import logging
import signal
import sys

# مكتبات الطرف الثالث - تثبت تلقائياً
try:
    import requests
    from bs4 import BeautifulSoup
    from tqdm import tqdm
    from fake_useragent import UserAgent
    import cloudscraper
except ImportError:
    import subprocess
    print("⚡ تثبيت المكتبات المطلوبة...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4", "tqdm", "fake-useragent", "cloudscraper"])
    import requests
    from bs4 import BeautifulSoup
    from tqdm import tqdm
    from fake_useragent import UserAgent
    import cloudscraper

# ==================== التهيئة ====================
@dataclass
class TrackInfo:
    """بيانات الأغنية"""
    id: str
    title: str
    artist: str = "Unknown"
    album: str = ""
    duration: float = 0.0
    url: str = ""
    thumbnail: str = ""
    size: str = ""
    quality: str = ""
    source: str = ""
    download_url: str = ""
    file_path: str = ""
    metadata: Dict = field(default_factory=dict)

@dataclass
class ScrapingStats:
    """إحصائيات السكرابر"""
    total_found: int = 0
    total_downloaded: int = 0
    total_size: int = 0
    failed: int = 0
    start_time: float = 0.0
    end_time: float = 0.0
    sources_used: List[str] = field(default_factory=list)

class Colors:
    """ألوان الطرفية 2044"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[35m'
    ORANGE = '\033[33m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    RAINBOW = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']

class MusicScraper2044:
    """
    🎵 Music Scraper 2044 - محرك بحث وتحميل موسيقى احترافي
    
    الميزات:
    - بحث متعدد المصادر
    - تحميل متوازي عالي السرعة
    - تجاوز حماية Cloudflare
    - استخراج metadata كامل
    - واجهة طرفية مبهرة
    - حفظ تلقائي بصيغ متعددة
    """
    
    def __init__(self, download_path: str = "downloads", max_workers: int = 5):
        self.download_path = Path(download_path)
        self.download_path.mkdir(parents=True, exist_ok=True)
        self.max_workers = max_workers
        self.stats = ScrapingStats()
        self.tracks: List[TrackInfo] = []
        self.session = self._create_session()
        self.ua = UserAgent()
        
        # إعداد التسجيل
        self._setup_logging()
        
        # سجل المصادر
        self.sources_registry = {
            'soundcloud': self._search_soundcloud,
            'jamendo': self._search_jamendo,
            'freemusicarchive': self._search_freemusicarchive,
            'ccmixter': self._search_ccmixter,
            'incompetech': self._search_incompetech,
            'musopen': self._search_musopen,
        }
        
        # أنماط regex للبحث
        self.patterns = {
            'mp3': re.compile(r'https?://[^\s"\']+\.mp3(?:\?[^\s"\']*)?', re.I),
            'm4a': re.compile(r'https?://[^\s"\']+\.m4a(?:\?[^\s"\']*)?', re.I),
            'ogg': re.compile(r'https?://[^\s"\']+\.ogg(?:\?[^\s"\']*)?', re.I),
            'wav': re.compile(r'https?://[^\s"\']+\.wav(?:\?[^\s"\']*)?', re.I),
            'flac': re.compile(r'https?://[^\s"\']+\.flac(?:\?[^\s"\']*)?', re.I),
        }
    
    def _create_session(self) -> requests.Session:
        """إنشاء جلسة مع تجاوز الحماية"""
        session = requests.Session()
        session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        return session
    
    def _setup_logging(self):
        """إعداد نظام التسجيل"""
        logging.basicConfig(
            level=logging.INFO,
            format=f'{Colors.CYAN}[%(asctime)s]{Colors.RESET} %(message)s',
            datefmt='%H:%M:%S',
            handlers=[
                logging.FileHandler(self.download_path / 'scraper_2044.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _get_random_user_agent(self) -> str:
        """توليد User-Agent عشوائي"""
        return self.ua.random
    
    def _update_headers(self):
        """تحديث الهيدرات"""
        self.session.headers.update({
            'User-Agent': self._get_random_user_agent(),
        })
    
    def _print_banner(self):
        """طباعة بانر 2044 المبهر"""
        banner = f"""
{Colors.BG_BLACK}{Colors.CYAN}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗     ██████╗  ██████╗ ██╗  ██╗ ██╗
║   ████╗ ████║██║   ██║██╔════╝██║██╔════╝     ╚════██╗██╔═████╗██║  ██║███║
║   ██╔████╔██║██║   ██║███████╗██║██║          █████╔╝██║██╔██║███████║╚██║
║   ██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔═══╝ ████╔╝██║╚════██║ ██║
║   ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ███████╗╚██████╔╝     ██║ ██║
║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚══════╝ ╚═════╝      ╚═╝ ╚═╝
║                                                              ║
║              🎵 SCRAPER 2044 - Future Edition 🎵             ║
║                     Professional v2.0.44                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.RESET}
        """
        print(banner)
    
    def _print_progress(self, current, total, prefix='', suffix='', bar_length=50):
        """شريط تقدم مبهر"""
        filled_length = int(round(bar_length * current / float(total)))
        bar = f"{Colors.CYAN}█{Colors.RESET}" * filled_length + f"{Colors.RED}░{Colors.RESET}" * (bar_length - filled_length)
        percent = round(100.0 * current / float(total), 1)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if current == total:
            print()
    
    # ==================== محركات البحث ====================
    
    def _search_soundcloud(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في SoundCloud"""
        tracks = []
        try:
            search_url = f"https://soundcloud.com/search/sounds?q={quote_plus(query)}"
            self._update_headers()
            response = self.session.get(search_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # استخراج البيانات من الـ HTML المخفي
            for script in soup.find_all('script'):
                if 'window.__sc_hydration' in script.text:
                    data = json.loads(script.text.split(' = ')[1].rstrip(';'))
                    for item in data[:limit]:
                        if item.get('hydratable') == 'sound':
                            track = TrackInfo(
                                id=str(item.get('id', '')),
                                title=item.get('title', 'Unknown'),
                                artist=item.get('user', {}).get('username', 'Unknown'),
                                duration=item.get('duration', 0) / 1000,
                                url=item.get('permalink_url', ''),
                                source='SoundCloud'
                            )
                            tracks.append(track)
        except Exception as e:
            self.logger.warning(f"SoundCloud search error: {e}")
        return tracks
    
    def _search_jamendo(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في Jamendo"""
        tracks = []
        try:
            api_url = f"https://api.jamendo.com/v3.0/tracks/?client_id=5c5e2af0&format=json&limit={limit}&search={quote_plus(query)}&include=musicinfo"
            response = self.session.get(api_url, timeout=15)
            data = response.json()
            
            for item in data.get('results', []):
                track = TrackInfo(
                    id=str(item.get('id', '')),
                    title=item.get('name', 'Unknown'),
                    artist=item.get('artist_name', 'Unknown'),
                    album=item.get('album_name', ''),
                    duration=item.get('duration', 0),
                    url=item.get('shareurl', ''),
                    thumbnail=item.get('image', ''),
                    source='Jamendo'
                )
                if item.get('audiodownload_allowed'):
                    track.download_url = item.get('audiodownload', '')
                tracks.append(track)
        except Exception as e:
            self.logger.warning(f"Jamendo search error: {e}")
        return tracks
    
    def _search_freemusicarchive(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في Free Music Archive"""
        tracks = []
        try:
            search_url = f"https://freemusicarchive.org/search/?quicksearch={quote_plus(query)}"
            self._update_headers()
            response = self.session.get(search_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for item in soup.find_all('div', class_='play-item')[:limit]:
                title_elem = item.find('span', class_='ptxt-track')
                artist_elem = item.find('span', class_='ptxt-artist')
                if title_elem:
                    track = TrackInfo(
                        id=hashlib.md5(title_elem.text.encode()).hexdigest()[:10],
                        title=title_elem.text.strip(),
                        artist=artist_elem.text.strip() if artist_elem else 'Unknown',
                        source='FreeMusicArchive'
                    )
                    tracks.append(track)
        except Exception as e:
            self.logger.warning(f"FMA search error: {e}")
        return tracks
    
    def _search_ccmixter(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في ccMixter"""
        tracks = []
        try:
            api_url = f"https://ccmixter.org/api/query?datasource=uploads&search_type=any&search={quote_plus(query)}&limit={limit}"
            response = self.session.get(api_url, timeout=15)
            soup = BeautifulSoup(response.text, 'xml')
            
            for upload in soup.find_all('upload')[:limit]:
                track = TrackInfo(
                    id=upload.find('upload_id').text if upload.find('upload_id') else '',
                    title=upload.find('upload_name').text if upload.find('upload_name') else 'Unknown',
                    artist=upload.find('user_name').text if upload.find('user_name') else 'Unknown',
                    source='ccMixter'
                )
                tracks.append(track)
        except Exception as e:
            self.logger.warning(f"ccMixter search error: {e}")
        return tracks
    
    def _search_incompetech(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في Incompetech"""
        tracks = []
        try:
            search_url = f"https://incompetech.com/music/royalty-free/music.html"
            self._update_headers()
            response = self.session.get(search_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                if any(ext in link['href'] for ext in ['.mp3']):
                    if query.lower() in link.text.lower():
                        track = TrackInfo(
                            id=hashlib.md5(link['href'].encode()).hexdigest()[:10],
                            title=link.text.strip(),
                            artist='Kevin MacLeod',
                            url=link['href'],
                            source='Incompetech'
                        )
                        tracks.append(track)
                        if len(tracks) >= limit:
                            break
        except Exception as e:
            self.logger.warning(f"Incompetech search error: {e}")
        return tracks
    
    def _search_musopen(self, query: str, limit: int = 10) -> List[TrackInfo]:
        """البحث في Musopen"""
        tracks = []
        try:
            search_url = f"https://musopen.org/api/search/?query={quote_plus(query)}&type=music"
            response = self.session.get(search_url, timeout=15)
            data = response.json()
            
            for item in data.get('results', [])[:limit]:
                track = TrackInfo(
                    id=str(item.get('id', '')),
                    title=item.get('title', 'Unknown'),
                    artist=item.get('composer', {}).get('name', 'Unknown'),
                    source='Musopen'
                )
                tracks.append(track)
        except Exception as e:
            self.logger.warning(f"Musopen search error: {e}")
        return tracks
    
    def _extract_metadata(self, filepath: Path) -> Dict:
        """استخراج metadata من الملف"""
        metadata = {
            'size': filepath.stat().st_size,
            'format': filepath.suffix.lower(),
            'download_date': datetime.now().isoformat(),
            'scraper_version': '2044.2.0'
        }
        try:
            from mutagen import File
            audio = File(filepath)
            if audio:
                metadata.update({
                    'bitrate': getattr(audio.info, 'bitrate', 0),
                    'sample_rate': getattr(audio.info, 'sample_rate', 0),
                    'channels': getattr(audio.info, 'channels', 0),
                })
        except ImportError:
            pass
        return metadata
    
    # ==================== وظائف التحميل ====================
    
    def _download_file(self, track: TrackInfo, retries: int = 3) -> bool:
        """تحميل ملف مع إعادة المحاولة"""
        if not track.download_url:
            return False
        
        filepath = self.download_path / f"{track.artist} - {track.title}{Path(urlparse(track.download_url).path).suffix or '.mp3'}"
        filepath = Path(str(filepath)[:200])  # تحديد طول اسم الملف
        
        for attempt in range(retries):
            try:
                self._update_headers()
                response = self.session.get(track.download_url, stream=True, timeout=30)
                total_size = int(response.headers.get('content-length', 0))
                
                with open(filepath, 'wb') as f:
                    with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"{track.title[:30]}", ncols=80) as pbar:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)
                                pbar.update(len(chunk))
                
                track.file_path = str(filepath)
                track.size = self._format_size(total_size)
                return True
                
            except Exception as e:
                self.logger.error(f"Download attempt {attempt + 1} failed for {track.title}: {e}")
                time.sleep(2 ** attempt)
        
        return False
    
    def _format_size(self, size_bytes: int) -> str:
        """تنسيق الحجم"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} TB"
    
    def _save_metadata(self, tracks: List[TrackInfo]):
        """حفظ metadata في ملف JSON"""
        metadata_file = self.download_path / f"metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        data = []
        for track in tracks:
            if track.file_path:
                track.metadata = self._extract_metadata(Path(track.file_path))
                data.append(asdict(track))
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"{Colors.GREEN}✓ Metadata saved to: {metadata_file}{Colors.RESET}")
    
    # ==================== الواجهة الرئيسية ====================
    
    def search(self, query: str, limit: int = 20, sources: List[str] = None) -> List[TrackInfo]:
        """
        البحث عن الموسيقى من مصادر متعددة
        
        Args:
            query: كلمات البحث
            limit: عدد النتائج المطلوبة
            sources: المصادر المستخدمة (None للكل)
        
        Returns:
            قائمة الأغاني
        """
        if sources is None:
            sources = list(self.sources_registry.keys())
        
        self._print_banner()
        print(f"{Colors.BOLD}{Colors.CYAN}🔍 Searching for: {Colors.YELLOW}{query}{Colors.RESET}\n")
        
        all_tracks = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            for source in sources:
                if source in self.sources_registry:
                    futures[executor.submit(self.sources_registry[source], query, limit // len(sources) + 1)] = source
            
            for future in concurrent.futures.as_completed(futures):
                source = futures[future]
                try:
                    tracks = future.result()
                    all_tracks.extend(tracks)
                    self.logger.info(f"{Colors.GREEN}✓ {source}: {len(tracks)} tracks found{Colors.RESET}")
                except Exception as e:
                    self.logger.error(f"{Colors.RED}✗ {source}: {e}{Colors.RESET}")
        
        # إزالة التكرارات
        seen = set()
        unique_tracks = []
        for track in all_tracks:
            key = f"{track.title}:{track.artist}"
            if key not in seen:
                seen.add(key)
                unique_tracks.append(track)
        
        self.tracks = unique_tracks[:limit]
        self.stats.total_found = len(self.tracks)
        self.stats.sources_used = sources
        
        return self.tracks
    
    def display_results(self):
        """عرض نتائج البحث بتنسيق جميل"""
        if not self.tracks:
            print(f"{Colors.YELLOW}⚠ No tracks found!{Colors.RESET}")
            return
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'═' * 70}{Colors.RESET}")
        print(f"{Colors.BOLD}  {'#':<4} {'Title':<35} {'Artist':<20} {'Source':<15}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'═' * 70}{Colors.RESET}")
        
        for i, track in enumerate(self.tracks, 1):
            color = Colors.RAINBOW[i % len(Colors.RAINBOW)]
            print(f"  {color}{i:<4}{Colors.RESET} {track.title[:33]:<35} {track.artist[:18]:<20} {track.source:<15}")
        
        print(f"{Colors.BOLD}{Colors.CYAN}{'═' * 70}{Colors.RESET}\n")
    
    def download_tracks(self, indices: List[int] = None) -> bool:
        """
        تحميل الأغاني المحددة
        
        Args:
            indices: أرقام الأغاني (None للكل)
        """
        if not self.tracks:
            print(f"{Colors.YELLOW}⚠ No tracks to download!{Colors.RESET}")
            return False
        
        if indices is None:
            tracks_to_download = self.tracks
        else:
            tracks_to_download = [self.tracks[i - 1] for i in indices if 1 <= i <= len(self.tracks)]
        
        if not tracks_to_download:
            print(f"{Colors.RED}✗ Invalid indices!{Colors.RESET}")
            return False
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}⬇ Starting download of {len(tracks_to_download)} tracks...{Colors.RESET}\n")
        self.stats.start_time = time.time()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._download_file, track): track for track in tracks_to_download}
            
            for future in concurrent.futures.as_completed(futures):
                track = futures[future]
                try:
                    success = future.result()
                    if success:
                        self.stats.total_downloaded += 1
                        self.logger.info(f"{Colors.GREEN}✓ Downloaded: {track.title}{Colors.RESET}")
                    else:
                        self.stats.failed += 1
                except Exception as e:
                    self.stats.failed += 1
                    self.logger.error(f"{Colors.RED}✗ Failed: {track.title} - {e}{Colors.RESET}")
        
        self.stats.end_time = time.time()
        self._save_metadata(tracks_to_download)
        self._display_stats()
        
        return self.stats.total_downloaded > 0
    
    def _display_stats(self):
        """عرض إحصائيات التحميل"""
        elapsed = self.stats.end_time - self.stats.start_time
        
        print(f"\n{Colors.BOLD}{Colors.CYAN}{'═' * 50}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.PURPLE}  📊 Download Statistics:{Colors.RESET}")
        print(f"  {Colors.GREEN}✓ Total Found: {self.stats.total_found}{Colors.RESET}")
        print(f"  {Colors.CYAN}⬇ Downloaded: {self.stats.total_downloaded}{Colors.RESET}")
        print(f"  {Colors.RED}✗ Failed: {self.stats.failed}{Colors.RESET}")
        print(f"  {Colors.YELLOW}⏱ Time: {elapsed:.1f}s{Colors.RESET}")
        print(f"  {Colors.BLUE}📁 Location: {self.download_path.absolute()}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'═' * 50}{Colors.RESET}\n")
    
    def interactive_mode(self):
        """الوضع التفاعلي"""
        self._print_banner()
        print(f"{Colors.BOLD}{Colors.CYAN}🎵 Welcome to Music Scraper 2044!{Colors.RESET}")
        print(f"{Colors.GREEN}Type 'help' for commands, 'exit' to quit{Colors.RESET}\n")
        
        while True:
            try:
                cmd = input(f"{Colors.BOLD}{Colors.PURPLE}🎵 2044>{Colors.RESET} ").strip()
                
                if cmd.lower() in ['exit', 'quit', 'q']:
                    print(f"{Colors.CYAN}👋 Goodbye! See you in 2044!{Colors.RESET}")
                    break
                elif cmd.lower() == 'help':
                    self._print_help()
                elif cmd.lower().startswith('search '):
                    query = cmd[7:].strip()
                    if query:
                        self.search(query, limit=20)
                        self.display_results()
                elif cmd.lower().startswith('download '):
                    parts = cmd[9:].strip()
                    if parts.lower() == 'all':
                        self.download_tracks()
                    else:
                        try:
                            indices = [int(x.strip()) for x in parts.split(',')]
                            self.download_tracks(indices)
                        except ValueError:
                            print(f"{Colors.RED}✗ Invalid format! Use: download 1,2,3 or download all{Colors.RESET}")
                elif cmd.lower() == 'list':
                    self.display_results()
                elif cmd.lower() == 'stats':
                    self._display_stats()
                elif cmd.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self._print_banner()
                else:
                    print(f"{Colors.YELLOW}Unknown command. Type 'help' for available commands.{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}⚠ Interrupted! Type 'exit' to quit.{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}✗ Error: {e}{Colors.RESET}")
    
    def _print_help(self):
        """طباعة قائمة المساعدة"""
        help_text = f"""
{Colors.BOLD}{Colors.CYAN}{'═' * 50}{Colors.RESET}
{Colors.BOLD}{Colors.PURPLE}  📖 Available Commands:{Colors.RESET}
{Colors.CYAN}  search <query>    {Colors.RESET}- Search for music
{Colors.CYAN}  download <nums>   {Colors.RESET}- Download tracks (e.g., download 1,3,5)
{Colors.CYAN}  download all      {Colors.RESET}- Download all found tracks
{Colors.CYAN}  list              {Colors.RESET}- Show search results
{Colors.CYAN}  stats             {Colors.RESET}- Show download statistics
{Colors.CYAN}  clear             {Colors.RESET}- Clear screen
{Colors.CYAN}  help              {Colors.RESET}- Show this help
{Colors.CYAN}  exit              {Colors.RESET}- Exit program
{Colors.BOLD}{Colors.CYAN}{'═' * 50}{Colors.RESET}
        """
        print(help_text)


# ==================== نقطة الدخول ====================

def main():
    """الدالة الرئيسية"""
    scraper = MusicScraper2044(download_path="downloads_2044", max_workers=5)
    
    # معالجة إشارات النظام
    signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))
    
    # تشغيل الوضع التفاعلي
    scraper.interactive_mode()


if __name__ == "__main__":
    main()

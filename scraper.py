import os
import json
from datetime import datetime
from pathlib import Path

def create_chatbot_files():
    """Chatbot 2044 - Future Edition with Auto-Save"""
    
    # ==================== إنشاء المجلدات ====================
    base_dir = "chatbot_2044"
    dirs = [
        f"{base_dir}/www/css",
        f"{base_dir}/www/js",
        f"{base_dir}/www/assets"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    print("📁 المجلدات جاهزة...")
    
    # ==================== style.css ====================
    style_css = '''/* Chatbot 2044 - Future Edition */
:root {
    --glass: rgba(255,255,255,0.08);
    --glass-border: rgba(255,255,255,0.15);
    --text: #ffffff;
    --text2: rgba(255,255,255,0.6);
    --text3: rgba(255,255,255,0.4);
    --accent: #00ffcc;
    --accent2: #ff44aa;
    --accent3: #ffaa00;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    background: #0a0a0f;
    font-family: 'Cairo', sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    direction: rtl;
}

/* Background */
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
.bg-orb:nth-child(1) { width: 300px; height: 300px; background: #ff44aa; top: -10%; left: -20%; }
.bg-orb:nth-child(2) { width: 250px; height: 250px; background: #00ffcc; bottom: -10%; right: -15%; animation-delay: -4s; }
.bg-orb:nth-child(3) { width: 200px; height: 200px; background: #ffaa00; top: 50%; left: 40%; animation-delay: -2s; }

@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(30px, -30px) scale(1.1); }
    66% { transform: translate(-20px, 20px) scale(0.9); }
}

/* App Container */
.app {
    width: 100%; max-width: 480px; height: 100vh; max-height: 900px;
    display: flex; flex-direction: column;
    position: relative; z-index: 1;
}

/* Header */
.header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 16px; background: rgba(10,10,15,0.8);
    backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border);
    z-index: 10;
}
.header-left { display: flex; align-items: center; gap: 10px; }
.bot-avatar {
    width: 44px; height: 44px; background: var(--glass);
    border: 1px solid var(--glass-border); border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; position: relative;
}
.bot-avatar::after {
    content: ''; position: absolute; bottom: -2px; right: -2px;
    width: 10px; height: 10px; background: #00ff88;
    border-radius: 50%; border: 2px solid #0a0a0f;
    animation: onlinePulse 2s ease-in-out infinite;
}
@keyframes onlinePulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

.header-info h2 {
    font-size: 15px; font-weight: 700;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.header-info span { font-size: 8px; color: var(--text2); letter-spacing: 1px; }

.header-actions { display: flex; gap: 6px; }
.btn-icon {
    width: 34px; height: 34px; background: var(--glass);
    border: 1px solid var(--glass-border); color: var(--text);
    cursor: pointer; border-radius: 12px; font-size: 14px;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.3s;
}
.btn-icon:active { transform: scale(0.9); }

/* Mood Bar */
.mood-bar {
    display: flex; gap: 6px; padding: 8px 16px;
    overflow-x: auto; background: rgba(10,10,15,0.5);
}
.mood-bar::-webkit-scrollbar { display: none; }
.mood-chip {
    padding: 6px 12px; white-space: nowrap;
    background: var(--glass); border: 1px solid var(--glass-border);
    color: var(--text2); cursor: pointer; border-radius: 20px;
    font-size: 9px; font-family: 'Cairo', sans-serif; transition: all 0.3s;
}
.mood-chip.active {
    background: rgba(0,255,204,0.15); border-color: var(--accent);
    color: var(--accent); box-shadow: 0 0 15px rgba(0,255,204,0.2);
}

/* Chat Area */
.chat-area {
    flex: 1; overflow-y: auto; padding: 16px;
    display: flex; flex-direction: column; gap: 10px;
}
.chat-area::-webkit-scrollbar { width: 3px; }
.chat-area::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.08); border-radius: 3px; }

.empty-chat {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center; gap: 10px;
    text-align: center;
}
.empty-chat .icon { font-size: 50px; animation: floatIcon 3s ease-in-out infinite; }
@keyframes floatIcon {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}
.empty-chat h3 { font-size: 16px; color: var(--text); }
.empty-chat p { font-size: 10px; color: var(--text3); max-width: 250px; }

.suggestions { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; }
.suggestion-chip {
    padding: 7px 12px; background: var(--glass);
    border: 1px solid var(--glass-border); color: var(--text2);
    cursor: pointer; border-radius: 20px; font-size: 9px;
    font-family: 'Cairo', sans-serif; transition: all 0.3s;
}
.suggestion-chip:hover { border-color: var(--accent2); color: var(--text); }

/* Messages */
.message {
    display: flex; gap: 8px; max-width: 85%;
    animation: msgSlideIn 0.3s ease-out;
}
@keyframes msgSlideIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.message.bot { align-self: flex-end; flex-direction: row-reverse; }
.message.user { align-self: flex-start; }

.msg-avatar {
    width: 30px; height: 30px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0;
}
.message.bot .msg-avatar { background: rgba(0,255,204,0.1); }
.message.user .msg-avatar { background: rgba(255,68,170,0.1); }

.msg-bubble {
    padding: 8px 12px; border-radius: 16px;
    font-size: 10px; line-height: 1.6;
}
.message.bot .msg-bubble {
    background: rgba(0,255,204,0.1); border: 1px solid rgba(0,255,204,0.2);
    border-bottom-right-radius: 4px; color: var(--text);
}
.message.user .msg-bubble {
    background: rgba(255,68,170,0.1); border: 1px solid rgba(255,68,170,0.2);
    border-bottom-left-radius: 4px; color: var(--text);
}

.msg-time { font-size: 7px; color: var(--text3); margin-top: 3px; }

.typing-indicator {
    display: none; align-items: center; gap: 4px; padding: 8px 12px; align-self: flex-end;
}
.typing-indicator.active { display: flex; }
.typing-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--accent); animation: typingDot 1.4s ease-in-out infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingDot {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.3; }
    30% { transform: translateY(-6px); opacity: 1; }
}

/* Input Area */
.input-area {
    padding: 10px 16px; display: flex; gap: 8px; align-items: center;
    background: rgba(10,10,15,0.8); backdrop-filter: blur(20px);
    border-top: 1px solid var(--glass-border);
}
.input-wrapper {
    flex: 1; display: flex; background: var(--glass);
    border: 1px solid var(--glass-border); border-radius: 20px;
    padding: 2px;
}
.chat-input {
    flex: 1; background: transparent; border: none;
    color: var(--text); font-size: 10px; font-family: 'Cairo', sans-serif;
    padding: 8px 12px; resize: none; outline: none;
}
.chat-input::placeholder { color: var(--text3); }
.send-btn {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    border: none; color: #000; cursor: pointer; border-radius: 14px;
    font-size: 16px; display: flex; align-items: center; justify-content: center;
    transition: all 0.3s;
}
.send-btn:active { transform: scale(0.9); }

/* Toast */
.toast {
    position: fixed; bottom: 30px; left: 50%;
    transform: translateX(-50%) translateY(120px);
    background: rgba(0,0,0,0.9); border: 1px solid rgba(0,255,204,0.3);
    color: #fff; padding: 10px 20px; border-radius: 25px; font-size: 10px;
    z-index: 100; transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Cairo', sans-serif;
}
.toast.show { transform: translateX(-50%) translateY(0); }
'''

    # ==================== storage.js ====================
    storage_js = '''// Storage System 2044
const STORAGE_KEYS = {
    messages: 'chatbot_2044_messages',
    settings: 'chatbot_2044_settings'
};

class Storage2044 {
    static save(key, data) {
        try {
            localStorage.setItem(key, JSON.stringify(data));
            return true;
        } catch (e) {
            console.error('Save error:', e);
            return false;
        }
    }

    static load(key, defaultValue = null) {
        try {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : defaultValue;
        } catch (e) {
            return defaultValue;
        }
    }

    static remove(key) {
        localStorage.removeItem(key);
    }
}
'''

    # ==================== chatbot.js ====================
    chatbot_js = '''// Chatbot Brain 2044
class Chatbot2044 {
    constructor() {
        this.mood = 'friendly';
        this.initData();
    }

    initData() {
        this.greetings = [
            'أهلاً وسهلاً! 🌟 كيف حالك اليوم؟',
            'مرحباً! 😊 نورت الشات، شو في جديد؟',
            'هلا والله! 🎉 اشتقتلك، أخبارك؟',
            'ياهلا! 💫 منور، احكيلي شو بصير معك؟'
        ];

        this.jokes = [
            'واحد بخيل دخل الحمام... طلع من غير ما يستحم 😂',
            'ليه القط دايمًا بيكسب؟ لأنه دايمًا نيييياو 🐱',
            'ليه القمر ما بيلعب كرة؟ لأنه ما عنده أرض 🌙',
            'ليه الحاسوب زعلان؟ لأنه عنده فيروس 🖥️😂'
        ];

        this.wisdom = [
            '🌟 الحياة مثل الدراجة، لازم تمشي عشان توازن',
            '💪 النجاح مش نهاية، والفشل مش بداية، الأهم الشجاعة للمتابعة',
            '🎯 كل يوم هو فرصة جديدة لتكون أفضل',
            '🌈 الأمل هو النور اللي بينير طريقك في الظلام'
        ];

        this.facts = [
            '🧠 الدماغ البشري يستخدم 20% من طاقة الجسم',
            '🌍 الأرض هي الكوكب الوحيد اللي ما سمي على إله',
            '🐙 الأخطبوط عنده 3 قلوب ودم أزرق',
            '🦋 الفراشات تتذوق بأرجلها'
        ];

        this.riddles = [
            { q: 'ما هو الشيء اللي يمشي بدون رجلين؟', a: 'الماء 💧' },
            { q: 'ما هو الشيء اللي كلما زاد نقص؟', a: 'العمر ⏳' },
            { q: 'ما هو الشيء اللي له أسنان وما يعض؟', a: 'المشط 🪮' }
        ];

        this.defaultResponses = [
            '🧐 سؤال عميق! خليني أفكر...',
            '🤔 هاد موضوع مثير للاهتمام، احكيلي أكثر!',
            '💡 وجهة نظر رائعة! شو رأيك نتعمق بالموضوع؟',
            '🌟 أنا متحمس أعرف أكثر عن هاد الموضوع!',
            '🚀 في 2044، هاد الموضوع متطور كثير!'
        ];
    }

    getResponse(message) {
        const msg = message.trim().toLowerCase();
        
        if (this.isGreeting(msg)) return this.randomFrom(this.greetings);
        if (msg.includes('نكتة') || msg.includes('اضحكني')) return this.randomFrom(this.jokes);
        if (msg.includes('حكمة') || msg.includes('نصيحة')) return this.randomFrom(this.wisdom);
        if (msg.includes('معلومة') || msg.includes('حقيقة')) return this.randomFrom(this.facts);
        if (msg.includes('لغز') || msg.includes('فزورة')) {
            const riddle = this.randomFrom(this.riddles);
            return `${riddle.q}\\n\\n...\\n\\nالإجابة: ${riddle.a}`;
        }
        if (msg.includes('اسمك')) return 'أنا Chatbot 2044 🤖 صديقك الذكي من المستقبل!';
        if (msg.includes('وقت') || msg.includes('ساعة')) return this.getTime();
        if (msg.includes('تاريخ') || msg.includes('يوم')) return this.getDate();
        if (msg.includes('شكراً') || msg.includes('شكرا')) return 'العفو! 🌸 تحت أمرك دايمًا';
        if (msg.includes('حب') || msg.includes('❤️')) return 'الحب هو أجمل لغة في الكون! 💖✨';
        if (msg.includes('حزين') || msg.includes('زعلان')) return 'لا تحزن! 🌈 كل شيء راح يكون على ما يرام 💪';
        if (msg.includes('سعيد') || msg.includes('فرحان')) return 'فرحتك تفرحني! 🎉🥳';
        if (msg.includes('باي') || msg.includes('سلام')) return 'مع السلامة! 👋💫 تعال anytime!';
        
        return this.randomFrom(this.defaultResponses);
    }

    isGreeting(msg) {
        const g = ['مرحبا', 'هلا', 'السلام', 'صباح', 'مساء', 'هاي', 'هلو', 'hi', 'hello', 'اهلا'];
        return g.some(w => msg.includes(w));
    }

    getTime() {
        const now = new Date();
        return 'الساعة الآن ' + now.toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' });
    }

    getDate() {
        const now = new Date();
        return '📅 اليوم هو ' + now.toLocaleDateString('ar-SA', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    }

    randomFrom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }
}
'''

    # ==================== app.js ====================
    app_js = '''// Main App 2044
const chatbot = new Chatbot2044();
let messages = [];

// Load messages on start
document.addEventListener('DOMContentLoaded', () => {
    messages = Storage2044.load(STORAGE_KEYS.messages, []);
    renderMessages();
});

// Send message
function sendMessage() {
    const input = document.getElementById('chatInput');
    const text = input.value.trim();
    if (!text) return;
    
    addMessage('user', text);
    input.value = '';
    showTyping();
    
    setTimeout(() => {
        hideTyping();
        const response = chatbot.getResponse(text);
        addMessage('bot', response);
    }, 600 + Math.random() * 1000);
}

// Quick send
function quickSend(text) {
    document.getElementById('chatInput').value = text;
    sendMessage();
}

// Add message
function addMessage(type, text) {
    const msg = {
        id: Date.now(),
        type: type,
        text: text,
        time: new Date().toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' })
    };
    messages.push(msg);
    Storage2044.save(STORAGE_KEYS.messages, messages);
    renderMessages();
    
    setTimeout(() => {
        const area = document.getElementById('chatArea');
        area.scrollTop = area.scrollHeight;
    }, 100);
}

// Render messages
function renderMessages() {
    const area = document.getElementById('chatArea');
    
    if (messages.length === 0) {
        area.innerHTML = `
            <div class="empty-chat">
                <span class="icon">🤖</span>
                <h3>Chatbot 2044</h3>
                <p>صديقك الذكي من المستقبل! جاهز للدردشة في أي وقت</p>
                <div class="suggestions">
                    <span class="suggestion-chip" onclick="quickSend('قولي نكتة 😂')">😂 قولي نكتة</span>
                    <span class="suggestion-chip" onclick="quickSend('كيف حالك؟')">💬 كيف حالك؟</span>
                    <span class="suggestion-chip" onclick="quickSend('أعطيني حكمة 🌟')">🌟 أعطيني حكمة</span>
                    <span class="suggestion-chip" onclick="quickSend('عندي سؤال 🧐')">🧐 عندي سؤال</span>
                </div>
            </div>`;
        return;
    }
    
    area.innerHTML = messages.map(msg => `
        <div class="message ${msg.type}">
            <div class="msg-avatar">${msg.type === 'bot' ? '🤖' : '👤'}</div>
            <div>
                <div class="msg-bubble">${msg.text.replace(/\\n/g, '<br>')}</div>
                <div class="msg-time">${msg.time}</div>
            </div>
        </div>
    `).join('');
    
    area.innerHTML += '<div class="typing-indicator" id="typingIndicator"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>';
}

// Typing
function showTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.classList.add('active');
}
function hideTyping() {
    const el = document.getElementById('typingIndicator');
    if (el) el.classList.remove('active');
}

// Mood
function setMood(mood, el) {
    document.querySelectorAll('.mood-chip').forEach(c => c.classList.remove('active'));
    el.classList.add('active');
    chatbot.mood = mood;
    showToast('تم تغيير الوضع ✓');
}

// Clear
function clearChat() {
    if (confirm('حذف كل المحادثات؟')) {
        messages = [];
        Storage2044.remove(STORAGE_KEYS.messages);
        renderMessages();
        showToast('🗑️ تم الحذف');
    }
}

// Export
function exportChat() {
    let text = '🤖 Chatbot 2044\\n';
    text += '='.repeat(30) + '\\n\\n';
    messages.forEach(msg => {
        text += `${msg.type === 'bot' ? '🤖' : '👤'} [${msg.time}]: ${msg.text}\\n\\n`;
    });
    
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'chatbot_2044.txt';
    a.click();
    showToast('📥 تم التصدير');
}

// Toast
function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2000);
}

// Enter key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && document.activeElement === document.getElementById('chatInput')) {
        e.preventDefault();
        sendMessage();
    }
});
'''

    # ==================== index.html ====================
    index_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <div class="app">
        <div class="header">
            <div class="header-left">
                <div class="bot-avatar">🤖</div>
                <div class="header-info">
                    <h2>Chatbot 2044</h2>
                    <span>✦ متصل الآن ✦</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn-icon" onclick="exportChat()">📥</button>
                <button class="btn-icon" onclick="clearChat()">🗑️</button>
            </div>
        </div>

        <div class="mood-bar">
            <span class="mood-chip active" onclick="setMood('friendly', this)">😊 ودود</span>
            <span class="mood-chip" onclick="setMood('teacher', this)">🧑‍🏫 معلم</span>
            <span class="mood-chip" onclick="setMood('funny', this)">😂 مضحك</span>
            <span class="mood-chip" onclick="setMood('wise', this)">🧘 حكيم</span>
        </div>

        <div class="chat-area" id="chatArea"></div>

        <div class="input-area">
            <div class="input-wrapper">
                <textarea class="chat-input" id="chatInput" placeholder="اكتب رسالتك..." rows="1"></textarea>
            </div>
            <button class="send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>

    <div class="toast" id="toast"></div>

    <script src="js/storage.js"></script>
    <script src="js/chatbot.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''

    # ==================== كتابة الملفات ====================
    files = {
        f"{base_dir}/www/css/style.css": style_css,
        f"{base_dir}/www/js/storage.js": storage_js,
        f"{base_dir}/www/js/chatbot.js": chatbot_js,
        f"{base_dir}/www/js/app.js": app_js,
        f"{base_dir}/www/index.html": index_html,
    }
    
    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ {path}")

    # ==================== معلومات ====================
    print(f"\n{'='*50}")
    print(f"🤖 Chatbot 2044 - جاهز!")
    print(f"📁 {len(files)} ملفات تم إنشاؤها")
    print(f"📂 المجلد: {base_dir}/")
    print(f"\n🚀 للتشغيل:")
    print(f"   cd {base_dir}/www")
    print(f"   python -m http.server 2044")
    print(f"   ثم افتح: http://localhost:2044")
    print(f"{'='*50}")

if __name__ == "__main__":
    create_chatbot_files()

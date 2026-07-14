import os
import json
from datetime import datetime
from pathlib import Path

def create_chatbot_files():
    """Chatbot 2044 - Future Edition with Auto-Save"""
    
    # ==================== إنشاء المجلدات ====================
    dirs = [
        "chatbot_2044/www/css",
        "chatbot_2044/www/js",
        "chatbot_2044/www/assets"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # ==================== 1. style.css ====================
    style_css = r'''/* ==================== Chatbot 2044 - Future Edition ==================== */
:root {
    --glass: rgba(255,255,255,0.08);
    --glass-border: rgba(255,255,255,0.15);
    --glass-hover: rgba(255,255,255,0.12);
    --text: #ffffff;
    --text2: rgba(255,255,255,0.6);
    --text3: rgba(255,255,255,0.4);
    --accent: #00ffcc;
    --accent2: #ff44aa;
    --accent3: #ffaa00;
    --shadow: 0 8px 32px rgba(0,0,0,0.2);
    --neumorph: 8px 8px 16px rgba(0,0,0,0.3), -4px -4px 12px rgba(255,255,255,0.05);
    --neumorph-inset: inset 4px 4px 8px rgba(0,0,0,0.4), inset -2px -2px 6px rgba(255,255,255,0.03);
    --bot-bubble: linear-gradient(135deg, rgba(0,255,204,0.15), rgba(0,255,204,0.05));
    --user-bubble: linear-gradient(135deg, rgba(255,68,170,0.2), rgba(255,68,170,0.08));
    --radius-sm: 12px;
    --radius: 20px;
    --radius-lg: 28px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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

/* ==================== BACKGROUND ==================== */
.bg-mesh {
    position: fixed; inset: 0; z-index: 0;
    background: conic-gradient(from 0deg at 50% 50%, 
        #0a0a2e 0%, #1a0a2e 25%, #0a1a2e 50%, #1a0a0a 75%, #0a0a2e 100%);
    animation: meshRotate 25s linear infinite;
}
@keyframes meshRotate { to { filter: hue-rotate(360deg); } }

.bg-orb {
    position: fixed; border-radius: 50%; filter: blur(100px); opacity: 0.3;
    animation: orbFloat 10s ease-in-out infinite;
}
.bg-orb:nth-child(1) { width: 350px; height: 350px; background: #ff44aa; top: -15%; left: -25%; animation-delay: 0s; }
.bg-orb:nth-child(2) { width: 300px; height: 300px; background: #00ffcc; bottom: -15%; right: -20%; animation-delay: -5s; }
.bg-orb:nth-child(3) { width: 250px; height: 250px; background: #ffaa00; top: 40%; left: 50%; animation-delay: -3s; }

@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) scale(1); }
    33% { transform: translate(40px, -40px) scale(1.1); }
    66% { transform: translate(-30px, 30px) scale(0.9); }
}

/* ==================== PARTICLES ==================== */
.particles-layer {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
}
.particle {
    position: absolute;
    background: radial-gradient(circle, var(--accent) 0%, transparent 70%);
    border-radius: 50%;
    animation: particleFloat 8s ease-in infinite;
    opacity: 0;
}
@keyframes particleFloat {
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    15% { opacity: 0.7; }
    85% { opacity: 0.15; }
    100% { transform: translateY(-120px) scale(1.8); opacity: 0; }
}

/* ==================== APP CONTAINER ==================== */
.app {
    width: 100%; max-width: 480px; height: 100vh; max-height: 900px;
    display: flex; flex-direction: column;
    position: relative; z-index: 1;
}

/* ==================== HEADER ==================== */
.header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 16px; background: rgba(10,10,15,0.7);
    backdrop-filter: blur(30px); border-bottom: 1px solid var(--glass-border);
    z-index: 100;
}
.header-left { display: flex; align-items: center; gap: 12px; }
.bot-avatar {
    width: 44px; height: 44px;
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: 16px; display: flex; align-items: center; justify-content: center;
    font-size: 22px; backdrop-filter: blur(20px);
    box-shadow: var(--neumorph);
    animation: avatarGlow 3s ease-in-out infinite;
    position: relative;
}
.bot-avatar::after {
    content: ''; position: absolute; bottom: -2px; right: -2px;
    width: 12px; height: 12px; background: #00ff88;
    border-radius: 50%; border: 2px solid #0a0a0f;
    animation: onlinePulse 2s ease-in-out infinite;
}
@keyframes avatarGlow {
    0%, 100% { box-shadow: var(--neumorph); }
    50% { box-shadow: 0 0 25px rgba(0,255,204,0.4), var(--neumorph); }
}
@keyframes onlinePulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

.header-info h2 {
    font-size: 15px; font-weight: 700;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.header-info span { font-size: 8px; color: var(--text2); letter-spacing: 1px; }

.header-actions { display: flex; gap: 8px; }
.btn-icon {
    width: 36px; height: 36px;
    background: var(--glass); border: 1px solid var(--glass-border);
    color: var(--text); cursor: pointer; border-radius: 12px;
    font-size: 14px; display: flex; align-items: center; justify-content: center;
    backdrop-filter: blur(20px); box-shadow: var(--neumorph);
    transition: var(--transition);
}
.btn-icon:hover { background: var(--glass-hover); border-color: var(--accent); }
.btn-icon:active { transform: scale(0.9); box-shadow: var(--neumorph-inset); }

/* ==================== MOOD SELECTOR ==================== */
.mood-bar {
    display: flex; gap: 6px; padding: 8px 16px;
    overflow-x: auto; scrollbar-width: none;
    background: rgba(10,10,15,0.5); backdrop-filter: blur(20px);
}
.mood-bar::-webkit-scrollbar { display: none; }
.mood-chip {
    padding: 6px 14px; white-space: nowrap;
    background: var(--glass); border: 1px solid var(--glass-border);
    color: var(--text2); cursor: pointer; border-radius: 20px;
    font-size: 10px; font-family: 'Cairo', sans-serif; font-weight: 500;
    backdrop-filter: blur(20px); transition: var(--transition);
}
.mood-chip:hover { border-color: rgba(255,255,255,0.3); color: var(--text); }
.mood-chip.active {
    background: rgba(0,255,204,0.15); border-color: var(--accent);
    color: var(--accent); box-shadow: 0 0 15px rgba(0,255,204,0.2);
}

/* ==================== CHAT AREA ==================== */
.chat-area {
    flex: 1; overflow-y: auto; padding: 16px;
    display: flex; flex-direction: column; gap: 12px;
}
.chat-area::-webkit-scrollbar { width: 3px; }
.chat-area::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.08); border-radius: 3px; }

.empty-chat {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center; gap: 12px;
    text-align: center; padding: 20px;
}
.empty-chat .icon {
    font-size: 60px; animation: floatIcon 3s ease-in-out infinite;
}
@keyframes floatIcon {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}
.empty-chat h3 {
    font-size: 16px; color: var(--text); font-weight: 700;
}
.empty-chat p {
    font-size: 10px; color: var(--text3); max-width: 250px; line-height: 1.6;
}

.suggestions { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; }
.suggestion-chip {
    padding: 8px 14px;
    background: var(--glass); border: 1px solid var(--glass-border);
    color: var(--text2); cursor: pointer; border-radius: 20px;
    font-size: 9px; font-family: 'Cairo', sans-serif;
    backdrop-filter: blur(20px); transition: var(--transition);
}
.suggestion-chip:hover {
    border-color: var(--accent2); color: var(--text);
    box-shadow: 0 0 15px rgba(255,68,170,0.2);
}

/* ==================== MESSAGE BUBBLES ==================== */
.message {
    display: flex; gap: 8px; max-width: 85%;
    animation: msgSlideIn 0.4s ease-out;
}
@keyframes msgSlideIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
.message.bot { align-self: flex-end; flex-direction: row-reverse; }
.message.user { align-self: flex-start; }

.msg-avatar {
    width: 32px; height: 32px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; flex-shrink: 0;
}
.message.bot .msg-avatar {
    background: rgba(0,255,204,0.1); border: 1px solid rgba(0,255,204,0.2);
}
.message.user .msg-avatar {
    background: rgba(255,68,170,0.1); border: 1px solid rgba(255,68,170,0.2);
}

.msg-bubble {
    padding: 10px 14px; border-radius: var(--radius);
    font-size: 11px; line-height: 1.7; position: relative;
    backdrop-filter: blur(20px);
}
.message.bot .msg-bubble {
    background: var(--bot-bubble); border: 1px solid rgba(0,255,204,0.15);
    border-bottom-right-radius: 4px; color: var(--text);
}
.message.user .msg-bubble {
    background: var(--user-bubble); border: 1px solid rgba(255,68,170,0.15);
    border-bottom-left-radius: 4px; color: var(--text);
}

.msg-time {
    font-size: 7px; color: var(--text3); margin-top: 4px;
    text-align: left;
}

.typing-indicator {
    display: none; align-items: center; gap: 4px;
    padding: 12px 16px; align-self: flex-end;
}
.typing-indicator.active { display: flex; }
.typing-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--accent); animation: typingDot 1.4s ease-in-out infinite;
}
.typing-dot:nth-child(1) { animation-delay: 0s; }
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes typingDot {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.3; }
    30% { transform: translateY(-8px); opacity: 1; }
}

/* ==================== INPUT AREA ==================== */
.input-area {
    padding: 12px 16px; display: flex; gap: 8px; align-items: flex-end;
    background: rgba(10,10,15,0.7); backdrop-filter: blur(30px);
    border-top: 1px solid var(--glass-border);
}
.input-wrapper {
    flex: 1; display: flex; align-items: flex-end;
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: var(--radius); backdrop-filter: blur(20px);
    box-shadow: var(--neumorph-inset); padding: 4px;
    transition: var(--transition);
}
.input-wrapper:focus-within {
    border-color: var(--accent); box-shadow: 0 0 20px rgba(0,255,204,0.15);
}
.chat-input {
    flex: 1; background: transparent; border: none;
    color: var(--text); font-size: 11px; font-family: 'Cairo', sans-serif;
    padding: 8px 12px; resize: none; outline: none;
    max-height: 100px; line-height: 1.5;
}
.chat-input::placeholder { color: var(--text3); }
.send-btn {
    width: 40px; height: 40px;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    border: none; color: #000; cursor: pointer; border-radius: 16px;
    font-size: 16px; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 8px 25px rgba(0,255,204,0.3);
    transition: var(--transition); flex-shrink: 0;
}
.send-btn:hover { box-shadow: 0 12px 35px rgba(0,255,204,0.5); transform: translateY(-2px); }
.send-btn:active { transform: scale(0.9); }

/* ==================== SIDEBAR ==================== */
.sidebar {
    position: fixed; top: 0; right: -320px; width: 300px; height: 100vh;
    background: rgba(10,10,15,0.95); backdrop-filter: blur(40px);
    border-left: 1px solid var(--glass-border);
    z-index: 200; transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex; flex-direction: column;
}
.sidebar.open { right: 0; }
.sidebar-overlay {
    position: fixed; inset: 0; background: rgba(0,0,0,0.6);
    z-index: 199; display: none;
}
.sidebar-overlay.show { display: block; }

.sidebar-header {
    padding: 16px; border-bottom: 1px solid var(--glass-border);
    display: flex; align-items: center; justify-content: space-between;
}
.sidebar-header h3 { font-size: 14px; color: var(--text); font-weight: 700; }
.sidebar-list {
    flex: 1; overflow-y: auto; padding: 8px;
}
.sidebar-list::-webkit-scrollbar { width: 3px; }
.sidebar-list::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.08); border-radius: 3px; }

.history-item {
    padding: 10px 12px; border-radius: var(--radius-sm);
    cursor: pointer; transition: var(--transition);
    border: 1px solid transparent; margin-bottom: 4px;
}
.history-item:hover { background: var(--glass-hover); border-color: var(--glass-border); }
.history-item .title { font-size: 10px; color: var(--text); font-weight: 600; }
.history-item .date { font-size: 8px; color: var(--text3); margin-top: 2px; }

/* ==================== TOAST ==================== */
.toast {
    position: fixed; bottom: 30px; left: 50%;
    transform: translateX(-50%) translateY(120px);
    background: rgba(0,0,0,0.9); backdrop-filter: blur(30px);
    border: 1px solid rgba(0,255,204,0.3); color: #fff;
    padding: 12px 24px; border-radius: 30px; font-size: 10px;
    z-index: 400; transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Cairo', sans-serif; box-shadow: 0 10px 30px rgba(0,255,204,0.2);
}
.toast.show { transform: translateX(-50%) translateY(0); }
'''

    # ==================== 2. storage.js ====================
    storage_js = r'''// ==================== Storage System 2044 ====================
const STORAGE_KEYS = {
    messages: 'chatbot_2044_messages',
    settings: 'chatbot_2044_settings',
    history: 'chatbot_2044_history'
};

class Storage2044 {
    static save(key, data) {
        try {
            localStorage.setItem(key, JSON.stringify(data));
            return true;
        } catch (e) {
            if (e.name === 'QuotaExceededError') {
                this.cleanOldData();
                return false;
            }
            console.error('Storage save error:', e);
            return false;
        }
    }

    static load(key, defaultValue = null) {
        try {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : defaultValue;
        } catch (e) {
            console.error('Storage load error:', e);
            return defaultValue;
        }
    }

    static remove(key) {
        localStorage.removeItem(key);
    }

    static cleanOldData() {
        const messages = this.load(STORAGE_KEYS.messages, []);
        if (messages.length > 100) {
            const trimmed = messages.slice(-50);
            this.save(STORAGE_KEYS.messages, trimmed);
        }
    }

    static getStorageInfo() {
        let total = 0;
        for (let key in localStorage) {
            if (localStorage.hasOwnProperty(key)) {
                total += localStorage[key].length * 2;
            }
        }
        return {
            used: (total / 1024).toFixed(1) + ' KB',
            percent: ((total / (5 * 1024 * 1024)) * 100).toFixed(1) + '%'
        };
    }
}
'''

    # ==================== 3. chatbot.js ====================
    chatbot_js = r'''// ==================== Chatbot Brain 2044 ====================
class Chatbot2044 {
    constructor() {
        this.mood = 'friendly';
        this.userName = '';
        this.learnedWords = new Map();
        this.initResponses();
    }

    initResponses() {
        this.greetings = [
            'أهلاً وسهلاً! 🌟 كيف حالك اليوم؟',
            'مرحباً! 😊 نورت الشات، شو في جديد؟',
            'هلا والله! 🎉 اشتقتلك، أخبارك؟',
            'ياهلا! 💫 منور، احكيلي شو بصير معك؟',
            'مراحب! ✨ جاهز للدردشة، شو بدك نحكي؟'
        ];

        this.jokes = [
            'واحد بخيل دخل الحمام... طلع من غير ما يستحم 😂',
            'ليه القط دايمًا بيكسب؟ لأنه دايمًا نيييياو 🐱',
            'ليه القمر ما بيلعب كرة؟ لأنه ما عنده أرض 🌙',
            'ليه الحاسوب زعلان؟ لأنه عنده فيروس كورونا 🖥️😂',
            'واحد غبي قال للشمس: كم الساعة؟ قالتله: مش شايفني قاعدة 😅'
        ];

        this.wisdom = [
            '🌟 الحياة مثل الدراجة، لازم تمشي عشان توازن',
            '💪 النجاح مش نهاية، والفشل مش بداية، الأهم الشجاعة للمتابعة',
            '🎯 كل يوم هو فرصة جديدة لتكون أفضل',
            '🌈 الأمل هو النور اللي بينير طريقك في الظلام',
            '🚀 إذا تقدر تحلم فيه، تقدر تحققه'
        ];

        this.facts = [
            '🧠 الدماغ البشري يستخدم 20% من طاقة الجسم',
            '🌍 الأرض هي الكوكب الوحيد اللي ما سمي على إله',
            '🐙 الأخطبوط عنده 3 قلوب ودم أزرق',
            '🌧️ تمطر على كوكب الزهرة حمض كبريتيك',
            '🦋 الفراشات تتذوق بأرجلها'
        ];

        this.riddles = [
            { q: 'ما هو الشيء اللي يمشي بدون رجلين؟', a: 'الماء 💧' },
            { q: 'ما هو الشيء اللي كلما زاد نقص؟', a: 'العمر ⏳' },
            { q: 'ما هو الشيء اللي له أسنان وما يعض؟', a: 'المشط 🪮' },
            { q: 'ما هو الشيء اللي يسمع بدون أذن ويتكلم بدون لسان؟', a: 'التلفون 📱' },
            { q: 'ما هو الشيء اللي في السماء وإذا ضفت عليه حرف صار في الأرض؟', a: 'نجم - منجم ⭐' }
        ];
    }

    getResponse(message) {
        const msg = message.trim().toLowerCase();
        
        if (this.isGreeting(msg)) return this.randomFrom(this.greetings);
        if (msg.includes('نكتة') || msg.includes('اضحكني')) return this.randomFrom(this.jokes);
        if (msg.includes('حكمة') || msg.includes('نصيحة')) return this.randomFrom(this.wisdom);
        if (msg.includes('معلومة') || msg.includes('حقيقة')) return this.randomFrom(this.facts);
        if (msg.includes('لغز') || msg.includes('فزورة')) {
            const riddle = this.riddles[Math.floor(Math.random() * this.riddles.length)];
            return `${riddle.q}\n\n...\n\nالإجابة: ${riddle.a}`;
        }
        if (msg.includes('اسمك')) return 'أنا Chatbot 2044 🤖 صديقك الذكي من المستقبل!';
        if (msg.includes('وقت') || msg.includes('ساعة')) return this.getTimeResponse();
        if (msg.includes('تاريخ') || msg.includes('يوم')) return this.getDateResponse();
        if (msg.includes('شكراً') || msg.includes('شكرا') || msg.includes('تسلم')) return 'العفو! 🌸 تحت أمرك دايمًا';
        if (msg.includes('حب') || msg.includes('❤️') || msg.includes('💕')) return 'الحب هو أجمل لغة في الكون! 💖✨';
        if (msg.includes('حزين') || msg.includes('زعلان') || msg.includes('😢')) return 'لا تحزن! 🌈 كل شيء راح يكون على ما يرام، أنا معك 💪';
        if (msg.includes('سعيد') || msg.includes('فرحان') || msg.includes('😊')) return 'فرحتك تفرحني! 🎉🥳 استمر في الإيجابية!';
        if (msg.includes('طقس') || msg.includes('جو') || msg.includes('مطر')) return '🌤️ الجو جميل جداً! مثالي للخروج والاستمتاع (في عالم 2044 نتحكم بالطقس 😉)';
        if (msg.includes('أغنية') || msg.includes('موسيقى') || msg.includes('🎵')) return '🎵 الموسيقى غذاء الروح! شو نوع الموسيقى المفضل عندك؟';
        if (msg.includes('باي') || msg.includes('سلام') || msg.includes('مع السلامة')) return 'مع السلامة! 👋💫 تعال anytime، أنا موجود 24/7';
        
        return this.getSmartResponse(msg);
    }

    getSmartResponse(msg) {
        const responses = [
            '🧐 سؤال عميق! خليني أفكر...',
            '🤔 هاد موضوع مثير للاهتمام، احكيلي أكثر!',
            '💡 وجهة نظر رائعة! شو رأيك نتعمق بالموضوع؟',
            '🌟 أنا متحمس أعرف أكثر عن هاد الموضوع!',
            '🎯 نقطة مهمة! شو رأيك نوضحها أكثر؟',
            '🚀 في 2044، هاد الموضوع متطور كثير! بدك تعرف كيف؟',
            '✨ مذهل! عندك أفكار إبداعية كثير'
        ];
        return this.randomFrom(responses);
    }

    isGreeting(msg) {
        const greetings = ['مرحبا', 'هلا', 'السلام', 'صباح', 'مساء', 'هاي', 'هلو', 'hi', 'hello', 'اهلا', 'ياهلا'];
        return greetings.some(g => msg.includes(g));
    }

    getTimeResponse() {
        const now = new Date();
        const time = now.toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' });
        const hour = now.getHours();
        let period = hour < 12 ? '☀️ الصباح' : hour < 17 ? '🌤️ الظهر' : hour < 20 ? '🌅 المساء' : '🌙 الليل';
        return `الساعة الآن ${time} - ${period}`;
    }

    getDateResponse() {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const date = now.toLocaleDateString('ar-SA', options);
        return `📅 اليوم هو ${date}`;
    }

    randomFrom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    setMood(mood) {
        this.mood = mood;
    }
}
'''

    # ==================== 4. app.js ====================
    app_js = r'''// ==================== Chatbot 2044 - Main App ====================
const chatbot = new Chatbot2044();
let messages = [];
let currentHistoryId = null;

document.addEventListener('DOMContentLoaded', () => {
    initApp();
    loadMessages();
    createParticles();
    setupEventListeners();
    updateHistoryList();
});

function initApp() {
    const settings = Storage2044.load(STORAGE_KEYS.settings, {});
    if (settings.userName) {
        chatbot.userName = settings.userName;
    }
}

function setupEventListeners() {
    document.getElementById('chatInput').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    document.getElementById('chatInput').addEventListener('input', autoResize);
}

function autoResize() {
    const textarea = document.getElementById('chatInput');
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 100) + 'px';
}

function sendMessage() {
    const input = document.getElementById('chatInput');
    const text = input.value.trim();
    if (!text) return;
    
    addMessage('user', text);
    input.value = '';
    input.style.height = 'auto';
    showTyping();
    
    setTimeout(() => {
        hideTyping();
        const response = chatbot.getResponse(text);
        addMessage('bot', response);
    }, 800 + Math.random() * 1200);
}

function addMessage(type, text) {
    const msg = {
        id: Date.now() + Math.random(),
        type: type,
        text: text,
        time: new Date().toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' })
    };
    messages.push(msg);
    saveMessages();
    renderMessages();
    scrollToBottom();
}

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
                    <span class="suggestion-chip" onclick="quickSend('عندي سؤال 🧐')">🧐 عندي سؤال</span>
                    <span class="suggestion-chip" onclick="quickSend('كيف حالك؟')">💬 كيف حالك؟</span>
                    <span class="suggestion-chip" onclick="quickSend('أعطيني حكمة 🌟')">🌟 أعطيني حكمة</span>
                </div>
            </div>`;
        return;
    }
    
    area.innerHTML = messages.map(msg => `
        <div class="message ${msg.type}">
            <div class="msg-avatar">${msg.type === 'bot' ? '🤖' : '👤'}</div>
            <div>
                <div class="msg-bubble">${msg.text.replace(/\n/g, '<br>')}</div>
                <div class="msg-time">${msg.time}</div>
            </div>
        </div>
    `).join('');
    
    area.innerHTML += '<div class="typing-indicator" id="typingIndicator"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>';
}

function showTyping() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) indicator.classList.add('active');
    scrollToBottom();
}

function hideTyping() {
    const indicator = document.getElementById('typingIndicator');
    if (indicator) indicator.classList.remove('active');
}

function scrollToBottom() {
    setTimeout(() => {
        const area = document.getElementById('chatArea');
        area.scrollTop = area.scrollHeight;
    }, 100);
}

function quickSend(text) {
    document.getElementById('chatInput').value = text;
    sendMessage();
}

function saveMessages() {
    Storage2044.save(STORAGE_KEYS.messages, messages);
    updateHistoryList();
}

function loadMessages() {
    messages = Storage2044.load(STORAGE_KEYS.messages, []);
    renderMessages();
    if (messages.length > 0) scrollToBottom();
}

function clearChat() {
    if (confirm('هل أنت متأكد من حذف كل المحادثات؟')) {
        messages = [];
        Storage2044.remove(STORAGE_KEYS.messages);
        renderMessages();
        showToast('🗑️ تم حذف كل المحادثات');
    }
}

function exportChat() {
    let text = '🤖 Chatbot 2044 - محادثة\n';
    text += '═'.repeat(40) + '\n\n';
    messages.forEach(msg => {
        text += `${msg.type === 'bot' ? '🤖 البوت' : '👤 أنت'} [${msg.time}]:\n${msg.text}\n\n`;
    });
    
    const blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `chatbot_2044_${new Date().toISOString().slice(0,10)}.txt`;
    a.click();
    showToast('📥 تم تصدير المحادثة');
}

function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
    document.getElementById('sidebarOverlay').classList.toggle('show');
}

function setMood(mood, el) {
    document.querySelectorAll('.mood-chip').forEach(c => c.classList.remove('active'));
    el.classList.add('active');
    chatbot.setMood(mood);
    const moods = {
        friendly: '😊 الوضع الودي - جاهز للدردشة!',
        teacher: '🧑‍🏫 وضع المعلم - جاهز للتعليم!',
        funny: '😂 وضع الكوميديا - جاهز للضحك!',
        wise: '🧘 وضع الحكمة - جاهز للتأمل!'
    };
    showToast(moods[mood] || 'تم تغيير المود');
}

function updateHistoryList() {
    const list = document.getElementById('historyList');
    const savedMessages = Storage2044.load(STORAGE_KEYS.messages, []);
    
    if (savedMessages.length === 0) {
        list.innerHTML = '<div style="text-align:center;color:rgba(255,255,255,0.3);padding:20px;font-size:10px;">لا توجد محادثات سابقة</div>';
        return;
    }
    
    const firstMsg = savedMessages[0]?.text?.substring(0, 30) || 'محادثة';
    const date = new Date().toLocaleDateString('ar-SA');
    
    list.innerHTML = `
        <div class="history-item" onclick="toggleSidebar()">
            <div class="title">💬 ${firstMsg}...</div>
            <div class="date">📅 ${date} - ${savedMessages.length} رسالة</div>
        </div>`;
}

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2500);
}

function createParticles() {
    const container = document.createElement('div');
    container.className = 'particles-layer';
    document.body.appendChild(container);
    
    const colors = ['#00ffcc', '#ff44aa', '#ffaa00'];
    for (let i = 0; i < 25; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.width = (Math.random() * 5 + 2) + 'px';
        particle.style.height = particle.style.width;
        particle.style.animationDelay = Math.random() * 8 + 's';
        particle.style.animationDuration = (Math.random() * 6 + 6) + 's';
        particle.style.background = `radial-gradient(circle, ${colors[Math.floor(Math.random()*3)]} 0%, transparent 70%)`;
        container.appendChild(particle);
    }
}
'''

    # ==================== 5. index.html ====================
    index_html = r'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Chatbot 2044 - Future Edition</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="bot-avatar">🤖</div>
                <div class="header-info">
                    <h2>Chatbot 2044</h2>
                    <span>✦ متصل الآن ✦</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn-icon" onclick="exportChat()" title="تصدير">📥</button>
                <button class="btn-icon" onclick="clearChat()" title="حذف">🗑️</button>
                <button class="btn-icon" onclick="toggleSidebar()" title="السجل">📋</button>
            </div>
        </div>

        <!-- Mood Bar -->
        <div class="mood-bar">
            <span class="mood-chip active" onclick="setMood('friendly', this)">😊 ودود</span>
            <span class="mood-chip" onclick="setMood('teacher', this)">🧑‍🏫 معلم</span>
            <span class="mood-chip" onclick="setMood('funny', this)">😂 مضحك</span>
            <span class="mood-chip" onclick="setMood('wise', this)">🧘 حكيم</span>
        </div>

        <!-- Chat Area -->
        <div class="chat-area" id="chatArea">
            <div class="empty-chat">
                <span class="icon">🤖</span>
                <h3>Chatbot 2044</h3>
                <p>صديقك الذكي من المستقبل! جاهز للدردشة في أي وقت</p>
                <div class="suggestions">
                    <span class="suggestion-chip" onclick="quickSend('قولي نكتة 😂')">😂 قولي نكتة</span>
                    <span class="suggestion-chip" onclick="quickSend('عندي سؤال 🧐')">🧐 عندي سؤال</span>
                    <span class="suggestion-chip" onclick="quickSend('كيف حالك؟')">💬 كيف حالك؟</span>
                    <span class="suggestion-chip" onclick="quickSend('أعطيني حكمة 🌟')">🌟 أعطيني حكمة</span>
                </div>
            </div>
        </div>

        <!-- Input Area -->
        <div class="input-area">
            <div class="input-wrapper">
                <textarea class="chat-input" id="chatInput" placeholder="اكتب رسالتك هنا..." rows="1"></textarea>
            </div>
            <button class="send-btn" onclick="sendMessage()">➤</button>
        </div>
    </div>

    <!-- Sidebar -->
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <h3>📋 سجل المحادثات</h3>
            <button class="btn-icon" onclick="toggleSidebar()">✕</button>
        </div>
        <div class="sidebar-list" id="historyList"></div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script src="js/storage.js"></script>
    <script src="js/chatbot.js"></script>
    <script src="js/app.js"></script>
</body>
</html>
'''

    # ==================== 6. README.md ====================
    readme_md = r'''# 🤖 Chatbot 2044 - Future Edition

<div align="center">

![Chatbot 2044](https://img.shields.io/badge/Chatbot-2044-00ffcc?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0.44-ff44aa?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-ffaa00?style=for-the-badge)

**صديقك الذكي من المستقبل - متطور، سريع، وجميل**

</div>

---

## ✨ الميزات

| الميزة | الوصف |
|--------|-------|
| 🎨 **تصميم 2044** | Glass Morphism + Neumorphism + Holographic |
| 💬 **ذكاء اصطناعي** | ردود ذكية ومتنوعة على أسئلتك |
| 💾 **حفظ تلقائي** | كل المحادثات تنحفظ في localStorage |
| 🎭 **أوضاع متعددة** | ودود، معلم، مضحك، حكيم |
| 📥 **تصدير المحادثة** | تصدير كملف نصي |
| 🌙 **خلفيات متحركة** | Mesh Gradient + Orbs + Particles |
| 📱 **متجاوب** | يعمل على كل الأجهزة |
| ⚡ **سريع** | ردود فورية مع تأثير كتابة |

---

## 🚀 طريقة التشغيل

```bash
# افتح الملف في المتصفح
open chatbot_2044/www/index.html

# أو باستخدام Python
cd chatbot_2044/www
python -m http.server 2044

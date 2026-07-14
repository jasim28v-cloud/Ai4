import os
import json
from datetime import datetime
from pathlib import Path

def create_games_hub():
    """Games Hub 2044 - Snake + Memory Games"""
    
    # ==================== إنشاء المجلدات ====================
    base_dir = "games_hub_2044"
    dirs = [
        f"{base_dir}/www/css",
        f"{base_dir}/www/js",
        f"{base_dir}/www/assets"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    print("📁 المجلدات جاهزة...")
    
    # ==================== style.css ====================
    style_css = '''/* Games Hub 2044 - Future Edition */
:root {
    --glass: rgba(255,255,255,0.08);
    --glass-border: rgba(255,255,255,0.15);
    --text: #ffffff;
    --text2: rgba(255,255,255,0.6);
    --text3: rgba(255,255,255,0.4);
    --accent: #00ffcc;
    --accent2: #ff44aa;
    --accent3: #ffaa00;
    --radius: 16px;
    --radius-sm: 12px;
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

/* Particles */
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

/* App */
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
.logo {
    width: 44px; height: 44px; background: var(--glass);
    border: 1px solid var(--glass-border); border-radius: var(--radius);
    display: flex; align-items: center; justify-content: center;
    font-size: 22px; animation: logoGlow 3s ease-in-out infinite;
}
@keyframes logoGlow {
    0%, 100% { box-shadow: 0 0 0 rgba(0,255,204,0); }
    50% { box-shadow: 0 0 25px rgba(0,255,204,0.4); }
}
.header-info h2 {
    font-size: 15px; font-weight: 700;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.header-info span { font-size: 8px; color: var(--text2); letter-spacing: 1px; }

.score-badge {
    background: rgba(255,68,170,0.2); border: 1px solid rgba(255,68,170,0.3);
    color: #ff44aa; padding: 6px 12px; border-radius: 20px;
    font-size: 8px; font-weight: 600; animation: badgePulse 2s ease-in-out infinite;
}
@keyframes badgePulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.btn-glass {
    width: 38px; height: 38px; background: var(--glass);
    border: 1px solid var(--glass-border); color: var(--text);
    cursor: pointer; border-radius: var(--radius-sm); font-size: 16px;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.3s;
}
.btn-glass:active { transform: scale(0.9); }

/* Game Selector */
.game-tabs {
    display: flex; gap: 6px; padding: 8px 16px;
    background: rgba(10,10,15,0.5);
}
.game-tab {
    flex: 1; padding: 8px; text-align: center;
    background: var(--glass); border: 1px solid var(--glass-border);
    color: var(--text2); cursor: pointer; border-radius: var(--radius);
    font-size: 10px; font-family: 'Cairo', sans-serif; font-weight: 600;
    transition: all 0.3s; display: flex; align-items: center;
    justify-content: center; gap: 6px;
}
.game-tab.active {
    background: rgba(0,255,204,0.15); border-color: var(--accent);
    color: var(--accent); box-shadow: 0 0 20px rgba(0,255,204,0.2);
}

/* Game Area */
.game-area {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; justify-content: center; padding: 16px;
    position: relative;
}

/* ==================== SNAKE GAME ==================== */
.snake-container {
    display: none; flex-direction: column; align-items: center; gap: 12px;
    width: 100%;
}
.snake-container.active { display: flex; }

.snake-canvas-wrapper {
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: var(--radius); padding: 8px; backdrop-filter: blur(20px);
    box-shadow: 0 0 30px rgba(0,255,204,0.15);
}
#snakeCanvas {
    display: block; border-radius: 8px;
    background: rgba(0,0,0,0.6);
}

.snake-info {
    display: flex; justify-content: space-between; width: 100%;
    max-width: 320px; gap: 8px;
}
.snake-stat {
    flex: 1; text-align: center; padding: 8px;
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm); backdrop-filter: blur(20px);
}
.snake-stat .label { font-size: 7px; color: var(--text3); }
.snake-stat .value { font-size: 14px; font-weight: 700; color: var(--accent); }

.snake-controls {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 6px; max-width: 200px;
}
.ctrl-dir {
    padding: 14px; background: var(--glass);
    border: 1px solid var(--glass-border); color: var(--text);
    cursor: pointer; border-radius: var(--radius-sm); font-size: 20px;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.2s;
}
.ctrl-dir:active { transform: scale(0.85); background: rgba(0,255,204,0.2); }
.ctrl-dir.up { grid-column: 2; }
.ctrl-dir.left { grid-column: 1; grid-row: 2; }
.ctrl-dir.right { grid-column: 3; grid-row: 2; }
.ctrl-dir.down { grid-column: 2; grid-row: 3; }

/* ==================== MEMORY GAME ==================== */
.memory-container {
    display: none; flex-direction: column; align-items: center; gap: 12px;
    width: 100%;
}
.memory-container.active { display: flex; }

.memory-grid {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 8px; max-width: 340px; width: 100%;
}
.memory-card {
    aspect-ratio: 1; background: var(--glass);
    border: 1px solid var(--glass-border); border-radius: var(--radius-sm);
    cursor: pointer; display: flex; align-items: center; justify-content: center;
    font-size: 30px; transition: all 0.4s; transform-style: preserve-3d;
    backdrop-filter: blur(20px); position: relative;
}
.memory-card:hover { border-color: rgba(255,255,255,0.3); }
.memory-card.flipped {
    background: rgba(0,255,204,0.15); border-color: var(--accent);
    transform: rotateY(180deg);
}
.memory-card.matched {
    background: rgba(0,255,204,0.25); border-color: var(--accent);
    box-shadow: 0 0 20px rgba(0,255,204,0.3); cursor: default;
    animation: matchPulse 0.5s ease-in-out;
}
@keyframes matchPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

.memory-info {
    display: flex; justify-content: space-between; width: 100%;
    max-width: 340px; gap: 8px;
}
.memory-stat {
    flex: 1; text-align: center; padding: 8px;
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm); backdrop-filter: blur(20px);
}
.memory-stat .label { font-size: 7px; color: var(--text3); }
.memory-stat .value { font-size: 14px; font-weight: 700; color: var(--accent2); }

/* Buttons */
.btn-game {
    padding: 10px 24px;
    background: linear-gradient(135deg, #00ffcc, #ff44aa);
    border: none; color: #000; cursor: pointer; border-radius: 20px;
    font-size: 11px; font-family: 'Cairo', sans-serif; font-weight: 700;
    box-shadow: 0 8px 25px rgba(0,255,204,0.3);
    transition: all 0.3s;
}
.btn-game:active { transform: scale(0.9); }

/* Scoreboard */
.scoreboard-overlay {
    position: fixed; inset: 0; background: rgba(0,0,0,0.8);
    z-index: 100; display: none; align-items: center; justify-content: center;
}
.scoreboard-overlay.show { display: flex; }

.scoreboard {
    background: rgba(10,10,15,0.95); border: 1px solid var(--glass-border);
    border-radius: var(--radius); padding: 20px; width: 90%; max-width: 360px;
    backdrop-filter: blur(30px); text-align: center;
}
.scoreboard h3 {
    font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 12px;
}
.score-list {
    max-height: 200px; overflow-y: auto; margin-bottom: 12px;
}
.score-list::-webkit-scrollbar { width: 3px; }
.score-list::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
.score-item {
    display: flex; justify-content: space-between; padding: 8px 12px;
    background: var(--glass); border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm); margin-bottom: 4px; font-size: 10px;
}
.score-item .rank { color: var(--accent); font-weight: 700; }
.score-item .pts { color: var(--accent2); font-weight: 700; }

/* Toast */
.toast {
    position: fixed; bottom: 30px; left: 50%;
    transform: translateX(-50%) translateY(120px);
    background: rgba(0,0,0,0.9); border: 1px solid rgba(0,255,204,0.3);
    color: #fff; padding: 10px 20px; border-radius: 25px; font-size: 10px;
    z-index: 200; transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-family: 'Cairo', sans-serif;
}
.toast.show { transform: translateX(-50%) translateY(0); }

/* Game Over */
.game-over-overlay {
    position: absolute; inset: 0; background: rgba(0,0,0,0.85);
    display: none; flex-direction: column; align-items: center;
    justify-content: center; gap: 12px; border-radius: var(--radius);
    z-index: 50;
}
.game-over-overlay.show { display: flex; }
.game-over-overlay h2 {
    font-size: 24px; font-weight: 800;
    background: linear-gradient(135deg, #ff44aa, #ffaa00);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.game-over-overlay .final-score {
    font-size: 40px; font-weight: 900; color: var(--accent);
    text-shadow: 0 0 30px rgba(0,255,204,0.5);
}
'''

    # ==================== storage.js ====================
    storage_js = '''// Storage System 2044
const STORAGE_KEYS = {
    snakeScores: 'games_hub_2044_snake_scores',
    memoryScores: 'games_hub_2044_memory_scores'
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

    static addScore(gameKey, score) {
        const scores = this.load(gameKey, []);
        scores.push({
            score: score,
            date: new Date().toLocaleDateString('ar-SA'),
            time: new Date().toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' })
        });
        scores.sort((a, b) => b.score - a.score);
        const top10 = scores.slice(0, 10);
        this.save(gameKey, top10);
        return top10;
    }

    static getTopScores(gameKey) {
        return this.load(gameKey, []);
    }
}
'''

    # ==================== snake.js ====================
    snake_js = '''// Snake Game 2044
class SnakeGame {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.gridSize = 15;
        this.tileSize = this.canvas.width / this.gridSize;
        this.snake = [{x: 7, y: 7}];
        this.direction = {x: 1, y: 0};
        this.food = this.spawnFood();
        this.score = 0;
        this.highScore = Storage2044.getTopScores(STORAGE_KEYS.snakeScores)[0]?.score || 0;
        this.gameLoop = null;
        this.isRunning = false;
        this.speed = 120;
        
        this.updateDisplay();
        this.draw();
        this.setupKeyboard();
    }

    spawnFood() {
        let pos;
        do {
            pos = {
                x: Math.floor(Math.random() * this.gridSize),
                y: Math.floor(Math.random() * this.gridSize)
            };
        } while (this.snake.some(s => s.x === pos.x && s.y === pos.y));
        return pos;
    }

    setupKeyboard() {
        document.addEventListener('keydown', (e) => {
            if (!this.isRunning) return;
            switch(e.key) {
                case 'ArrowUp': if (this.direction.y === 0) this.direction = {x: 0, y: -1}; break;
                case 'ArrowDown': if (this.direction.y === 0) this.direction = {x: 0, y: 1}; break;
                case 'ArrowLeft': if (this.direction.x === 0) this.direction = {x: -1, y: 0}; break;
                case 'ArrowRight': if (this.direction.x === 0) this.direction = {x: 1, y: 0}; break;
            }
        });
    }

    move(dx, dy) {
        if (!this.isRunning) return;
        if (dx === 0 && this.direction.y === 0) this.direction = {x: dx, y: dy};
        if (dy === 0 && this.direction.x === 0) this.direction = {x: dx, y: dy};
    }

    update() {
        const head = {
            x: this.snake[0].x + this.direction.x,
            y: this.snake[0].y + this.direction.y
        };

        // Wall collision
        if (head.x < 0 || head.x >= this.gridSize || head.y < 0 || head.y >= this.gridSize) {
            return this.gameOver();
        }

        // Self collision
        if (this.snake.some(s => s.x === head.x && s.y === head.y)) {
            return this.gameOver();
        }

        this.snake.unshift(head);

        // Food
        if (head.x === this.food.x && head.y === this.food.y) {
            this.score += 10;
            this.food = this.spawnFood();
            if (this.speed > 60) this.speed -= 2;
            clearInterval(this.gameLoop);
            this.gameLoop = setInterval(() => this.update(), this.speed);
        } else {
            this.snake.pop();
        }

        this.updateDisplay();
        this.draw();
    }

    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Grid
        this.ctx.strokeStyle = 'rgba(255,255,255,0.03)';
        for (let i = 0; i < this.gridSize; i++) {
            for (let j = 0; j < this.gridSize; j++) {
                this.ctx.strokeRect(i * this.tileSize, j * this.tileSize, this.tileSize, this.tileSize);
            }
        }

        // Food
        this.ctx.fillStyle = '#ff44aa';
        this.ctx.shadowColor = '#ff44aa';
        this.ctx.shadowBlur = 15;
        this.ctx.beginPath();
        this.ctx.arc(
            this.food.x * this.tileSize + this.tileSize / 2,
            this.food.y * this.tileSize + this.tileSize / 2,
            this.tileSize / 2 - 2, 0, Math.PI * 2
        );
        this.ctx.fill();
        this.ctx.shadowBlur = 0;

        // Snake
        this.snake.forEach((s, i) => {
            this.ctx.fillStyle = i === 0 ? '#00ffcc' : 'rgba(0,255,204,0.6)';
            this.ctx.fillRect(
                s.x * this.tileSize + 1, s.y * this.tileSize + 1,
                this.tileSize - 2, this.tileSize - 2
            );
            if (i === 0) {
                this.ctx.fillStyle = '#000';
                this.ctx.fillRect(s.x * this.tileSize + 4, s.y * this.tileSize + 4, 3, 3);
                this.ctx.fillRect(s.x * this.tileSize + 9, s.y * this.tileSize + 4, 3, 3);
            }
        });
    }

    updateDisplay() {
        document.getElementById('snakeScore').textContent = this.score;
        document.getElementById('snakeBest').textContent = this.highScore;
    }

    start() {
        this.snake = [{x: 7, y: 7}];
        this.direction = {x: 1, y: 0};
        this.food = this.spawnFood();
        this.score = 0;
        this.speed = 120;
        this.isRunning = true;
        this.updateDisplay();
        this.draw();
        document.getElementById('snakeGameOver').classList.remove('show');
        
        if (this.gameLoop) clearInterval(this.gameLoop);
        this.gameLoop = setInterval(() => this.update(), this.speed);
    }

    gameOver() {
        this.isRunning = false;
        clearInterval(this.gameLoop);
        
        if (this.score > this.highScore) {
            this.highScore = this.score;
        }
        
        Storage2044.addScore(STORAGE_KEYS.snakeScores, this.score);
        document.getElementById('snakeFinalScore').textContent = this.score;
        document.getElementById('snakeGameOver').classList.add('show');
        document.getElementById('snakeBest').textContent = this.highScore;
    }

    destroy() {
        clearInterval(this.gameLoop);
        this.isRunning = false;
    }
}
'''

    # ==================== memory.js ====================
    memory_js = '''// Memory Game 2044
class MemoryGame {
    constructor() {
        this.emojis = ['🎮', '🚀', '💎', '🌟', '🎵', '🔥', '🌈', '🦄'];
        this.cards = [];
        this.flippedCards = [];
        this.matchedPairs = 0;
        this.totalPairs = 8;
        this.moves = 0;
        this.isLocked = false;
        
        this.setupGrid();
    }

    setupGrid() {
        const cardPairs = [...this.emojis, ...this.emojis];
        this.cards = cardPairs.sort(() => Math.random() - 0.5);
        this.renderGrid();
    }

    renderGrid() {
        const grid = document.getElementById('memoryGrid');
        grid.innerHTML = '';
        
        this.cards.forEach((emoji, index) => {
            const card = document.createElement('div');
            card.className = 'memory-card';
            card.dataset.index = index;
            card.dataset.emoji = emoji;
            card.textContent = '?';
            card.onclick = () => this.flipCard(card, index);
            grid.appendChild(card);
        });
    }

    flipCard(card, index) {
        if (this.isLocked) return;
        if (card.classList.contains('flipped') || card.classList.contains('matched')) return;
        if (this.flippedCards.length >= 2) return;

        card.classList.add('flipped');
        card.textContent = card.dataset.emoji;
        this.flippedCards.push({ card, index, emoji: card.dataset.emoji });

        if (this.flippedCards.length === 2) {
            this.moves++;
            document.getElementById('memMoves').textContent = this.moves;
            this.checkMatch();
        }
    }

    checkMatch() {
        const [first, second] = this.flippedCards;

        if (first.emoji === second.emoji) {
            first.card.classList.add('matched');
            second.card.classList.add('matched');
            this.matchedPairs++;
            document.getElementById('memPairs').textContent = `${this.matchedPairs}/${this.totalPairs}`;
            this.flippedCards = [];

            if (this.matchedPairs === this.totalPairs) {
                this.win();
            }
        } else {
            this.isLocked = true;
            setTimeout(() => {
                first.card.classList.remove('flipped');
                second.card.classList.remove('flipped');
                first.card.textContent = '?';
                second.card.textContent = '?';
                this.flippedCards = [];
                this.isLocked = false;
            }, 800);
        }
    }

    win() {
        const score = Math.max(1000 - (this.moves * 10), 100);
        Storage2044.addScore(STORAGE_KEYS.memoryScores, score);
        document.getElementById('memFinalScore').textContent = score;
        document.getElementById('memoryGameOver').classList.add('show');
    }

    restart() {
        this.matchedPairs = 0;
        this.moves = 0;
        this.flippedCards = [];
        this.isLocked = false;
        document.getElementById('memMoves').textContent = '0';
        document.getElementById('memPairs').textContent = '0/8';
        document.getElementById('memoryGameOver').classList.remove('show');
        this.setupGrid();
    }

    destroy() {
        document.getElementById('memoryGrid').innerHTML = '';
    }
}
'''

    # ==================== app.js ====================
    app_js = '''// Games Hub 2044 - Main App
let snakeGame = null;
let memoryGame = null;
let currentGame = 'snake';

document.addEventListener('DOMContentLoaded', () => {
    createParticles();
    initGames();
    updateBestScores();
});

function initGames() {
    snakeGame = new SnakeGame('snakeCanvas');
    memoryGame = new MemoryGame();
}

function switchGame(game) {
    currentGame = game;
    
    document.querySelectorAll('.game-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.snake-container, .memory-container').forEach(c => c.classList.remove('active'));
    
    if (game === 'snake') {
        document.querySelector('.game-tab:nth-child(1)').classList.add('active');
        document.getElementById('snakeContainer').classList.add('active');
        snakeGame.start();
        if (memoryGame) memoryGame.destroy();
    } else {
        document.querySelector('.game-tab:nth-child(2)').classList.add('active');
        document.getElementById('memoryContainer').classList.add('active');
        memoryGame.restart();
        if (snakeGame) snakeGame.destroy();
    }
}

function restartGame() {
    if (currentGame === 'snake') {
        snakeGame.start();
    } else {
        memoryGame.restart();
    }
}

function updateBestScores() {
    const snakeScores = Storage2044.getTopScores(STORAGE_KEYS.snakeScores);
    const memoryScores = Storage2044.getTopScores(STORAGE_KEYS.memoryScores);
    
    if (snakeScores.length > 0) {
        document.getElementById('snakeBest').textContent = snakeScores[0].score;
    }
    if (memoryScores.length > 0) {
        // Show best moves (lower is better for memory, but we store computed score)
    }
}

function showScoreboard() {
    const overlay = document.getElementById('scoreboardOverlay');
    const list = document.getElementById('scoreList');
    
    const scores = currentGame === 'snake' 
        ? Storage2044.getTopScores(STORAGE_KEYS.snakeScores)
        : Storage2044.getTopScores(STORAGE_KEYS.memoryScores);
    
    if (scores.length === 0) {
        list.innerHTML = '<div style="color:rgba(255,255,255,0.3);padding:20px;">لا توجد نتائج بعد</div>';
    } else {
        list.innerHTML = scores.map((s, i) => `
            <div class="score-item">
                <span class="rank">#${i + 1}</span>
                <span class="pts">${s.score} نقطة</span>
                <span style="color:rgba(255,255,255,0.4);font-size:8px;">${s.date}</span>
            </div>
        `).join('');
    }
    
    overlay.classList.add('show');
}

function hideScoreboard() {
    document.getElementById('scoreboardOverlay').classList.remove('show');
}

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 2000);
}

function createParticles() {
    const container = document.getElementById('particles');
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

    # ==================== index.html ====================
    index_html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Games Hub 2044</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="bg-mesh"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>
    <div class="particles-layer" id="particles"></div>

    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="header-left">
                <div class="logo">🎮</div>
                <div class="header-info">
                    <h2>Games Hub 2044</h2>
                    <span>✦ Future Edition ✦</span>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn-glass" onclick="showScoreboard()">🏆</button>
                <button class="btn-glass" onclick="restartGame()">🔄</button>
            </div>
        </div>

        <!-- Game Tabs -->
        <div class="game-tabs">
            <button class="game-tab active" onclick="switchGame('snake')">🐍 ثعبان</button>
            <button class="game-tab" onclick="switchGame('memory')">🧠 ذاكرة</button>
        </div>

        <!-- Snake Game -->
        <div class="game-area snake-container active" id="snakeContainer">
            <div class="snake-canvas-wrapper">
                <canvas id="snakeCanvas" width="300" height="300"></canvas>
            </div>
            <div class="snake-info">
                <div class="snake-stat">
                    <div class="label">النقاط</div>
                    <div class="value" id="snakeScore">0</div>
                </div>
                <div class="snake-stat">
                    <div class="label">أعلى نتيجة</div>
                    <div class="value" id="snakeBest">0</div>
                </div>
            </div>
            <div class="snake-controls">
                <button class="ctrl-dir up" onclick="snakeGame.move(0, -1)">▲</button>
                <button class="ctrl-dir left" onclick="snakeGame.move(-1, 0)">◀</button>
                <button class="ctrl-dir right" onclick="snakeGame.move(1, 0)">▶</button>
                <button class="ctrl-dir down" onclick="snakeGame.move(0, 1)">▼</button>
            </div>
            <div class="game-over-overlay" id="snakeGameOver">
                <h2>انتهت اللعبة!</h2>
                <div class="final-score" id="snakeFinalScore">0</div>
                <button class="btn-game" onclick="snakeGame.start()">▶️ العب مرة أخرى</button>
            </div>
        </div>

        <!-- Memory Game -->
        <div class="game-area memory-container" id="memoryContainer">
            <div class="memory-grid" id="memoryGrid"></div>
            <div class="memory-info">
                <div class="memory-stat">
                    <div class="label">المحاولات</div>
                    <div class="value" id="memMoves">0</div>
                </div>
                <div class="memory-stat">
                    <div class="label">الأزواج</div>
                    <div class="value" id="memPairs">0/8</div>
                </div>
            </div>
            <div class="game-over-overlay" id="memoryGameOver">
                <h2>🎉 أحسنت!</h2>
                <div class="final-score" id="memFinalScore">0</div>
                <p style="color:rgba(255,255,255,0.6);font-size:10px;">نقطة</p>
                <button class="btn-game" onclick="memoryGame.restart()">▶️ العب مرة أخرى</button>
            </div>
        </div>
    </div>

    <!-- Scoreboard -->
    <div class="scoreboard-overlay" id="scoreboardOverlay" onclick="hideScoreboard()">
        <div class="scoreboard" onclick="event.stopPropagation()">
            <h3>🏆 لوحة الصدارة</h3>
            <div class="score-list" id="scoreList"></div>
            <button class="btn-game" onclick="hideScoreboard()">إغلاق</button>
        </div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast"></div>

    <script src="js/storage.js"></script>
    <script src="js/snake.js"></script>
    <script src="js/memory.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''

    # ==================== كتابة الملفات ====================
    files = {
        f"{base_dir}/www/css/style.css": style_css,
        f"{base_dir}/www/js/storage.js": storage_js,
        f"{base_dir}/www/js/snake.js": snake_js,
        f"{base_dir}/www/js/memory.js": memory_js,
        f"{base_dir}/www/js/app.js": app_js,
        f"{base_dir}/www/index.html": index_html,
    }
    
    total_size = 0
    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        size = len(content.encode('utf-8'))
        total_size += size
        print(f"  ✓ {path} ({size/1024:.1f} KB)")

    print(f"\n{'='*55}")
    print(f"🎮 Games Hub 2044 - جاهز!")
    print(f"📁 {len(files)} ملفات | 📦 {total_size/1024:.1f} KB")
    print(f"🐍 لعبة الثعبان + 🧠 لعبة الذاكرة")
    print(f"💾 حفظ تلقائي لأعلى 10 نتائج")
    print(f"🚀 تصميم 2044: Glass Morphism + Particles + Neumorphism")
    print(f"\n📂 للتشغيل:")
    print(f"   cd {base_dir}/www")
    print(f"   python -m http.server 2044")
    print(f"   ثم افتح: http://localhost:2044")
    print(f"{'='*55}")

if __name__ == "__main__":
    create_games_hub()

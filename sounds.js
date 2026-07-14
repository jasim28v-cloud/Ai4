let audioCtx = null;
function initAudio() { try { audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch(e) {} }
function playBeep(freq = 440, dur = 0.1, vol = 0.1) { if (!audioCtx) return; try { const o = audioCtx.createOscillator(); const g = audioCtx.createGain(); o.connect(g); g.connect(audioCtx.destination); o.frequency.value = freq; o.type = 'sine'; g.gain.value = vol; o.start(); o.stop(audioCtx.currentTime + dur); } catch(e) {} }
function playEat() { playBeep(660, 0.08, 0.08); setTimeout(() => playBeep(880, 0.08, 0.08), 80); }
function playGolden() { playBeep(880, 0.1, 0.1); setTimeout(() => playBeep(1100, 0.1, 0.1), 100); setTimeout(() => playBeep(1320, 0.15, 0.1), 200); }
function playDie() { playBeep(220, 0.2, 0.1); setTimeout(() => playBeep(165, 0.2, 0.1), 200); setTimeout(() => playBeep(110, 0.3, 0.1), 400); }
function playAchievement() { playBeep(523, 0.1, 0.1); setTimeout(() => playBeep(659, 0.1, 0.1), 100); setTimeout(() => playBeep(784, 0.1, 0.1), 200); setTimeout(() => playBeep(1047, 0.2, 0.1), 300); }
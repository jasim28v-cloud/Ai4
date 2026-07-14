let audioCtx=null,soundEnabled=true;
function initAudio(){try{audioCtx=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}}
function toggleSound(){soundEnabled=!soundEnabled;saveSettings({theme:currentTheme,ghost:isGhost,sound:soundEnabled});document.getElementById('soundBtn').classList.toggle('active',!soundEnabled);showToast(soundEnabled?'🔊 الصوت مفعل':'🔇 الصوت مكتوم')}
function playBeep(freq=440,dur=0.1,vol=0.08){if(!audioCtx||!soundEnabled)return;try{const o=audioCtx.createOscillator();const g=audioCtx.createGain();o.connect(g);g.connect(audioCtx.destination);o.frequency.value=freq;o.type='sine';g.gain.setValueAtTime(vol,audioCtx.currentTime);g.gain.exponentialRampToValueAtTime(0.001,audioCtx.currentTime+dur);o.start();o.stop(audioCtx.currentTime+dur)}catch(e){}}
function playEat(){playBeep(660,0.07,0.06);setTimeout(()=>playBeep(880,0.07,0.06),70)}
function playGolden(){playBeep(880,0.08,0.08);setTimeout(()=>playBeep(1100,0.08,0.08),80);setTimeout(()=>playBeep(1320,0.12,0.08),160)}
function playDie(){playBeep(220,0.15,0.08);setTimeout(()=>playBeep(165,0.15,0.08),150);setTimeout(()=>playBeep(110,0.25,0.08),300)}
function playAchievement(){playBeep(523,0.08,0.08);setTimeout(()=>playBeep(659,0.08,0.08),80);setTimeout(()=>playBeep(784,0.08,0.08),160);setTimeout(()=>playBeep(1047,0.15,0.08),240)}
function playLevelUp(){playBeep(523,0.1,0.06);setTimeout(()=>playBeep(659,0.1,0.06),100);setTimeout(()=>playBeep(784,0.1,0.06),200);setTimeout(()=>playBeep(1047,0.1,0.06),300);setTimeout(()=>playBeep(1318,0.15,0.06),400)}
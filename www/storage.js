const KEYS={scores:'snake2044_scores',achievements:'snake2044_achievements',settings:'snake2044_settings'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function saveScore(score,level){const scores=loadData(KEYS.scores,[]);scores.push({score,level,date:new Date().toLocaleDateString('ar-SA')});scores.sort((a,b)=>b.score-a.score);return saveData(KEYS.scores,scores.slice(0,10))}
function getBestScore(){const scores=loadData(KEYS.scores,[]);return scores.length?scores[0].score:0}
function getTopScores(){return loadData(KEYS.scores,[])}
function getAchievements(){return loadData(KEYS.achievements,[])}
function unlockAchievement(id){const achs=loadData(KEYS.achievements,[]);if(!achs.includes(id)){achs.push(id);saveData(KEYS.achievements,achs);return true}return false}
function saveSettings(settings){return saveData(KEYS.settings,settings)}
function loadSettings(){return loadData(KEYS.settings,{theme:'neon',ghost:false})}
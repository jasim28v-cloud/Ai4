const KEYS={favorites:'fmradio2044_favs',lastFreq:'fmradio2044_last',volume:'fmradio2044_vol'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function getFavorites(){return loadData(KEYS.favorites,[])}
function addFavorite(name,freq){let f=getFavorites();if(!f.find(s=>s.freq===freq)){f.push({name:name||('FM '+freq),freq:freq,date:new Date().toLocaleDateString('ar-SA')});saveData(KEYS.favorites,f)}return f}
function removeFavorite(freq){let f=getFavorites();f=f.filter(s=>s.freq!==freq);saveData(KEYS.favorites,f);return f}
function isFavoriteFreq(freq){return getFavorites().some(s=>s.freq===freq)}
function saveLastFreq(freq){saveData(KEYS.lastFreq,freq)}
function getLastFreq(){return loadData(KEYS.lastFreq,87.5)}
function saveVolume(v){saveData(KEYS.volume,v)}
function getVolume(){return loadData(KEYS.volume,70)}
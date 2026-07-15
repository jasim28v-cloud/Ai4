const KEYS={channels:'tv2044_channels',favorites:'tv2044_favs',lastChannel:'tv2044_last',volume:'tv2044_vol'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function getChannels(){return loadData(KEYS.channels,[])}
function saveChannels(chs){saveData(KEYS.channels,chs)}
function getFavorites(){return loadData(KEYS.favorites,[])}
function toggleFavChannel(num){let f=getFavorites();const i=f.indexOf(num);i>-1?f.splice(i,1):f.push(num);saveData(KEYS.favorites,f);return f}
function isFavChannel(num){return getFavorites().includes(num)}
function saveLastChannel(num){saveData(KEYS.lastChannel,num)}
function getLastChannel(){return loadData(KEYS.lastChannel,1)}
function saveVolume(v){saveData(KEYS.volume,v)}
function getVolume(){return loadData(KEYS.volume,70)}
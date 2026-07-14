const KEYS={favorites:'radio2044_favorites',lastStation:'radio2044_last',settings:'radio2044_settings',volume:'radio2044_volume'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function getFavorites(){return loadData(KEYS.favorites,[])}
function toggleFav(stationName){let favs=getFavorites();const idx=favs.indexOf(stationName);if(idx>-1){favs.splice(idx,1)}else{favs.push(stationName)}saveData(KEYS.favorites,favs);return favs}
function isFavorite(stationName){return getFavorites().includes(stationName)}
function saveLastStation(index){saveData(KEYS.lastStation,index)}
function getLastStation(){return loadData(KEYS.lastStation,0)}
function saveVolume(vol){saveData(KEYS.volume,vol)}
function getVolume(){return loadData(KEYS.volume,70)}
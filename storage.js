const KEYS={favorites:'weather2044_favs',lastCity:'weather2044_last'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getFavorites(){return loadData(KEYS.favorites,[])}
function addFavorite(city){let f=getFavorites();if(!f.includes(city)){f.push(city);saveData(KEYS.favorites,f)}return f}
function removeFavorite(city){let f=getFavorites().filter(c=>c!==city);saveData(KEYS.favorites,f);return f}
function saveLastCity(city){saveData(KEYS.lastCity,city)}
function getLastCity(){return loadData(KEYS.lastCity,'Riyadh')}
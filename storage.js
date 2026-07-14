const KEYS={saved:'pixelart2044_saved',settings:'pixelart2044_settings'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function savePixelArt(data){const saved=loadData(KEYS.saved,[]);saved.unshift({...data,date:new Date().toISOString()});return saveData(KEYS.saved,saved.slice(0,20))}
function getSavedArt(){return loadData(KEYS.saved,[])}
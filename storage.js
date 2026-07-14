const KEYS={patterns:'stitch2044_patterns',settings:'stitch2044_settings'};
function saveData(key,data){try{localStorage.setItem(key,JSON.stringify(data));return true}catch(e){return false}}
function loadData(key,def=null){try{const d=localStorage.getItem(key);return d?JSON.parse(d):def}catch(e){return def}}
function savePattern(pattern){const patterns=loadData(KEYS.patterns,[]);patterns.unshift({...pattern,date:new Date().toISOString()});return saveData(KEYS.patterns,patterns.slice(0,20))}
function getPatterns(){return loadData(KEYS.patterns,[])}
const KEYS={playlist:'sonic2044_playlist',settings:'sonic2044_settings',lyrics:'sonic2044_lyrics',eq:'sonic2044_eq'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function savePlaylist(pl){const data=pl.map(t=>({id:t.id,name:t.name,size:t.size,data:t.data,addedAt:t.addedAt}));return saveData(KEYS.playlist,data)}
function loadPlaylist(){return loadData(KEYS.playlist,[])}
function saveEQ(eq){saveData(KEYS.eq,eq)}
function loadEQ(){return loadData(KEYS.eq,{bands:[0,0,0,0,0,0,0,0,0,0],bass:30,spatial:50})}
function saveLyrics(trackId,lyrics){const all=loadData(KEYS.lyrics,{});all[trackId]=lyrics;saveData(KEYS.lyrics,all)}
function getLyrics(trackId){const all=loadData(KEYS.lyrics,{});return all[trackId]||null}
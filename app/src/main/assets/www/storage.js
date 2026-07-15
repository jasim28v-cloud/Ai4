const K={ch:'tv2044_ch',fav:'tv2044_fav',last:'tv2044_last'};
function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function load(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getChannels(){return load(K.ch,[])}
function saveChannels(ch){save(K.ch,ch)}
function getFavorites(){return load(K.fav,[])}
function toggleFav(n){let f=getFavorites();const i=f.indexOf(n);i>-1?f.splice(i,1):f.push(n);save(K.fav,f);return f}
function isFav(n){return getFavorites().includes(n)}
function saveLast(n){save(K.last,n)}
function getLast(){return load(K.last,0)}
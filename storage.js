const KEYS={gallery:'aiart2044_gallery',settings:'aiart2044_settings'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getGallery(){return loadData(KEYS.gallery,[])}
function addToGallery(imgData,prompt,style){const g=getGallery();g.unshift({id:Date.now(),data:imgData,prompt,style,date:new Date().toLocaleDateString('ar-SA')});if(g.length>50)g.pop();saveData(KEYS.gallery,g);return g}
function removeFromGallery(id){let g=getGallery();g=g.filter(i=>i.id!==id);saveData(KEYS.gallery,g)}
function clearGallery(){saveData(KEYS.gallery,[])}
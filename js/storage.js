const KEYS={cart:'rest2044_cart',orders:'rest2044_orders',favorites:'rest2044_favs',ratings:'rest2044_ratings'};
function saveData(k,v){try{localStorage.setItem(k,JSON.stringify(v));return 1}catch(e){return 0}}
function loadData(k,d=null){try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}}
function getCart(){return loadData(KEYS.cart,[])}
function saveCart(cart){saveData(KEYS.cart,cart)}
function getOrders(){return loadData(KEYS.orders,[])}
function saveOrders(orders){saveData(KEYS.orders,orders)}
function getFavorites(){return loadData(KEYS.favorites,[])}
function toggleFavorite(id){let f=getFavorites();const i=f.indexOf(id);i>-1?f.splice(i,1):f.push(id);saveData(KEYS.favorites,f);return f}
function isFavorite(id){return getFavorites().includes(id)}
function getRatings(){return loadData(KEYS.ratings,{})}
function saveRating(itemId,rating,review){const r=getRatings();if(!r[itemId])r[itemId]=[];r[itemId].push({rating,review,date:new Date().toISOString()});saveData(KEYS.ratings,r)}
function getItemRating(itemId){const r=getRatings();if(!r[itemId]||!r[itemId].length)return 0;return r[itemId].reduce((s,i)=>s+i.rating,0)/r[itemId].length}
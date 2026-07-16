let currentRating=0,currentOrderId=null;
function openRating(orderId){currentOrderId=orderId;currentRating=0;document.getElementById('ratingModal').classList.add('show');document.getElementById('reviewText').value='';updateStars()}
function closeRating(){document.getElementById('ratingModal').classList.remove('show')}
function setRating(r){currentRating=r;updateStars()}
function updateStars(){document.querySelectorAll('.star').forEach((s,i)=>{s.textContent=i<currentRating?'★':'☆';s.classList.toggle('active',i<currentRating)})}
function submitRating(){if(!currentRating||!currentOrderId)return;const orders=getOrders();const order=orders.find(o=>o.id===currentOrderId);if(order){order.items.forEach(i=>{saveRating(i.id,currentRating,document.getElementById('reviewText').value)})}closeRating();renderMenu();renderOrders();showToast('⭐ شكراً لتقييمك!')}
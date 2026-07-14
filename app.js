function showLoading(){document.getElementById('loadingOverlay').classList.add('show')}
function hideLoading(){document.getElementById('loadingOverlay').classList.remove('show')}
function showToast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2200)}
initParticles();
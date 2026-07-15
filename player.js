function startVisualizer(){setInterval(()=>{if(!isRadioOn)return;document.querySelectorAll('.g-bar').forEach(b=>{b.style.height=(Math.random()*28+4)+'px'})},180)}
function showToast(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2500)}
setInterval(()=>{if(isRadioOn)updateSignalBars()},2000);
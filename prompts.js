let selectedStyle='realistic',selectedSize='512';
function selectStyle(s,el){document.querySelectorAll('#tabContentGenerate .style-chip').forEach(b=>b.classList.remove('active'));el.classList.add('active');selectedStyle=s}
function selectSize(s,el){document.querySelectorAll('#tabContentGenerate .size-options .style-chip').forEach(b=>b.classList.remove('active'));el.classList.add('active');selectedSize=s}
function usePrompt(p){document.getElementById('promptInput').value=p}
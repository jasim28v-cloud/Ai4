function showLeaderboardList() {
    const scores = getTopScores();
    const list = document.getElementById('panelBody');
    if (!scores.length) { list.innerHTML = '<div style="text-align:center;opacity:0.4;padding:20px">لا توجد نتائج بعد</div>'; return; }
    list.innerHTML = scores.map((s, i) => `
        <div class="score-item">
            <div class="score-rank">#${i + 1}</div>
            <div>المستوى ${s.level || 1}</div>
            <div class="score-pts">${s.score} نقطة</div>
            <div style="font-size:8px;opacity:0.4">${s.date}</div>
        </div>
    `).join('');
}
function showLeaderboard() { document.getElementById('panelTitle').innerText = '🏆 لوحة الصدارة'; showLeaderboardList(); document.getElementById('panelOverlay').classList.add('show'); }
function showAchievements() { document.getElementById('panelTitle').innerText = '🎯 الإنجازات'; showAchievementsList(); document.getElementById('panelOverlay').classList.add('show'); }
function hidePanel() { document.getElementById('panelOverlay').classList.remove('show'); }
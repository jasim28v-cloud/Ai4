const ACHIEVEMENTS = [
    { id: 'first_game', name: 'البداية', desc: 'أول لعبة تلعبها', icon: '🎮' },
    { id: 'score_50', name: 'مبتدئ', desc: 'وصل 50 نقطة', icon: '⭐' },
    { id: 'score_100', name: 'محترف', desc: 'وصل 100 نقطة', icon: '🌟' },
    { id: 'score_200', name: 'خبير', desc: 'وصل 200 نقطة', icon: '💫' },
    { id: 'score_500', name: 'أسطورة', desc: 'وصل 500 نقطة', icon: '👑' },
    { id: 'score_1000', name: 'إله الثعبان', desc: 'وصل 1000 نقطة', icon: '🔱' },
    { id: 'golden_5', name: 'صائد الذهب', desc: 'اجمع 5 فواكه ذهبية', icon: '🏅' },
    { id: 'golden_20', name: 'كنز الذهب', desc: 'اجمع 20 فاكهة ذهبية', icon: '💎' },
    { id: 'level_5', name: 'صاعد', desc: 'وصل للمستوى 5', icon: '📈' },
    { id: 'level_10', name: 'القمة', desc: 'وصل للمستوى 10', icon: '🏔️' },
    { id: 'ghost_win', name: 'شبح', desc: 'اربح جولة بوضع الشبح', icon: '👻' },
    { id: 'no_poison', name: 'نظيف', desc: 'اجمع 50 فاكهة بدون سم', icon: '🍀' },
    { id: 'speed_demon', name: 'سريع', desc: 'اجمع 10 فواكه سرعة', icon: '⚡' },
    { id: 'combo_10', name: 'كومبو', desc: 'وصل لكومبو x10', icon: '🔥' },
    { id: 'all_themes', name: 'فنان', desc: 'جرب كل الثيمات', icon: '🎨' }
];
function showAchievementsList() {
    const list = document.getElementById('panelBody');
    const unlocked = getAchievements();
    list.innerHTML = ACHIEVEMENTS.map(a => {
        const isUnlocked = unlocked.includes(a.id);
        return `<div class="ach-item ${isUnlocked ? '' : 'ach-locked'}"><div class="ach-icon">${a.icon}</div><div class="ach-info"><div class="ach-name">${a.name}</div><div class="ach-desc">${a.desc}</div></div>${isUnlocked ? '✅' : '🔒'}</div>`;
    }).join('');
}
function checkScoreAchievements(score, golden, level, combo, poisonFree, speedCount) {
    if (score >= 50) unlockAchievement('score_50');
    if (score >= 100) unlockAchievement('score_100');
    if (score >= 200) unlockAchievement('score_200');
    if (score >= 500) unlockAchievement('score_500');
    if (score >= 1000) unlockAchievement('score_1000');
    if (golden >= 5) unlockAchievement('golden_5');
    if (golden >= 20) unlockAchievement('golden_20');
    if (level >= 5) unlockAchievement('level_5');
    if (level >= 10) unlockAchievement('level_10');
    if (combo >= 10) unlockAchievement('combo_10');
    if (poisonFree >= 50) unlockAchievement('no_poison');
    if (speedCount >= 10) unlockAchievement('speed_demon');
}
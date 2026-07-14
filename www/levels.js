const LEVELS=[
    {name:'مبتدئ',speed:130,obstacles:0,required:50,desc:'المرحلة الأولى - تعلم الأساسيات'},
    {name:'سهل',speed:115,obstacles:0,required:100,desc:'زيادة السرعة قليلاً'},
    {name:'متوسط',speed:100,obstacles:1,required:150,desc:'ظهور أول عائق'},
    {name:'متقدم',speed:90,obstacles:2,required:200,desc:'عائقين في الملعب'},
    {name:'صعب',speed:80,obstacles:3,required:250,desc:'ثلاثة عوائق'},
    {name:'محترف',speed:70,obstacles:4,required:300,desc:'أربعة عوائق'},
    {name:'خبير',speed:60,obstacles:5,required:350,desc:'خمسة عوائق'},
    {name:'أسطورة',speed:50,obstacles:6,required:400,desc:'ستة عوائق - السرعة القصوى'},
    {name:'مجنون',speed:42,obstacles:8,required:500,desc:'الجنون الحقيقي'},
    {name:'مستحيل',speed:35,obstacles:10,required:999,desc:'هل تقبل التحدي؟'}
];
let currentLevel=0,obstacles=[];
function getLevel(){return LEVELS[currentLevel]||LEVELS[0]}
function getSpeed(){return getLevel().speed}
function getRequired(){return getLevel().required}
function spawnObstacles(gridSize){obstacles=[];const count=getLevel().obstacles;for(let i=0;i<count;i++){let pos;do{pos={x:Math.floor(Math.random()*gridSize),y:Math.floor(Math.random()*gridSize)}}while(pos.x===Math.floor(gridSize/2)&&pos.y===Math.floor(gridSize/2));obstacles.push(pos)}return obstacles}
function checkObstacle(x,y){return obstacles.some(o=>o.x===x&&o.y===y)}
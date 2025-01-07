var stoped = false;
var exploded = false;
var timerDisplay = document.getElementById('timer');
var timeLeft = 5
function formatTime(unit){
    if (unit <10){
        unit = '0' + unit
    }
    return unit
}
function timerUpdate(){
    let minutes = Math.floor(timeLeft/60)
    let seconds = timeLeft%60

    timerDisplay.innerHTML=`${formatTime(minutes)}:${formatTime(seconds)}`
 
}
function start() {
    document.getElementById("wire_good").onclick = stopTimer;
    document.getElementById("wire_bad").onclick = explode;
    timerUpdate()
    timer = setInterval(function(){
        if (timeLeft> 0)
            {
                timeLeft--;
                timerUpdate()
            }
        else{
            explode()
        }
    },1000)
}
function stopTimer() {
    clearInterval(timer)
    stoped = true;
    if(exploded === false) {
        document.getElementById("wire_good").style.backgroundColor = "white";
        document.getElementById("timer").className = "blinking";
        alert('Bomb defused!');
    }
}

function explode() {
    clearInterval(timer)
    exploded = true;
    if(stoped === false) {
        document.getElementById("timer").innerHTML = "";
        document.getElementById("container").style.backgroundImage = "url('explosion.png')";
        document.getElementById("container").style.height = "600px";
    }else{
        document.getElementById("timer").innerHTML = "";
        document.getElementById("wire_bad").style.backgroundColor = "#DFDFDF";
    }
}

start();
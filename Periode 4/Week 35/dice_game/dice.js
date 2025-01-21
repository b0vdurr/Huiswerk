var container = document.getElementById("container");
var dice = document.getElementById("dice");
var timer = false;
var score = 0;

var diceFaces = [
    [1, 'dice_face_1.png', "You rolled a 1"],
    [2, 'dice_face_2.png', "You rolled a 2"],
    [3, 'dice_face_3.png', "You rolled a 3"],
    [4, 'dice_face_4.png', "You rolled a 4"],
    [5, 'dice_face_5.png', "You rolled a 5"],
    [6, 'dice_face_6.png', "You rolled a 6"]
];

var currentFace = 0;
dice.style.backgroundImage = "url('"+diceFaces[0][1]+"')";
dice.onclick = diceClick;


function startDiceRoll() {
    timer = setInterval(() => {
        currentFace = Math.floor(Math.random() * 6);
        dice.style.backgroundImage = 'url(' + diceFaces[currentFace][1] + ')';
    }, 50);
}
function diceClick () {
    if (timer !== false) {
        var p = document.createElement("p");
        p.innerHTML = diceFaces[currentFace][2];
        document.getElementById("log").prepend(p);

        score = score + diceFaces[currentFace][0];

        if(score >= 18) {
            alert('You win, score: '+score);
            clearInterval(timer);
            timer  = false;
        }else{
            clearInterval(timer);
            timer  = false;

            setTimeout(function () {
                startDiceRoll();
            },1500);
        }
    }
};

startDiceRoll();
const amountOfButtons = 3;
var container = document.getElementById('container')
var colors = ["magenta","cyan","greenyellow","red"];
var win = false;

function checkWin() {
    for(i=0;i<amountOfButtons;i++){
        if(buttonsLooping[i]==true){
            return false
        }
    }
    button_color=document.getElementById('colorPicker1').style.backgroundColor
    for (i= 0; i < amountOfButtons; i++){
        if (buttons[i].style.backgroundColor != button_color){
            return false
        }
    }
    middle_button=Math.floor(amountOfButtons/2)
    if (amountOfButtons%2 != 0){middle_button+=1}
    document.getElementById('colorPicker' + (middle_button-1)).innerHTML='W'    
    document.getElementById('colorPicker' + (middle_button)).innerHTML='I'
    document.getElementById('colorPicker' + (middle_button+1)).innerHTML='N'      
    if(amountOfButtons%2 == 0){document.getElementById('colorPicker' + (middle_button+2)).innerHTML='!'      }
}

function getNextColor(color) {
    var position = colors.indexOf(color);
    position++;

    if(position === colors.length){
        position = 0;
    }

    var nextColor = colors[position];
    return nextColor;
}

var buttonColors = [];
var buttonsLooping = [];
var buttons = [];

for (var i = 0; i < amountOfButtons; i++){
    button=document.createElement('button')
    button.id = "colorPicker"+(i+1)
    container.appendChild(button)
    buttons.push(document.getElementById("colorPicker"+(i+1)));
    buttonColors.push("");
    buttonsLooping.push(true);

    var colorIndex = Math.floor(Math.random() * colors.length);
    var color = colors[colorIndex];

    buttonColors[i] = color;

    buttons[i].style.backgroundColor = color;
    buttons[i].onclick = function () {
        if(win === false) {
            var position = buttons.indexOf(this);

            if (buttonsLooping[position] === false) {
                buttonsLooping[position] = true;
            } else {
                buttonsLooping[position] = false;
                checkWin();
            }
        }
    };
}

setInterval(function () {
    for (var i = 0; i < buttons.length; i++){
        if(buttonsLooping[i] !== false) {
            var color = buttonColors[i];
            var newColor = getNextColor(color);

            buttons[i].style.backgroundColor = newColor;
            buttonColors[i] = newColor;
        }
    }
}, 500);
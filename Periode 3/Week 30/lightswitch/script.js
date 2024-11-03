document.body.style.background='black'
var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = 'Switch light on';
document.body.appendChild(btn);
var light_on = false;
btn.addEventListener('click', switchLight);
function switchLight(){
    if (light_on ==true){
        btn.innerHTML='Switch light on';
        document.body.style.background='black'
        light_on=false;
        console.log('Light is off');
    }
    else{
        btn.innerHTML='Switch light off';
        document.body.style.background='yellow'
        light_on=true;
        console.log('Light is on');
    }
}
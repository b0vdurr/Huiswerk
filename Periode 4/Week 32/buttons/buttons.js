const colors = [
    { name: "blue", message: "Je hebt op Button 1 gekilkt" },
    { name: "red", message: "Je hebt op Button 2 gekilkt" },
    { name: "green", message: "Je hebt op Button 3 gekilkt" },
    { name: "yellow", message: "Je hebt op Button 4 gekilkt" },
    { name: "cyan", message: "Je hebt niet op Button 1, Button 2, Button 3 of Button 4 gekilkt" },
    { name: "magenta", message: "Je hebt niet op Button 6 gekilkt" }
];

function makeButton(index,color,message) {
    const button = document.createElement('button');
    button.style.backgroundColor = color;
    button.id = `button ${index+1}`;
    button.innerText = `Button ${index+1}`;
    button.onclick = () =>{
        document.body.style.backgroundColor = color
        alert(message)
    }
    document.getElementById("container").appendChild(button);
}

colors.forEach((kleur, index) => {
    makeButton(index, kleur.name, kleur.message);
});
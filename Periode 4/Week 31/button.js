let container = document.getElementById('container')

container.style.backgroundColor='grey'
container.style.width='650px'
for(let i=1;i<=30;i++){
    let button = document.createElement('button')
    button.textContent=i
    button.style.padding = 10;
    button.style.backgroundColor='green'
    button.style.color='black'
    button.style.width='110px'
    button.style.height='75px'
    button.style.margin='10px'
    button.style.fontSize='50px'
    container.appendChild(button)
    button.addEventListener('click',function(){
        color = button.style.backgroundColor='red'
        button.addEventListener('click',function(){
            color = button.style.backgroundColor='purple'
            button.addEventListener('click',function(){
                color = button.style.backgroundColor='blue'
                button.addEventListener('click',function(){
                    color = button.style.backgroundColor='black'
                    button.addEventListener('click',function(){
                        container.removeChild(button)
                    })
                })
            })
        })
    })
}
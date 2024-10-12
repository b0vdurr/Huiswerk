from random import choice
from os import system
system('clear')
with open('Periode 3/Week 21/HP3.W21.OB - Woordspelletje/woorden.txt','r') as file:
    content=file.read()
woorden_lijst=content.split('\n')
antwoord=list(choice(woorden_lijst))
print(''.join(antwoord))
woord=list('_'*len(antwoord))
pogingen=10
already_checked_letters=[]
while pogingen > 0:
    if woord == antwoord:
        break
    print(f'Te raden woord: {' '.join(woord)}')
    print('Voer de letter in die je wilt raden en toets enter...:')
    print('-'*20)
    print(f'Je hebt {pogingen} kansen om het woord te raden!')
    print('Veel success')
    print('-'*20)
    while True: 
        letter=input('Voer de letter in: ')
        if len(letter) !=1 or not letter.isalpha():
            print('Voer een letter!')
            continue
        break
    system('clear')
    if letter in already_checked_letters:
        print('Al eerder gehad')
        continue
    elif letter in antwoord:
        print('Keurig, zit er in!')
        for i in range(len(antwoord)):
            if antwoord[i] == letter:
                woord[i] = letter
    else:
        print('Helaas, zit er niet in :(')
    already_checked_letters.append(letter)
    pogingen-=1
else:
    print(f'Helaas, je hebt geraden: {''.join(woord)}')
    print(f'Het woord was {''.join(antwoord)}')
    quit()
print('Goed gedaan, woord geraden!!!')
print('#'*20)
print('Hartelijk dank voor het spelen van deze ronde')
print(f'Het word was: {''.join(antwoord)}')
print(f'Door jou geraden: {''.join(antwoord)}')
print('#'*20)
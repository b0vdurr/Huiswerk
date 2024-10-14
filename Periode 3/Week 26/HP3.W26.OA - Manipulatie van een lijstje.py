from random import randint
lijst=[5,12,19,27,3]
print(lijst)
lijst.append(25)
print(lijst)
print(f'Er zitten {len(lijst)} elementen in de lijst.')
lijst.remove(12)
print(lijst)
print(f'Het numer {lijst.pop(0)} is verwijderd')
lijst.insert(0,36)
print(lijst)
print(f'Het totaal van de lijst is {sum(lijst)}')
lijst = []
print(lijst)
lijst=[x for x in range(1,6)]
print(lijst)
lijst+= [randint(1,10),randint(50,100)]
print(f'Er nu zitten {len(lijst)} elementen in de lijst en het totaal van de lijst is {sum(lijst)}.')

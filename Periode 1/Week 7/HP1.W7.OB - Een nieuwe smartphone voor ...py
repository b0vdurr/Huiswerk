IPhone_prijs=float(input('Voer de prijs van IPhone in: '))
Samsung_prijs=float(input('Voer de prijs van Samsung in: '))
if IPhone_prijs>Samsung_prijs:
    duurste_prijs=IPhone_prijs
    duurste = 'IPhone'
    goedkoopste_prijs=Samsung_prijs
    goedkoopste='Samsung'
else:
    duurste_prijs=Samsung_prijs
    duurste='IPhone'
    goedkoopste_prijs=IPhone_prijs
    goedkoopste='Samsung'

print(f'De {duurste} is het duurst, de telefoon kost: {duurste_prijs} Euro')
print(f'De {goedkoopste} is het goedkoopst, de telefoon kost: {goedkoopste_prijs} Euro')
if IPhone_prijs - Samsung_prijs<= 50:
    advies = 'IPhone'
else:advies='Samsung'
print(f'Het advies is dus de {advies} te kopen.')

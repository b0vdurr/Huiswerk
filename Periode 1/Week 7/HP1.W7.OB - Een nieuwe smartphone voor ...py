IPhone_prijs=float(input('Voer de prijs van IPhone in: '))
Samsung_prijs=float(input('Voer de prijs van Samsung in: '))

if IPhone_prijs>Samsung_prijs:
    duurste_prijs=IPhone_prijs
    duurste = 'IPhone'
    goedkoopste_prijs=Samsung_prijs
    goedkoopste='Samsung'
else:
    duurste_prijs=Samsung_prijs
    duurste='Samsung'
    goedkoopste_prijs=IPhone_prijs
    goedkoopste='IPhone'

print(f'De {duurste} is het duurst, de telefoon kost: {duurste_prijs} Euro')
print(f'De {goedkoopste} is het goedkoopst, de telefoon kost: {goedkoopste_prijs} Euro')
if IPhone_prijs > 900 or Samsung_prijs > 900:
    quit('Het advies is dus geen telefoon te kopen, ze zijn te duur.')
prijsverschil=IPhone_prijs-Samsung_prijs
if prijsverschil<= 50:
    advies = 'IPhone'
else:advies='Samsung'
print(f'Het advies is dus de {advies} te kopen. Deze is namelijk {abs(prijsverschil)} euro {'duurder' if prijsverschil > 0 else 'goedkooper'} dan de {'IPhone' if advies =='Samsung' else 'Samsung'}')
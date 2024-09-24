telefonen={'IPhone':0,'Samsung':0,'Zenfone':0}
telefonen['IPhone']=float(input('Voer de prijs van IPhone in: '))
telefonen['Samsung']=float(input('Voer de prijs van Samsung in: '))
telefonen['Zenfone']=float(input('Voer de prijs van Zenfone in: '))
if max(telefonen.values()) == telefonen['IPhone']:
    duurste_prijs=telefonen['IPhone']
    duurste='IPhone'
    if min(telefonen['Samsung'],telefonen['Zenfone']) == telefonen['Samsung']:
        goedkoopste_prijs=telefonen['Samsung']
        goedkoopste='Samsung'
        midden='Zenfone'
        midden_prijs=telefonen['Zenfone']
    else:
        goedkoopste_prijs=telefonen['Zenfone']
        goedkoopste='Zenfone'
        midden = 'Samsung'
        midden_prijs = telefonen['Samsung']
elif max(telefonen.values()) == telefonen['Samsung']:
    duurste_prijs=telefonen['Samsung']
    duurste='Samsung'
    if min(telefonen['IPhone'],telefonen['Zenfone']) == telefonen['IPhone']:
        goedkoopste_prijs=telefonen['IPhone']
        goedkoopste='IPhone'
        midden='Zenfone'
        midden_prijs=telefonen['Zenfone']
    else:
        goedkoopste_prijs=telefonen['Zenfone']
        goedkoopste='Zenfone'
        midden='IPhone'
        midden_prijs = telefonen['IPhone']
else: 
    duurste_prijs=telefonen['Zenfone']
    duurste='Zenfone'
    if min(telefonen['IPhone'],telefonen['Samsung']) == telefonen['IPhone']:
        goedkoopste_prijs=telefonen['IPhone']
        goedkoopste='IPhone'
        midden='Samsung'
        midden_prijs=telefonen['Samsung']
    else:
        goedkoopste_prijs=telefonen['Samsung']
        goedkoopste='Samsung'
        midden='IPhone'
        midden_prijs=telefonen['IPhone']

print(f'De {duurste} is het duurst, de telefoon kost: {duurste_prijs} Euro')
print(f'De {goedkoopste} is het goedkoopst, de telefoon kost: {goedkoopste_prijs} Euro')
print(f'De {midden} zit er tussenin met: {midden_prijs} Euro')
if telefonen['Zenfone'] < telefonen['IPhone'] - 100 and telefonen['Zenfone'] < telefonen['IPhone'] - 100:
    advies = 'Zenfone'
else:
    prijsverschil = telefonen['IPhone'] - telefonen['Samsung']
    if prijsverschil <= 50:
        advies = "IPhone"
    else:
        advies = "Samsung"
advies_prijs = telefonen.pop(advies)
keys=list(telefonen.keys())
values= list(telefonen.values())
print(f"Het advies is dus de {advies} te kopen. Deze is namelijk {abs(advies_prijs - values[0])} Euro {'duurder' if advies_prijs - values[0] > 0 else 'goedkoper'} dan de {keys[0]} en {abs(advies_prijs - values[1])} Euro {'duurder' if advies_prijs - values[1] > 0 else 'goedkoper'} dan de {keys[1]}") 

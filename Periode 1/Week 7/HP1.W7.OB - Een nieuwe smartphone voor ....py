telefoons={'IPhone':0,'Samsung':0}
telefoons['IPhone']=int(input('Hoeveel kost de IPhone?'))
telefoons['Samsung']=int((input('Hoeveel kost de Samsung?')))
difference = telefoons['IPhone'] - telefoons['Samsung']

print(difference)
if difference < 0:
    print(f'Het advies is dus de IPhone te kopen. Deze is namelijk {abs(difference)} euro goedkooper dan de Samsung')
elif difference <= 50:
    print(f'Het advies is dus de IPhone te kopen. Deze is namelijk {difference} euro duurder dan de Samsung')
elif difference == 0:
    print('Het advies is dus de IPhone te kopen. De prijs is hetzelfde')
else: print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {difference} euro goedkooper dan de Iphone')
telefoons={'IPhone':0,'Samsung':0}
telefoons['IPhone']=int(input('Hoeveel kost de IPhone?'))
telefoons['Samsung']=int((input('Hoeveel kost de Samsung?')))
print(f'De {max(telefoons)} is het duurst, de telefoon kost: {telefoons.get(max(telefoons))} Euro')
print(f'De {min(telefoons)} is het goedkoopst, de telefoon kost: {telefoons.get(min(telefoons))} Euro')
if telefoons.get('IPhone') - telefoons.get('Samsung') >= 50: advies = 'Samsung'
else:advies = 'IPhone'
print(f'Het advies is dus de {advies} te kopen')
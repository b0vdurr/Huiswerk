getalen=[]
for i in range(10):
    print(f'INPUT #{i+1}')
    while True:
        try:
            getal=int(input('Voer een getal in: \n'))
            getalen.append(getal)
            break
        except ValueError:
            print('Onjuiste invoer')
            continue

deelbar_door_3_aantal=0
for i in getalen:
    if i%3==0: deelbar_door_3_aantal+=1
print(f'Het grootste getal is: {max(getalen)}')
print(f'Het kleinste getal is: {min(getalen)}')
print(f'Het aantal getallen deelbaar door 3 (zonder rest) is: {deelbar_door_3_aantal}')
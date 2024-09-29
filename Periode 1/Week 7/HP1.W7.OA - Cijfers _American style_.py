while True:
    try:
        cijfer=float(input('Voer je cijfer in: '))
    except ValueError:
        print('Voer een nummer')
        continue
    if cijfer > 10 or cijfer < 1:
        print('Voer een correcte cijfer in')
    else: break
if cijfer >= 8.5:print('A')
elif cijfer >= 7.5 and cijfer < 8.5:print('B')
elif cijfer >= 6.5 and cijfer < 7.5:print('C')
elif cijfer >= 5.5 and cijfer < 6.5:print('D')
else: print('F')
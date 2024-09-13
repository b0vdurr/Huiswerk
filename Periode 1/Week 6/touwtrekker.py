#Touwtrekker van Davyd Tskhovrebov
TOUW_DIAMETERS = [3.0, 4.5, 6.3]
TOUW_PRIJZEN = [1.23, 2.45, 4.1]
aantal_touwen=[]
lengte_touwen=[]
totaal=0
for i in range(len(TOUW_DIAMETERS)):
    aantal=int(input(f'Hoeveel touwen van {TOUW_DIAMETERS[i]} dikte wil je?: '))
    lengte=float(input('Welke lengte? (m): '))
    aantal_touwen.append(aantal)
    lengte_touwen.append(lengte)

print(f'{'*'*15} KASSA BON {'*'*15}')
for i in range(len(TOUW_DIAMETERS)):
    if aantal_touwen[i] == 0 or lengte_touwen[i] == 0:
        continue
    else:
        print(f'{TOUW_DIAMETERS[i]} touw:\t{aantal_touwen[i]} x {lengte_touwen[i]}m = {aantal_touwen[i]*lengte_touwen[i]}')
        totaal+=lengte_touwen[i]*aantal_touwen[i]
print(f'Te betalen:\t\t{totaal}')
print('*'*41)
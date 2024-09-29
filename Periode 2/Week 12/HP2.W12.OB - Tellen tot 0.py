num=int(input('Voer een getal in: '))

for i in range(num, 0, -1 if num > 0 else 1):
    print(i)
    if i == 1 or num ==-1:print(0)
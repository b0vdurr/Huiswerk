def print_multiplication(number:int, multiplier:int)->str: return f'{number} x {multiplier} = {number*multiplier}'
while True:
    try: 
        num = int(input('Voer een getal in: '))
        break
    except ValueError:  pass
for i in range(1,11):
    print(print_multiplication(num,i))
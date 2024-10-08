def RomanToInt(num:str)->int:
    num=num.replace('IV','I'*4)
    num=num.replace('IX','I'*9)
    num=num.replace('XL','I'*40)
    num=num.replace('XC','I'*90)
    num=num.replace('CD','I'*400)
    num=num.replace('CM','I'*900)
    num=num.replace('M','I'*1000)
    num=num.replace('D','I'*500)
    num=num.replace('C','I'*100)
    num=num.replace('L','I'*50)
    num=num.replace('X','I'*10)
    num=num.replace('V','I'*5)
    return len(num)

def IntToRoman(num:int)->str:
    roman_num=''
    while num!=0:
        if num >= 1000:
            roman_num+='M'
            num-=1000
        elif num >= 900:
            roman_num+='CM'
            num -=900
        elif num >= 500:
            roman_num+='D'
            num-=500
        elif num >= 400:
            roman_num+='CD'
            num -=400
        elif num >=100:
            roman_num+='C'
            num-=100
        elif num >=90:
            roman_num+='XC'
            num-=90
        elif num >=50:
            roman_num+='L'
            num-=50
        elif num>=40:
            roman_num+='XL'
            num-=40
        elif num >=10:
            roman_num+='X'
            num-=10
        elif num>=9:
            roman_num+='IX'
            num-=9
        elif num>=5:
            roman_num+='V'
            num-=5
        elif num>=4:
            roman_num+='IV'
            num-=4
        elif num >=1:
            roman_num+='I'
            num-=1
    return roman_num
is_int=False
usr = input('Voer een getal in: ')
try:
    usr=int(usr)
    is_int=True
except ValueError:
    pass
if is_int:
    print(IntToRoman(usr))
else:
    for i in usr:
        if i not in ['I','V','X','L','C','D','M']:
            quit('Verkeerde getal!')
    print(RomanToInt(usr))
        

woord_1=input('Voer de eerste woord in: ')
woord_2=input('Voer de tweede woord in: ')
common_letters=''
for i in woord_1:
    if i in woord_2 and i not in common_letters:    
        common_letters+=i
print(common_letters)
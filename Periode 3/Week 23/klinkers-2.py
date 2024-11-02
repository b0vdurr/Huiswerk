VOWELRATIO = 3
sentence = input('Geef jouw zin vol klanken!\n')

totalVowels = 0
for character in sentence:
  print(character)
  if character in 'aeiouy':
    totalVowels += 1

if totalVowels > len(sentence) // VOWELRATIO:
  print('Heel klinkend!')
else:
  print('Klinkt echt niet!')
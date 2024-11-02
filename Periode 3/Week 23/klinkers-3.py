VOWELRATIO = 3
moreText = True

while moreText:
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

  answer = input('Nog iets laten klinken? ja/nee\n')
  moreText = answer.lower() == 'ja'
list=[1, "aap", 2, "apen", 3, "watermeloen", 15, 27, 15, 'lekker bezig', '6', 7.23, 'makkelijk hoor']
aantal=0
for i in list:
    if type(i) == int:  aantal+=1
print(aantal)
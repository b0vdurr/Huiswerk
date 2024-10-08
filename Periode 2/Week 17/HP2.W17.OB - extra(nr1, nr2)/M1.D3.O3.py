from random import randint

A = randint(-1000, 1000)
B = randint(-1000, 1000)
C = randint(-1000, 1000)
D = randint(-1000, 1000)

sorted_getalen={'A':A,'B':B,'C':C,'D':D}
sorted_getalen = dict(sorted(sorted_getalen.items(), key=lambda item: item[1]))

print(f'getal {list(sorted_getalen.keys())[0]} ({list(sorted_getalen.values())[0]}) is wat het is, getal {list(sorted_getalen.keys())[1]} ({list(sorted_getalen.values())[1]}) is groter, getal {list(sorted_getalen.keys())[2]} ({list(sorted_getalen.values())[2]}) is nog groter, maar getal {list(sorted_getalen.keys())[3]} ({list(sorted_getalen.values())[3]}) is het grootst!')
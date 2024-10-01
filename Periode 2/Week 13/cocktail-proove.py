from random import choice
cocktails=[
    {
        'name': 'Blue lagoon',
        'price': 9.95,
        'ingridients': ['malbu','blue Curacao', 'sprite']
    },
    {
        'name':'Bora bora',
        'price':9.95,
        'ingridients':['vodka','orange juice','passionfruit puree','grenadine']
    },
    {
        'name':'Strawberry daquiri',
        'price':11.25,
        'ingridients':['rum','triple sec','fresh strawberries juice', 'lime juice']
    },
    {
        'name':'Pornstar martini',
        'price':11.25,
        'ingridients':['vodka', 'passoa', 'vanila syrup', 'egg white','tropical juice']
    },
    {
        'name':'Pina colada',
        'price':9.95,
        'ingridients':['rum','coconat syrup', 'pineapple juice','whipped cream']
    },
    {
        'name':'Moscow mule',
        'price':9.95,
        'ingridients':['vodka','ginger beet','fresh lime','Anngostura bitter']
    },
    {
        'name':'The Hulk',
        'price':9.95,
        'ingridients':['vodka','Pisang Ambon','melon liqueur','orange juice','kiwi syrup']
    },
    {
        'name':'Sinas Split',
        'price':9.95,
        'ingridients':['liqueur 43','orange juice', 'cream']
    }
]
possible_cocktails=cocktails
while len(possible_cocktails)>1:
    random_cocktail=possible_cocktails[choice(range(0,len(possible_cocktails)))]
    random_ingridient=random_cocktail['ingridients'][choice(range(0,len(random_cocktail['ingridients'])))]
    while True:
        usr=input(f'Bevat je cocktail {random_ingridient}? (j/n)')
        if usr.lower() in ['j','n']:break
    if usr=='j':possible_cocktails=[possible_cocktails[x] for x in range(len(possible_cocktails)) if random_ingridient in possible_cocktails[x]['ingridients']]
    else:possible_cocktails=[possible_cocktails[x] for x in range(len(possible_cocktails)) if random_ingridient not in possible_cocktails[x]['ingridients']]
print(f'Name: {possible_cocktails['name']}')
print(f'Price: {possible_cocktails['price']}')



    
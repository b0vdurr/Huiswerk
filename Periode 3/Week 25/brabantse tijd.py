def brabantse_tijd(minuten:int)->str:
    brabantse_uur=f'{minuten//60} uur'
    minuten-=60*(minuten//60)
    print(minuten)
    if minuten>=15:
        kwartiertje=f' en {minuten//15} kwartier'
    else:
        kwartiertje= ' precies'    
    return brabantse_uur + kwartiertje
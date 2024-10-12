def bereken_poten(giraffen, struisvogels, zebras):
    poten_giraffen = 4
    poten_struisvogels = 2
    poten_zebras = 4
    totaal_poten = (giraffen * poten_giraffen) + (struisvogels * poten_struisvogels) + (zebras * poten_zebras)
    
    return totaal_poten

giraffen = int(input("Voer het aantal giraffen in: "))
struisvogels = int(input("Voer het aantal struisvogels in: "))
zebras = int(input("Voer het aantal zebra's in: "))

totaal_poten = bereken_poten(giraffen, struisvogels, zebras)
print(f"Het totale aantal poten is: {totaal_poten}")
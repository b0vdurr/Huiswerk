import math

deur_hoogte_meter = float(input('Voer deur hoogte in(m): '))
deur_breedte_meter = float(input('Voer deur breedte in (m): '))
aantal_deuren = int(input('Voer aantal deuren in: '))
verf_vermogen_m2 = float(input('Hoeveel vierkante meter kan een bus verf verven?'))
bus_verf_inhoud_ml = float(input('Hoeveel milliliter verf zit er in een bus?: '))
prijs_bus_verf = float(input('Wat is de prijs van één bus verf?:'))
oppervlakte_schuurpapier_m2 = float(input('Hoeveel vierkante meter kan één vel schuurpapier opschuren?: '))
prijs_schuurpapier = float(input('Wat is de prijs van één vel schuurpapier?:'))

deur_oppervlakte = deur_hoogte_meter * deur_breedte_meter * 2
totaal_oppervlakte = deur_oppervlakte * aantal_deuren

aantal_bussen_verf = math.ceil(totaal_oppervlakte / verf_vermogen_m2)
kosten_verf = round(aantal_bussen_verf * prijs_bus_verf, 2)

aantal_vellen_schuurpapier = math.ceil(totaal_oppervlakte / oppervlakte_schuurpapier_m2)
kosten_schuurpapier = round(aantal_vellen_schuurpapier * prijs_schuurpapier, 2)

print(f"Totale oppervlakte om te verven: {round(totaal_oppervlakte, 2)} m2")
print(f"Benodigde bussen verf: {aantal_bussen_verf}")
print(f"Totale kosten voor verf: {kosten_verf}")
print(f"Benodigde vellen schuurpapier: {aantal_vellen_schuurpapier}")
print(f"Totale kosten voor schuurpapier: {kosten_schuurpapier}")

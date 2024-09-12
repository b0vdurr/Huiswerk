import math

deur_hoogte_meter = 2
deur_breedte_meter = 0.8
aantal_deuren = 13
verf_vermogen_m2 = 6
bus_verf_inhoud_ml = 750
prijs_bus_verf = 23.45
oppervlakte_schuurpapier_m2 = 1.5
prijs_schuurpapier = 0.47

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

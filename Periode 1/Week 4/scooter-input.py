band_prijs = float(input("Wat is de prijs van een nieuwe band?: "))
arbeid_per_band = float(input("Wat zijn de arbeidskosten per band?: "))
lampje_prijs = float(input("Wat is de prijs van een nieuw lampje?: "))
lampje_vervangen = float(input("Wat zijn de kosten voor het vervangen van een lampje?: "))

versleten_band = int(input("Hoeveel banden zijn versleten?: "))
kapot_lampje = int(input("Hoeveel lampjes moeten vervangen worden?: "))

totale_kosten = (band_prijs + arbeid_per_band) * versleten_band + (lampje_prijs + lampje_vervangen) * kapot_lampje

print(f"Totale kosten voor de opknapbeurt van de scooter: €{round(totale_kosten, 2)}")

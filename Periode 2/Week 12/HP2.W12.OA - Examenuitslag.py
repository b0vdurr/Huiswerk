def berekenen(ScoreE,ScoreP,ScoreO,ScoreS):
    totaal=ScoreE+ScoreP-ScoreO-ScoreS
    if ScoreP==8 and ScoreE>4 and ScoreO==0 and ScoreS==0:return 'Goed'
    elif (ScoreS==0 and totaal > 7 and totaal < 13) or (ScoreS==1 and totaal > 9):return 'Voldoende'
    else:return 'Onvoldoende'
def actie_invoeren(naam, maximaal):
    while True:
        try:
            user=int(input(f'Voer {naam} acties in: '))
        except ValueError:
            print('Voer een getal')
            continue
        if user > maximaal or user < 0:
            print('Out of range')
        else:return user

ScoreE=actie_invoeren('excellent',6)
ScoreP=actie_invoeren('professionele',8)
ScoreO=actie_invoeren('onprofessionele',5)
ScoreS=actie_invoeren('slechte',2)

print(berekenen(ScoreE,ScoreP,ScoreO,ScoreS))
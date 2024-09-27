score_engels = int(input('Wat was je score voor het Engels examen?'))
geslaagd_engels = score_engels >= 5

score_nederlands = int(input('Wat was je score voor het Nederlands examen?'))
geslaagd_nederlands = score_nederlands >= 4

score_rekenen = int(input('Wat was je score voor het rekenen examen?'))
geslaagd_rekenen = score_rekenen >= 4

score_ontwikkeling = int(input('Wat was je score voor het vak Ontwikkelingsvaardigheden?'))
geslaagd_ontwikkeling = score_ontwikkeling >= 4

dimensies_scores = []
for dimensie in ['politiek-juridische dimensie', 'economische dimensie', 'maatschappelijk-sociale dimensie', 'vitaal burgerschap']:
    dimensies_scores.append(int(input(f'Wat was je score voor de {dimensie}?')))

is_burgerschap_gehaald = False
gemiddelde_burgerschap = sum(dimensies_scores) / len(dimensies_scores)
if gemiddelde_burgerschap >= 6:
    is_burgerschap_gehaald = True

if all([geslaagd_engels, geslaagd_nederlands, geslaagd_rekenen, geslaagd_ontwikkeling, is_burgerschap_gehaald]):
    print('Gefeliciteerd! Je hebt je diploma gehaald.')
else:
    print('Helaas, je hebt niet genoeg punten behaald. Je hebt geen diploma gehaald.')
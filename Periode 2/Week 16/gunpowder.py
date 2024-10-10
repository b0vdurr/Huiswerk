from test_lib import test,report
NITRATE_PERC = 75
CHARCOAL_PERC = 15
SULFUR_PERC = 10
 
def calculate_mix(nitrate: float, charcoal: float, sulfur: float) -> tuple:
    NITRATE_PERC = 75
    CHARCOAL_PERC = 15
    SULFUR_PERC = 10

    p1 = nitrate / NITRATE_PERC
    c1 = round(CHARCOAL_PERC * p1, 2)
    s1 = round(SULFUR_PERC * p1, 2)

    p2 = charcoal / CHARCOAL_PERC
    n2 = round(NITRATE_PERC * p2, 2)
    s2 = round(SULFUR_PERC * p2, 2)

    p3 = sulfur / SULFUR_PERC
    n3 = round(NITRATE_PERC * p3, 2)
    c3 = round(CHARCOAL_PERC * p3, 2)

    if charcoal >= c1 and sulfur >= s1:
        return (nitrate, c1, s1)
    elif nitrate >= n2 and sulfur >= s2:
        return (n2, charcoal, s2)
    else:
        return (n3, c3, sulfur)
  
mix = calculate_mix(515.4,159.2,87.3)
expected = (515.4,103.08,68.72)
test('example test',expected, mix)
report()
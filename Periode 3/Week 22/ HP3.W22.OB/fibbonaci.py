def calculate_fibbonaci(n:int):
    fibbonaci_sequence=[0,1]
    if n <2:
        return [0]
    while len(fibbonaci_sequence) < n:
        fibbonaci_sequence.append(fibbonaci_sequence[len(fibbonaci_sequence)-2]+fibbonaci_sequence[len(fibbonaci_sequence)-1])
    return fibbonaci_sequence
def calculate_golden_ratio(fibbonaci_sequence:list)->float:
    if len(fibbonaci_sequence) < 2:return None
    a=fibbonaci_sequence[-2]
    b=fibbonaci_sequence[-1]
    if a == 0: return None
    return (a + b) / a
fibbonaci_sequence=calculate_fibbonaci(501)
print(fibbonaci_sequence)
print(calculate_golden_ratio(fibbonaci_sequence))
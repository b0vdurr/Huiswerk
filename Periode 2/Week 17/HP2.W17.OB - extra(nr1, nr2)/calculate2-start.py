from test_lib import test, report
from math_operations import increment, decrement, add, subtract, multiply, divide

nr1 = 3
nr2 = 11
nr3 = 37
nr4 = 79

# example
result1 = nr1 + nr3
result2 = add(nr1,nr3)
test('example', result1, result2)

result1 = nr1 / nr4
result2 = divide(nr1,nr4)
test('add', result1,result2)

result1 = nr4 / (nr1 / nr2) * nr3
result2 = multiply(divide(nr4,divide(nr1,nr2)),nr3)
test('expression-1',result1, result2)

result1 = round((nr3 - nr2) / nr4, nr3)
result2 = round(divide((subtract(nr3,nr2)),nr4),nr3)
test('expression-2',result1, result2)

result1 = (nr1 * round((nr4 - nr2) / (nr2 + nr3), nr2 - 9))
result2 = multiply(nr1,round(divide(subtract(nr4,nr2),add(nr2,nr3)),nr2-9) )
test('expression-3', result1, result2)

result1 = abs(nr1 - (nr2 * (nr4 - nr3)) / (nr1 + nr2))
result2 = abs(subtract(nr1,divide(multiply(nr2,subtract(nr4,nr3)),add(nr1,nr2))))
test('expression-4', result1, result2)

result1 = nr4 - round((nr1 * (nr4 - nr3)) / (nr2 + nr3), nr1) * (nr2 + nr4) + 1 # use increment()
result2 = increment(subtract(nr4,multiply(round(divide((multiply(nr1,subtract(nr4,nr3))),add(nr2,nr3)),nr1),add(nr2,nr4))))
test('expression-5', result1, result2)

report()

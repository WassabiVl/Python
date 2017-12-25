# purpose to find multiple of 3 and 5 fro 0 to 1000 and add up their sum
ArrayIncrement = 0
sumTotal = 0
MultipleArray = []
for x in range(0, 1000):
    if x % 3 == 0 and x % 5 == 0:
        ArrayIncrement += 1
        MultipleArray.append(x)
        sumTotal += x
    elif x % 3 == 0 or x % 5 == 0:
        ArrayIncrement += 1
        MultipleArray.append(x)
        sumTotal += x
print(MultipleArray)
print(sumTotal)

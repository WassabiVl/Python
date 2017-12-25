y = 0
t = 0
z = []
for x in range(0, 1000):
    if x % 3 == 0 and x % 5 == 0:
        y += 1
        z.append(x)
        t += x
    elif x % 3 == 0 or x % 5 == 0:
        y += 1
        z.append(x)
        t += x
print(z)
print(t)

def squareroot(num):
    a = num/2
    b = num/a
    while a != b:
        b = num/a
        a = (a+b)/2
    return a

print(squareroot(30))

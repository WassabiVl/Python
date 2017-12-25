# return the sum of the even fibonacci numbers less than 4 million
def fib_iterative(n):
    z = []
    a, b, c = 0, 1, 0
    while n > 0:
        a, b = b, a + b
        if a % 2 == 0:  # find the even numbers
            z.append(a)  # add them to an array to check
            c += a
        n -= 1
    return z, c


print(fib_iterative(34))

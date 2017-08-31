'''
exhaustive search looks through possibilities until it can find the answer
'''


def exhastiveSearchSquareRoot(x):  #
    epsilon = 0.01  # the difference between the close answer and real one
    step = epsilon**2  # decreases the difference as it moves uo
    numGuesses = 0  # to calculate the amount of guesses needed
    ans = 0.0  # the actual answer
    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1
    if abs(ans**2 - x) >= epsilon:
        return 'Failed on Square root of', x, ' and numGuesses =', numGuesses
    else:
        return ans, 'is close to square root of', x, ' and numGuesses =', numGuesses


def advExhastiveSearchSquareRoot(x):  # this tires to guess where the number is between low and max
    epsilon = 0.01  # the difference between the close answer and real one
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    lowa, higha, ansa = [], [], []
    while abs(ans**2 - x) >= epsilon:
        lowa.append(low)
        higha.append(high)
        ansa.append(ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return 'numGuessese =', numGuesses, 'and', ans, 'is close to the square root of', x


print(advExhastiveSearchSquareRoot(10000))
print(exhastiveSearchSquareRoot(10000))

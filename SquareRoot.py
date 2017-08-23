'''  using Heron of Alexandra or Babylonians this implementation follows the following steps
1) start with a guess g.... since we can guess anywhere why not half the number
2) IF g*g is close to x (the number), stop and say that g is the answer
3) otherwise create  a new guess by averaging g and x/g
    a)this gave me the idea for the while statement
4) repeat till we get a close guess
'''


def principalsquareroot(x):  # the positive number of the square root
    if x == 0:  # to save computing time on zero
        return 0
    elif x > 0:
        g = x / 2  # got to start somewhere, so why not half the number
        b = x / g  # just to be certain that 2 was not chosen and to start the while loop
        while g != b:  # this loop checks if the number is the square root of the function
            b = x / g  # create variable b = x/g
            g = (g + b) / 2  # find the new number by averaging a and b
            return g
    else:  # this needs to calculate imaginary numbers
        g = principalsquareroot(-x)
        return str(g) + "i "


def negativesquareroot(x):  # to get the negative version of the square root
    a = principalsquareroot(x)
    if a is isinstance(a, str):  # not working
        return "-" + a
    else:
        return a * -1


print(principalsquareroot(-1))
print(negativesquareroot(-1))

'''
improvement to this algo would be to check which mult 
'''

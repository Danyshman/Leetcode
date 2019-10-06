import math


def maxNumberOfBallons(text):
    b= 0
    a = 0
    l = 0
    o = 0
    n = 0
    for letter in text:
        if letter == 'b':
            b += 1
        elif letter == 'a':
            a += 1
        elif letter == 'l':
            l += 0.5
        elif letter == 'o':
            o += 0.5
        elif letter == 'n':
            n += 1
    return min([b,a,l,o,n])



print(maxNumberOfBallons('nlaebolko'))

print(math.floor(195.5))
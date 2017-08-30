#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    ar.sort(reverse=True)
    max = ar[0]
    c = 0
    for item in ar:
        if max == item:
            c = c + 1
        else:
            break
    return c

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

result = birthdayCakeCandles(n, ar)
print(result)

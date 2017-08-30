#!/bin/python3

import sys, time

def timeConversion(s):
    t = time.strptime(s, "%I:%M:%S%p")
    conversion = time.strftime("%H:%M:%S", t)
    return conversion

s = input().strip()
result = timeConversion(s)
print(result)

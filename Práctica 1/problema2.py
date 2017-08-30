#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
max_sum = 0
min_sum = 999999999999999999999999999
for number in arr:
    if sum(arr) - number > max_sum:
        max_sum = sum(arr) - number
    if sum(arr) - number < min_sum:
        min_sum = sum(arr) - number

print('{} {}'.format(min_sum, max_sum))

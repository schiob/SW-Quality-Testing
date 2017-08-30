#!/bin/python3

# HackerRank Problema 2: Mini-Max Sum.

import sys

# Pone en una lista una serie de números separados por un espacio.
arr = list(map(int, input().strip().split(' ')))
# Se guardan las sumas mínimas y máximas respectivamente.
max_sum = 0
# En el caso de la mínima se usa un número por default más alto que 5 veces el constraint de cada número (5x10^9).
min_sum = 999999999999999999999999999
for number in arr:
	# Para cada número de la lista:
	# Si la suma de los elementos de la lista menos el número actual es mayor a la suma máxima esta se reemplaza.
	if sum(arr) - number > max_sum:
		max_sum = sum(arr) - number
	# Si la suma de los elementos de la lista menos el número actual es menor a la suma mínima esta se reemplaza.
	if sum(arr) - number < min_sum:
		min_sum = sum(arr) - number

# Imprime con formato ambas sumas, P. ej.: 13 25.
print('{} {}'.format(min_sum, max_sum))

from pyDatalog import pyDatalog
from random import randrange
import math
import numpy


pyDatalog.create_terms('sum_of_range, N, Sum_of_range, average, arr, Average, median, Median, prod, Prod, fact')
n = 1000000

sum_of_range[N] = (0 + N) * n/2
print(sum_of_range[n]==Sum_of_range)

average[N] = sum_of_range[N] / N
print(average[n]==Average)

arr = list(numpy.random.rand(10))
arr.sort()

median = arr[n//2] if n%2==1 else (arr[n//2 - 1] + arr[n//2]) / 2
print(median==Median)

fact[N] = N * fact[N-1]
fact[min(arr)] = min(arr)

prod = fact[max(arr)-min(arr)] ** (n / (max(arr)-min(arr)))
print(prod==Prod)

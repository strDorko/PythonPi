# Calculating Pi to the Nth number
# Author: Rodrigo Martin
# Using: Leibniz's formula - https://www.geeksforgeeks.org/calculate-pi-with-python/
# Date : 31 / 12 / 2022 [DD / MM / YYYY]
from math import *
from decimal import *

nth_num = input("To what Nth number would you like to roudn it up to? (Max 16 digits after the '.'): ")

k = 1
s = 0

for i in range(10000000):

    if i % 2 == 0:
        s += 4/k
    else:

        s-= 4/k

    k+= 2

print(round(s, int(nth_num)))








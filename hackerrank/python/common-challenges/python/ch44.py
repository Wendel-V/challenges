# itertools.product()

A = list(map(int,input().split()))
B = list(map(int,input().split()))

from itertools import product
print(*list(product(A,B)))

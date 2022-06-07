
# Enter your code here. Read input from STDIN. Print output to STDOUT

S, k = input().split()
k = int(k)

from itertools import permutations
permutations = list(permutations(S, k))
permutations.sort()

for i in permutations:
    print(''.join(i))
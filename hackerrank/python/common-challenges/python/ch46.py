# Enter your code here. Read input from STDIN. Print output to STDOUT

S, k = input().split()
k = int(k)

from itertools import combinations_with_replacement
replacement = [c for c in list(combinations_with_replacement(sorted(S),k))]

for c in replacement:
    print(''.join(c))
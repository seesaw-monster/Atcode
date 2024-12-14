# import sys
# sys.setrecursionlimit(10**6)
from itertools import combinations
a, b, c, d, e = map(int, input().split())

S = 'ABCDE'

def call_point(S):
    point = 0
    if 'A' in S:
        point += a
    
    if 'B' in S:
        point += b

    if 'C' in S:
        point += c

    if 'D' in S:
        point += d

    if 'E' in S:
        point += e

    return point

def get_all_substrings(s):
    substrings = []
    length = len(s)
    for i in range(1, length+1):
        for combo in combinations(s, i):
            c = ''.join(combo)
            substrings.append([c, call_point(c)])
    return substrings

L = get_all_substrings(S)
L.sort(key=lambda x: (-x[1],x[0]))

for l in L:
    print(l[0])

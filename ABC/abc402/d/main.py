# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, M = map(int, input().split())

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

if N%2!=0:
    print((1+M)//2)
else:
    mid = N//2
    ng = set()
    count = defaultdict(int)


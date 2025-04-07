# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, W = map(int, input().split())

block = [[] for _ in range(W)]
max_y = -1

for _ in range(N):
    x, y = map(int, input().split())
    if y>max_y:
        max_y = y
    block[x-1].append(y)

block.sort()

S = [deque() for _ in range(W)]

for w in range(W):
    S[w] = deque(block[w])

T = [[0 for _ in range(max_y)] for _ in range(W)]

Q = int(input())
q = []
for _ in range(Q):
    t, a = map(int, input().split())

    if len(S[a]) and S[a][0]<=t:
        _ = S[a].popleft()
        print('Yes')
    else:
        print('No')

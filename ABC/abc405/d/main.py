# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
H, W = map(int, input().split())
S = []

for _ in range(H):
    S.append(list(input()))

D = [[0 for _ in range(W)] for _ in range(H)]

q = deque()
XY = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# Clist = ['^', 'v', '>', '<']
Clist = {'-1 0': 'v', '1 0': '^', '0 1': '<', '0 -1': '>'}
T = S.copy()
for i in range(H):
    for j in range(W):
        if S[i][j]=='E':
            q.append((i, j))

while q:
    h, w = q.popleft()
    for x, y in XY:
        if 0<=h+x<H and 0<=w+y<W and S[h+x][w+y]=='.':
            if D[h+x][w+y]!=0 and D[h+x][w+y]<D[h][w]+1:
                continue

            D[h+x][w+y]=D[h][w]+1
            S[h+x][w+y]=Clist[f'{x} {y}']
            q.append((h+x, w+y))


# for i in range(H):
#     print(*D[i])

for i in range(H):
    s = ''
    for j in range(W):
        s+=T[i][j]
    print(s)

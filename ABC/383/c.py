import sys
sys.setrecursionlimit(10**6)
H, W, D = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(input()))

C = [[False for _ in range(W)] for _ in range(H)]

def cal_mn(i, j, a, b):
    return abs(i-a)+abs(j-b)

ind = []

for i in range(H):
    for j in range(W):
        if S[i][j]=='H':
            ind.append((i, j))

c = 0
for i in range(H):
    for j in range(W):


print(s)

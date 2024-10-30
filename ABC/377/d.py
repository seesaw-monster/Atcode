# import sys
# sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

LR = []

for _ in range(N):
    l, r = map(int, input().split())
    LR.append((l, r))

LR = sorted(LR, key=lambda x: x[1])

max_len = LR[0][0]

diff = max_len*(M-LR[0][1]+1)

for i in range(1, len(LR)):
    l, r = LR[i]
    if l > max_len:
        diff += (l-max_len)*(M-r+1)
        max_len = l

print(M*(M+1)//2-diff)

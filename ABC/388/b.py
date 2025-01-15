# import sys
# sys.setrecursionlimit(10**6)
N, D = map(int, input().split())
TL = []

for _ in range(N):
    t, l = map(int, input().split())
    TL.append((t, l))

for k in range(1, D+1):
    max_weight = 0
    for i in range(N):
        now_weight = (TL[i][1]+k)*TL[i][0]
        if max_weight<now_weight:
            max_weight = now_weight

    print(max_weight)


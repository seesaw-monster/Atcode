# import sys
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split())
P = list(map(int, input().split()))


for i in range(K):
    B = []
    for p in range(N):
        B.append(P[P[p]-1])

    P = B

print(P)

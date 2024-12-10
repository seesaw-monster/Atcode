# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

T = 0
W = 0
for _ in range(N):
    t, v = map(int, input().split())
    W = max(W-(t-T), 0)

    W += v

    T = t
    # print(W)

print(W)

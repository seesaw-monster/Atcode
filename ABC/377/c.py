# import sys
# sys.setrecursionlimit(10**6)
N, M = map(int, input().split())

s = set()

d = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for k in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    s.add((a, b))
    for x, y in d:
        if a+x >= 0 and a+x < N and b+y >= 0 and b+y < N:
            s.add((a+x, b+y))

print(N*N-len(s))


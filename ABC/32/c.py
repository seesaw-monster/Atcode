# import sys
# sys.setrecursionlimit(10**6)
N, K = map(int, input().split())

x = 1
l = 0
S = []
for i in range(N):
    s = int(input())
    if s == 0:
        l = N
    x *= s
    S.append(s)
    while x>K and S:
        x/=S.pop(0)

    if x<=K and l<len(S):
        # print(S)
        l = len(S)

print(l)

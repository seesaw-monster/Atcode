# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, P = map(int, input().split())

c = 0

def f(w):
    return len(str(w))+1

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for w in range(1, N+1):
    dp[0][f(w)]=26

for i in range(1, N+1):
    for j in range(1, N):
        for w in range(1, i):
            if j-f(w):
                dp[i][j] += dp[i-w][j-f(w)]*25

print(dp)
print(max(dp[-1])%P)

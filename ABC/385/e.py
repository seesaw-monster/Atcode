# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
dp = {}

for i in range(N):
    dp[f'{i+1}'] = set()

for _ in range(N):
    u, v = map(int, input().split())
    dp[f'{u+1}'].add(v)
    dp[f'{v+1}'].add(u)

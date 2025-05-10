# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, M = map(int, input().split())
dp = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    dp[a].append(b)
    dp[b].append(a)

for i in range(N):
    if len(dp[i])!=2:
        print('No')
        exit()

count = [0 for _ in range(N)]
q = deque([0])
while q:
    X = dp[q.popleft()]
    for x in X:
        if count[x]<2:
            count[x]+=1
            q.append(x)

for c in count:
    if c!=2:
        print('No')
        exit()

print('Yes')

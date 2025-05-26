# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N, M = map(int, input().split())
ans = (M*(M-1))//2
cnt = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    cnt[(a+b)%N]+=1

for c in cnt:
    ans -= (c*(c-1))//2

print(ans)

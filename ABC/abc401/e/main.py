# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, M = map(int, input().split())
dp = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1
    dp[u].append(v)
    dp[v].append(u)

answer = -1

d = deque()

l = [0 for _ in range(N-1)]
l[0] = 1
for x in dp[0]:
    d.append((x, l, 1))

while d:
    next_point, count_list, need_count = d.popleft()

    if count_list[next_point]==1:
        if sum(count_list)==len(count_list)+1:
            if answer==-1 or M-need_count<answer:
                answer=M-need_count
        else:
            continue

    count_list[next_point]+=1
    for x in dp[next_point]:
        d.append((x, count_list, need_count+1))

print(answer)

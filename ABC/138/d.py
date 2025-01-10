# import sys
# sys.setrecursionlimit(10**6)
from collections import defaultdict, deque
N, Q = map(int, input().split())
count = [0 for _ in range(N+1)]
flag = [True for _ in range(N+1)]
d = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    count[p]+=x

q = deque([(1, 0)])
while len(q)!=0:
    idx, before_idx = q.popleft()
    if not flag[idx]:
        continue

    for x in d[idx]:
        q.append((x, idx))

    count[idx]+=count[before_idx]
    flag[idx] = False

print(*count[1:])

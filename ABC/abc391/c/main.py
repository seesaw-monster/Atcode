# import sys
# sys.setrecursionlimit(10**6)
from collections import deque, defaultdict
N, Q = map(int, input().split())

bird = [i for i in range(N+1)]
count = [0 for _ in range(N+1)]
count[1] = N
idx = [1 for _ in range(N+1)]

for _ in range(Q):
    query = input().split()
    if len(query)==1:
        print(N-count[0]-count[1])
    else:
        # 鳩P -> 巣H
        p = int(query[1])
        h = int(query[2])

        count[idx[h]]-=1
        count[idx[h]+1]+=1
        count[idx[bird[p]]]-=1
        count[idx[bird[p]]-1]+=1
        idx[h]+=1
        idx[bird[p]]-=1
        bird[p]=h

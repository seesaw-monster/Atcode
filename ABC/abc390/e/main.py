# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
N, X = map(int, input().split())
V1 = []
V2 = []
V3 = []

for _ in range(N):
    v, a, c = map(int, input().split())
    if v==1:
        V1.append([a, c])
    elif v==2:
        V2.append([a, c])
    else:
        V3.append([a, c])

V1.sort(key=lambda x: (x[1], x[0]))
V2.sort(key=lambda x: (x[1], x[0]))
V3.sort(key=lambda x: (x[1], x[0]))

if len(V1)==0 or len(V2)==0 or len(V3)==0:
    print(0)
    exit()

idx_v1 = len(V1)-1
idx_v2 = len(V2)-1
idx_v3 = len(V3)-1

while not (idx_v1==0 and idx_v2==0 and idx_v3==0) and V1[idx_v1][1]+V2[idx_v2][1]+V3[idx_v3][1]>X:
    n_v1 = V1[idx_v1][1] if idx_v1!=0 else -1
    n_v2 = V2[idx_v2][1] if idx_v2!=0 else -1
    n_v3 = V3[idx_v3][1] if idx_v3!=0 else -1

    max_next = max(n_v1, n_v2, n_v3)

    if max_next==n_v1:
        idx_v1-=1
        while idx_v1>0 and V1[idx_v1-1][1]==max_next:
            idx_v1-=1
    elif max_next==n_v2:
        idx_v2-=1
        while idx_v2>0 and V2[idx_v2-1][1]==max_next:
            idx_v2-=1
    else:
        idx_v3-=1
        while idx_v3>0 and V3[idx_v3-1][1]==max_next:
            idx_v3-=1


if V1[idx_v1][1]+V2[idx_v2][1]+V3[idx_v3][1]<=X:
    print(min(V1[idx_v1][0],V2[idx_v2][0],V3[idx_v3][0]))
else:
    print(0)

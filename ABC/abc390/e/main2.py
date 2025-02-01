# import sys
# sys.setrecursionlimit(10**6)
from collections import deque
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

idx_v1 = 0
idx_v2 = 0
idx_v3 = 0

def cal_calorie(idx1, idx2, idx3):
    return V1[idx1][1]+V2[idx2][1]+V3[idx3][1]

if cal_calorie(idx_v1, idx_v2, idx_v3)>X:
    print(0)
    exit()

min_a = min(V1[idx_v1][0], V2[idx_v2][0], V3[idx_v3][0])

d = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
# dp = deque([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
dp = deque(d)
# s = set([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
s = set(d)

while len(dp):
    d1, d2, d3 = dp.popleft()
    next_v1 = idx_v1+d1
    next_v2 = idx_v2+d2
    next_v3 = idx_v3+d3
    if not (next_v1<len(V1) and next_v2<len(V2) and next_v3<len(V3)):
        continue

    if cal_calorie(next_v1, next_v2, next_v3)>X:
        continue
    else:
        min_a = min(min_a, min(V1[next_v1], V2[next_v2], V3[next_v3]))
        for a, b, c in d:
            if not (d1+a, d2+b, d3+c) in s:
                dp.append((d1+a, d2+b, d3+c))

print(min_a)

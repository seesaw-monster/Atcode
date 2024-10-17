def search(i, DP, D, count):
    for dp in DP[i]:
        if D[dp]:
            count[dp] += count[i]+1
            D[dp] = False
            count = search(dp, DP, D, count)

    return count
# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

DP = [[] for _ in range(N)]

key = ''
v = 0
for _ in range(N-1):
    A, B = map(int, input().split())

    DP[A-1].append(B-1)
    DP[B-1].append(A-1)

D = [True for _ in range(N)]
count = [0 for _ in range(N)]

D[0] = False
count = search(0, DP, D, count)
idx = 0
for k in range(1, N):
    if count[idx]<count[k]:
        idx = k

D = [True for _ in range(N)]
count = [0 for _ in range(N)]
D[idx] = False
count = search(idx, DP, D, count)
max_idx = 0
max_value = count[0]
for k in range(1, N):
    if max_value<count[k]:
        max_idx = k
        max_value = count[k]

if max_value > v:
    key = f'{idx+1} {max_idx+1}'
    v = max_value

print(key)

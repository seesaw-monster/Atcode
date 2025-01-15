# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

up_idx = 0
down_idx = 1

flag = [False for _ in range(N)]
count = [set() for _ in range(N)]

while up_idx<N and down_idx<N:
    while A[up_idx]*2>A[down_idx]:
        down_idx+=1
        if down_idx==N:
            break

    if len(count[up_idx])!=0 and down_idx!=N:
        flag[up_idx] = False
        flag[up_idx+1] = True
    if down_idx!=N:
        flag[down_idx] = True
        count[down_idx].add(up_idx)
    up_idx+=1
    down_idx+=1

for i in range(1, N):
    flag[i] = True if flag[i-1] or flag[i] else False
    count[i] = count[i].union(count[i-1])

print(min(sum(flag), len(count[-1])))

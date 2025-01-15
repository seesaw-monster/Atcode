# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

up_idx = 0
down_idx = 1

count = 0
while up_idx<N and down_idx<N:
    while A[up_idx]*2>A[down_idx]:
        down_idx+=1
        if down_idx==N:
            break

    count+=(N-down_idx)
    up_idx+=1

print(count)

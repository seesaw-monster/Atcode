# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

count = [0 for _ in range(N)]

B = []

for i in range(N):
    b = count[i]+A[i]
    B.append(max(b-(N-i-1), 0))

    if b>0 and i<N-1:
        count[i+1]+=count[i]+1

    if b>0 and b<(N-i-1):
        count[i+b+1]-=1

print(*B)

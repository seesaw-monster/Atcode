# import sys
# sys.setrecursionlimit(10**6)
N, S = map(int, input().split())
A = list(map(int, input().split()))

s_A = sum(A)
lS = S%s_A

A.extend(A)

s = 0
r = 0
for l in range(2*N):
    while s<lS and r<2*N:
        # print()
        s+=A[r]
        r+=1

    if s==lS:
        print('Yes')
        exit()

    s-=A[l]

print('No')

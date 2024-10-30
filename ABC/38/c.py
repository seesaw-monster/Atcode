# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

q = []
r = 0
c = 0
for l in range(N):
    if not q:
        q.append(A[l])
        r+=1

    while r < N and q and q[-1] < A[r]:
        q.append(A[r])
        r+=1

    c+=len(q)
    q.pop(0)

print(c)

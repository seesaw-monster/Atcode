# import sys
# sys.setrecursionlimit(10**6)
N, M, X = map(int, input().split())

C = []
A = []

for _ in range(N):
    B = list(map(int, input().split()))
    C.append(B[0])
    A.append(B[1:])

min_cost = -1
for i in range(2**N):
    m = [0 for _ in range(M)]
    cost = 0
    for j in range(N):
        if i >> j & 1:
            cost += C[j]
            for k in range(M):
                m[k]+= A[j][k]

    flag = True
    for x in m:
        if x < X:
            flag = False
            break

    if flag and (min_cost > cost or min_cost == -1):
        min_cost = cost

print(min_cost)


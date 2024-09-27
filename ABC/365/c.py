N, M = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

sum_A = sum(A)

if sum_A <= M:
    print('infinite')
    exit()

for i in range(1, N):
    sum_A -= (A[i-1]-A[i])*(i)

    if sum_A <= M:
        print(A[i])
        break

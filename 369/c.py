import math

N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(1)
    exit()

count = N + (N - 1)

l = 0
diff = A[1]-A[0]
r = 2
while r < N:
    if A[r]-A[r-1] == diff:
        r+=1
    else:
        M = (r-1)-l+1
        for m in range(3, M+1):
            count += (M-m+1)
        diff = A[r]-A[r-1]
        l = r - 1
        r += 1

if r == N:
    M = (r-1)-l+1
    for m in range(3, M+1):
        count += (M-m+1)

print(int(count))


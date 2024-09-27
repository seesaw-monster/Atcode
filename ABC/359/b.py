N = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(1, 2*N-1):
    if A[i-1] == A[i+1]:
        count += 1

print(count)


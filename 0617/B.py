A = list(map(int, input().split()))

s = 0
for i in range(len(A)):
    s+=A[i]*2**i

print(s)


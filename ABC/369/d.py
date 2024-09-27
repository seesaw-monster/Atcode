N = int(input())
A = list(map(int, input().split()))

B = [[A[0], 0]]

for i in range(1, N):
    B.append([max(B[i-1][0], B[i-1][1]+A[i]), max(B[i-1][0]+2*A[i], B[i-1][1])])

print(max(B[-1][0], B[-1][1]))

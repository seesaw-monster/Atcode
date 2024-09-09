N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = []

for i in range(N):
    AB.append((A[i], B[i]))

sum_A = [0, 0, 0]
AB = sorted(AB, key=lambda x: x[0], reverse=True)

for i in range(N):
    sum_A[0] += AB[i][0]
    sum_A[1] += AB[i][1]
    sum_A[2] += 1
    if sum_A[0] > X: 
        break
    elif sum_A[1] > Y:
        break

sum_B = [0, 0, 0]
AB = sorted(AB, key=lambda x: x[1], reverse=True)

for i in range(N):
    sum_B[0] += AB[i][0]
    sum_B[1] += AB[i][1]
    sum_B[2] += 1
    if sum_B[0] > X: 
        break
    elif sum_B[1] > Y:
        break

print(min(sum_A[2], sum_B[2]))

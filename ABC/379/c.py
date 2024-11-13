from decimal import Decimal
def move_cost(d):
    d = Decimal(d)
    return int((d-1)*d/2)

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

B = [[X[i], A[i]] for i in range(len(X))]
B.append([1, 0])
B.append([N, 0])

B.sort(key=lambda x: -x[0])

cost = 0

for i in range(len(B)-1):
    diff = B[i][0]-B[i+1][0]
    if diff == 0:
        B[i+1][1]=B[i][1]
        continue
    cost += move_cost(diff)
    B[i+1][1] -= diff-1
    if B[i][1]<=0:
        cost+=(abs(B[i][1])+1)*diff
        B[i+1][1] -= abs(B[i][1])+1
    elif B[i][1]>1:
        print(-1)
        exit()

print(cost if B[-1][1]>0 else -1)

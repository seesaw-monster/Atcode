N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

Box = [[] for _ in range(N)]

for i in range(N):
    Box[A[i]-1].append(W[i])

cost = 0
for i in range(N):
    if len(Box[i]) > 1:
        Box[i].sort()
        cost += sum(Box[i][:len(Box[i])-1])

print(cost)

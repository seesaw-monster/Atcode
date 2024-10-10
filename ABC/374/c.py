# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
K = list(map(int, input().split()))

AB = [[] for _ in range(N)]

AB[0].append([K[0], 0]) 
AB[0].append([0, K[0]]) 

for i in range(1, N):
    for a, b in AB[i-1]:
        AB[i].append([a+K[i], b])
        AB[i].append([a, b+K[i]])

MAB = AB[-1]

for i in range(len(MAB)):
    MAB[i] = max(MAB[i])

print(min(MAB))

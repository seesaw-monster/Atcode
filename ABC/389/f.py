# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

# LR = []
count = [0 for _ in range(5*10**5+1)]
for _ in range(N):
    l, r = map(int, input().split())
    # LR.append((l, r))
    count[l]+=1
    count[r+1]-=1

for i in range(1, len(count)):
    count[i]+=count[i-1]

Q = int(input())
for _ in range(Q):
    x = int(input())

print(count[:11])

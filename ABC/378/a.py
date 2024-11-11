# import sys
# sys.setrecursionlimit(10**6)
C = [0 for _ in range(6)]
# [0, 0, 0, 0, 0, 0]
A = list(map(int, input().split()))

for a in A:
    C[a] += 1

count = 0
for c in C:
    count += c//2

print(count)

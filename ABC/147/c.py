# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
xy = [[] for _ in range(N)]
for i in range(N):
    A = int(input())
    for _ in range(A):
        x, y = map(int, input().split())
        xy[i].append([x, y])

max_count = 0
for i in range(2**N):
    flag = True
    for j in range(N):
        if ((i >> j) & 1):
            for x, y in xy[j]:
                if not ((i >> (x-1) & 1) == y):
                    flag = False
                    break
        if not flag:
            break

    if flag:
        if max_count < bin(i).count('1'):
            max_count = bin(i).count('1')

print(max_count)

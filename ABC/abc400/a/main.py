# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict

A = int(input())

for b in range(1, 401):
    if A*b==400:
        print(b)
        exit()

print(-1)

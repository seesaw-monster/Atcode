# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict

n, m = map(int, input().split())

threshold = 10**9

s = 0

for i in range(m+1):
    s += n**i

    if s > threshold:
        print('inf')
        exit()

print(s)

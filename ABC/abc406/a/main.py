# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
a, b, c, d = map(int, input().split())

if a > c:
    print('Yes')
    exit()
elif a == c and b > d:
    print('Yes')
    exit()

print('No')

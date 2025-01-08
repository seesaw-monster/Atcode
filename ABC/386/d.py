# import sys
# sys.setrecursionlimit(10**6)
from collections import defaultdict
N, M = map(int, input().split())

XYx = []
XYy = []
# XY = []
for _ in range(M):
    x, y, c = input().split()
    x, y = int(x), int(y)

    XYx.append((x, y, c))
    XYy.append((x, y, c))

XYx.sort(key=lambda x: (x[0], x[1]))
XYy.sort(key=lambda x: (x[1], x[0]))

min_x = float('inf')
for x, y, c in XYy:
    if c == 'B':
        if x >= min_x:
            print('No')
            exit()
    elif c == 'W':
        min_x = min(x, min_x)

min_y = float('inf')
for x, y, c in XYx:
    if c=='B':
        if y >= min_y:
            print('No')
            exit()
    elif c=='W':
        min_y = min(y, min_y)

print('Yes')

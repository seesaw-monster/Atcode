# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
D = input()

d = {"N": 'S', 'E': 'W', 'W': 'E', 'S': 'N', 'NE': 'SW', 'SW': 'NE', 'NW': 'SE', 'SE': 'NW'}

print(d[D])

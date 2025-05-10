# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
S = input()

for i in range(97, 123):
    if not chr(i) in S:
        print(chr(i))
        exit()

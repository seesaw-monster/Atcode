# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
N = int(input())
c = 0
login = False

for _ in range(N):
    S = input()

    if S=='login':
        login=True
    elif S=='logout':
        login=False

    if S=='private' and not login:
        c+=1

print(c)

# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
T = input()
U = input()

for i in range(len(T)-len(U)+1):
    is_S = True
    for j in range(len(U)):
        if T[i+j]==U[j] or T[i+j]=='?':
            continue
        else:
            is_S = False
            break

    if is_S:
        print('Yes')
        exit()

print('No')

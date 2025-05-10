# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque, defaultdict
Q = int(input())

X = [[] for _ in range(5*10**5+1)]
Y = set()

for _ in range(Q):
    t, s = input().split()

    if t=='1':
        X[len(s)].append(s)
    else:
        Y.add(s)

    if len(Y)==0:
        print(0)
        continue

    remove_list = []
    for y in Y:
        flag = True
        for i in range(1, len(y)+1):
            if not flag:
                break

            for j in range(len(X[i])):
                if X[i][j] == y[:len(X[i][j])]:
                    remove_list.append(y)
                    flag = False
                    break

    for y in remove_list:
        Y.remove(y)

    print(len(Y))

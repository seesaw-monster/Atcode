# import sys
# sys.setrecursionlimit(10**6)
# from collections import deque
H, W = map(int, input().split())

S = []

for _ in range(H):
    S.append(list(input()))

# # = 黒, . = white, ? = none

min_i, max_i = 10000, -1
min_j, max_j = 10000, -1
count = 0
flag = False

for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            count+=1
            if min_i>i:
                min_i = i

            if max_i<i:
                max_i = i

            if min_j>j:
                min_j = j

            if max_j<j:
                max_j = j
        elif S[i][j]=='?':
            flag=True

if count:
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if S[i][j]=='.':
                print('No')
                exit()
elif not flag:
    print('No')
    exit()

print('Yes')

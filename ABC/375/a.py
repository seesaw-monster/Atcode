# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
S = input()
# # = 座ってる
count = 0

for i in range(N-2):
    if S[i] == '#' and S[i+1] == '.' and S[i+2] == '#':
        count += 1

print(count)
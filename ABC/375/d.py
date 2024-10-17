# import sys
# sys.setrecursionlimit(10**6)
S = input()

Alph = [[] for _ in range(ord('Z')-ord('A')+1)]
unit = [0 for _ in range(ord('Z')-ord('A')+1)]
count = 0

for k in range(2, len(S)):
    Alph[ord(S[k-2])-ord('A')].append(k-2)

    for i in range(ord('Z')-ord('A')+1):
        unit[i] += len(Alph[i])

    count += unit[ord(S[k])-ord('A')]

print(count)

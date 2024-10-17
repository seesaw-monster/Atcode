# import sys
# sys.setrecursionlimit(10**6)
S = input()

s = 0
for i in range(2**(len(S)-1)):
    idx = 0
    for j in range(len(S)-1):
        if (i >> j & 1):
            s += int(S[idx:j+1])
            idx = j+1
    s+=int(S[idx:])

print(s)


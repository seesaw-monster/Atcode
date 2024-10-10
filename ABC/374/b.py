# import sys
# sys.setrecursionlimit(10**6)
S = input()
T = input()

if S==T:
    print(0)
else:
    i = 0
    while i<len(S) and i<len(T):
        if S[i]!=T[i]:
            break
        i+=1

    print(i+1)

# import sys
# sys.setrecursionlimit(10**6)
K = int(input())
S = input()
T = input()

if S==T:
    print('Yes')
    exit()

diff = len(S)-len(T)
if diff==0:
    c = 0
    for i in range(len(S)):
        if S[i]!=T[i]:
            c+=1

    if c==1:
        print('Yes')
        exit()
elif diff==1:
    l, r = 0, 0
    c = 0
    while l<len(S) and r<len(T) and c<=1:
        if S[l]==T[r]:
            l+=1
            r+=1
        else:
            l+=1
            c+=1

    if c<=1:
        print('Yes')
        exit()

elif diff==-1:
    l, r = 0, 0
    c = 0
    while l<len(S) and r<len(T) and c<=1:
        if S[l]==T[r]:
            l+=1
            r+=1
        else:
            r+=1
            c+=1

    if c<=1:
        print('Yes')
        exit()

print('No')

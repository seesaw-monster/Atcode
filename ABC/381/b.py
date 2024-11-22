# import sys
# sys.setrecursionlimit(10**6)
S = input()
Alph = [0 for _ in range(ord('z')-ord('a')+1)]

def is_T(S, N):
    if not N%2==0:
        return False

    for i in range(N//2-1):
        if not S[2*i-2]==S[2*i-1]:
            return False

    for i in range(N):
        Alph[ord(S[i])-ord('a')]+=1

    for a in Alph:
        if not (a==2 or a==0):
            return False

    return True

print('Yes' if is_T(S, len(S)) else 'No')

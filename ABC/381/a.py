# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
S = input()

def is_T(S, N):
    if not N%2!=0:
        return False

    for i in range((N+1)//2-1):
        if not S[i]=='1':
            return False

    if not S[(N+1)//2-1]=='/':
        return False

    for i in range((N+1)//2, N):
        if not S[i]=='2':
            return False

    return True

print('Yes' if is_T(S, N) else 'No')

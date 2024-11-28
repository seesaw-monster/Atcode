# import sys
# sys.setrecursionlimit(10**6)
N, M, P = map(int, input().split())

def cal(N, M, P):
    if M==0:
        return 1
    elif M%2==0:
        return cal(N, M/2, P)**2%P
    else:
        return cal(N, M-1, P)*N%P

print(cal(N, P, M))

# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

B = [True for _ in range(10**6+1)]
C = [[] for _ in range(10**6+1)]

C[0].append(0)
C[1].append(1)

for n in range(2, 10**6+1):
    if not B[n]:
        continue

    C[n].append(n)

    for i in range(2*n, 10**6+1, n):
        B[i] = False
        C[n].append(n)

def judge(A):
    count = [0 for _ in range(10**6+1)]

    for i in range(len(A)):
        for n in C[i]:
            count[n]+=1

    return True if len(A) in count else False

GCD_N = True if judge(A) else False

for i in range(len(A)-1):
    gcd = judge([A[i], A[i+1]])
    if gcd:
        print('pairwise coprime')
    elif GCD_N:
        print('setwise coprime')
    else:
        print('not coprime')

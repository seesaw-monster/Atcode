N, Q = map(int, input().split())
S = list(input())
C = [True if S[i:i+3]==['A', 'B', 'C'] else False for i in range(N-2)]

for _ in range(Q):
    x, c = map(str, input().split())
    x = int(x)

    before_s = S[x-1]
    S[x-1] = c

    if x-1 <= N-3:
        C[x-1] = False
    if x-1 >= 1 and x-1 <= N-2:
        C[x-2] = False
    if x-1 >= 2:
        C[x-3] = False

    if c == 'A' and x-1 <= N-3:
        if S[x-1:x+2]==['A', 'B', 'C']:
            C[x-1] = True
    elif c == 'B' and x-1 >= 1 and x-1 <= N-2 :
        if S[x-2:x+1]==['A', 'B', 'C']:
            C[x-2] = True
    elif c == 'C' and x-1 >= 2:
        if S[x-3:x]==['A', 'B', 'C']:
            C[x-3] = True

    print(sum(C))

N, Q = map(int, input().split())
S = list(input())
C = [True if S[i:i+3]==['A', 'B', 'C'] else False for i in range(N-2)]

ans = sum(C)

for _ in range(Q):
    x, c = map(str, input().split())
    x = int(x) - 1

    for i in range(-2, 1):
        if 0 <= x+i and x+i < N-2:
            if S[x+i:x+i+3]==['A', 'B', 'C']:
                ans -= 1

    S[x] = c
    for i in range(-2, 1):
        if 0 <= x+i and x+i < N-2:
            if S[x+i:x+i+3]==['A', 'B', 'C']:
                ans += 1

    print(ans)

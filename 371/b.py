N, M = map(int, input().split())

AB = [[] for i in range(N)]

for _ in range(M):
    a, b = map(str, input().split())
    a = int(a)

    if not 'M' in AB[a-1] and b=='M':
        print('Yes')
    else:
        print('No')

    AB[a-1].append(b)

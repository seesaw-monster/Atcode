from decimal import Decimal

N = int(input())
AB = []

for i in range(N):
    a, b = map(Decimal, input().split())
    AB.append([i+1, a/(a+b)])

AB.sort(key=lambda x: (-x[1], x[0]))

ans = [x[0] for x in AB]
print(*ans)

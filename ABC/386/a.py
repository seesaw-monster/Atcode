# import sys
# sys.setrecursionlimit(10**6)
a, b, c, d = map(int, input().split())

for i in range(1, 14):
    card = [a, b, c, d, i]
    card.sort()

    if card[0]==card[2] and card[2]!=card[3] and card[3]==card[4]:
        print('Yes')
        exit()
    if card[0]==card[1] and card[1]!=card[3] and card[2]==card[4]:
        print('Yes')
        exit()

print('No')

s_x, s_y = map(int, input().split())
t_x, t_y = map(int, input().split())

price = 0

price += abs(t_y - s_y)

def cal(a, b, j):
    if j%2 == 0:
        c = (b//2) - (a//2)
    else:
        c = (b-1)//2 - (a-1)//2

    return c

if abs(t_y - s_y) == 0:
    if s_x < t_x:
        price += cal(s_x, t_x, s_y)
    else:
        price += cal(t_x, s_x, t_y)
else:
    if abs(t_y - s_y)+1 <= abs(t_x - s_x):
        if s_x < t_x:
            price += cal(s_x + abs(t_y-s_y), t_x, t_y)
        else:
            price += cal(t_x, s_x - abs(t_y-s_y), t_y)

print(price)

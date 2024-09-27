s_x, s_y = map(int, input().split())
t_x, t_y = map(int, input().split())

if (s_x+s_y)%2 != 0:
    s_x -= 1

if (t_x + t_y) % 2 != 0:
    t_x -= 1

t_x = abs(t_x - s_x)
t_y = abs(t_y - s_y)


print(t_y + max(0, t_x-t_y)//2)

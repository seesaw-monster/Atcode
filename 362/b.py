x_a, y_a = map(int, input().split())
x_b, y_b = map(int, input().split())
x_c, y_c = map(int, input().split())

ab = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5
bc = ((x_b - x_c) ** 2 + (y_b - y_c) ** 2) ** 0.5
ca = ((x_c - x_a) ** 2 + (y_c - y_a) ** 2) ** 0.5

if max(ab, bc, ca) == ab:
    if ab == (bc**2 + ca**2)**0.5:
        print('Yes')
    else:
        print('No')
elif max(ab, bc, ca) == bc:
    if bc == (ab**2 + ca**2)**0.5:
        print('Yes')
    else:
        print('No')
else:
    if ca == (bc**2 + ab**2)**0.5:
        print('Yes')
    else:
        print('No')

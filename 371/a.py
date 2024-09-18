s_ab, s_ac, s_bc = map(str, input().split())

s = []
if s_ab == '<':
    # A B
    if s_ac == '>':
        print('A')
    elif s_bc == '<':
        print('B')
    else:
        print('C')
else:
    # B A
    if s_bc == '>':
        print('B')
    elif s_ac == '<':
        print('A')
    else:
        print('C')

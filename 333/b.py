ss = input()
s1 = ss[0]
s2 = ss[1]
P = ['A', 'B', 'C', 'D', 'E']
tt = input()
t1 = tt[0]
t2 = tt[1]

def judge(a, b):
    a_number = 0
    b_number = 0
    for i in range(len(P)):
        if a==P[i]:
            a_number=i
        if b==P[i]:
            b_number=i

    if (a_number+1)%5 == b_number or (a_number+4)%5 == b_number:
        return True

    return False

if judge(s1, s2)==judge(t1, t2):
    print('Yes')
else:
    print('No')

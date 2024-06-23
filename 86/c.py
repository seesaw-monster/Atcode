def main():
    """
    start: (0, 0)
    t_i: (x_i, y_i)
    s.t. 1<=i<=N
    """
    N = int(input())
    before_xy = [0, 0, 0]
    for i in range(N):
        t, x, y = map(int, input().split())

        if (t-before_xy[0])%2==(abs(x-before_xy[1])+abs(y-before_xy[2]))%2:
            if t-before_xy[0]>=abs(x-before_xy[1])+abs(y-before_xy[2]):
                before_xy = [t, x, y]
                continue
            else:
                print('No')
                return
        else:
            print('No')
            return

    print('Yes')

main()

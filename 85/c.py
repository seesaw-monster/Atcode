def main():
    """
    10k, 5k, 1k
    x, y, z

    N枚, Y円

    x+y+z=N
    10x+5y+z=Y
    """

    N, Y = map(str, input().split())
    N = int(N)
    Y = int(Y[:-3])
    x=-1; y=-1; z=-1

    for i in range(N+1):
        for j in range(N+1-i):
            k = N-i-j
            if i*10+j*5+k==Y:
                print(i, j, k)
                return

    print(x, y, z)

main()

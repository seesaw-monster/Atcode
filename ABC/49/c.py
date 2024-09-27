def main():
    """
    S = T
    T <- dream, dreamer, erase, eraser
    """

    S = input()
    T = ['dream', 'dreamer', 'erase', 'eraser']

    while True:
        c = False
        for t in T:
            if S[-len(t):]==t:
                S = S[:-len(t)]
                c = True
                break

        if not c:
            break

    if len(S)==0:
        print('YES')
    else:
        print('NO')

main()

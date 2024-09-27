def main():
    N = int(input())
    N-=1

    l = [256, 64, 16, 4, 1]
    num = ''
    for y in l:
        num+=f'{N//y}'
        N=N%y

    while True:
        c = 0
        if num[c]=='0' and len(num)>=2:
            num=num[c+1:]
        elif num[c]=='0':
            num = ''
            break
        else:
            break

    print(num+'3')

if __name__=='__main__':
    main()

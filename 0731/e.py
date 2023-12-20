import sys
import math

def main(lines):
    N=int(lines[0])
    C=list(map(int,lines[1].split()))
    C=sorted(C)

    s=0
    value=set()
    c=0
    for i in range(N):
        value.add(C[i])
        if len(C[i+1:])>=2:
            s+=math.factorial(len(C[i+1:]))
        else:
            break

    print((math.factorial(len(C))-s)%100003)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

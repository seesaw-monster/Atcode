import sys

def main(lines):
    N=int(lines[0])
    A=list(map(int,lines[1].split()))

    s=set()
    for i in range(N):
        s.add(A[i])
        if len(s)!=i+1:
            return i+1

    return -1

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    print(main(lines))

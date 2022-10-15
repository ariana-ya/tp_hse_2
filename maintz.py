from functions import _min, _max, _sum, _mult

def main():
    a = open(input(), 'r')
    c = a.readline().split(' ')
    f = []
    for i in c:
        f.append(int(i))
    a.close()

    print(_min(f))
    print(_max(f))
    print(_sum(f))
    print(_mult(f))

main()

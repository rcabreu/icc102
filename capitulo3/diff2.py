import sys

def diff2(n):
    return n % 10 == 0 or (n + 1) % 10 == 0 \
           or (n + 2) % 10 == 10 or (n - 1) % 10 == 0 \
           or (n - 2) % 10 == 10

def main():
    n = int(sys.stdin.readline())
    print('la distancia a un multiplo de 10 no es mas que 2?: ' + str(diff2(n)))

if __name__ == '__main__':
    main()
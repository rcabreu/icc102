import sys

def fib(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        contador = 3
        while contador <= n:
            c = a + b
            a = b
            b = c
            contador += 1
        return b



def main():
    n = int(sys.stdin.readline())
    print('N-esimo termino: ' + str(fib(n)))

if __name__ == '__main__':
    main()
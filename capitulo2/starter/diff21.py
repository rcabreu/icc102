import sys

# Dado un entero n, retorna la diferencia absoluta entre y 21. Sin embargo, retorna el doble de la diferencia absoluta si n es mayor a 21.
def diff21(n):
    return 0


def main():
    n = int(sys.stdin.readline())

    ans = diff21(n)

    print(ans)

# llamar al punto de inicio del programa
if __name__ == '__main__':
    main()
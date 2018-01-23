import sys
from distutils import util

# Tenemos dos monos, a y b, y los parámetros a_smile y b_smile indican, respectivamente, si los monos están sonriendo.
# Estamos en problemas si ambos están sonriendo o si ninguno lo está. Retorna True si estamos en problemas.
def monkey_trouble(a_smile, b_smile):
    return False


def main():
    a_smile, b_smile = map(bool, map(util.strtobool, sys.stdin.readline().split()))

    ans = monkey_trouble(a_smile, b_smile)

    print(ans)

# llamar al punto de inicio del programa
if __name__ == '__main__':
    main()
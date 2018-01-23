import sys

# Dados dos números enteros, retorna su suma. Ahora, si ambos números tienen el mismo valor, entonces retorna
# 
# el doble de la suma.
def sum_double(a, b):
    return 0


def main():
    a, b = map(int, sys.stdin.readline().split())

    ans = sum_double(a, b)

    print(ans)

# llamar al punto de inicio del programa
if __name__ == '__main__':
    main()
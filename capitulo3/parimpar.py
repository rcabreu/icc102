import sys

def parimpar(lista):
    contador = 0
    tamano = len(lista)
    i = 0
    while i < tamano:
        if lista[i] % 2 == 0:
            contador += 1
        i += 1
    print('Pares: ' + str(contador))
    print('Impares: ' + str(tamano - contador))
 
def main():
    lista = list(map(int, sys.stdin.readline().split()))
    parimpar(lista)
 
if __name__ == '__main__':
    main()

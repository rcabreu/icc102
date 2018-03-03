import sys

# implementa aqui la solucion
# esta funcion debe devolver
# la respuesta como un numero decimal
def solucion(x1, y1, x2, y2):
    return 'solucion aun no implementada'

def main():
    x1, y1, x2, y2 = map(float, sys.stdin.readline().split())
    respuesta = solucion(x1, y1, x2, y2)
    print(respuesta) #aqui debes imprimir redondeando a 4 decimales

main()

import sys

# implementa aqui la solucion
# los parametros de esta funcion son:
# tipo_conversion: entero con dos posibles valores:
#     0: debe convertirse de Morse a texto
#     1: debe convertirse de texto a Morse
# cadena: la cadena a convertir a la otra representacion
def solucion(tipo_conversion, cadena):
    return 'solucion no implementada'

def main():
    tipo_conversion = int(input())
    cadena = input()
    respuesta = solucion(tipo_conversion, cadena)
    print(respuesta)
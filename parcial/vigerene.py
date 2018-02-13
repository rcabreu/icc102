import sys

ALFA = 'abcdefghijklmnopqrstuvwxyz'
def encriptar(msg, llave):
  res = ''
  i = 0
  j = 0
  while i < len(msg):
    chM = msg[i]
    chL = llave[j]
    idx = int(ALFA.index(chM))
    idx += int(ALFA.index(chL))
    res += ALFA[idx % 26]
    i += 1
    j += 1
    if j == len(llave):
      j = 0
  return res

def desencriptar(cifrado, llave):
  return 'todavia no implementado'

def main():
  llave = 'aosksow'
  print('digita la cadena que quieres encriptar')
  mensaje = input()
  cifrado = encriptar(mensaje, llave)
  print('resultado: ' + cifrado)
  print('mensaje original: ' + desencriptar(cifrado, llave))
  
main()

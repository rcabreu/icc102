import sys

# primera manera (utilizando while)
def bin2dec(numStr):
    sum = 0
    pot = len(numStr) - 1
    i = 0
    while i < len(numStr):
        if numStr[i] == '1':
            sum += 2 ** pot
        i += 1
        pot -= 1
    return sum
 # segunda manera (con for)
def bin2decver2(numStr):
    sum = 0
    pot = len(numStr) - 1
    for i in range(len(numStr)):
        if numStr[i] == '1':
            sum += 2 ** pot
        pot -= 1
    return sum
# tercera manera (for mejorado)
def bin2decver3(numStr):
    sum = 0
    n = len(numStr)
    for i in range(n):
        if numStr[i] == '1':
            sum += 2 ** (n - i - 1)
    return sum

#version 4 (usando libreria de Python)
def bin2decver4(numStr):
    return int(numStr, 2)

def main():
    numStr = input("digita el numero en binario ")
    numDec = bin2decver4(numStr)
    print("el resultado es: " + str(numDec))


if __name__ == '__main__':
    main()

# version 1 (usando reversed)
def dec2bin(num):
    cadBin = ''
    while num > 0:
        if num % 2 == 0:
            cadBin = '0' + cadBin
        else:
            cadBin = '1' + cadBin
        num //= 2
    return cadBin

# version 2 (a traves de la potencia de 2)
def dec2binver2(num):
    pot = 1
    while pot <= num:
        pot *= 2
    pot //= 2
    cadBin = ''
    while pot > 0:
        if pot <= num:
            cadBin += '1'
            num -= pot
        else:
            cadBin += '0'
        pot //= 2
    return cadBin

def main():
    num = int(input("digita el numero en decimal: "))
    numBin = dec2binver2(num)
    print("el resultado es: " + numBin)


if __name__ == '__main__':
    main()
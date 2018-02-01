import sys

def adivina_numero(a, b, x):
    pasos = 0
    while a <= b:
        pasos += 1
        pm = (a + b) // 2
        if pm == x:
            return pasos
        elif pm > x:
            b = pm - 1
        else:
            a = pm + 1
    return pasos


def main():
    a, b, x = map(int, sys.stdin.readline().split())
    print(str(adivina_numero(a, b, x)))

if __name__ == '__main__':
    main()
import sys

def num6(a, b):
    if a== 6 or b == 6:
        return True
    elif abs(a-b)==6:
        return True
    elif a+b==6:
        return True
    else:
        return False




def main():
    a, b = map(int, sys.stdin.readline().split())
    print(str(num6(a, b)))

if __name__ == '__main__':
    main()
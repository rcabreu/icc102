import sys
from distutils import util

# El parámetro weekday es True si es un día de semana, y el parámetro vacation es True si estamos en vacaciones.
# Dormimos en casa si no es un día de semana o si estamos en vacaciones. Determina si dormimos en casa.
def sleep_in(weekday, vacation):
    ans = True
    return ans


def main():
    weekday, vacation = map(util.strtobool, sys.stdin.readline().rstrip('\n').split(' '))

    ans = sleep_in(weekday, vacation)

    print(ans)

# llamar al punto de inicio del programa
if __name__ == '__main__':
    main()
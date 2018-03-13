def bubble_sort(lista):
    n = len(lista)
    while True:
        i = 0
        hubo_cambio = False
        while i <= n - 2:
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                hubo_cambio = True
            i += 1
        if hubo_cambio == False:
            break

    return lista

def main():
    lista = list(map(int, input().split()))
    lista_ord = bubble_sort(lista)
    print(lista_ord)

main()

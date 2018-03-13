def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i - 1
        elem = lista[i]
        while j >= 0:
            if elem < lista[j]:
                lista[j+1] = lista[j]
                lista[j] = elem
                j -= 1
            else: break

    return lista

def main():
    lista = list(map(int, input().split()))
    lista_ord = insertion_sort(lista)
    print(lista_ord)

main()

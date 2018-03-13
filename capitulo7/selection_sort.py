
def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        temp = lista[i]
        lista[i] = lista[min_idx]
        lista[min_idx] = temp

    return lista

def main():
    lista = list(map(int, input().split()))
    lista_ord = selection_sort(lista)
    print(lista_ord)

main()

def string_splosion(str):
    cad = ''
    n = len(str)
    i = 0
    j = 0
    while i < n:
        j = 0
        while j <= i:
            cad += str[j]
            j += 1
        i += 1
    return cad

def string_splosion(str):
    cad = ''
    n = len(str)
    for i in range(n):
        for j in range(i+1):
            cad += str[j]
    return cad



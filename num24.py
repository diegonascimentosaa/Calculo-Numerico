def bubble_sort(lista):
    for j in range (len(lista) - 1):
        for i in range (len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
l = ['F','O','R','A','O','R','D','E','M']
print(bubble_sort(l))
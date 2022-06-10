l1 = []
l2 = []
l3 = []
for cont in range (10):
    x = int(input('Digite um valor para a lista 1: \n'))
    y = int(input('Digite um valor para a lista 2: \n'))
    l1.insert(cont,x)
    l2.insert(cont,y)
for cont in range (10):
    x = l1[cont]
    y = l2[cont]
    soma = x + y
    l3.insert(cont,soma)
    print('A soma de:',l1[cont],'+',l2[cont],'= ',l3[cont])
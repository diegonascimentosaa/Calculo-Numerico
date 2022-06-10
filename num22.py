import random
l1 = []
l2 = []
for cont in range(100):
    l1.append(random.randint(1, 10))
print('Lista Original')
print(l1)
print('____________________________________________\n')
l1.sort()
print('Lista Ordenada')
print(l1)
print('____________________________________________\n')
rep = 0
for cont in range(99):
    if l1[cont]==l1[cont+1]:
        rep += 1
        if cont == 98:
            l2.append(rep+1)
    else:
        l2.append(rep+1)
        rep=0
print('Lista 2')
print(l2)
print('____________________________________________\n')
for cont in range(9):
    print('O numero ',cont+1,', se repete: ',l2[cont],' vezes')
l = []
l1 = []
n = int(input('Digite o tamamnho da lista: '))
for cont in range(n):
    x = int(input('Digite um numero: '))
    l.append(x)
for cont in l:
    if cont not in l1:
        l1.append(cont)
    l1.sort()
print(l1)
a = int(2)
b = int(3)
l = [40,5,4,10,104,2,23,65,78,974]
x = l[a]+l[b]

print('A) O resultado da formula X[A + 1], é', l[a+1],'\n')
print('B) O resultado da formula X[A * 1], é', l[a*2],'\n')
print('C) O resultado da formula X[A + B], é', l[a+b],'\n')
print('D) O resultado da formula X[A * B], é', l[a+b],'\n')
print('E) O resultado da formula X[A]+X[B], é', l[a]+l[b],'\n')
print('F) O resultado da formula X[X[A] + B], é', l[l[a]+b],'\n')
print('G) O resultado da formula X[X[X[A + B]]], é', l[l[l[a+b]]],'\n')
print('H) O resultado da formula X[X[A] ∗ 2], é', l[l[a]*2],'\n')
print('I) O resultado da formula X[X[A] + X[B]], esta fora do escopo da lista, a posição é: ', x)
    
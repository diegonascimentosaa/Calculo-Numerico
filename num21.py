import random
l = list(range(1,101))
random.shuffle(l)
n = int(input('Quantos numeros de 1 a 100 voce deseja sortear?\n'))
for cont in range(n):
    print('O ',cont+1,'ª numero sorteado é: ', l[cont])
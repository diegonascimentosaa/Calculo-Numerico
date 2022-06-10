vel = []
dis = []
mult = []
med = []
ds = 0
nm = float(0)
x = 0
trec = int(input('Digite o numero de trechos: '))
for cont in range(trec):
    d = int(input('\nDigite quantos metros tem o trecho: \n'))
    dis.append(d)
    v = int(input('\nDigite a velocidade nesse trecho: \n'))
    vel.append(v)
    ds = ds + d
for cont in range(trec):
    n = dis[cont]*vel[cont]
    x = x + n
nm = x / ds
print('A valocidade media é: ',nm,'\n')
for cont in range (trec):
    if nm < vel[cont]:
        print('O trecho ',cont+1,' teve a velocidade em cima da media')

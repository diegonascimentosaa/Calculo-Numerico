maior = int(0)
resp = 'S'
while resp == 'S':
    num = int(input('\nDigite um numero: '))
    if num>maior:
        maior=num
    resp = str(input('Quer continuar? [S/N] ')).upper()
print('\nO maior número é: ',maior)

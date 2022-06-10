resp = 'S'
while resp == 'S':
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero": '))
    op = str(input('Digite a operação desejada: (/ * + -): '))
    if op == '*':
        print('O resultado da multiplicação é: ', n1*n2)
    elif op == '+':
        print('O resultado da soma é: ', n1+n2)
    elif op == '-':
        print('O resultado da subtração é: ', n1-n2)
    elif op == '/':
        if n2 != 0:
            print('O resultado da divisão é: ', n1/n2)
        elif n2 == 0:
            print('Impossivel dividir por 0, tente novamente com outro numero: ')
    elif op != '+' and op != '-' and op != '/' and op != '*':
        print('Operação invalida')
    resp = str(input('\nQuer continuar? [S/N] ')).upper()


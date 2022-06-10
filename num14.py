num1 = int(input('O primeiro numero deve ser o maior, digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
rest = int
n1 = num1
n2 = num2
while rest != 0:
    rest = n1 % n2
    n1 = n2
    n2 = rest
print('O mdc de:',num1,' e ', num2, ' é:', n1)

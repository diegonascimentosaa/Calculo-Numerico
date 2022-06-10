a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = float((b ** 2) - 4 * a * c)
if a == 0:
    print('Nào é uma equação do segundo grau! ')
if delta < 0:
    print('A equação não possui raizes! ')
elif delta == 0:
    print('A equação possui apenas uma raiz')
    print('A raiz é: ',(-b)/(2*a))
else:
    print('A primeira raiz é: ', (-b - (delta ** 0.5))/(2*a))
    print('A segunda raiz é: ', (-b + (delta ** 0.5))/(2*a))
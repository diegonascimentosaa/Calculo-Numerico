num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))
num3 = float(input('Digite outro numero: '))
if((num1>num2) and (num1>=num3)):
    print(num1, 'É o maior numero: ')
elif((num2>num3) and (num2>=num1)):
    print(num2, 'É o maior numero: ')
elif((num3>num2) and (num3>=num1)):
    print(num3, 'É o maior numero: ')

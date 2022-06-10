opc = str(input('Digite C para converter Fahrenheit para Celsius, ou digite F, para converter Fahrenheit para Celsius: ')).upper()
if(opc=='C'):
    f = float(input('Digite garus Fahrenheit: '))
    x = float((5/9)*(f-32))
    print('A temperatura em Celsius é: ', x)
elif(opc=='F'):
    c = float(input('Digite graus Celsius: '))
    y = float(((9/5)*c)+32)
    print('A temperatura em Fahrenheit é: ', y)
else:
    print('Opção invalida')


numint = 0
numfloat = 0.0
class input_int():
    while True:
        try:
            global numint 
            numint = int(input('Digite um numero inteiro: '))
            break
        except:
            print('Número inválido! Tente novamente.')
class input_float():
    while True:
        try:
            global numfloat
            numfloat = float(input('Digite um numero flutuante: '))
            break
        except:
            print('Número inválido! Tente novamente.')
input_int()
input_float()
print(numint)
print(numfloat)
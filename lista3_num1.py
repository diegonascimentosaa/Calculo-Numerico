def ConvDec(number, base):
    if((base>0 and base<=10) or base==16):
        result = 0.0
        index = -1 
        for i in number:
            if(i != '.'):
                index += 1 
            else:
                break
        for i in number:
            if(i != '.'):
                if(i == 'A'):
                    result += 10*base**index
                    index -= 1
                elif(i == 'B'):
                    result += 11*base**index
                    index -= 1
                elif(i == 'C'):
                    result += 12*base**index
                    index -= 1
                elif(i == 'D'):
                    result += 13*base**index
                    index -= 1
                elif(i == 'E'):
                    result += 14*base**index
                    index -= 1
                elif(i == 'F'):
                    result += 15*base**index
                    index -= 1
                else:
                    result += int(i)*base**index
                    index -= 1
        return result
    else:
        print('Por favor, insira um número válido para a base (1 até 10 ou 16).')
def ConvBas(number, base, precision):
    if((base>0 and base<=10) or base==16):
        intg = int(number) # Parte inteira
        fract = number - intg 
        result = "" 
        while(intg): 
            rem = intg % base
            if(rem<10):
                result += str(rem) # Converte o resto da divisão pela base para string e concatena ao array
            else: # Caso seja uma conversão para hexadecimal, é necessário substituir os algarismos maiores que 10 por letras
                if(rem==10):
                    result += 'A'
                elif(rem==11):
                    result += 'B'
                elif(rem==12):
                    result += 'C'
                elif(rem==13):
                    result += 'D'
                elif(rem==14):
                    result += 'E'
                elif(rem==15):
                    result += 'F'
            intg //= base
        result = result[ : : -1]
        result += '.' 
        while(precision):
            fract *= base 
            fract_num = int(fract)
            fract -= fract_num
            if(fract_num<10):
                result += str(fract_num) 
            else: 
                if(fract_num==10):
                    result += 'A'
                elif(fract_num==11):
                    result += 'B'
                elif(fract_num==12):
                    result += 'C'
                elif(fract_num==13):
                    result += 'D'
                elif(fract_num==14):
                    result += 'E'
                elif(fract_num==15):
                    result += 'F'
            precision -= 1
        return result
print('a) 425.135 da base 8 para base 10',ConvDec('425.135', 8))
print('1001101.1101 da base 2 para base 10',ConvDec('1001101.1101', 2))
print('12FA7.4C8 da base 16 para base 10',ConvDec('12FA7.4C8', 16))
print('b) 126.485 da base 10 para base 2',ConvBas(126.485, 2, 8))
print('126.485 da base 10 para base 4',ConvBas(126.485, 4, 8))
print('126.485 da base 10 para base 8',ConvBas(126.485, 8, 8))
print('126.485 da base 10 para 16',ConvBas(126.485, 16, 8))
var = ConvDec('1010010.011',2)
print('c) 1010010.011 da base 2 para base 4, 8, 10, 16: ', ConvBas(var, 4, 8) , ' , ', ConvBas(var, 8, 8), ' , ', var, ConvBas(var, 16, 8)) 
from date28 import ano_bissexto, dias_mes, mes
a = int(input('Digite o ano, para saber se é bissexto: \n'))
print(ano_bissexto(a))
m = int(input('\nDigite o mes, para saber quantos dias tem: \n'))
print(dias_mes(a,m))
print(mes(m))
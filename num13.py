num = int(input("Digite o numero que deseja: ") )
result = 1
for n in range(1,num+1):
    result *= n
print('O fatorial de ', num,' é:', result)
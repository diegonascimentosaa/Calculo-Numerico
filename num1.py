segundos = int(input('Informe o numero de segundos: ')) # Usuario deve digitar os segundos
horas = int(segundos/3600) # Esse calculo é responsavel por tranformar segundos em hora, a variavel tem que ser inteira para ignorar as casas decimais
minutos = int((segundos%3600)/60) # Esse calculo é responsavel por tranformar o restante da hora em minutos, a variavel tem que ser inteira para desconsiderar as casas decimais
segundo = int((segundos%3600)%60) # Esse calculo é responsavel por pegar o restante dos minutos, que é os segundos que sobraram.
print('Horas: ', horas, ', minutos: ',minutos,' segundos:', segundo ) # Escreve uma linha em branco
print('Vamos realizar o calculo de juros simples, primeiramente preencha os dados a seguir')
capital = float(input('Digite o capital: '))
taxa = float(input('Digite a taxa a ser calculado: '))
tempo = float(input('Digite o tempo: '))
juros = (capital*taxa*tempo)/100
print('O jutos simples é de: ', juros)
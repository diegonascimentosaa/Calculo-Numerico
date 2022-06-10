for i in range(10):
    nome = input('Digite o nome do Aluno: ')
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    nota = (n1*0.3 + n2*0.3 + n3*0.4)
    if nota>=60:
        print(nome, ' foi aprovado na disciplina com nota: ', nota)
    else:
        print(nome, ' foi reprovado na disciplina com nota: \n', nota)

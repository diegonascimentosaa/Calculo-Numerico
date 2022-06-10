def ano_bissexto(ano):
    if ano%4==0 and ano%100!=0 or ano%400==0:
        return True
    else:
        return False
def dias_mes(ano, mes):
    ld = [31,28,31,30,31,30,31,31,30,31,30,31]
    ldb = [31,29,31,30,31,30,31,31,30,31,30,31]
    if ano%4==0 and ano%100!=0 or ano%400==0:
        return ldb[mes-1]
    else:
        return ld[mes-1]
def mes(mes):
    lm = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'] 
    return lm[mes-1]
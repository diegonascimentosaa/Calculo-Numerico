import numpy as np
import matplotlib.pyplot as pyplot
def fg(fx, x): 
    return x - 0.05 * eval(fx)
def funcaoEval(fx, x): 
    return eval(fx)
def plotgrafico(fx, a, b):
    xx = np.linspace(a, b)
    pyplot.plot(xx, funcaoEval(fx, xx))
    pyplot.grid()
    pyplot.show()
def pontoFixo(a, b, tol, n, func): 
    x = (a + b) / 2
    for k in range(n):
        x = fg(func, x)
        if (abs(funcaoEval(func, x)) < tol):
            break
    print("A raiz aproximada do ponto fixo é : {r:+5.5f}\n".format(r=x)+"erro: {err:+5.10f}\n".format(err=abs(funcaoEval(func,x))))
def posicaoFalsa(a, b, tol, n, func):
    xi = float("nan")
    for i in range(n):
        x = (a * funcaoEval(func, b) - b * funcaoEval(func, a)) / (funcaoEval(func, b) - funcaoEval(func, a))
        erro = abs((x - xi) / max(x, 1))
        xi = x 
        fx = funcaoEval(func, x)
        flag = funcaoEval(func, a) * fx
        if (fx == 0) or (erro < tol): 
            break
        if flag > 0:
            a = x
        else:
            b = x
    print("A raiz aproximada do posição falsa é : {r:+5.5f}\n".format(r=x)+"erro: {err:+5.10f}\n".format(err=erro))
def secante(a, b, tol, n, func): 
    x = a
    xi = b
    for i in range(n):
        erro = abs((x - xi) / max(x, 1))
        fx = funcaoEval(func, x)
        fxi = funcaoEval(func, xi)
        if (fx == 0) or (erro < tol):
            break
        xii = x - fx * ((x - xi) / (fx - fxi))
        xi = x
        x = xii
    print("A raiz aproximada da secante: {r:+5.5f}\n".format(r=x)+"erro: {err:+5.10f}\n".format(err=erro))
if __name__ == "__main__": 
    func = input("Qual a funcão a ser analisada? ")
    resposta = 'nao'
    while(resposta!='sim'): 
        a = float(input("Qual o início do intervalo:\n"))
        b = float(input("Qual  o fim do intervalo:\n"))
        plotgrafico(func, a, b) 
        resposta=input("Digite `sim` para proceseguir, ou digite `nao` para digitar o intervalo novamente.\n")
    e = float(input("Qual a tolerância mínima?"))
    n = int(input("Quantas iterações?"))
    secante(a, b, e, n, func)
    posicaoFalsa(a, b, e, n, func)
    pontoFixo(a, b, e, n, func)
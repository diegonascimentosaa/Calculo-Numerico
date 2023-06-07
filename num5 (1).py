import numpy as np
import matplotlib.pyplot as plot
def function(f, x):
    return eval(f)
def g(f, x):
    return x - 0.05 * function(f, x) 
def fp(a, b, tol, n, f):
    x = (a+b)/2
    for k in range(n):
        gx = g(f, x); xi = x; x = g(f, x)
        flag = function(f, x)
        print('Iteração {k}: Valor de x: {x:.6f}, '.format(k=k+1, x=xi) + 'Valor de g(x): {gx:.6f}, '.format(gx=gx) + 'Valor de f(x): {flag:.6f}'.format(flag=flag))
        if (abs(function(f, x)) < tol): 
            break
fp(0.1, 2, 0.00001, 20, 'np.log(x)')
fp(0, 5, 0.00001, 20, 'np.exp(x)')
fp(1, 2, 0.00001, 20, 'np.cos(x)')
fp(-2, 0, 0.00001, 20, 'x**2+2*x+1')
fp(-2, -0.5, 0.00001, 20, 'np.exp(2-x**2)*(x+1)**2')
fp(-5, 5, 0.00001, 20, 'x**3+3*x-1')
fp(-2, -0.5, 0.00001, 20, 'np.sin(x)+x**2')
fp(-10, 5, 0.00001, 20, 'np.exp(x)-x**2-10')
fp(0, 2, 0.00001, 20, 'np.sqrt(x)-np.cos(x)')
fp(2, 4, 0.00001, 20, 'x-3-x**(-x)')

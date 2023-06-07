import numpy as np
def f(x):
   return np.log(x)
def fp(a, b, tol, v):
   x2 = float('nan')
   for cont in range(v):
       x1 = (a * f(b) - b * f(a)) / (f(b) - f(a))
       erro = abs((x1 - x2) / max(x1, 1))
       x2 = x1
       print("Iteracao", cont, "Valores:. a:", a, "| b:", b, "| Erro: ", erro, " x':", x1, " F(x):", f(x1), "F(x)*F(a):", f(x1) * f(a))
       if ((f(x1) == 0) or (erro < tol)):
           break
       if (f(x1) * f(a)) > 0:
           a = x1
       else:
           b = x1
fp(0.1, 3.0, 0.00001, 20)
#fp(0, 5, 0.00001, 20)
#fp(0.5, 4, 0.00001, 20) 
#fp(-3, 0.5, 0.00001, 20)
#fp(-3, -0.5, 0.00001, 20)
#fp(-8, 7, 0.00001, 20)
#fp(-4, 3, 0.00001, 20)
#fp(-8, 6, 0.00001, 20)
#fp(0.1, 9, 0.00001, 20)
#fp(0, 9, 0.00001, 20)
def ErroAbs(x, xi): 
    abs = x - xi
    return abs
def ErroRel(x, xi): 
    rel = (x - xi) / x
    return rel
print('a) o erro absoluto {abs:.8f} ,e relativo {rel:.8f}'.format(abs = ErroAbs(1.00001, 1), rel = ErroRel(1.00001, 1)))
print('b) o erro absoluto {abs:.8f} ,e relativo {rel:.8f}'.format(abs = ErroAbs(100001, 100000), rel = ErroRel(100001, 100000)))
print('c) o erro absoluto {abs:.8f} ,e relativo {rel:.8f}'.format(abs = ErroAbs(32.65483, 34.1645), rel = ErroRel(32.65483, 34.1645)))
print('d) o erro absoluto {abs:.8f} ,e relativo {rel:.8f}'.format(abs = ErroAbs(5.87135, 5.87049), rel = ErroRel(5.87135, 5.87049)))
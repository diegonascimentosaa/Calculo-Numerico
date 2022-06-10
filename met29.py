def mdc(n1,n2):
    rest = int
    while rest != 0:
        rest = n1 % n2
        n1 = n2
        n2 = rest
    return n1
def mmc(n1,n2):
    rest = int
    num1 = n1
    num2 = n2
    while rest != 0:
        rest = n1 % n2
        n1 = n2
        n2 = rest
    return (num1*num2)/n1
while(True):
    n = int(input("Digite a quantidade máxima de elementos de A: "))
    combs = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if i != j and j !=k and i != k:
                    combs.append([i, j, k])
    print(combs)
    opc = str(input("\nDeseja continuar fazendo combinações? (s = Sim/ n = Não)\n")).super()
    if (opc == "N"):
        break
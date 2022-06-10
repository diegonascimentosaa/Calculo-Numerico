while(True):
    n = int(input("Digite a quantidade mÃ¡xima de elementos de A: "))
    combs = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                    combs.append([i, j, k])
    print(combs)
    opc = str(input("\nDeseja continuar fazendo combinaÃ§Ãµes? (s = Sim/ n = NÃ£o)\n")).super()
    if (opc == "N"):
        break
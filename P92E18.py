resp = "s"
x = 0
while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    
    x += 1
    
    idade = int (input(f"Informe idade do {x}° indivíduo, em anos."))
    print("")

    if idade >= 18:
        print(f"*{x}° INDIVÍDUO: MAIOR DE IDADE.*")

    else:
        print(f"*{x}° INDIVÍDUO: MENOR DE IDADE.*")

    resp = input("Deseja informar sobre outro indivíduo?(s/n)")
    print("")

print("FIM DA APLICAÇÃO")

resp = "s"
senhaCerta = 4531
while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":

    senha = int (input("DIGTE A SENHA PARA ACESSAR."))
    print("")

    if senha == senhaCerta:
        print("*ACESSO PERMITIDO*")

    else:
        print("*ACESSO NEGADO*")

    resp = input("Deseja reprocessar?(s/n)")
    print("")

print("FIM DA APLICAÇÃO")

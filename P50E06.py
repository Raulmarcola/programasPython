x = 0
resp = "s"
while resp == "s" or resp == "S" or resp == "Sim" or resp == "SIM" or resp == "sIM" or resp == "sim": 

    x += 1
    print(f"Informe sobre o {x}° funcionário, em R$: ")
    print("")
    sal = float (input ("Salário: ") )
    vend = float (input ("Valor das vendas: ") )

    comiss = vend * 0.04
    salfin = comiss + sal    

    print("")
    print(f"COMISSÃO: R$ {comiss:.2f}")
    print(f"SALÁRIO FINAL: R$ {salfin:.2f}")
    print("")

    resp = input("Digite 's' para inforar sobre outro funcionário.")
    print("")

print("FIM DA APLICAÇÃO!")
#é possível adicionar total de gasto, maior salário, maior comissão etc.

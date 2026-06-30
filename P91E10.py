resp = "s"
print("**CALCULADORA - CONSESSÃO DE CRÉDITO NO BANCO CONFORME MÉDIA DE SALDO**")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    print("")
    custo = float (input (f"informe o custo de fabricação do carro, em R$: "))

    if custo <= 12000:
        dist = custo * 0.05
        imp = 0

    elif custo <= 25000:
        dist = custo * 0.10
        imp = custo * 0.15

    else:
        dist = custo * 0.15
        imp = custo * 0.20
    
    nCusto = custo + dist + imp
    
    print("")
    print(f"IMPOSTOS: R$ {imp}")
    print(f"DISTRIBUIÇÃO: R$ {dist}")
    print("")
    print(f"VALOR FINAL DO CARRO: R$ {nCusto}")
    print("")

    resp = input("Deseja calcular novamente?")
print("")
print("FIM DA APLICAÇÃO!")

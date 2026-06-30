resp = "s"
x = 0
print("**CALCULADORA - CONSESSÃO DE CRÉDITO NO BANCO CONFORME MÉDIA DE SALDO**")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    x += 1
    print("")
    saldo = float (input (f"informe o saldo médio do {x}° cliente, em R$: "))

    if saldo <= 200:
        cred = saldo * 0.10

    elif saldo <= 300:
        cred = saldo * 0.20

    elif saldo <= 400:
        cred = saldo * 0.25

    else:
        cred = saldo * 0.30

    print("")
    print(f"SALDO MÉDIO DO {x}° CLIENTE: R$ {saldo}")
    print(f"CRÉDITO DO {x}° CLIENTE: R$ {cred}")
    print("")

    resp = input("Há outro cliente para informar sobre?")
print("")
print("FIM DA APLICAÇÃO!")

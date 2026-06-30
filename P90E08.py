resp = "s"
x = 0
print("**CALCULADORA - REAJUSTE DE SALÁRIO DA FIRMA**")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    x += 1
    print("")
    sal = float (input (f"informe o salário do {x}° funcionário, em R$: "))

    if sal <= 300:
        aum = sal * 0.35

    elif sal > 300:
        aum = sal * 0.15

    nsal = sal + aum

    print(f"SALÁRIO REAJUSTADO DO {x}° FUNCIONÁRIO: R$ {nsal}")
    print("")

    resp = input("Há outro funcionário para informar sobre?")
print("")
print("FIM DA APLICAÇÃO!")

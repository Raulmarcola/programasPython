resp = "s"
x = 0
print("**CALCULADORA - BÔNUS DE NATAL DA FIRMA**")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    x += 1
    print("")
    print(F"informe sobre o {x}° funcionário: ")
    hExtra = int (input("Número de horas extra: "))
    hFalta = int (input("Número de horas falta: "))
    print("")

    H = hExtra - ( 2/3 * (hFalta) )
    H = H * 60

    if H >= 2400:
        premio = 500

    elif H >= 1800:
        premio = 400

    elif H >= 1200:
        premio = 300

    elif H >= 600:
        premio = 200

    else:
        premio = 100

    print(f"PRÊMIO DO {x}° FUNCIONÁRIO: R$ {premio}")
    print("")

    resp = input("Há outro funcionário para informar sobre?")
print("")
print("FIM DA APLICAÇÃO!")

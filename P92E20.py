resp = "s"
x = 0
print("**CATEGORIA DOS NADADORES**")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    x += 1
    print("")
    idade = int (input (f"informe a idade do(a) {x}° nadador(a), em anos: "))

    if idade >= 30:
        categ = "SÊNIOR"

    elif idade >= 16:
        categ = "ADULTO"

    elif idade >= 11:
        categ = "ADOLESCENTE"

    elif idade >= 8:
        categ = "JUVENIL"

    elif idade >= 5:
        categ = "INFANTIL"

    else:
        categ = "NÃO PODE PARTICIPAR"

    print(f"CATEGORIA DO(A) {x}° NADADOR(A): {categ}")
    print("")

    resp = input("Há outro nadador(a) para informar sobre?")
print("")
print("FIM DA APLICAÇÃO!")

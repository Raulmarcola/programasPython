resp = "s"
print("**MENU DE OPERAÇÕES**")
print("")
print("1 - Média entre os números digitados")
print("2 - Diferença do maior pelo menor")
print("3 - Produto entre os números digitados")
print("4 - Divisão do primeiro pelo segundo")
print("")

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    print("")
    opera = int (input("Informe a operação escolhida: "))

    if opera < 5 and opera > 0:

        n1 = float (input("Digite primeiro número: "))
        n2 = float (input("Digite segundo número: "))
        print("")

        if opera == 1:
            r = (n1 + n2) / 2
            print(f"RESULTADO DA OPERAÇÃO: {r}")
            print("")

        elif opera == 2:
            if n1 > n2:
                r = n1 - n2
            else:
                r = n2 - n1
            print(f"RESULTADO DA OPERAÇÃO: {r}")
            print("")
    
        elif opera == 3:
            r = n1 * n2
            print(f"RESULTADO DA OPERAÇÃO: {r}")
            print("")

        elif opera == 4:
            while n2 == 0:
                print("IMPOSSÍVEL DIVIDIR POR ZERO.")
                n2 = float (input("Digite segundo número: "))
            r = n1 / n2
            print(f"RESULTADO DA OPERAÇÃO: {r}")
            print("")

    else:
        print("CÓDIGO NUMÉRICO INEXISTENTE.")
        print("")

    resp = input("Deseja operar novamente?")

print("")
print("FIM DA APLICAÇÃO!")

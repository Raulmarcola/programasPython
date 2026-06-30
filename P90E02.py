resp = "s"
x = 0

while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim" or resp == "sIM":
    x += 1
    print("")
    print(f"Sobre {x}° aluno informe -")    

    print("")

    n1 = float (input ("primeira nota: "))
    n2 = float (input ("segunda nota: "))

    print("")

    med = (n1 + n2) / 2

    print(f"MÉDIA DE {x}° ALUNO: {med}")

    if med < 3:
        print("SITUAÇÃO: REPROVADO") 
    
    elif med < 7:
        print("SITUAÇÃO: EXAME")

    else:
        print("SITUAÇÃO: APROVADO")
    
    print("")
    
    resp = input ("Há outro aluno a informar sobre?")

print("Fim da aplicação!")

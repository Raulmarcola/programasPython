print("*CALCULADORA DE MÉDIA*")
print("")
print("1° nota: peso 2")
print("2° nota: peso 3")
print("")

resp = "s"
x = 0

while resp == "s" or resp == "S" or resp == "Sim" or resp == "SIM" or resp == "sIM" or resp == "sim": 
    x += 1    

    print(f"Informe sobre o {x}° aluno -")
    print("")

    nota1 = float (input ("Primeira nota.") )
    nota2 = float (input ("Segunda nota.") )

    medp = ( (nota1 / 5) * 2 ) + ( (nota2 / 5) * 3 )

    print("")
    print(f"MÉDIA PONDERADA: {medp}")

    resp = input ("Deseja informar sobre outro aluno? (s/n)")
    print("")

print ("FIM DA APLICAÇÃO!")

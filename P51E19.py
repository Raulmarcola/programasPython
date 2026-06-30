print("*CALCULA POTÊNCIA DE ILUMINAÇÃO PARA UM CÔMODO*")
resp = "s"
x = 0
while resp == "s" or resp == "S" or resp == "SIM" or resp == "sim":

    print("")

    x += 1
    print(f"Informe as dimensões do {x}° cômodo, em metros.")
    lado1 = float (input ("Comprimento do 1° lado: ") )
    lado2 = float (input ("Comprimento do 2° lado: ") )

    area = lado1 * lado2
    pot = area * 18
    print("")

    print(f"ÁREA DO CÔMODO: {area} M²")
    print(f"POTÊNCIA LUMINOSA NECESSÁRIA PARA {x}° CÔMODO: {pot} W ")

    resp = input("Há outro cômodo a informar? (s/n)")

print("")
print("FIM DA APLICAÇÃO")    

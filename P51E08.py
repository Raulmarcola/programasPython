print("*CONVERTER PESO EM Kg PARA GRAMAS*")

resp = "s"
x = 0
while resp == "s" or resp == "S":
    x += 1
    print("")
    pkg = float (input (F"Informe peso do {x}° indivíduo, em Kg: ") )

    pg = pkg * 1000
    print("")
    print (f"PESO EM GRAMAS: {pg:.2f} ")

    resp = input("Deseja informar sobre outro indivíduo? (s/n)") 

print("FIM DA APLICAÇÃO!")

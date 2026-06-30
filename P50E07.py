x = 0
resp = "s"
while resp == "s" or resp == "S" or resp == "Sim" or resp == "SIM" or resp == "sIM" or resp == "sim": 

    x += 1
    peso = float ( input(f"Informe o peso do {x}° indivíduo, em Kg: ") )
    print("")

    p_eng = peso * 1.15
    p_ema = peso * 0.8

    print(f"PESO AO ENGORDAR 15%: {p_eng:.2f} Kg")
    print(f"PESO AO EMAGRECER 20%: {p_ema:.2f} Kg")
    print("")

    resp = input("Deseja informar sobre outro indivíduo? (s/n)")

print("FIM DA APLICAÇÃO!")

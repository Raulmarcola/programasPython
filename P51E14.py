resp = "s"
x = 0
print("*CALCULADORA DE IDADES*")
print("")
ano_atual = int (input ("Informe ano atual: ") )    
while resp == "s" or resp == "S" or resp == "Sim" or resp == "sIM" or resp == "SIM" or resp == "sim":

    x += 1
    ano_nasc = int (input (F"Ano de Nascimento do {x}° indivíduo: ") ) 
    
    idade_a = ano_atual - ano_nasc
    idade_m = idade_a * 12
    idade_d = idade_a * 365
    idade_s = idade_a * 52.18

    print(f"IDADE DO {x}° INDIVÍDUO EM: ")
    print("")
    print(f"ANOS: {idade_a} ")
    print(f"MESES: {idade_m} ")
    print(f"DIAS: {idade_d} ")
    print(f"SEMANAS: {idade_s:.2f} ")
    print("")

    resp = input ("Deseja informar novamente? (s/n)")

print("FIM DA APLICAÇÃO!")

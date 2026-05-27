sexo = input("Informe o sexo do indivíduo (M/F).")
print("")
h = float (input("Informe a altura do indivíduo."))

if sexo == "M" or sexo == "masc" or sexo == "masculino" or sexo == "MASCULINO" or sexo == "Masc" or sexo == "Masculino" or sexo == "m":
    p_i = (72.7 * h) - 58
    print(f"O peso ideal do indivíduo é {p_i}")
elif sexo == "F" or sexo == "fem" or sexo == "feminino" or sexo == "FEMININO" or sexo == "Fem" or sexo == "Feminino" or sexo == "f":
    p_i = (62.1 * h) - 44.7
    print(f"O peso ideal do indivíduo é {p_i}")
else:
    print("Escolha uma opção válida")
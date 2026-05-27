resposta = "sim"

print("**CALCULA O ÂNGULO DO TRIÂNGULO A PARTIR DE DOIS PRIMEIROS**")

while resposta == "sim" or resposta == "Sim" or resposta == "SIM" or resposta == "s" or resposta == "S":

    ang1 = float (input ("Informe a medida do 1° ângulo do triângulo: "))
    ang2 = float (input ("Informe a medida do 2° ângulo do triângulo: "))
    print("")
    ang3 = 180 - (ang1 + ang2)

    print(f"Medida do 3° ângulo do triângulo analisado: {ang3} ")
    
    print("")
    resposta = input ("Deseja calcular ângulo de triângulo novamente?(s/n)")

print("FIM DA APLICAÇÃO")
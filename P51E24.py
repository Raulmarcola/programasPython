resp = "s"
x = 0
while resp == "s" or resp == "S" or resp == "SIM" or resp == "Sim" or resp == "sim":
    x += 1    
    print("")        

    reais = float (input (f"Informe dinheiro do {x}° viajante em R$: "))
    print("")    

    dolar = reais / 1.8
    marco = reais / 2
    libra = reais / 3.57

    print(f"DINHEIRO DO {x}° VIAJANTE: ")
    print("")    
    print(f"{dolar:.2f} DÓLARES")
    print(f"{marco:.2f} MARCOS ALEMÃES")
    print(f"{libra:.2f} LIBRAS ESTERLINAS")

    resp = input("Há outro viajante? (s/n)")
print("")    
print("FIM DA APLICAÇÃO")

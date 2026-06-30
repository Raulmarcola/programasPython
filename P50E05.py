resp = "s"
print("*CAIXA DO SUPEMERCADO*")


x = 1
soma = 0
while resp == "s" or resp == "S" or resp == "Sim" or resp == "SIM" or resp == "sIM" or resp == "sim": 

    preco = float (input(f"Informe o preço do {x}° produto, em R$: "))
    
    novo_preco = preco * 0.9
    print("")
    print(f"PREÇO COM DESCONTO DE 10%: R$ {novo_preco:.2f}")
    
    soma += novo_preco

    resp = input("Há outro produto a informar?(s/n) ")
    print("")
    x += 1  
print(f"VALOR TOTAL DA COMPRA: R$ {soma:.2f}")

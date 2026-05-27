cont_5060 = 0
cont_olho = 0
perc_olho = cont_olho * 100 / 6

for x in range (1, 6):    
    print(f"Informe os seguintes dados do indivíduo {x} - ")
    idade = int (input ("Idade: ") )
    peso = float (input ("peso: ") )
    altura = float (input ("altura: ") )
    cor_o = (input ("cor do olho: ") )
    cor_c = (input ("cor do cabelo: ") )

    if (idade > 50) and (peso < 60):
        cont_5060 += 1
    if (cor_o == "A"):
        cont_olho += 1    
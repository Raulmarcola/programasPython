cont_otimo = 0
soma_idade = 0
cont_regular = 0
cont_bom = 0

print(" - TABELA DE OPINIÕES - ")
print("3 - Ótimo")
print("2 - Bom")
print("1 - Regular")
print("")
t = 16 #aqui a variável t poderia ser um input em que o usuário informa sobre quantos expectadores quer informar
print(f"Preencha dados de {(t-1)} espectadores")

for x in range (1, t):  #coloquei o máximo como uma variável t para poder alterar e testar com mais praticidade

    print(f"Informações sobre o {x}° espectador -")
    idade = int (input ("Idade: "))
    opiniao = int (input ("Opinião: "))
    print("") #pular linha para organização

    #verificando cada caso de resposta 'opinião'
    if opiniao == 3:
        cont_otimo  += 1
        soma_idade += idade
    elif opiniao == 2:
        cont_bom  += 1        
    elif opiniao == 1:
        cont_regular  += 1    
    else:
        print("DIGITE CÓDIGO NUMÉRICO VÁVLIDO PARA 'OPINIÃO' ") # se nenhum caso bateu o código está incorreto; queria tentar alguma forma de voltar para entrada de dados quando acontecer isso

med = soma_idade / cont_otimo #idade de todas as pessoas que responderam ótimo somadas pelo número de pessoas 

porc_bom = cont_bom * 100 / (t - 1) #aplicação de t: coloquei "-1", pois t representa o máximo, ou seja, o número de espectadores analisados será um a menos que t

print(f" MÉDIA DE IDADE DOS ESPECTADORES QUE RESPONDERAM 'ÓTIMO': {med} anos")
print(f" QUANTIDADE DE ESPECTADORES QUE RESPONDERAM 'REGULAR': {cont_regular}")
print(f" PORCENTAGEM DE ESPECTADORES QUE RESPONDERAM 'BOM': {porc_bom}%") #Aqui poderia pular linhas também para melhorar a visibilidade, mas acho que junto fica mais bonito
print("")
print("Leia o livro de atos dos apóstolos da Bíblia e veja que a fé em Jesus é muito maior e mais bonita do que somente ir à igreja.") #Isso é só uma mensagem para você :)
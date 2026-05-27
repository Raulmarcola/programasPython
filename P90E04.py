N1 = float (input ( "Informe o primeiro número: ") )
N2 = float (input ( "Informe o segundo número: ") )
N3 = float (input ( "Informe o terceiro número: ") )

if N1 > N2 and N1 > N3:
	print(f"{N1} é o maior número.")

elif N2 > N1 and N2 > N3:
	print(f"{N2} é o maior número.")

elif N3 > N2 and N3 > N1:
	print(f"{N3} é o maior número.")
else:
	print("Os três números são iguais.")

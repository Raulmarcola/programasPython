def volume(r):
    resultado = 4/3 * (r ** 3) * 3.14
    return resultado

raio = float(input('Informe o raio da esfera: '))
print(volume(raio)) # Assim, 'r' será substituído no bloco de instruções por 'raio'

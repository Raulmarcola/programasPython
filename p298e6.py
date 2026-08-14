def pesoIdeal(alt, s):
    if s == 'M' or s == 'm':
        resultado = (alt * 72.7) - 58
    elif s == 'F' or s == 'f':
        resultado = (alt * 62.1) - 44.7
    else:
        resultado = 'Resposta inválida'

    return resultado

altura = float(input('Informe altura, em metros.'))
sexo = input('Informe sexo, conforme código de caractér (m/f).')

print(f'PESO IDEAL: {pesoIdeal(alt = altura, s = sexo)}')

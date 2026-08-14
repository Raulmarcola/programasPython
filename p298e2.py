def convertSeg(h, m, s):
    resultado = (h * 3600) + (m * 60) + s
    return resultado

horas = int(input('Digite horas: '))
minutos = int(input('Digite minutos: '))
segundos = int(input('Digite segundos: '))

print(convertSeg(horas, minutos, segundos))

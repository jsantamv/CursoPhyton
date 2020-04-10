import time

objetivo = int(input('Escoje un entero:'))

respuesta = 0

print(time.time())
while respuesta ** 2 < objetivo:
    respuesta+= 1

if respuesta ** 2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cudrada exacta')

print(time.time())


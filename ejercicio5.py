#Escriba una funcion que reciba como parametro el radio de un cidruclo y
#devuelva una tupla conteniendo en el primer elemento el perimetro y en el
#segundo el area del mismo.

import math
def calcular_circulo(radio: int) -> tuple:
    return 2 * math.pi * radio, math.pi * radio ** 2

print(calcular_circulo(5))
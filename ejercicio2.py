#Escribir la funcion factorial, que reciba como parametro el numero inicial y compute el resultado.
#Hacer la implementacion recursiva y tambien la iterativa.

def factorial_recursivo(numero: int) -> int:
    if numero > 0:
        return numero * factorial_recursivo(numero - 1)
    else:
        return 1

print(factorial_recursivo(8))

def factorial_iterativo(numero: int) -> int:
    resultado = 1
    for n in range(1,numero + 1):
        resultado = resultado * n
    return resultado

print(factorial_iterativo(8))

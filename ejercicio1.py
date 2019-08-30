#Escribir una funcion que reciba como parametros el inicio y fin (inclusive) de un rango numerico.

def generar_numeros(inicio: int, fin: int):
    numeros = [n for n in range(inicio,fin) if n % 7 == 0 and n % 5 != 0]
    for n in numeros:
        print(n)
    for i,n in enumerate(numeros):
        print(n,end='')
        if i < len(numeros) - 1:
            print(',',end='')

generar_numeros(1,100)
#Escribir una funcion que reciba como parametros el inicio y fin (inclusive) de un rango numerico. La funcion debe:
#a. Imprimir en pantalla todos aquellos numeros que sean divisibles por 7 pero no sean divisibles por 5.
#b. Imprimir el mismo resultado anterior, pero separados por coma.

def generar_numeros(inicio: int, fin: int):
    numeros = [n for n in range(inicio,fin) if n % 7 == 0 and n % 5 != 0]
    for n in numeros:
        print(n)
    for i,n in enumerate(numeros):
        print(n,end='')
        if i < len(numeros) - 1:
            print(',',end='')

            
if __name__ == "__main__":
    generar_numeros(1,100)

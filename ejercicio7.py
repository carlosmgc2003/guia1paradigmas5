#Se necesita una funcion que reciba un texto de varias palabras separadas por
#un espacio, con letras mayusculas y minuscular, y retorne una coleccion de las
#palabras utilizadas, todas en minuscula y sin duplicados.

if __name__ == "__main__":
    texto = input('Por favor, ingrese un texto: ')
    conjunto = set(list(map(lambda x : x.lower(), list(texto.split()))))
    print(conjunto)
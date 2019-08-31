#En Años anteriores, se necesitaba una función en python que reciba un texto conteniendo bits (simbolos
#1 y 0), y debia armar una lista conteniendo 8 bits por elementos (1 byte). Por ejemplo, si se incova la
#funcion con el siguiente texto como parámetro:
#"1001010101000101010101100101001010101010"
#la funcion devuelve: ['10010101', '01000101', '01010110', '01010010',
#'10101010']

def ej08a(texto):
#"""Arma una lista de bytes acorde al texto recibido por parametro"""
    indice = 0
    resultado = []
    current_byte = ""
    for i in texto:
        #a. Propongo de que en caso de que no sea la cadena correcta raise Exception
        if i != '0' and i != '1':
            raise Exception('La cadena no es valida')
        current_byte += i # se agrega el nuevo caracter al byte actual
        indice += 1 # se incrementa en uno el indice
        if indice % 8 == 0: #b. cortar el elemento al octavo caracter de la cadena
        # Comienza un nuevo byte
            resultado.append(str(current_byte))
            current_byte = ""
    return list(set(resultado)) #Si hacer un set


print(ej08a("10010101100101010100101010101100101001010101010"))
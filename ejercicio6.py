#Se necesita un programa que reciba linea por linea de comando una serie de palabras,
#hasta que reciba la palabra "exit". El resultado debe ser una lista, 
#con las plabras ordenadas alfabeticamente, y cada una debe estar
#capitalizada.

if __name__ == "__main__":
    prompt = 'Ingrese palabra: '
    palabra = input(prompt)
    palabras = []
    while(palabra != 'exit'):
        palabras.append(palabra)
        palabra = input(prompt)
    print(sorted(list(map(lambda cadena : cadena.capitalize(),palabras))))

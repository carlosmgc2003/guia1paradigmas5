#Se necesita un programa que reciba por parámetro un texto, y que devuelva una tupla conteniendo en el
#primer lugar, la cantidad de letras (mayúsculas o minúsculas), en el segundo lugar la cantidad de dígitos
#numéricos y en el tercer lugar, otros símbolos.


def analizar_texto(texto:str) -> tuple:
    lista = list(texto)
    cant_letras = sum(list(map(lambda c : c.isalpha(), lista)))
    cant_digitos = sum(list(map(lambda c : c.isdigit(), lista)))
    cant_otros = len(texto) - (cant_digitos + cant_letras)
    return cant_letras, cant_digitos, cant_otros


print(analizar_texto('Esta es una mañana LLuviosa!! 25 días más serán así??'))
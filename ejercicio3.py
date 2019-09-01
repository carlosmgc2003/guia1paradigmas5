#Hacer una funcion que genere y retorne un diccionario ASCII de la forma {'a': 97, 'b': 98, ...}
import string
def ascii_dict():
    claves = list(string.ascii_lowercase)
    valores = claves[:]
    valores = list(map(lambda x : ord(x),claves))
    return dict(zip(claves,valores))

if __name__ == "__main__":
    print(ascii_dict())

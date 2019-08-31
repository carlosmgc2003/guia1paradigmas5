def formatear_lista(lista : list) -> list:
    return list(map(lista_from_string, lista))

def lista_from_string(string : str) -> list:
    lista = list(string.split(','))
    return [int(lista[0]), lista[1], bool(lista[2])]

ejemplo = [
            '14,Juana Perez,True',
            '16,Raul Dell,False',
            '18,Mariana Castillo,True',
            '176,Pedro Rodriguez,False'
            ]

print(lista_from_string(ejemplo[0]))

print(formatear_lista(ejemplo))
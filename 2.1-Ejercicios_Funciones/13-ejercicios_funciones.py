# Crear una función que recibe una lista de palabras y 
# devuelve un diccionario con las palabras como llaves y su longitud como valores.


def longitud_palabras(lista):
    diccionario = {}
    for palabra in lista:
        diccionario[palabra] = len(palabra)
    return diccionario
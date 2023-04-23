# Crear una función que cuente la cantidad de veces que aparece un elemento en
# una lista. Recibe una lista y un elemento como parámetros y devuelve la
# cantidad de veces que aparece en la lista.


def contar_elemento(lista, elemento):
    contador = 0
    for i in lista:
        if i == elemento:
            contador += 1
    return contador
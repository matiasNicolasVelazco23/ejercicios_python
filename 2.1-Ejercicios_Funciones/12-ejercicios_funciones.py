# Crea una función que reciba dos listas de nombres, y 
# devuelva una lista con los nombres que aparecen en ambas listas


def nombres_comunes(lista1, lista2):
    nombres = []
    for nombre1 in lista1:
        for nombre2 in lista2:
            if nombre1 == nombre2:
                nombres.append(nombre1)
    return nombres
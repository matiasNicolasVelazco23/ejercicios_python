# Crear una función que recibe una lista de números y devuelve un diccionario 
# con el valor mínimo, el valor máximo y el promedio de los números en la lista.


def estadisticas_numeros(lista):
    diccionario = {}
    minimo = lista[0]
    maximo = lista[0]
    suma = 0
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > maximo:
            maximo = numero
        suma += numero
    diccionario['minimo'] = minimo
    diccionario['maximo'] = maximo
    diccionario['promedio'] = suma / len(lista)
    return diccionario
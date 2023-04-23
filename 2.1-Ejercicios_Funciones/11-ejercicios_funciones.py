#Crea una función que reciba como parámetro una cadena de texto y devuelva la cantidad de vocales que tiene.

def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador
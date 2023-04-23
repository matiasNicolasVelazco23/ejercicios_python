def calcular_promedio(lista):
    """
    Calcula el promedio de una lista de números.


    Parámetros:
    lista (list): Una lista de números.


    Devuelve:
    float: El promedio de la lista.
    """
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
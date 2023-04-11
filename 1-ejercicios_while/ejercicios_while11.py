#Dada una lista de palabras, imprimir todas las palabras que tengan una longitud mayor a 5 caracteres.

lista_de_palabras = ["python", "programación", "computadora", "algoritmo", "datos", 
            "aprendizaje", "inteligencia", "código", "desarrollo", "web"]

indice = 0
while indice < len(lista_de_palabras):
    if len(lista_de_palabras[indice]) > 5:
        print(lista_de_palabras[indice])
    indice+=1
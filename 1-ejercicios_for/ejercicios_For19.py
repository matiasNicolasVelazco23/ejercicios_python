#Dada una lista de palabras, imprimir las palabras que tienen una letra mayúscula.

lista_de_palabras = ["silla", "gAto", "planta", "aZul", "libro", "computadoraA"]

for palabra in lista_de_palabras:
    for letra in palabra:
        if letra.isupper() == True:
            print(palabra)

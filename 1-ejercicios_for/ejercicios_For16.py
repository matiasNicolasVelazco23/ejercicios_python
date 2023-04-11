#Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

lista_de_palabras = ["manzana", "perro", "gato", "computadora", "elefante", 
                     "playa", "montaña", "libro", "televisión"]

for palabra in lista_de_palabras:

    for letra in palabra:
        if letra == "m":
            print(palabra)
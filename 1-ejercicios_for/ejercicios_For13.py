#Dada una lista de palabras, imprimir las palabras que tienen una longitud impar.

lista_de_palabras = ["manzana", "perro", "gato", "computadora", "elefante", 
                     "playa", "montaña", "libro", "televisión"]


for palabra in lista_de_palabras:
    if len(palabra) % 2 != 0:
        print(palabra)
#Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.
ingreso_palabra = input("Ingrese palabra: ")

indice = 0
while indice < len(ingreso_palabra):   #si el índice es menor que el tamaño de la palabra, sigue iterando
#la primera vez toma el índice 0, hasta llegar a el límite en el caso de la palabra pato, cuando índice llegue a 4 sale
#va a imprimir el índice en el que está, el índice 0 es p, el 1 es a, el 2 es t, y el 4 es o.
    print(ingreso_palabra[indice])     
    indice += 1
#Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

lista_de_palabras = ["Moto", "Ducha", "Hola"]
acumulador_vocales = 0

for palabra in lista_de_palabras:
    for letra in palabra:
        if (letra == "a" or letra =="e" or letra =="i" or letra == "o" or
            letra == "u"):
            acumulador_vocales+=1

        
print (acumulador_vocales)

#recorre cada palabra de la lista de palabras
#luego recorre cada letra de cada palabra en las iteraciones del segundo for
# si hay una vocal, entonces suma al acumulador de vocales
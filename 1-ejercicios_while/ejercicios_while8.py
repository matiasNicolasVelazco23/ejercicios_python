#Dada una cadena de texto, imprimir la cantidad de vocales en la cadena.

ingreso_palabra = input("Ingreso de palabra: ")
indice = 0
contador_de_vocales = 0
while indice < len(ingreso_palabra):
    if (ingreso_palabra[indice] == "a" or ingreso_palabra[indice] == "e" 
        or ingreso_palabra[indice] == "i" or ingreso_palabra[indice] == "o" or 
        ingreso_palabra[indice] == "u"):
        contador_de_vocales+=1
    indice+=1

print(contador_de_vocales)
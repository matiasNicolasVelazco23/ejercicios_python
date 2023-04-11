#Dada una cadena de texto, imprimir la cantidad de veces que aparece una letra específica en la cadena.

palabra = "tortaFrita"
indice = 0
contador_letra_especifica = 0
while indice <len(palabra):
    if palabra[indice] == "t":
        contador_letra_especifica+=1
    indice+=1
print(contador_letra_especifica)
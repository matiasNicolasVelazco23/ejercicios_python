#Dada una lista de palabras, imprimir la palabra más larga de la lista.

lista_palabras = ["Rueda", "Canasta", "Roberta", "Yoyo", "Estación", "Rita"]
flagPrimeraPalabra = True

for palabra in lista_palabras:
    if(flagPrimeraPalabra == True):
        palabra_mas_larga = palabra
        flagPrimeraPalabra = False
    elif (len(palabra)>len(palabra_mas_larga)):
        palabra_mas_larga = palabra
print(palabra_mas_larga)


#en este ejercicio uso len para comprar el tamaño de las palabras.
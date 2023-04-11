#xDada una lista de números, imprimir la cantidad de números negativos en la lista.

lista_numeros = [5, 12, 3, 19, 8, 16, -20, 4, 10, 18, -1, 9, 6, 13, 11, 7, 14, 
                 17, 15, 2]
indice= 0
contador_de_negativos = 0

while indice < len(lista_numeros):
    if lista_numeros[indice]<0:
        contador_de_negativos+=1
    indice+=1

print(contador_de_negativos)
#Dada una lista de números, imprimir la cantidad de números pares en la lista.

lista_de_numeros = [5,8,12,48,9,11,5]
contador_de_pares = 0
indice = 0

while indice < len(lista_de_numeros):
    if lista_de_numeros[indice] % 2 == 0:
        contador_de_pares+=1

    indice+=1
print(contador_de_pares)
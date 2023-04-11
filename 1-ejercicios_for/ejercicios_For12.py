#Dada una lista de números, imprimir la cantidad de números pares en la lista.

lista_de_numeros = [21, 2, 12, 8 , 13, 49 , 9 , 1, 0]
contador_de_pares = 0
for numero in lista_de_numeros:
    if numero % 2 == 0:
        contador_de_pares+=1

print(contador_de_pares)
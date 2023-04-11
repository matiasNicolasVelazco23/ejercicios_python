#Dada una lista de números, imprimir todos los números que son mayores que el número anterior en la lista.

lista_de_numeros = [8, 14, 19, 20, 4, 8, 3]
indice = 0
numero_anterior = lista_de_numeros [0]  #inicia el número anterior en el primer número de la lista

while indice < len(lista_de_numeros):
    if lista_de_numeros[indice] > numero_anterior:
        print(lista_de_numeros[indice])

    numero_anterior = lista_de_numeros[indice]
    indice+=1
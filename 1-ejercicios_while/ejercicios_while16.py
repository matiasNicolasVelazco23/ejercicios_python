#Dada una lista de números, imprimir todos los números que son múltiplos de 3.

lista_de_numeros = [8,9,5,3,12]
indice = 0


while indice < len(lista_de_numeros):
    if lista_de_numeros[indice] % 3 == 0:
        print(lista_de_numeros[indice])
    indice+=1
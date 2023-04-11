#Dada una lista de números, imprimir todos los números que son mayores que el promedio de la lista.

lista_de_numeros = [21, 8, 9 ,12 , 1, 3]
indice = 0
suma_de_numeros = 0

while indice < len(lista_de_numeros):
    suma_de_numeros+= lista_de_numeros[indice]
    indice+=1

promedio_de_numeros = suma_de_numeros / len(lista_de_numeros)
indice = 0

while indice < len(lista_de_numeros):
    if lista_de_numeros[indice] > promedio_de_numeros:
        print(lista_de_numeros[indice], end= " ")
    indice+=1
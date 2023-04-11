#Dada una lista de números, imprimir la suma de todos los elementos de la lista.

lista_de_numeros = [1,2,3,8,5,6]
indice = 0
suma_lista = 0

while indice<len(lista_de_numeros):
    suma_lista+=lista_de_numeros[indice]
    indice+=1
print(suma_lista)


#chatGPT me dice que use sum(lista), una función que suma todos los números de la lista
# lista_de_numeros = [1, 2, 3, 8, 5, 6]
# suma_lista = sum(lista_de_numeros)
# print(suma_lista)
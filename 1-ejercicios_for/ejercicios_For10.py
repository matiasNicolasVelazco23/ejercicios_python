# Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.

lista_de_palabras = ["manteca", "obvio", "robar", "mentir", "dibujar"]
acumulador_palabras_con_letra_igual = 0
#Luego, estamos utilizando la indexación de cadena para obtener
#  la primera letra de la palabra (palabra[0]) y asignarla a la variable 
# primera_letra, y para obtener la última letra de la palabra (palabra[-1]) 
# y asignarla a la variable ultima_letra.
for palabra in lista_de_palabras:
    primera_letra = palabra[0]
    ultima_letra = palabra [-1]
    if primera_letra == ultima_letra:
        print(palabra, " ")



# mi_lista = [1, 2, 3, 4, 5]
# ultimo_elemento = mi_lista[-1]
# print(ultimo_elemento)

#En este ejemplo, se accede al último elemento de la lista utilizando
#  el índice -1. El índice -1 siempre hace referencia al último elemento 
# de la lista, el índice -2 hace referencia al penúltimo elemento, y así sucesivamente.
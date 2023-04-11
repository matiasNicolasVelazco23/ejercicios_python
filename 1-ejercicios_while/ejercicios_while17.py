#Dada una cadena de texto, imprimir la cadena al revés.

palabra = "Texto"
indice = len(palabra) - 1  #hago esto para que empieze en el índice 4 y vaya hasta el 0
                           # 4,3,2,1,0 (5 caracteres)

while indice >= 0:         #itera mientras el índice sea mayor o igual a 0
    print(palabra[indice], end='')
    indice -= 1            # se reduce para que el while no sea infinito
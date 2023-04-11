# Dada una lista de números, imprimir el número más pequeño de la lista.

lista_de_numeros = [5,9,8,1,3,5,9,2,-2,8,1,5,8,10]
flag_primer_numero = True

for numero in lista_de_numeros:
    if flag_primer_numero == True:
        masPequeño = numero
        flag_primer_numero = False
    elif numero < masPequeño:
        masPequeño = numero
print(masPequeño)
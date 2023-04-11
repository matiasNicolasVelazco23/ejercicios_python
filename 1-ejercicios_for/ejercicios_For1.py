# Dada una lista de números, imprimir el número más grande de la lista.

lista_de_numeros = [1,5,8,2,3,9,18,16,5,2]

flag_PrimerIngreso = True   #uso de flag

# "numero" es el elemento que recorre de la lista, número es una variable solo del for
# la primera vez va a ser 1, la segunda 5, etc
for numero in lista_de_numeros:        
    if (flag_PrimerIngreso ==True): 
        #puedo declarar una variable en el for y usarla luego
        numero_mas_grande = numero      
        flag_PrimerIngreso = False

        
    elif numero > numero_mas_grande:
        numero_mas_grande = numero

print(numero_mas_grande)


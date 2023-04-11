# Escribir un programa que le pida al usuario que ingrese un número entero 
# positivo, y luego imprima "El número es primo" si el número es primo, o
# "El número no es primo" si el número no es primo.

numero_texto= input("Ingrese un número positivo: ")
numero_entero= (int(numero_texto))

if numero_entero <= 1:
    print("El número no es primo")
else:
    es_primo = True    
    #si no es menor o igual a 1 entra al else
    #si es primo y el resto entre la iteración del número es 0 cambia el valor
    #de la bandera de arriba a falsa, porque se puede dividir por otro número
    #además de 1 y el mismo número.
    for divisor in range(2, numero_entero-1): 
        #según la lógica de chatGpt, comprobar
        #si es divisible por el mismo número es redundante,
        #el valor de i empieza en 2 y aumenta hasta el número-1
        if numero_entero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
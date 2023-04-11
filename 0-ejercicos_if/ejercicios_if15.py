# Escribir un programa que le pida al usuario que ingrese un número entero
# positivo, y luego imprima "El número es primo" si el número es primo, o 
# "El número no es primo" si el número no es primo.

numero_texto = input("Ingrese un número entero positivo: ")
numero_entero = int(numero_texto)
esPrimo = True

if numero_entero > 1:
    for divisor in range(2, numero_entero):
        #lo que hace este código es que si confirma que un divisor da resto 0,
        #  entonces no es primo, empieza desde 2 y se mueve hasta el número-1
        if numero_entero % divisor == 0:
            esPrimo = False
            break
else:
    print("Escribiste un número impar")
if esPrimo == True:
    print("El número es primo")
else:
    print("El número no es primo")
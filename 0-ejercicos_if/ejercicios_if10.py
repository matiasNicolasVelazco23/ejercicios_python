# Escribir un programa que le pida al usuario que ingrese un número entero, y 
# luego imprima "El número es positivo y par" 
# si el número es positivo y divisible por 2, o "El número no cumple ninguna condición" 
# si el número no cumple ninguna de las dos condiciones anteriores.
numero_texto = input("Ingrese un número entero: ")
numero_entero = int(numero_texto)

if numero_entero % 2 == 0 and numero_entero > 0:
    print("El número es positivo y par")
elif numero_entero % 2 == 0 and numero_entero < 0:
    print("El número es divisible por 2 pero es negativo ")
elif numero_entero % 2 != 0 and numero_entero > 0:
    print("El número no es divisible por 2 pero es positivo")
else:
    print("El número no cumple ninguna condición")
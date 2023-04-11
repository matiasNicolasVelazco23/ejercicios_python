# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número es divisible por 3 y por 5" si el número es divisible
# por 3 y por 5, o "El número no es divisible por 3 y por 5" si el número no es
# divisible por 3 y por 5.

numero_texto = input("Ingrese un número: ")
numero_entero = int(numero_texto)
 
if numero_entero % 3 == 0 and numero_entero % 5 == 0:
    print("El número es divisible por 3 y por 5")
else:
    print("El número no es divisible por 3 y por 5")

# En resumen, aunque los códigos se escriben de manera similar, 
# lo que se está verificando es diferente debido a la naturaleza 
# de los números y sus relaciones.
#  se comprueb que 15/3= es 5 y se comprueba que 15/5 = es 3
#  el problema es diferente pero la lógica es la misma
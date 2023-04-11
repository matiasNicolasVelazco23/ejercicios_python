# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es positivo" si el primer número es mayor 
# que cero, "El segundo número es positivo" si el segundo número es mayor que
# cero, o "Ambos números son negativos" si los dos números son negativos.

numero_texto1 = input("Ingrese el primer número: ")
numero_texto2 = input("Ingrese el segundo número: ")
numero_entero1 = int(numero_texto1)
numero_entero2 = int(numero_texto2)

if numero_entero1 > 0 and numero_entero2 > 0:
    print("Ambos números son positivos")
elif numero_entero1 > 0:
    print("El primer número es positivo")
elif numero_entero2 > 0:
    print("El segundo número es positivo")
else:
    print("Ninguno de los números es positivo")
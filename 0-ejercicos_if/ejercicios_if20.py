# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "Los dos números son iguales" si los dos números son iguales,
# "El primer número es mayor" si el primer número es mayor que el segundo, o 
# "El segundo número es mayor" si el segundo número es mayor que el primero.

numero_texto1 = input("Ingrese un número entero")
numero_entero1 = int(numero_texto1)
numero_texto2 = input("Ingrese un número entero")
numero_entero2 = int(numero_texto1)

if numero_entero1 == numero_entero2:
    print("Los dós números son iguales")
elif numero_entero1 > numero_entero2:
    print("El primer número es mayor que el segundo")
else:
    print("El segundo número es el mayor")
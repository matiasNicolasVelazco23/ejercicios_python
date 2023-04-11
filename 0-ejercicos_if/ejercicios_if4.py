# Escribir un programa que le pida al usuario que ingrese dos números enteros
# , y luego imprima "El primer número es mayor" si el primer número es mayor que
# el segundo, "El segundo número es mayor" si el segundo número es mayor que el 
# primero, o "Los dos números son iguales" si los dos números son iguales.


numero_entero_texto1 = input("Ingresa primer número: ")
numero_entero1 = int(numero_entero_texto1)
numero_entero_texto2 = input("Ingrese segundo número: ")
numero_entero2 = int(numero_entero_texto2)

if (numero_entero1 > numero_entero2):
    print("El primer número es mayor")
elif(numero_entero1 == numero_entero2):
    print("El primer número y el segundo número son iguales")
else:
    print("El segundo número es mayor")
 
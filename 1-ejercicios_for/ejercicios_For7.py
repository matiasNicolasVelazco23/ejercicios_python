# Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.

numero_entero = int(input("Ingrese un número: "))

for numero in range(1, numero_entero+1):
    if numero % 2 != 0:
        print(numero, end= ' ')
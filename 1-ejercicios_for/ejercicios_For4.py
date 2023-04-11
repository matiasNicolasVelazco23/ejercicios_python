# Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

numero_entero = int(input("Ingrese un número: "))
acumulador_numeros = 0

for numero in range(1, numero_entero+1):
    if numero % 2 != 0:
        acumulador_numeros = acumulador_numeros+numero
print(acumulador_numeros)

#imprimo la suma de todos los impares mediante el acumulador de numeros
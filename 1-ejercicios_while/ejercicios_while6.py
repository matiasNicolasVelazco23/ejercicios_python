#Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.

numero_entero = int(input("Ingrese un número"))
numeros_anteriores = 0
suma_numeros = 0

while numeros_anteriores <= numero_entero:
    if numeros_anteriores %  2 == 0:
        suma_numeros+=numeros_anteriores
    numeros_anteriores+=1
print(suma_numeros)
        
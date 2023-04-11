#Dado un número entero n, imprimir la suma de todos los números impares menores o iguales a n.

numero_n = int(input("Ingrese un número ="))
numeros_anteriores = 0
suma_impares = 0

while numeros_anteriores <= numero_n:
    if numeros_anteriores % 2 ==1:
        suma_impares+= numeros_anteriores
    numeros_anteriores+=1
print(suma_impares)
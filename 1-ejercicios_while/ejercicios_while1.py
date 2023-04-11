#Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.

numero_entero = int(input("Ingrese número entero: "))
contador = numero_entero

while contador >= 1: #mientras el contador sea mayor o igual a 1 iteraa, cuando deja de serlo, sale
    print(contador)
    contador -= 1
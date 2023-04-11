#Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.

numero_entero = int(input("Ingrese número entero: "))
contador = 1

while contador <= numero_entero:   #mientras sea menor sigue iterando, pero se suma 1 cada vez que pasa
    print(contador)
    contador += 1
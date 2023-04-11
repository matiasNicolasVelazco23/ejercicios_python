#Dado un número entero n, imprimir la secuencia de números triangulares menores o iguales a n.

n = int(input("Ingrese un número entero: "))

for i in range(1, n+1):
    triangular = (i*(i+1)) // 2 # Fórmula para calcular números triangulares
    if triangular <= n:
        print(triangular, end=" ")

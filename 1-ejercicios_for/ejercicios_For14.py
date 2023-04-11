#Dado un número entero n, imprimir la secuencia de números perfectos menores o iguales a n.

numero_entero = int(input("Ingrese un número entero: "))

while numero_entero < 1:
    print("Numero inválido, es negativo, ingrese un número válido")
    numero_entero = int(input("Ingrese un número: "))

for numero_entero in range(1, numero_entero+1):
    raiz=numero_entero ** 0.5
    if raiz **2 == numero_entero:
        print(numero_entero, end= ' ')
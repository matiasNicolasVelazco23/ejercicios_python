#Dado un número entero n, imprimir todos los números impares menores o iguales a n.

numero_entero = int(input("Ingrese el número: "))
numero_anterior = 0

while numero_anterior<= numero_entero:
    if numero_anterior % 2 ==1:
        print(numero_anterior)
    numero_anterior+=1

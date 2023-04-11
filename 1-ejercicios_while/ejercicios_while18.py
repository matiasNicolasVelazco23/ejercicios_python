#Dado un número entero n, imprimir la suma de todos los números que son múltiplos de 5 menores o iguales a n.

numero_entero = int(input("Ingrese un número: "))
numeros_anteriores = 1
suma_multiplos_de_5= 0

while numeros_anteriores <= numero_entero:
    if numeros_anteriores % 5 == 0:
        suma_multiplos_de_5+=numeros_anteriores
    numeros_anteriores+=1
print(suma_multiplos_de_5)
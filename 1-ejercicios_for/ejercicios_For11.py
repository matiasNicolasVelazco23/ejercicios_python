# Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.


numero_texto = input("Ingrese un número: ")
numero_entero = int(numero_texto)

# Al establecer esPrimo en True al principio, asumimos que el número 
# es primo hasta que se demuestre lo contrario. Luego, dentro del ciclo 
# for anidado, se verifican todos los posibles divisores del número y si 
# se encuentra un divisor, se establece esPrimo en False.
for numero in range(2, numero_entero+1):
    esPrimo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            esPrimo = False
            break
    if esPrimo:
        print(numero, end = " ")

#para estos casos tengo que usar sí o sí un booleano
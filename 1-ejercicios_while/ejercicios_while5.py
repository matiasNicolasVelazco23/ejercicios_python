#Dado un número entero n, imprimir si el número es primo o no.

numero_entero = int(input("Ingrese un número entero: "))
es_primo = True
divisor = 2

while divisor < numero_entero:
    if numero_entero % divisor == 0:
        es_primo = False
        break
    divisor += 1

if es_primo:
    print("{0} es un número primo".format(numero_entero))
else:
    print("{0} no es un número primo".format(numero_entero))

    #print(f"{numero_entero} es un número primo") otra forma de usar el format

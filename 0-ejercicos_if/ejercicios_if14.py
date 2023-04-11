# Escribir un programa que le pida al usuario que ingrese un número entero
# , y luego imprima "El número es múltiplo de 4 y de 6" si el número es
# múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" si el
# número no es múltiplo de 4 y de 6.

numero_texto = input("Ingrese un número: ")
numero_entero = int(numero_texto)

if numero_entero % 4 == 0 and numero_entero%6 == 0:
    print("El número  es múltiplo de 4 y de 6")
else:
    print("El número no es múltiplo de 4 y 6")

# se comprueba que multiplicando 4*n=24   se comprueba que al multiplica 6*n=24
#  el problema es diferente pero la lógica es la misma
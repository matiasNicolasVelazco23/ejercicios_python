# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número ingresado es par" si el número es divisible por
# 2, o "El número ingresado es impar" si el número no es divisible por 2.

numero_texto = input("Ingrese un número: ")

numero_entero = (int(numero_texto))
#hago casting, con el casteo a int
resto = numero_entero%2 
#escribo la operación en una variable

if (resto == 0): 
    #uso la variable en el if para comparar
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")
#otra forma válida de plantearlo
# if(int (numero_texto) % 2 == 0): *casteo en la condicion el numero_texto
#      print("El número ingresado es par")
# else:
#      print("El número ingresado es impar")

  
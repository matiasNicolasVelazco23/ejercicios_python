
# Escribir un programa que le pida al usuario que ingrese un número 
# entero positivo, y luego imprima "El número es un cuadrado perfecto" 
# si el número es un cuadrado perfecto, o "El número no es un cuadrado perfecto" 
# si el número no es un cuadrado perfecto.

# Pedimos al usuario que ingrese un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

# Validamos que el número ingresado sea positivo
while num < 1:
    num = int(input("El número debe ser positivo. Por favor "
                    "ingrese otro número: "))
#sacamos la raiz del número para obtener el operador base de la potenciación
# por ejemplo 25, el operador base sería 5
raiz= num**0.5

#acá usamos la raiz, y si al potenciarla 2 veces da como resultado el num 
#original es un cuadrado perfecto
if raiz ** 2 == num:
    print("El número es sun cuadrado perfecto")
else:
    print("El número no es un cuadrado perfecto")
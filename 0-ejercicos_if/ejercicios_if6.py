# Escribir un programa que le pida al usuario que ingrese su nombre y su edad
# , y luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o
# igual a 65, o "No puedes votar" si la edad es menor a 18 o mayor a 65.

edad_texto = input("Ingrese su edad: ")
edad_entero = (int(edad_texto))

if edad_entero >= 18 and edad_entero <= 65:
    print("Puedes votar")
else:
    print("No puedes votar")
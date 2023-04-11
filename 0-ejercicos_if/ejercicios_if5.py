# Escribir un programa que le pida al usuario que ingrese su nombre, y luego
# imprima "Hola [nombre]" si el nombre ingresado es "Juan", "María" o "Pedro",
# o "Hola desconocido" si el nombre ingresado no es uno de esos tres.

nombre= input("Ingrese un nombre: ")

if (nombre == "Juan"):
    print("Hola Juan")
elif (nombre == "Maria"):
    print("Hola Maria")
elif (nombre == "Pedro"):
    print("Hola Pedro")
else:
    print("Hola desconocido")
# Escribir un programa que le pida al usuario que ingrese su edad,              
# y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18, o 
# "Eres menor de edad" si la edad es menor a 18.}

edad_texto = input("Ingrese su edad: ")
edad_entero = (int(edad_texto))

if (edad_entero >= 18):
    print("Eres mayor de edad")
elif(edad_entero < 0):
    print("No podés poner una edad negativa")

else:
    print("Eres menor de edad")  
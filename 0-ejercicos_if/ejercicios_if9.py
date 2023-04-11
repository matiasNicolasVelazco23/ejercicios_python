# Escribir un programa que le pida al usuario que ingrese una letra, y luego
# imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), o
# "Es una consonante" si la letra es una consonante.

ingreso_letras = input("Ingrese una letra: ")

if (ingreso_letras == "a" or ingreso_letras == "e" or ingreso_letras == "i" or
    ingreso_letras == "o" or ingreso_letras == "u"): 
    print("Es una vocal")
else:
    print("Es una consonante")
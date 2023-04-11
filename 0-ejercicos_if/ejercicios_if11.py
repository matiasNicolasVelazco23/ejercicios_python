# Escribir un programa que le pida al usuario que ingrese su edad, y luego
# imprima "Eres un niño" si la edad es menor a 12, "Eres un adolescente" 
# si la edad está entre 12 y 17 inclusive, "Eres un adulto" si la edad
# está entre 18 y 64

ingreso_edad_texto = input ("Ingrese su edad: ")
edad_entero= int(ingreso_edad_texto)

if edad_entero < 12 and edad_entero>=0:
    print("Eres un niño")
elif edad_entero >=12 and edad_entero <=17:
    print("Eres un adolescente")
elif edad_entero >=18 and edad_entero <=64:
    print("Eres un adulto")
else:
    print("Ingrese una edad válida")
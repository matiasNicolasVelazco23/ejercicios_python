# Crear una función que calcule el área de un círculo. Recibe un parámetro 
# (radio) y devuelve el área del círculo.

def calcular_area_circulo(radio):
    pi = 3.14159
    resultado= pi * radio**2
    return resultado

area_circulo= calcular_area_circulo(8)
print(area_circulo)
# Crear una función que calcule el área de un triángulo.
# Recibe dos parámetros (base y altura) y devuelve el área.

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


base = 10
altura = 5
area = area_triangulo(base, altura)
print("El área del triángulo es:", area)
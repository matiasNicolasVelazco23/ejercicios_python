# Crear una función que calcule el descuento aplicado a un producto.
# Recibe dos parámetros (precio original y precio con descuento) y
# devuelve el porcentaje de descuento aplicado.


def calcular_descuento(precio_original, precio_con_descuento):
    descuento = precio_original - precio_con_descuento
    porcentaje_descuento = (descuento / precio_original) * 100
    return porcentaje_descuento
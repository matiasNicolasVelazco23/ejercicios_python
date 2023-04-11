# Crea un diccionario que represente una lista de las compras. 
# Cada clave del diccionario debe ser el nombre de un producto y
# cada valor debe ser su cantidad. Pedir al usuario que ingrese 
# el nombre del producto e imprimir la cantidad

diccionario_lista_de_compras = {
    "manzanas": 5,
    "plátanos": 3,
    "pan": 2,
    "leche": 1,
    "huevos": 12,
    "queso": 2
}

ingreso_producto = input("Ingrese el nombre del producto: ")

for producto, valor in diccionario_lista_de_compras.items():
    if ingreso_producto == producto:
        print(valor)
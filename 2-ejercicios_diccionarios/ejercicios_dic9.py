# Crea un diccionario que contenga las capitales de los países de América del Sur. 
# Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.

diccionario_capitales = {
    "Argentina": "Buenos Aires",
    "Bolivia": "La Paz",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Guyana": "Georgetown",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Suriname": "Paramaribo",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}

nombre_pais = input("Ingrese nombre del país")

for clave, valor in diccionario_capitales.items():
    if nombre_pais == clave:
        print(valor)
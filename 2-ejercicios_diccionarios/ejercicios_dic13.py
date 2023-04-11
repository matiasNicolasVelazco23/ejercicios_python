# Crea un diccionario que contenga el nombre y el nivel de dificultad de varios
# juegos de mesa. Luego, pedirle al usuario un nivel de dificultad, buscar los 
# que coinciden e imprimir sus nombres

diccionario_juegos_de_mesa = {
    "Ajedrez": "Alto",
    "Risk": "Medio",
    "Jenga": "Bajo"
}

ingreso_dificultad = input("Ingrese dificultad: ")

for clave, valor in diccionario_juegos_de_mesa.items():
    if ingreso_dificultad == valor:
        print("{0}".format(clave))
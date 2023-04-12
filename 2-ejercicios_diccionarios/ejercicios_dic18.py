# Crea un diccionario que represente los juegos de una consola, donde las claves
# son los nombres de los juegos y los valores son las puntuaciones correspondientes.
# Solicita al usuario el nombre de un juego y luego su puntuación,
# si el juego no existe agregarlo y si existe actualizar su puntuación 

diccionario_juegos = {
    "Fifa23": 7,
    "Gta": 7,
    "CandyCrush": 8
}

ingreso_juego = input("Ingrese juego: ")
ingreso_puntuacion = int(input("Ingrese puntuación "))

for clave, valor in diccionario_juegos.items():
    clave2=ingreso_juego
    if  clave2 == clave:
        diccionario_juegos[ingreso_juego] = ingreso_puntuacion
        print("Se actualizó la puntuación del"
             "juego {0} a {1}.".format(ingreso_juego, ingreso_puntuacion))
        break
  
    else:
        clave = ingreso_juego
        diccionario_juegos[ingreso_juego] = ingreso_puntuacion
        print("Se agregó el juego {0} con una puntuación de {1}.".format(ingreso_juego, ingreso_puntuacion))


        
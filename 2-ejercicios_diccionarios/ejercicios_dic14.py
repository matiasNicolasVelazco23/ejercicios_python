# Crea un diccionario que contenga el nombre como clave y el puntaje como valor
# de varios jugadores en un juego. Luego, pedirle al usuario el nombre del jugador
# y nuevo puntaje y actualizar el valor correspondiente en el diccionario.

diccionario_jugadores = {
    "Ana": 120,
    "Juan": 80,
    "María": 200,
    "Carlos": 150
}


for clave, valor in diccionario_jugadores.items():
    clave2=input("Ingrese nombre del jugador: ")
    valor2=input("Ingrese nuevo valor: ")
    if  clave == clave2:
        diccionario_jugadores[clave] = valor2
        print(diccionario_jugadores[clave])
        break

print("El nuevo puntaje del jugador {0} es {1}".format(clave2,diccionario_jugadores[clave2]))
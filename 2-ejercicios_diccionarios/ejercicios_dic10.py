# Crea un diccionario que represente las notas de un examen de varios estudiantes
# , donde las claves son los nombres de los estudiantes y los valores son sus notas.
# Imprime el promedio de las notas.

diccionario_notas = {
    "Juan": 9,
    "Emilia": 2,
    "Daniela": 3,
    "Pepe": 8,
    "José": 1,
    "Herta": 10,
    "Dylan": 5
}    
acumulador_notas = 0
contador_notas = 0
for valor in diccionario_notas:
    valor=diccionario_notas[valor]
    acumulador_notas+=valor
    contador_notas+=1

promedio_notas = acumulador_notas/contador_notas
promedio_notas = round(promedio_notas,2)

print(promedio_notas)
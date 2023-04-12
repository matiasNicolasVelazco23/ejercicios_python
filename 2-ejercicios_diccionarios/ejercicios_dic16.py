#Crea un diccionario que represente una lista de tareas pendientes, 
#donde las claves son las tareas y los valores son "True" si están
# completadas y "False" si no lo están. Solicita al usuario el nombre de una 
#tarea y modifica el valor para marcarla como completada. Imprimir el listado de tareas pendientes



diccionario_tareas_pendientes = {"Ducha" : True, "Comer" : False,
                                 "Ejercicios" : False, "Médico" : True ,
                                 "Dormir": False}
clave2 = input("Ingrese una tarea para marcarla como completada")

for clave, valor in diccionario_tareas_pendientes.items():
    if clave2 == clave:
        diccionario_tareas_pendientes[clave] = True
        tarea_completa= "esta completa"
        break
print("La tarea {0} {1}".format(clave,tarea_completa))

for clave, valor in diccionario_tareas_pendientes.items():
    if valor==False:
        valor2= "pendiente"
        print("La tarea {0} está {1}".format(clave,valor2))
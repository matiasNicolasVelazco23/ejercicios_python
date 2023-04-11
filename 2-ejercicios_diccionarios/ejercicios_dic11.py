#Crea un diccionario que represente una lista de tareas por hacer. 
#Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe 
#ser su estado (los estados son:  pendiente, en proceso, completada). 
#Imprimir todas las tareas seguido de su estado

diccionario_de_tareas = {"comer" : "completada" , "ducharme" : "completada",
                         "del cole" : "en proceso" , "ejercicios" : "pendiente"}

for tarea, estado in diccionario_de_tareas.items():
    print("La tarea {0} está {1}".format(tarea,estado))
# Crea un diccionario que represente las edades de varias personas, donde las 
# claves son los nombres de las personas y los valores son sus edades. 
# Imprime la edad de la persona más joven.
diccionario_edades = {
    "Juan": 11,
    "Emilia": 22,
    "Daniela": 34,
    "Pepe": 8,
    "José": 1,
    "Herta": 2,
    "Dylan": 29
}    
flag_primeringreso= True

for edad in diccionario_edades.keys():
    edad = diccionario_edades[edad]
    if flag_primeringreso == True:
        el_menor = edad
        flag_primeringreso = False

    elif edad < el_menor:
        el_menor = edad

print(el_menor)



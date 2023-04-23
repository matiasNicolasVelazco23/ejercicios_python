# Crear una función que calcule el promedio de edad de un grupo de personas.
# Recibe una lista de edades y devuelve el promedio.

def calcular_promedio_edad(edades):
    sum_edades = 0
    for edad in edades:
        sum_edades += edad
    promedio_edades = sum_edades / len(edades)
    return promedio_edades

edades = [22, 25, 30, 35]
sum_edades = sum(edades)
print(sum_edades)  # salida: 112
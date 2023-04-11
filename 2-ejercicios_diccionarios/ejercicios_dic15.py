# Crea un diccionario que contenga el nombre y el sueldo de varios empleados. 
# Luego, permite al usuario aumentar el sueldo de un empleado y 
# actualizar el valor correspondiente en el diccionario.
diccionario_sueldos_empleados = {"Juan" : 89900, "Daniela" : 56000, "Moria" : 112000}

# ingrese_empleado = input("Ingrese empleado: ")
# if ingrese_empleado in diccionario_sueldos_empleados.keys():
#     aumento_sueldo = int(input("Ingrese aumento acordado: "))
#     sueldo_actual = diccionario_sueldos_empleados[ingrese_empleado]
#     nuevo_sueldo = sueldo_actual + aumento_sueldo
#     diccionario_sueldos_empleados[ingrese_empleado] = nuevo_sueldo
#     print("El nuevo sueldo de {0} es {1}".format(ingrese_empleado, nuevo_sueldo))
# else:
#     print("El empleado ingresado no existe en el diccionario.")

for clave, valor in diccionario_sueldos_empleados.items():
    empleado=input("Ingrese nombre del empleado: ")
    if  clave == empleado:
        aumento_sueldo=int(input("Ingrese aumento de sueldo: "))
        sueldo_actual = diccionario_sueldos_empleados[clave]
        nuevo_sueldo= aumento_sueldo+sueldo_actual
        print(diccionario_sueldos_empleados[clave])
        break

print("El nuevo sueldo de {0} es {1}".format(clave,nuevo_sueldo))
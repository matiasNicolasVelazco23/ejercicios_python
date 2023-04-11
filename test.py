#for i in range(-2,5):
#    print(i)

# lista_de_nombres = ["LIO","EMA", "VERO", "EMA", "VERO", "EMA", "VERO", "EMA",
#                      "VERO", "EMA", "VERO", "EMA", "VERO"]
# for indice in range (10):
#     print (lista_de_nombres [indice]) 
#     #si imprimo índice imprime los primeros 10
#     #si imprimo la lista de nombres en base al índice imprime los primeros 10 nombres

# lista_numeros_texto = []
# for indice in range (10):
#     numero_texto = input ("Numero: ")
#     if(numero_texto == "EXIT"):
#         break
#         lista_numeros_texto.append(numero_texto)
#         #el .append agrega un ementos a una lista


# lista =[1,2,3,4]

# lista.pop(2)

# print(lista)  Elimina el índice

# n = int(input())
# for i in range(1, n+1):
#     print(i, end='')
# print()

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
    empleado=input("Ingrese nombre del empleado")
    aumento_valor=input("Ingrese aumento de sueldo")
    if  clave == empleado:
        diccionario_sueldos_empleados[clave] = aumento_valor+diccionario_sueldos_empleados[empleado]
        print(diccionario_sueldos_empleados[clave])
        break
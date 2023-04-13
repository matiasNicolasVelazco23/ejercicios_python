# Gimnasio - Lista de diccionarios
# Un gimnasio desea llevar el control de sus miembros. 
# Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía 
# (por ejemplo, mensual o anual). La información se encuentra almacenada en una lista de listas,
# donde cada sublista representa a un miembro y contiene los siguientes elementos: número de identificación
# , nombre, edad y tipo de membresía.

lista_gimnasio = [{"ID" : 92, "nombre" : "Juan", 
                   "edad" : 23,"membresia" : "anual"}, 
                  {"ID" : 23, "nombre" : "Mariela", 
                   "edad" : 21, "membresia" : "mensual"},
                  {"ID" : 54, "nombre" : "Luciana", 
                   "edad" : 20, "membresia" : "anual"}]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
          # Solicitar los datos del nuevo miembro al usuario
        nuevo_id = int(input("Ingrese el ID del nuevo miembro: "))
        nuevo_nombre = input("Ingrese el nombre del nuevo miembro: ")
        nueva_edad = int(input("Ingrese la edad del nuevo miembro: "))
        nueva_membresia = input("Ingrese la membresía del nuevo miembro"
                                 "(anual/mensual): ")

        # Crear un diccionario con los datos del nuevo miembro
        nuevo_miembro = {"ID": nuevo_id, "nombre": nuevo_nombre,
                          "edad": nueva_edad, "membresia": nueva_membresia}

        # Agregar el nuevo miembro a la lista de gimnasio
        lista_gimnasio.append(nuevo_miembro)
        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for miembro in lista_gimnasio:
            print("ID: {0}, Nombre: {1},Edad: {2}, Membresía: {3}"
                  .format(miembro['ID'] ,miembro['nombre'], 
                          miembro['edad'] ,miembro['membresia']))
 
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        # Solicitar el ID del miembro cuya membresía se va a actualizar
        id_a_actualizar = int(input("Ingrese el ID del miembro cuya membresía" 
                                    "desea actualizar: "))

        # Buscar el miembro en la lista de gimnasio y actualizar su membresía
        encontrado = False
        for miembro in lista_gimnasio:
            if miembro["ID"] == id_a_actualizar:
                encontrado = True
                nueva_membresia = input("Ingrese la nueva membresía del"
                                        "miembro (anual/mensual): ")
                miembro["membresia"] = nueva_membresia
                print("La membresía del miembro ha sido actualizada" 
                      "correctamente a {0}".format(nueva_membresia))
                break

        # Mostrar un mensaje de error si no se encontró el miembro
        if not encontrado:
            print("No se encontró ningún miembro con ese ID.")
        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_buscado = input("Ingrese el ID del miembro que desea buscar: ")

        for miembro in lista_gimnasio:
            if miembro["ID"] == int(id_buscado):
                print("Información del miembro con ID {0}: Nombre: {1}, Edad:"
                      "{2}, Membresía: {3}".format(
                      miembro["ID"], 
                      miembro["nombre"], 
                      miembro["edad"], 
                      miembro["membresia"]))
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        suma_edades = 0
        cantidad_miembros = len(lista_gimnasio)

        for miembro in lista_gimnasio:
            suma_edades += miembro["edad"]

        promedio_edad = suma_edades / cantidad_miembros

        print("El promedio de edad de los miembros es: {0}"
              .format(promedio_edad))
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        miembro_mas_joven = None
        miembro_mas_viejo = None

        for miembro in lista_gimnasio:
            if (miembro_mas_joven is None or miembro["edad"] <
                miembro_mas_joven["edad"]):
                miembro_mas_joven = miembro
    
            if (miembro_mas_viejo is None or miembro["edad"] >
                 miembro_mas_viejo["edad"]):
                miembro_mas_viejo = miembro

        print("El miembro más joven es: Nombre: {0}, Edad: {1}"
              .format(miembro_mas_joven["nombre"], miembro_mas_joven["edad"]))
        print("El miembro más viejo es: Nombre: {0}, Edad: {1}"
              .format(miembro_mas_viejo["nombre"], miembro_mas_viejo["edad"]))
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

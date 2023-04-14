# Gimnasio - Listas paralelas
# Un gimnasio desea llevar el control de sus miembros. Cada miembro tiene un 
# número de identificación, nombre, edad y tipo de membresía (por ejemplo, mensual o anual)
# . La información se encuentra almacenada en cuatro listas paralelas: una lista con los números de identificación
# , otra lista con los nombres, una lista con las edades y una lista con los tipos de membresía.

miembro_id = [21,42,55,80]
miembro_nombre= ["Diana", "Ramiro", "Daniel", "Martina"]
miembro_edad= [19, 18, 15, 21]
miembro_membresia = ["anual", "mensual", "anual", "mensual"]
indice=0

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
        nuevo_id = int(input("Ingrese nuevo id: "))
        miembro_id.append(nuevo_id)
        nuevo_miembro = input("Ingrese un nuevo miembro: ")
        miembro_nombre.append(nuevo_miembro)
        nueva_edad = int(input("Ingrese nueva edad: "))
        miembro_edad.append(nueva_edad)
        nueva_membresia = input("Ingrese tipo de membresia"
                                "(Anual o Mensual): ")
        miembro_membresia.append(nueva_membresia)

        print(miembro_id, miembro_nombre, miembro_edad, miembro_membresia)

        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for indice in range(len(miembro_id)):
            print("Nro ID: {0}\tNombre: {1}\tEdad: {2}\tTipo "
               "membresia: {3}".format(miembro_id[indice],
                                  miembro_nombre[indice],
                                  miembro_edad[indice],
                                  miembro_membresia[indice]))

       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        buscar_id= int(input("Ingrese un id: "))
        for indice in range(len(miembro_id)):
            if buscar_id == miembro_id[indice]:
               cambio_de_membresia=input("Ingrese la nueva membresia: ")
               miembro_membresia[indice]=cambio_de_membresia
               print("Sí, exite"
                     ", la membresia se actualizó a {0}"
                     .format(miembro_membresia[indice]))
               break
               
            else:
                print("Este id no se encuentra en la lista de ID's")
            


        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        ingrese_un_miembro=int(input("Ingrese una id existente"))
        for indice in range(len(miembro_id)):
            if ingrese_un_miembro == miembro_id[indice]:
                print(miembro_id[indice], miembro_nombre[indice], 
                      miembro_edad[indice], miembro_membresia[indice])
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        acumulador_edades = 0
        for indice in range(len(miembro_id)):
            print(indice)
            acumulador_edades+=miembro_edad[indice]
        indice=indice+1
        promedio_edades= acumulador_edades / indice
        print(promedio_edades)
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        flagPrimerJoven = True
        edad_menor = miembro_edad[0]
        miembro_edad_menor = miembro_nombre[0]
        for indice in range(len(miembro_id)):
            if  miembro_edad[indice] <= edad_menor:
                edad_menor = miembro_edad[indice]
                nombre_edad_menor = miembro_nombre[indice]
        print("El menor es {0}"
            "y su edad es {1}".format(nombre_edad_menor, edad_menor))
        flagPrimerviejo = True
        edad_viejo = miembro_edad[0]
        miembro_edad_viejo = miembro_nombre[0]
        for indice in range(len(miembro_id)):
            if  miembro_edad[indice] >= edad_viejo:
                edad_viejo = miembro_edad[indice]
                nombre_edad_viejo = miembro_nombre[indice]
        print("El menor es {0}"
            "y su edad es {1}".format(nombre_edad_viejo, edad_viejo))
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

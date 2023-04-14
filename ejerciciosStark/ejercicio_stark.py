from data_stark import lista_personajes

#Recorrer la lista imprimiendo por consola el nombre de cada superhéroe

#Construir un menú que permita elegir qué dato obtener


while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Recorrer la lista imprimiendo por" 
          "consola el nombre de cada superhéroe")
    print("2. Recorrer la lista imprimiendo por consola nombre de cada"
          "superhéroe junto a la altura del mismo")
    print("3. Recorrer la lista y determinar cuál es el" 
          "superhéroe más alto (MÁXIMO)")
    print("4. Recorrer la lista y determinar cuál es el superhéroe" 
          "más bajo (MÍNIMO)")
    print("5. Recorrer la lista y determinar la altura"
           "promedio de los  superhéroes (PROMEDIO)")
    print("6. Informar cual es el Nombre del superhéroe asociado a cada uno de"
           "los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("6. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("7. Ordenar el código implementando una función para cada uno de los valores informados.")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        for personaje in lista_personajes:
          print(personaje["nombre"])

        pass
       
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
#"2. Recorrer la lista imprimiendo por consola nombre de cada "superhéroe junto a la altura del mismo"
        for personaje in lista_personajes:
            print(personaje["nombre"], personaje["altura"])
        pass
 
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        #3. Recorrer la lista y determinar cuál es el "superhéroe más alto (MÁXIMO)")
        for personaje in lista_personajes:
           miembro_mas_alto = None
           if (miembro_mas_alto is None or personaje):
               pass
        #      
        #         miembro_mas_joven = miembro
    
        #     if (miembro_mas_viejo is None or miembro["edad"] >
        #          miembro_mas_viejo["edad"]):
        #         miembro_mas_viejo = miembro

        # print("El miembro más joven es: Nombre: {0}, Edad: {1}"
        #       .format(miembro_mas_joven["nombre"], miembro_mas_joven["edad"]))
        # print("El miembro más viejo es: Nombre: {0}, Edad: {1}"
        #       .format(miembro_mas_viejo["nombre"], miembro_mas_viejo["edad"]))

        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":

        pass

    elif opcion == "8":
        print("Caso 8")
    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")
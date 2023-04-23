####Me falta indentar!!!

from data_stark import lista_personajes


#estas son las funciones que uso en las opciones
def mostrar_superheroes():
    for personaje in lista_personajes:
        print(personaje["nombre"])
    
def mostrar_nombre_y_altura():
    for personaje in lista_personajes:
        print("El nombre es {0} y la altura es {1}".format(personaje
                                                           ["nombre"], 
                                                           personaje
                                                           ["altura"]))
def mostrar_miembro_mas_alto():
    for indice in range(len(lista_personajes)):
        # si miembro más alto es menor que listapersonajes[indice]["altura"] entonces el nuevo máximo es listapersonajes[indice]["altura"]
        if (indice == 0  or miembro_mas_alto < float(lista_personajes[indice]["altura"])):
            # guardo el miembro más alto y el índice más alto para usarlo
            miembro_mas_alto = float(lista_personajes[indice]["altura"])
            maximo_indice = indice
    # imprimo el superhéroe más alto y su altura
    print("El superhéroe más alto es {0} y su altura es {1}".format(lista_personajes[maximo_indice]["nombre"]
                                                                    , lista_personajes[maximo_indice]["altura"]))
def mostrar_miembro_mas_bajo():
    for indice in range(len(lista_personajes)):
            #si miembro más bajo es mayor que listapersonajesindicealtura entonces el nuevo minimo es listapersonajesindicealtura
        if (indice == 0  or float(lista_personajes[minimo_indice]["altura"]) > float(lista_personajes[indice]["altura"])):
                #guardo el miembro más bajo y el índice mas bajo para usarlo
                minimo_indice = indice
                #acá sé que puedo omitir imprimir el dato de la altura, pero lo usé para probar
    print("El super heroe más bajo es {0} y su altura es {1}".format(lista_personajes[minimo_indice]["nombre"]
                                                                        ,lista_personajes[minimo_indice]["altura"]))
def mostrar_promedio():
    suma_alturas=0
        
    for personaje in lista_personajes:
            altura = float(personaje['altura'])
            suma_alturas += altura

    promedio_alturas = suma_alturas / len(lista_personajes)
    # Opción 6: Buscar el miembro más joven y el más viejo
    print("El promedio de altura de los miembros es {0} ".format(promedio_alturas))

#Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def informar_maximo_minimo():
    for indice in range(len(lista_personajes)):
        # si miembro más alto es menor que listapersonajes[indice]["altura"] entonces el nuevo máximo es listapersonajes[indice]["altura"]
        if (indice == 0  or miembro_mas_alto < float(lista_personajes[indice]["altura"])):
            # guardo el miembro más alto y el índice más alto para usarlo
            miembro_mas_alto = float(lista_personajes[indice]["altura"])
            maximo_indice = indice
    for indice in range(len(lista_personajes)):
        if (indice == 0  or float(lista_personajes[minimo_indice]["altura"]) > float(lista_personajes[indice]["altura"])):
                minimo_indice = indice
    print("El superhéroe más alto es {0} y el más bajo es {1}".format(lista_personajes[maximo_indice]["nombre"]
                                                                    , lista_personajes[minimo_indice]["nombre"]))
def mostrar_nombre_personaje_mas_y_menos_pesado():
    for indice in range(len(lista_personajes)):
        if (indice == 0  or float(lista_personajes[minimo_indice]["peso"]) > float(lista_personajes[indice]["peso"])):
                minimo_indice = indice
    for indice in range(len(lista_personajes)):
        if (indice == 0  or float(lista_personajes[maximo_indice]["peso"]) < float(lista_personajes[indice]["peso"])):
                maximo_indice = indice
    print("El menos pesado es {0} y el más pesado es {1} ".format(lista_personajes[minimo_indice]["nombre"], 
                                                                  lista_personajes[maximo_indice]["nombre"]))
                                                            
def todos_los_valores_informados():

        mostrar_superheroes()
        mostrar_nombre_y_altura()  
        mostrar_miembro_mas_alto()
        mostrar_miembro_mas_bajo()
        mostrar_promedio()
        informar_maximo_minimo()
        mostrar_nombre_personaje_mas_y_menos_pesado()
     


while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    # \n salto de linea
    print("1. Recorrer la lista imprimiendo por" 
          "consola el nombre de  cada  superhéroe")
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
    print("7. Calcular e informar cual es el superhéroe más y menos pesado.")
    print("8. Ordenar el código implementando una función para cada uno de los"
          "valores informados.")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")

#tengo que escribir la función sin def para llamarla, la función la hago arriba
    if opcion == "1":
        mostrar_superheroes()
       
    elif opcion == "2":
        mostrar_nombre_y_altura()  
 
    elif opcion == "3":
        mostrar_miembro_mas_alto()

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        mostrar_miembro_mas_bajo()


    # Opción 5: Calcular el promedio de altura de los miembros
    elif opcion == "5":
        mostrar_promedio()

    elif opcion == "6":
        informar_maximo_minimo()
        pass

    elif opcion == "7":
        mostrar_nombre_personaje_mas_y_menos_pesado()

    elif opcion == "8":
        todos_los_valores_informados()
    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

        
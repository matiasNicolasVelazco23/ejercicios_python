from data import lista_bzrp

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
    respuesta_str = input("\nIngrese la opción deseada: ")
    #falta validar
    respuesta_int = int(respuesta_str)

    match(respuesta_int):
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            #itera la lista_bzrp, a esa variable le asigno una clave, que va a llegar con un valor
            for video in lista_bzrp:
                print("Titulo del vide: {0}, views {1}, y el lenght es {2}".format(video["title"], video["views"], video["length"]))
        case 8: 
            break
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

# lista_diccionarios = [    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},    {"nombre": "María", "edad": 30, "ciudad": "Barcelona"},    {"nombre": "Pedro", "edad": 35, "ciudad": "Valencia"}]

# primer_elemento = lista_diccionarios[0]

# print(primer_elemento)

# nombre = primer_elemento["nombre"]

# print(nombre)

# for diccionario in lista_diccionarios:
#     nombre = diccionario["nombre"]
#     edad = diccionario["edad"]
#     print(f"{nombre} tiene {edad} años")

#clase contador de algo en un diccionario
lista_pelicula = [{"Nombre" : "Vover1", "genero": "Drama"},
{"Nombre" : "Vover2", "genero": "Ficcidjsada"},
{"Nombre" : "Vover3", "genero": "Drama"},
{"Nombre" : "Vover4", "genero": "Ficcion"},
{"Nombre" : "Vover5", "genero": "Drama"}]

def calcular_peliculas_por_genero():
    diccionarioContadorDePeliculas= {}

    for pelicula in lista_pelicula:
        texto_genero= pelicula["genero"]
        if texto_genero in diccionarioContadorDePeliculas:
            diccionarioContadorDePeliculas[texto_genero]+= 1
        else:
            diccionarioContadorDePeliculas[texto_genero]=1
    return diccionarioContadorDePeliculas


    for pelicula in lista_pelicula:
        texto_genero= pelicula["genero"]
        if texto_genero in diccionarioContadorDePeliculas:
            diccionarioContadorDePeliculas[texto_genero]+= 1
        else:
            diccionarioContadorDePeliculas[texto_genero]=1
    return diccionarioContadorDePeliculas


contadores = calcular_peliculas_por_genero()
print(contadores)
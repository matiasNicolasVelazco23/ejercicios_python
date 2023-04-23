from data import lista_bzrp
'''
[
    
    {
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
    }
]
1 - Tema mas visto
2 - Tema menos visto
3 - Tema mas largo
4 - Tema mas corto
5 - Duracion promedio de temas
6 - Promedio de vistas 
7 - Salir
'''


def print_tema(tema):
    '''
    Mustra un tema por terminal
    Recibe el diccionario del tema a mostrar
    Retorno - No aplica
    '''    
    print("\nTitulo: {0}- views: {1} - length: {2}".format(
                                    tema['title'],
                                    tema['views'],
                                    tema['length']))

def mostrar_lista_videos (lista_de_temas):
    '''
    Muestra una lista de temas por terminal
    Recibe la lista de temas
    Retorno - No aplica
    '''    
    for tema in lista_de_temas:
        print_tema(tema)

# Doy máximo True para que entre al if y calcle el máximo, para que de el menos visto, entrará al false.
def calcular_tema_mas_menos_por_clave(lista_de_temas,clave,maximo=True ):
    '''
    Calcula el tema mas/menos por clave ( views - length )
    Recibe la lista de temas,clave ( views - length ) y parametro que indica si busca max o min
    Retorno - El dict del tema mas/menos visto
    '''    

    indice_max_min = 0
    for indice_actual in range(1,len(lista_de_temas)):
        if(maximo):
            if(lista_de_temas[indice_actual][clave] > lista_de_temas[indice_max_min][clave]):
                indice_max_min = indice_actual
        else:
            if(lista_de_temas[indice_actual][clave] < lista_de_temas[indice_max_min][clave]):
                indice_max_min = indice_actual

    return lista_de_temas[indice_max_min]

#retorna todos los valores en ese índice y lo asigno a máximo
maximo=calcular_tema_mas_menos_por_clave(lista_bzrp, clave="views", maximo=True) #calcula máximo
#imprimo lo que contiene ese índice máximo
#{'title': 'NATHY PELUSO || BZRP Music Sessions #36', 'views': 333843650, 'length': 176, 'img_url': 'https://i.ytimg.com/vi/0OkiUUU3Odw/sddefault.jpg', 'url': 'https://youtube.com/watch?v=0OkiUUU3Odw', 'date': '2020-11-27 00:00:00'}
print(maximo)



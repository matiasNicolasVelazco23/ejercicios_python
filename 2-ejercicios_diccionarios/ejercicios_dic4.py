# Crea un diccionario que contenga la información de una dirección: nombre de 
# la calle, altura, localidad, código postal, partido y provincia. Luego, imprime
# el nombre de la calle, seguido de su altura.

dic_info_dirrecionPersona = {"nombre_calle" : "CallePepito" , "altura" : "500" ,
                    "localidad" : "LocalidadPepito" , 
                    "codigo_postal" : "1439" , "partido" : "Partido Pepito" ,
                    "Provincia" : "Santa Fe"}
print ("El nombre de la calle "
       "es {0} a la altura {1}".format(dic_info_dirrecionPersona
                                      ["nombre_calle"],
                                      dic_info_dirrecionPersona
                                      ["altura"]))
#poner varios valores en un .format
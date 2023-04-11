#Dada una lista de números, imprimir la suma de los números en la lista que 
#son mayores que el promedio de la lista.

lista_de_numeros = [8,12,15,21,2]
acumulador_de_numeros = 0
contador_de_numeros = 0
acumulador_de_numeros_mayores = 0

for numero in lista_de_numeros:
    acumulador_de_numeros+=numero
    contador_de_numeros+=1

promedio = acumulador_de_numeros/contador_de_numeros
print(promedio)

for numero in lista_de_numeros:
    if numero > promedio:
        acumulador_de_numeros_mayores+=numero
    
print(acumulador_de_numeros_mayores)



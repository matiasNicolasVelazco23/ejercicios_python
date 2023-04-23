#Crear una función que convierta grados Celsius a grados Fahrenheit. 
#Recibe un parámetro (grados Celsius) y devuelve el resultado en grados Fahrenheit.

def pasar_de_celsius_a_fahrenheit(grados_celsius):
    grados_farenheit= (grados_celsius*1.8)+32
    return grados_farenheit


ingrese_grados_celsius_texto = input("Ingrese grados Celsius")
ingrese_grados_celsius_entero = int(ingrese_grados_celsius_texto)

pasaje_a_farenheit = pasar_de_celsius_a_fahrenheit(ingrese_grados_celsius_entero)
print(pasaje_a_farenheit)

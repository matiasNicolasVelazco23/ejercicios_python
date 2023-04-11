# Dado un número entero n, imprimir todos los números perfectos menores o iguales a n.
# Los números perfectos son aquellos números enteros positivos que son iguales 
# a la suma de sus divisores propios (excluyendo al propio número). En otras palabras,
# si sumamos todos los divisores propios de un número (excluyendo el número en sí mismo)
# y el resultado es igual al número, entonces ese número se considera un número perfecto.

# Por ejemplo, el primer número perfecto es 6, ya que sus divisores propios son 
# 1, 2 y 3, y 1 + 2 + 3 = 6. Otros ejemplos de números perfectos son 28, 496 y 8128. 
# Actualmente se conocen más de 50 números perfectos, y se cree que existen infinitos
# números perfectos, aunque no se ha podido demostrar matemáticamente esta afirmación.

numero_entero = int(input("Ingrese un número: "))
divisores = 1
suma_divisores = 0


while divisores < numero_entero:
    esDivisor = False
    if numero_entero % divisores == 0:
        esDivisor = True
    if esDivisor == True:
        suma_divisores+=divisores
    divisores+= 1
    
 

if (suma_divisores == numero_entero):
    print("{0} es un número perfecto.".format(numero_entero))
else:
    print("{0} no es un número perfecto.".format(numero_entero))

#Dado un número entero n, imprimir todos los números primos menores o iguales a n.

numero_entero = int(input("Ingrese un número: "))
numeros_anteriores = 1



while numeros_anteriores <= numero_entero:
# En otras palabras, en cada iteración del bucle, el valor de divisores aumenta 
# y el valor de esPrimo puede cambiar de True a False. Si no se inicializan estas
# variables dentro del primer while, el valor de divisores y esPrimo de la iteración 
# anterior se mantendrán en la siguiente iteración, lo que podría provocar resultados
# incorrectos.
# tengo que iniciar divisores en 2 porque sino siempre va a ser false esPrimo
    divisores = 2
    esPrimo = True
    while divisores<numeros_anteriores:
        if numeros_anteriores % divisores == 0:
            esPrimo= False

        divisores +=1
    if esPrimo == True:
        print(numeros_anteriores)
    numeros_anteriores+=1
#Dado un número entero n, imprimir la secuencia de números de Harshad menores o iguales a n.

# Qué es un número Harshad?
# Un número de Harshad, también conocido como número Niven, 
# es un número entero positivo que es divisible por la suma de sus dígitos.
# Por ejemplo, el número 18 es un número de Harshad porque la suma de sus 
# dígitos es 1 + 8 = 9, y 18 es divisible por 9.

numero_entero= int(input("Ingrese un número: ")) 

for numero_entero in range(10,numero_entero+1):
        suma_digitos = 0 # la declaro acá y no en el segundo for para que no vuelva a 0
        for digito in str(numero_entero):

        #el for recibe un número entero. En la primera línea.

        # Luego, se itera sobre cada uno de los caracteres de la cadena generada
        #  a partir del digito. convierte cada caracter a un número entero utilizando 
        # la función int(), y lo suma a la variable suma.
        # por ejemplo, 19, itera 1 y luego 9 y lo suma 
        # 1er bucle: 0+1
        # 2do bucle 1+9
        # etc.
                suma_digitos += int(digito)    
        #es un número entero positivo que es divisible por la suma de sus dígitos.
        # se cumple  Harshad?
        if numero_entero % suma_digitos == 0:
                print(numero_entero)
        
# Crear una función que determine si un número es primo o no. 
# Recibe un parámetro (número) y devuelve True si es primo y False si no lo es.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
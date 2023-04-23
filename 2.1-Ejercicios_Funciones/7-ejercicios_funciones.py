# Crear una función que calcule el máximo común divisor de dos números. 
# Recibe dos parámetros (números) y devuelve el máximo común divisor.

def maximo_comun_divisor(numero1, numero2):
    if numero2 == 0:
        return numero1
    for i in range(1, numero2 + 1):
        if numero1 % i == 0 and numero2 % i == 0:
            mcd = i
    return mcd
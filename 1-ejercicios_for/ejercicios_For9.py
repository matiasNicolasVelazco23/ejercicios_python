# Dada una lista de números, imprimir la cantidad de números negativos en la lista.

lista_de_numeros = [1,6,9,4,1,0,2,28,29,-5,-6,-8,12,13,-8, 0]
acumulador_numeros_negativos = 0

for numeros in lista_de_numeros:
    if (numeros<0):
        acumulador_numeros_negativos+=1
print(acumulador_numeros_negativos)
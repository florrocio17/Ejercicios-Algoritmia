#Cargar dos listas de números A y B con N números al azar entre 1 y 100, donde
#N se ingresa por teclado. Mostrar ambas listas por pantalla. Luego construir e
#imprimir tres nuevas listas C, D y E que contengan:
#· La concatenación de los valores pares de A con los impares de B. (valores
#pares o valores impares se refiere a los elementos propiamente dichos
#y no a sus posiciones).
#· La concatenación de los valores impares de A con el reverso de los valores
#pares de B.
#· La intercalación de los elementos de A y B.
import random
def crearlista(n):
    posiciones = 0
    lista = []
    while posiciones < n:
        numero = random.randint(1,100)
        lista.append(numero)
        posiciones = posiciones + 1
    return lista
#· La concatenación de los valores pares de A con los impares de B.
def concatenarlistas(primerlista, segundalista):
    listapares = []
    listaimpares = []
    listaconcatenada = []
    for i in range(len(primerlista)):
        if primerlista[i] % 2 == 0:
            listapares.append(primerlista[i])
    for i in range(len(segundalista)):
        if segundalista[i] % 2 != 0:
            listaimpares.append(segundalista[i])
    listaconcatenada = listapares + listaimpares
    return listaconcatenada
#· La intercalación de los elementos de A y B.       
def intercalarlistas(primerlista, segundalista):
    new_list = []
    for i in range(len(primerlista)):
        new_list.append(primerlista[i])
        new_list.append(segundalista[i])
    return new_list

cantidad = int(input('ingrese cantidad de numeros para la lista:'))
listaA = crearlista(cantidad)
listaB = crearlista(cantidad)
listaC = concatenarlistas(listaA,listaB)
print(listaA,listaB, listaC)

d = intercalarlistas(listaA,listaB)
print(d)
    

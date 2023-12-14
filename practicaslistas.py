# practica de listas 
"""
1- hacer un array con numeros random
2- hacer un random con numero que se ingresa como input
3- buscar un dato en un array
4- crear una lista sin duplicados
5- crear lista y eliminar duplicados despues de crearla
6- buscar un dato en un array y eliminarlo
7- ingresar valor y agregarlo al array, en orden

import random
def crear_lista(largo):
    lista = []
    posiciones = 0
    while posiciones < largo:
        numero = random.randint(0,50)
        lista.append(numero)
        posiciones = posiciones + 1
    return lista

def busquedavalor(lista, valor):
    largo = len(lista)
    aux = 'no se encontro el valor'
    for i in range(largo):
        if lista[i] == valor:
            aux = lista[i]
    return aux




largo_lista = int(input('ingrese la cantidad de numeros que quiere agregar a la lista:'))
lista1 = crear_lista(largo_lista)
print(lista1)

n = int(input('ingrese el numero a buscar:'))
busqueda = busquedavalor(lista1, n)
print(busqueda)
"""
#Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos
#repetidos. El valor de N se ingresa por teclado. Resolver este problema utilizando
#dos estrategias distintas:
#· Impidiendo el agregado de elementos repetidos
import random
def crear_lista(n):
    lista = []
    posiciones = 0 
    while posiciones < n:
        numero = random.randint(0,89)
        #repetido = False
        if numero not in lista:
            lista.append(numero)
       # for i in range(len(lista)):
       #     if lista [i] == numero:
       #             repetido = True
       # if repetido == False:
       #     lista.append(numero)
        else:
             reemplazo = random.randint(90,100)  
             lista.append(reemplazo)
        posiciones = posiciones + 1
    return lista

# def randomNoRepetido(lista):
#      flag = 0
#      numero = 0
#      while flag != -1:
#         numero = random.randint(0,10)
#         if numero not in lista:
#             flag = -1
#      return numero
     
num = int(input('ingrese numero:'))
lista1 = crear_lista(num)
print(lista1)

    
#Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos
#repetidos. El valor de N se ingresa por teclado. Resolver este problema utilizando
#dos estrategias distintas:
#· Impidiendo el agregado de elementos repetidos
#· Eliminando los duplicados luego de generar la lista. Asegurarse que la
#cantidad final de elementos sea la solicitada.

import random
def crearlista(n):
    lista = []
    posiciones = 0
    while posiciones < n:
        numero = random.randint(0,10)
        lista.append(numero)
        posiciones = posiciones + 1
    return lista

def eliminarRepetidos(lista):

    for i in range(len(lista)):
        cont  = 0
        #estamos trabajando con i con valor = 1
        for j in range(len(lista)):
        # si el cont es > 1, se reemplaza valor
            if lista[i] == lista[j]:
                cont = cont + 1
        if cont > 1:
            lista[i] = random.randint(0,100)
            # del lista[i]
            # reemplazo = random.randint(0,100)
            # lista.append(reemplazo)
    return lista

# def eliminarduplicados2(lista, lista2): # [1,2,3]  [1, 2]
#     nuevolis = []
#     for i in range(len(lista2)):
#         for j in range(len(lista)):
#             if lista2[i] == lista[j]:
#     print(nuevolis)


def eliminarRepetidosDario(lista):
    newArray = []
    for i in range(len(lista)):
        if lista[i] not in newArray:
            newArray.append(lista[i])
    return newArray

def eliminardupli(lista):
    i = 0
    while i < len(lista) -1:
        if lista[i] == lista[i + 1]:
            del lista[i]
        else:
            i = i  + 1 
    return lista
                   
#programa principal
n = int(input('ingrese un numero:'))

lista = crearlista(n)
lista2 = [1,2,1,1,2,3,4]


nuevo = eliminardupli(lista)
print(nuevo)

# eliminarduplicados2([1, 1, 9, 8, 10, 7, 1])



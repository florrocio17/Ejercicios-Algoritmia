#Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir
#el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que
#se encuentre. La carga de datos termina cuando se obtenga un 0 como número
#al azar, el que no deberá cargarse en la lista.

'''primero se crea la lista
se debe leer 
imprimir el valor minimo y posicion
en caso de que el minimo se repita, se debe imprimir la lista con las posiciones del minimo
se debe detener si el valor agregado es 0 y no incluirla.
'''

import random
def crearlista():
    lista = []
    numeros = random.randint(0,100)
    while numeros != 0:
        lista.append(numeros)
        numeros = random.randint(0,100)
    return lista

def busquedaminimo(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if minimo > lista[i]:
            minimo = lista[i]
    return minimo
        

def busquedaposiciones(lista, num_minimo):
    lista_pos_minimo = []
    for i in range(len(lista)):
        #por cada vuelta, si el elemento es igual al numero minimo agregar a la lista
        if lista[i] == num_minimo:              
            lista_pos_minimo.append(i)  
    return lista_pos_minimo                                 
    

# Programa principal
#cant = int(input("¿Cuántos elementos desea cargar? ")) 
milista = crearlista()
print(milista)
min_numero = busquedaminimo(milista)
print('el valor minimo es:', min_numero)

lista_posiciones = busquedaposiciones(milista, min_numero)

print('se encuentra en estas posiciones:', lista_posiciones)

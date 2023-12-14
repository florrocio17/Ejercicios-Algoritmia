#ejercicio 2
#Cargar una lista con numeros ingresados por un usuario hasta que se ingresa -1 y reemplzar
#un valor en una posicion determinada por el usuario.
#Imprimir la lista antes y despues del reemplazo.

import random

def cargarlista():
    lista = []
    numero = int(input('ingrese numero a la lista o -1 para terminar la carga:'))
    while numero != -1:
        lista.append(numero)
        numero = int(input('ingrese numero a la lista o -1 para terminar la carga:'))
    return lista

def reemplazo(lista):
    largo = len(lista)
    posicion = int(input('ingrese la posicion que desea cambiar:'))
    if posicion >= 0 and posicion < largo:
        lista[posicion] = random.randint(0,100)
    else:
        print('posicion no encontrada')
        reemplazo(lista)
    return lista    
    
def reemplazo2(lista):
    largo = len(lista)
    cantposiciones = largo - 1
    posicion = int(input('ingrese la posicion que desea cambiar:'))
    while posicion > cantposiciones or posicion < 0:
        posicion = int(input('ingrese la posicion que desea cambiar:'))
    nuevovalor = int(input('ingrese el nuevo valor del reemplazo'))
    lista[posicion] = nuevovalor
    return lista
#programa principal

lista = cargarlista()
if len(lista) > 0:
    print(lista)
    nuevalista = reemplazo2(lista)
    print('la nueva lista es:', nuevalista)
    
else:
    print('no se ingresaron valores')



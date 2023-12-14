#ejercicio 1
'''
Escribir un programa que utilice funciones para:
1-Cargar una lista de N elementos con numeros enteros entre 50 y 700 obtenidos al azar.
El valor de N se ingresa por teclado.
2-Ordenar la lista en forma ascendente utilizando cualquier metodo de ordenamiento estudiado.
3-Pedir un dato al usuario y buscarlo con busqueda binaria e informar su posicion o -1 sino se encuntra.
4-Luego eliminar de la lista, el valor minimo en todas sus posiciones
Imprimir por pantalla la lista luego de realizar cada tarea

#ejercicio 2
Cargar una lista con numeros ingresados por un usuario hasta que se ingresa -1 y reemplzar
un valor en una posicion determinada por el usuario.
Imprimir la lista antes y despues del reemplazo.
'''
import random

def crearlista(n):
    lista = []
    posiciones = 0
    while posiciones < n:
        numero = random.randint(50,700)
        lista.append(numero)
        posiciones = posiciones + 1
    return lista

def metododeseleccion(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] <dato:
            izq = centro + 1
        else:
            der = centro -1
    return pos

def busquedaminimo(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def eliminarminimo(lista, minimo):
    listanueva = []
    for i in range(len(lista)):
        if lista[i] != minimo:
            listanueva.append(lista[i])
    return listanueva

def eliminarminimo2(lista, minimo):
    min = minimo
    i = 0
    while i < len(lista):
        if lista[i] == min:
            del lista[i]
            i = i -1
        i = i + 1
    return lista

#programa principal
n = int(input('ingrese cantidad de numeros a agregar a la lista:'))
lista = crearlista(n)
print(lista)

listaordenada = metododeseleccion(lista)
print(listaordenada)
#Pedir un dato al usuario y buscarlo con busqueda binaria e informar su posicion o -1 sino se encuntra.

datobuscado = int(input('que valor desea buscar:'))
posiciondato = busquedabinaria(lista, datobuscado)
print(posiciondato)
minimonum = busquedaminimo(lista)
print(minimonum)

listasinminimo= eliminarminimo(lista, minimonum)
print(listasinminimo)
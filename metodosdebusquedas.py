
def busquedasecuencial(lista, dato):
    i = 0 
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1
    
def metododeseleccion(lista): #Consiste en buscar el menor elemento detodo el arreglo e intercambiarlo con el de laprimera posición.
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


def busquedaburbuja(lista): #Se basa en comparar cada elemento con el que tiene a su derecha.
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
                desordenado = True
    return lista

def metododeinsercion(lista):
    for i in range(1, len(lista)):  #empieza por el segundo elemento
        aux = lista[i]
        j = i
        while j > 0 and lista[j-1] > aux:
            lista[j] = lista[j-1]
            j = j - 1
            lista[j] = aux
    return lista
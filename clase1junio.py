import random
def cargarlista(cantidad):
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(1,100))
    return lista

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ") 
        print()
        
def busquedasecuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1
# Programa principal
cant = int(input("¿Cuántos elementos desea cargar? ")) 
milista = cargarlista(cant)
imprimirlista(milista)
n = int(input("Ingrese el número a buscar: ")) 
pos = busquedasecuencial(milista,n)
if pos >= 0:
    print("El elemento",n,"se encontró en la posición", pos) 
else:
    print("El valor",n,"no se encontró en la lista")
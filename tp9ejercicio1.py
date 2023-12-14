#Leer los números de legajo de los alumnos de un curso y su nota de examen
#final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar
#que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
#· Cantidad de alumnos que aprobaron con nota mayor o igual a 4
#· Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
#· Promedio de nota y los legajos que superan el promedio
#Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera
#ascendente según el número de legajo. Resolver de dos formas: Utilizando
#dos listas paralelas y utilizando una matriz de dos filas.

def metododeseleccion(lista, listanotas): #Consiste en buscar el menor elemento detodo el arreglo e intercambiarlo con el de laprimera posición.
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                auxnotas = lista_notas[i]
                lista[i] = lista[j]
                listanotas[i] = listanotas[j]
                lista[j] = aux
                listanotas[j] = auxnotas
    return lista, listanotas

def legajos_sup_promedio(promedio):
    lista_superiores = []
    for i in range(len(lista_legajos)):
        if lista_notas[i] > promedio:
            lista_superiores.append(lista_legajos[i])
    return lista_superiores

legajo = int(input('ingrese numero de legajo o -1 para terminar:'))
contador_aprobados = 0
contador_desaprobados = 0
contador_notas = 0
suma_notas = 0
lista_legajos = []
lista_notas = []
while legajo != -1:
    nota = int(input('ingrese numero de nota:'))
    while nota > 10 or nota < 1:
        print('nota invalida')
        nota = int(input('ingrese numero de nota:'))
    if nota >= 4:
        contador_aprobados= contador_aprobados+ 1
    else:
        contador_desaprobados = contador_desaprobados + 1
    lista_legajos.append(legajo)
    lista_notas.append(nota)
    contador_notas = contador_notas + 1
    suma_notas = suma_notas + nota
    legajo = int(input('ingrese numero de legajo o -1 para terminar:'))

if legajo != -1:
    print('la cantidad de desaprobados es:', contador_desaprobados)
    print('la cantidad de aprobados es:', contador_aprobados)
    promedio = suma_notas / contador_notas
    ordenamiento_legajos = metododeseleccion(lista_legajos, lista_notas)
    print('la lista siguiente ya esta ordenada:',ordenamiento_legajos)

    legajos_superiores = legajos_sup_promedio(promedio)
    print('el promedio es:', promedio,'y los legajos que lo superan son los siguientes:', legajos_superiores)
else:
    print('no se ingresaron valores')
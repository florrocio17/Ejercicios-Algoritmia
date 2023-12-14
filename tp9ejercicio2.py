#Una Administradora de Consorcios necesita un sistema para poder gestionar el
#cobro de las expensas de un edificio de departamentos de 20 unidades. En dos
#listas almacena la siguiente información: Número de unidad y superficie en metros
#cuadrados. Validar que no se ingresen números de unidades duplicadas. Cada
#unidad paga de expensas un valor fijo por metro cuadrado, el que se ingresa
#por teclado. Se pide:
#· Informar el promedio de expensas del mes.
#· Ordenar los listados de mayor a menor según la superficie. Mostrar por
#pantalla el listado ordenado informando el número de unidad y la superficie
#en metros cuadrados.

def crearlista(n):
    lista = []
    sup_metros_2 = []
    posiciones = 0
    while posiciones < n:
        numero = int(input('ingrese numero de unidad:'))
        flag = True
        for i in range(len(lista)): # 1,2,3,4     3
            if numero == lista[i]:
                flag= False
                print('numero ya ingresado')
        if flag:
            lista.append(numero)
            superficie = int(input('ingrese cantidad de metros 2:'))
            sup_metros_2.append(superficie)
        else:
            posiciones = posiciones - 1
        posiciones = posiciones + 1
    return [lista, sup_metros_2]

def sumatotal(lista, precio):
    acumulador = 0
    for i in range(len(lista)):
        acumulador = acumulador + (lista[i] * precio)
        #print(lista[i], precio)
    return acumulador

def metododeseleccion(lista, segundalista): #Consiste en buscar el menor elemento detodo el arreglo e intercambiarlo con el de laprimera posición.
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] < lista[j]:
                aux = lista[i]
                auxsegundo = segundalista[i]
                lista[i] = lista[j]
                segundalista[i] = segundalista[j]
                lista[j] = aux
                segundalista[j] = auxsegundo
    return lista, segundalista

#programa principal
cant_deptos = 4

listas = crearlista(cant_deptos)


valor_m2 = int(input('ingrese el valor de cada metro cuadrado:'))
suma_metros = sumatotal(listas[1], valor_m2)
promedio = suma_metros / cant_deptos
ordenamiento = metododeseleccion(listas[1],listas[0])
print('el promedio de las expensas del mes es de:', promedio)
print('las listas estan ordenadas de mayor a menor segun tamaño de superficie:', ordenamiento)


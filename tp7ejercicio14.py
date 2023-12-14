#Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del
#año, con el propósito de ofrecerles un agasajo especial en su día. Desarrollar un
#programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de
#cada uno de los alumnos que concurren a dicha escuela. La carga finaliza con un
#número de legajo igual a -1. Emitir un informe donde aparezca -mes por mes cuántos
#alumnos cumplen años a lo largo del año. Imprimir también una leyenda
#que indique cuál es el mes con mayor cantidad de cumpleaños.

def busquedamaximo(lista):
    maximo = lista[0]
    pos = 0 
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            pos = i
    print('el mes con mas cumpleanos es el mes:', pos +1)

def imprimircantcumples(lista):
    for i in range(len(lista)):
        print('en el mes', i +1, 'hubo', lista[i], 'cumpleanos')

legajo = int(input('ingrese numero de legajo o -1 para terminar:'))
#Creamos el vector y lo inicializamos con 0 
listameses=[]
meses = 12
for i in range(meses):
    listameses.append(0)
while legajo != -1:
    mes = int(input('ingrese mes de cumple:'))
    if mes > 12:
        mes = int(input('numero de mes incorrecto, coloque otro:'))  #[0,0,0,0,0,0,0,0,0,0...]
    listameses[mes -1] = listameses[mes -1] + 1  #contador para el index
    legajo = int(input('ingrese numero de legajo o -1 para terminar:'))

imprimircantcumples(listameses)

busquedamaximo(listameses)

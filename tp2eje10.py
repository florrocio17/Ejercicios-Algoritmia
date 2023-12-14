#se desee llevar un registro de los socios que visitan el club cada dia. para ello se ingres el numero
#de socio de 5 digitos hasta ingresar un 0 como fin de carga. se solicita 
#a- informar cuantas VECES ingreso al club para cada socio
#b- solicitar un numero de socio que se dio de baja y eliminar todos sus ingresos. Mostrar lista de antes y despues d eliminarlo
'''
hagamos lista de socios que no se repiten
despues creamos la lista contador para cada socio con el index de cada uno 
'''
def ingresarsocios(lista, lista_contador):
    socio = int(input('ingrese su numero de socio de 5 digitos o 0 para terminar:'))
    while socio != 0:
        if socio < 10000 or socio > 99999:
            socio = int(input('numero incorrecto, ingrese numero de socio de 5 digitos:'))
        if socio not in lista:
            lista.append(socio)
            lista_contador.append(1)
            # lista_contador[socio] = 1
        else:
            lista_contador[lista.index(socio)] = lista_contador[lista.index(socio)] + 1
        socio = int(input('ingrese su numero de socio de 5 digitos o 0 para terminar:'))

def eliminar_socio(socio, lista, listacontador):
    aux = lista_contador[lista.index(socio)]
    listacontador.remove(aux)
    lista.remove(socio)
    return listacontador
    

#programa principal

lista1 = []
lista_contador = []

ingresarsocios(lista1, lista_contador)
for i in range(len(lista1)):
    print('el socio numero:', lista1[i] , 'ingreso ', lista_contador[i], 'veces')

print(lista1, lista_contador)

socio_a_elimiar = int(input('ingrese numero de socio de 5 digitos a eliminar:'))
lista_sin_socio = eliminar_socio(socio_a_elimiar, lista1, lista_contador)
print('la lista de socios eliminando el socio anterior es:', lista1)
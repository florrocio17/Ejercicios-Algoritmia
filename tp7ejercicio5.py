#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva
#lista con los mismos elementos de la primera, pero en orden inverso. Por
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5].

#funcion para crear lista
def serie_numeros(a,b):
    lista = []
    print ("Ingrese un numero entre: ", a, " y ", b, " sino -1 para terminar")
    numero = int(input('ingrese un numero:'))
    while numero != -1:
        if numero >= a and numero <= b:
            lista.append(numero)
        elif numero <= a and numero >= b:
            lista.append(numero)
        else:
            print('error, ingresar otro numero')
        numero = int(input('ingrese un numero'))
    return lista

def lista_inversa(primer_lista):
    lista_vacia = []
    largo = len(primer_lista)
    cant_posiciones = largo - 1
#en range empezamos por el index ultimo, hasta el index 0 por eso colocamos -1, para que llegue a la posicion 0, el ultimo -1 es para que vaya de atras para adelante
    for i in range(cant_posiciones, -1, -1):
        #print(primer_lista[i])
        lista_vacia.append(primer_lista[i])
    return lista_vacia

prueba_lista = serie_numeros(1,5)


prueba_inversa = lista_inversa(prueba_lista)

print(prueba_inversa)

            
    

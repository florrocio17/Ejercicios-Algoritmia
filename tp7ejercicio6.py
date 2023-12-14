#Escribir una función para devolver una lista con todas las posiciones que ocupa
#un valor pasado como parámetro, utilizando búsqueda secuencial en una lista
#desordenada. La función debe devolver una lista vacía si el elemento no se encuentra
#en la lista original.
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

def lista_posiciones (lista, valor):
    lista_vac = []
    largo = len(lista)
    for i in range(largo):
        if lista[i] == valor:
            lista_vac.append(i)
    return lista_vac

#programa principal
menor_rango = int(input('ingrese un limite minimo:'))
mayor_rango = int(input('ingrese un limite maximo:'))
primer_lista = serie_numeros(menor_rango,mayor_rango)
print(primer_lista)
valor_buscado = int(input('que valor desea buscar:'))
posiciones_encontradas = lista_posiciones(primer_lista,valor_buscado)
print('la lista con las posiciones que ocupa', valor_buscado, 'es:', posiciones_encontradas)



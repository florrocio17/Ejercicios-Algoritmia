#Escribir una función para contar cuántas veces aparece un valor dentro de la
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
#un número entero.

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

def contador_valor(lista, valor):
    contador = 0
    largo = len(lista)
    for i in range(largo):
        if lista[i] == valor:
            contador = contador + 1
    return contador

menor_rango = int(input('ingrese un limite minimo:'))
mayor_rango = int(input('ingrese un limite maximo:'))
primer_lista = serie_numeros(menor_rango,mayor_rango)
print(primer_lista)


valor_buscado = int(input('ingrese el valor que desea contar:'))
contador_num = contador_valor(primer_lista, valor_buscado)
print('el valor aparece',contador_num, 'veces dentro de la lista')



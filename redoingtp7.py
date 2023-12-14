#Escribir una función para ingresar desde el teclado una serie de números entre A
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función
#mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B. 



def crearlista (a,b):
    lista = []
    numero = int(input('ingrese un numero a la lista:'))
    while numero != -1:
        if numero <= a and numero >= b:
            lista.append(numero)
        else:
            print('numero fuera de los rangos')
        numero = int(input('ingrese un numero a la lista:'))
    return lista

#Calcular la suma de los números de la lista.
def sumalista(lista):
    suma= 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma

#Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual
#modo de izquierda a derecha y de derecha a izquierda.
def capicua(lista):
    palindromo = True
    for i in range(len(lista)):
        if lista[i] != lista[len(lista) - 1- i]:
            palindromo = False
    return palindromo

#Escribir una función para contar cuántas veces aparece un valor dentro de la
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
#un número entero.
def busquedaenlista(lista, numero):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            contador = contador + 1
    return contador

#programa principal
a = int(input('ingrese limite mayor:'))
b = int(input('ingrese limite menor:'))

lista = crearlista(a,b)
if len(lista) > 0:
    print(lista)
else:
    print('no se ingresaron valores a la lista')

valorbuscado = int(input('ingrese el valor que desea buscar:'))
sumatotal = sumalista(lista) 
print(sumatotal)

listapalindromo = capicua(lista)

if listapalindromo:
    print('es capicua')
else:
    print('no es capicua')

c = busquedaenlista(lista, valorbuscado)

print('el valor', valorbuscado, 'figura', c, 'veces en la lista')







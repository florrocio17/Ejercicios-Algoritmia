#Escribir una función para ingresar desde el teclado una serie de números entre A
#y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la función
#mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
#carga se deberá ingresar -1. La función recibe como parámetros los valores de A
#y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
#valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.  
'''
mi desglose:
funcion con 2 parametros de limites
esa funcion debe permitir ingresar numeros hasta que coloquen -1
esos numeros deben ser entre limite a y b y guardarse en una lista
en caso de que no, se debe imprimir error 
al final de la funcion se debe colocar return con la lista
'''
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
'''
#ejercicio 2
#Calcular la suma de los números de la lista.
primer_numero = int(input('ingrese primer numero:'))
segundo_numero = int(input('ingrese segundo numero:'))

prueba = serie_numeros(primer_numero, segundo_numero)
suma = 0
largo= len(prueba)
for i in range(largo):
    suma = suma + prueba[i]
print('la suma de los numeros de la lista es:', suma)

'''
'''
#ejercicio 3 
pseudocodigo

[1,5,3,1]

largo= len(prueba)
#flag = true // esto seria en una primera ocasion un palindromo.
for i in range(largo):

   if prueba[i] != prueba[largo-i] # me interesa saber si no se cumple aunque sea 1 sola vez o la primera vez 
    flag = false # si entra una sola vez, esto NO es un palindromo.

if(flag)
print()

Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual
modo de izquierda a derecha y de derecha a izquierda.

'''
primer_numero = int(input('ingrese primer numero:'))
segundo_numero = int(input('ingrese segundo numero:'))

prueba = serie_numeros(primer_numero, segundo_numero)

largo= len(prueba)
bandera = True
for i in range(largo):
    cant_posiciones = largo -1
    if prueba[i] != prueba[cant_posiciones - i]:
        bandera = False

if bandera == True:
    print('es palindromo')
else:
    print('no es palindromo')

#Escribir una función para contar cuántas veces aparece un valor dentro de la
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve
#un número entero.
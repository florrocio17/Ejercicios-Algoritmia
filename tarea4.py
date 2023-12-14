'''
#no salio
cant = 0
numero = int(input("Ingrese un número o -1 para terminar: "))

while numero != -1:
    cant = cant + 1
    numero = int(input("Ingrese un número o -1 para terminar: "))
if numero != -1:
        print(numero)
else:
        print(cant)
'''
'''
#ejercicio 1 
#debe ingresar numeros hasta que pongan -1
#se debe mostrar primer numero y ultimo numero
cant = 0
ultimoNumero = 0
primerNumero = 0
numero = int(input("Ingrese un número o -1 para terminar: "))


while numero != -1:
    ultimoNumero = numero
    cant = cant + 1
    if cant == 1:
        primerNumero = numero
    numero = int(input("Ingrese un número o -1 para terminar: "))

print('el ultimo numero ingresado es:',ultimoNumero)
print('el primer numero ingresado es:', primerNumero)
'''
'''
# ejercicio 2
#Realizar un programa para ingresar desde el teclado un conjunto de números e
#informar si la cantidad de elementos es impar o par, sin utilizar contadores. Finalizar
#la lectura de datos con -1.
numero = int(input("Ingrese un número o -1 para terminar: "))
impar = 0

while numero != -1:
    if impar == 0:
        impar = 1
    else:
        impar = 0

    numero = int(input("Ingrese un número o -1 para terminar: "))

if impar:
    print('es impar')
else:
    print('es par')

'''
#Desarrollar un programa que imprima los números naturales comprendidos entre
#1 y N. El valor de N se ingresa desde el teclado.
#ejercicio 5 
iniciador = 1
final = int(input("Ingrese un número:"))

while final >= iniciador:
        print(iniciador)
        iniciador = iniciador + 1

        
#primer ejercicio if
'''
PrimerNumero = int(input("ingrese primer numero:"))
SegundoNumero = int(input("ingrese segundo numero:"))

if PrimerNumero == SegundoNumero :
    print("son iguales")
else :
    print("son diferentes")

#segundo
numeroNat = int(input("ingrese numero:"))
if numeroNat % 2 == 0:
    print("es numero par")
else:
    print("es impar")

#tercer ejercicio
ingresarMes = int(input("ingrese numero de mes:"))

if ingresarMes == 1 :
    print("enero")
elif ingresarMes == 2:
    print("febrero")
elif ingresarMes == 3:
    print("marzo")
elif ingresarMes == 4:
    print("abril")
elif ingresarMes == 5:
    print("mayo")
elif ingresarMes == 6:
    print("junio")
elif ingresarMes == 7:
    print("julio")
elif ingresarMes == 8:
    print("agosto")
elif ingresarMes == 9:
    print("septiembre")
elif ingresarMes == 10:
    print("octubre")
elif ingresarMes == 11:
    print("noviembre")
elif ingresarMes == 12:
    print("diciembre")
else :
    print("mes invalido")


#4 ejercicio
primerNota = int(input("ingresar 1 nota:"))
segundaNota = int(input("ingresar 2 nota 2:"))



if primerNota >= 0 and primerNota <= 10 and segundaNota >= 0 and segundaNota <= 10:
    if primerNota >= 7 :
        print("promociono")
    if primerNota >= 4 and segundaNota >= 4 :
        print("aprobo")
    if primerNota < 4 or segundaNota < 4 :
        print("debe recuperar")
else :
    print("notas invalidas")

#ejercicio 6
kmTotal = int(input('cuantos km desea viajar?'))
valorViaje = kmTotal * 30
valorViajeLargo = kmTotal * 20

if valorViaje > 250 and kmTotal < 10:
    print(valorViaje)
elif  kmTotal >= 10 :
        print(valorViajeLargo)
else :
      print("debe pagar 250")

'''
#ejercicio 7
ingreseAnio = int(input('ingrese año:'))

if ingreseAnio % 4 == 0 and (ingreseAnio % 100 != 0 or ingreseAnio % 400 == 0):
    print("es año bisiesto")
else :
    print("no es año bisiesto")

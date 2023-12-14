#ejercicio 2
"""
a = int(input("ingrese numero:"))
b = int(input("ingrese otro numero:"))
primerResultado = a + b
segundoResultado = a - b
print("este es la suma de los numeros:", primerResultado)
print("esta es la diferencia:",abs(segundoResultado))

#ejercicio 3

primerNota = int(input("ingrese nota primer parcial:"))
segundaNota = int(input("ingrese nota segundo parcial:"))
promedio = (primerNota + segundaNota) / 2
print(promedio)

#ejercicio 4

edad = int(input("ingrese su edad:"))
cantDias = 365
EdadEnDias = edad * cantDias
print("su edad en dias es:", EdadEnDias)


#ejericio 5

inversion1 = int(input("ingrese su inversion:"))
inversion2 = int(input("ingrese su inversion:"))
inversion3 = int(input("ingrese su inversion:"))
totalInversion = inversion1 + inversion2 + inversion3
porcentajeInv1 = inversion1 * 100 / totalInversion
porcentajeInv2 = inversion2 * 100 / totalInversion
porcentajeInv3 = inversion3 * 100 / totalInversion
print ("el porcentaje de inversion 1 es", porcentajeInv1)


#ejercicio 7 

capital = int(input("ingrese su capital:"))
interesMensual = 0.02
cantMeses = int(input("cuantos meses quiere dejar?:"))
Resultado = capital * interesMensual * cantMeses
print("si deja su dinero ", cantMeses, "meses, obtendra: ", Resultado)


#ejercicio 8 
metros = int(input("ingrese metros:"))
centimetros = metros * 100
pulgada = 2.54
pies = 12 * pulgada
yarda = 3 * pies
centAPulgadas = centimetros / pulgada
centAPies = centimetros / pies 
centAYardas = centimetros / yarda
print("esos", metros, "metros son", centimetros, "centimetros. En pulgadas:", round(centAPulgadas,2), ", pies:", round(centAPies,2), "y" , round(centAYardas,2), "yardas")


#ejercicio 9

numeroDeVendedor = input("ingrese numero de empleado:")
cantVentas = int(input("cuantas ventas realizo?"))
           
        #if valor de ventas es mayor a 1
#preguntar la cantidad de veces elvalor de cada venta
"""
"""
valorVentas = int(input("ingrese valor de ventas:"))
comisionVentas = cantVentas * 5000
segundaComision = valorVentas * 0.05
salarioBase = 50000
salario = salarioBase + comisionVentas + segundaComision
print("el empleado numero:", numeroDeVendedor, "realizo", cantVentas, "ventas, al valor total de",valorVentas)

"""

"""
test = [0] * 4
[0,0,0,0]

for key, value in test.items():
    valorVenta = int(input("ingrese valor de ventas:"))
    test[key] = valorVenta
    print(key)
print(test)


#ejercicio 10
a = int(input("ingrese valor de cantidad de segundos:"))
dias = a // 86400
restodia = a % 86400
horas =  restodia // 3600
restohoras = restodia % 3600
minutos = restohoras // 60
segundos = restohoras % 60

print(a, "segundos son", dias, "dias,", horas, "horas,", minutos, "minutos y ", segundos, "segundos")
"""
#ejercicio 11
cantidadIngresada = int(input("ingrese valor de dinero ingresado:"))
billetesMil = cantidadIngresada // 1000
restoDeMil = cantidadIngresada % 1000
billetesQuin = restoDeMil // 500
restoQuin = restoDeMil % 500
billetesCien = restoQuin // 100
restoCien = restoQuin % 100
billetesCinc = restoCien // 50
restoCinc = restoCien % 50
billetesDiez = restoCinc // 10
restoDiez = restoCinc % 10
billetesCinco = restoDiez // 5
billetesUno = restoDiez % 5

print("se va a recibir",billetesMil, "billetes de 1000,", billetesQuin, "billetes de 500," , billetesCien, "billetes de 100,", billetesCinc, "billetas de 50,", billetesDiez, "billetes de 10,", billetesCinco, "billetes de 5 y", billetesUno, "billetes de 1")

#hol

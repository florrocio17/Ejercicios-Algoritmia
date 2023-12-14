# tp 5, ejercicio 1
'''
Mayores = 0
Menores = 0
edades = int(input("ingrese edad:"))
sumaMenores = 0
sumaMayores = 0

while edades != -1:
    if edades >= 0 and edades < 18:
        Menores = Menores + 1
        sumaMenores = sumaMenores + edades
    elif edades >= 18 and edades <=100 :
        Mayores = Mayores + 1
        sumaMayores = sumaMayores + edades
    else:
        print("numero invalido")
    edades = int(input("ingrese edad:"))

print("la cantidad de mayores es :" ,Mayores, "la cantidad de menores es:" , Menores)
if Mayores > 0 :
    promMayores = sumaMayores/Mayores
    print("el promedio de los mayores es:" , promMayores )
else :
    print("no hay edades mayores a 18")

if Menores > 0 :
    promMenores = sumaMenores/Menores
    print("el promedio de los menores es:" , promMenores )
else :
    print("no hay edades menores a 18")

#ejercicio 2

legajo = int(input("ingrese numero de legajo:"))

alumnosAprobados = 0
alumnosDesaprobados = 0
alumnosAplazados = 0

while legajo != -1:
    notaFinal = int(input("ingrese nota final:"))
    if notaFinal >= 4 and notaFinal <= 10:
        alumnosAprobados = alumnosAprobados + 1
    elif notaFinal < 4 and notaFinal > 1 :
        alumnosDesaprobados = alumnosDesaprobados + 1
    elif notaFinal == 1:
        alumnosAplazados = alumnosAplazados + 1
    else :
        print('nota invalida')

    legajo = int(input("ingrese numero de legajo:"))
alumnosDesaprobados = alumnosDesaprobados + alumnosAplazados
totalAlumnos = alumnosAprobados + alumnosDesaprobados
porcentajeAplazados = alumnosAplazados * 100 / totalAlumnos
print('la cantidad total de notas es:', totalAlumnos)
print('la cantidad de aprobados es', alumnosAprobados, ', la cantidad de alumnos desaprobados es:', alumnosDesaprobados, 'y el porcentaje de alumnos aplazados es:', porcentajeAplazados)

'''

'''
#ejercicio 3
productos = int(input("ingrese productos a comprar:"))
precioBase = int(input('ingrese el precio base:'))
ventasTotal = 0
ventasConDiezDto = 0
ventasPrecioBase = 0

valorTotal = 0
precioPromedio = 0

while productos != -1:

    if productos <= 12 :
        valorTotal = productos * precioBase
        ventasPrecioBase = ventasPrecioBase + 1
        ventasTotal = ventasTotal + 1
    elif productos >= 13 and productos <= 100:
        ventasTotal = ventasTotal + 1
        ventasConDiezDto = ventasConDiezDto + 1
        valorTotal = 12 * precioBase + (productos - 12) * 0.9
    else:
        ventasTotal = ventasTotal + 1
        valorTotal = 12 * precioBase + 88 * 0.9 * precioBase + ( productos - 100) * precioBase * 0.75
     
    if productos != -1:
        precioPromedio = valorTotal / productos
        print('el valor total es de:', valorTotal, 'y el promedio es de:', precioPromedio) 
     
    productos = int(input("ingrese productos a comprar:"))  
    if productos == -1:
        print('termino el programa')
    else:
        precioBase = int(input('ingrese el precio base:'))

print('se realizaron', ventasTotal, 'ventas')
print('se realizaron', ventasConDiezDto, 'ventas con 10porciento de dto')
print('se realizaron', ventasPrecioBase, 'ventas con precio base')


'''
'''
#ejercicio 4
nroCliente = int(input('ingrese numero de cliente:'))
montoFactura = int(input('ingrese monto de factura total:'))
dosPorcentaje = montoFactura * 2 / 100
diezPorcentaje = montoFactura * 10 / 100
PrimerMonto = 0
SegundoMonto = 0

if dosPorcentaje > 200:
    PrimerMonto = montoFactura - dosPorcentaje   
else :
    PrimerMonto = montoFactura - 200
    
if diezPorcentaje > 350 :
    SegundoMonto = montoFactura + diezPorcentaje
else :
    SegundoMonto = montoFactura + 350

print('el cliente:', nroCliente, 'debe pagar en los primeros 10 dias:', PrimerMonto)
print('si paga del 10 al 20 abona:', montoFactura)
print('y si paga despues del 20, debe abonar:', SegundoMonto)


'''
'''
monto_a_ahorrar = 0
while monto_a_ahorrar < 80000 or monto_a_ahorrar > 100000:
    monto_a_ahorrar = float(input("Ingrese el monto que desea ahorrar (entre 80000 y 100000): "))

deposito_semanal = 0
total_depositos = 0

# Continuar haciendo depósitos semanales hasta que se alcance el monto deseado
while total_depositos < monto_a_ahorrar:
    # Validar que el depósito semanal esté en el rango requerido
    while deposito_semanal < 5000 or deposito_semanal > 10000:
        deposito_semanal = float(input("Ingrese el depósito semanal (entre 5000 y 10000): "))
    total_depositos += deposito_semanal
    deposito_semanal = 0

print(f"Se ha alcanzado el monto deseado de {monto_a_ahorrar} con un total de depósitos de {total_depositos}")

#ejercicio 6 

contador = 0
numero = int(input("Ingrese un numero: "))

if numero < 0:
    numero = numero * -1

while numero > 0:
  numero = numero // 10
  contador = contador + 1

print ("Cantidad de digitos del numero:", contador)

'''
'''
# ejercicio 5
dia = int(input('ingrese un numero de dia:'))
mes = int(input('ingrese un numero de mes:'))
anio = int(input('ingrese un numero de anio:'))
numeroSumar = int(input('ingrese un numero de dias a sumar:'))

while dia <= 0 or dia > 31:
    print('numero de dia invalido invalido')
    dia = int(input('ingrese un numero de dia:'))
while mes <= 0 or mes > 12:
    print('numero  de mes invalido')
    mes = int(input('ingrese un numero de mes:'))
while anio <= 0:
    print('numero de anio invalido ')
    anio = int(input('ingrese un numero de anio:'))

dia = dia + numeroSumar
diaDelMes = 0
# chequeamos que los dias sea mayor a 0 para que entre al while
while dia > diaDelMes:
    if dia > diaDelMes:
        # chequeamos que sean meses de 30 dias o febrero de año bisiesto o no para descontar bien los dias
        if mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if mes == 2:
                if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
                    diaDelMes = 29
                    dia = dia - 29
                else:
                    diaDelMes = 28
                    dia = dia - 28
            else:
                diaDelMes = 30
                dia = dia - 30
        #si no se debe descontar los dias de los meses restantes que tienen 31 dias
        else:
            diaDelMes = 31
            dia = dia - 31

        mes = mes + 1
    if mes > 12:
        anio = anio + 1
        mes = mes - 12


print('la nueva fecha es:', dia, mes, anio)
'''
#Ingresar un número N y validar que sea positivo. Luego:
#a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
#b. Informar la suma de esos números impares.
#ejercicio 9
'''
inicializador = 1
numeroFinal = int(input('ingrese un numero limite:'))
contador = 0
while numeroFinal < 0:
    print('numero incorrecto')
    numeroFinal = int(input('ingrese un numero limite:'))
while numeroFinal >= inicializador:
    print(inicializador)
    contador = contador + inicializador
    inicializador = inicializador +2
    

print('la suma de estos numero es:', contador)
    
'''
'''
Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
informe que contenga:
· Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio
 '''   
cantidadEmpleados = int(input('ingrese cantidad de empleados:'))


totalSalarios = 0
cantSalarios = 0 
empleadoDoscientos = 0
empleadosMenorCincuenta = 0
mayorSueldo = 0
menorSueldo = 0
legajoMayor = 0
sueldoCategoria1 = 0
sueldoCategoria2 = 0
sueldoCategoria3 = 0


while cantidadEmpleados > cantSalarios:
   legajo = int(input('ingrese numero de legajo:'))
   categoria = int(input('ingrese categoria 1, 2 o 3:'))
   salario = int(input('ingrese sueldo:')) 
   cantSalarios = cantSalarios + 1
   totalSalarios = totalSalarios + salario
   while categoria < 0 or categoria > 4:
       print('categoria incorrecta')
       categoria = int(input('ingrese categoria 1, 2 o 3:'))
   while salario <= 0:
       print('sueldo invalido')
       salario = int(input('ingrese sueldo:'))
    
   if cantSalarios == 1:
       mayorSueldo = salario
       menorSueldo = salario
       legajoMayor = legajo
   if salario > mayorSueldo:
       mayorSueldo = salario
       legajoMayor = legajo
   if salario < menorSueldo:
       menorSueldo = salario
    
   #print(salario, mayorSueldo, salario > mayorSueldo)
       
   if salario >= 200000:
       empleadoDoscientos = empleadoDoscientos + 1
   if salario <= 50000 and categoria == 3:
       empleadosMenorCincuenta = empleadosMenorCincuenta + 1
    
   if categoria == 1:
       sueldoCategoria1 = sueldoCategoria1 + salario
   if categoria == 2:
       sueldoCategoria2 = sueldoCategoria2 + salario
   if categoria == 3:
       sueldoCategoria3 = sueldoCategoria3 + salario
promedio = totalSalarios / cantSalarios    
print('el menor sueldo es:', menorSueldo)
print('el mayor sueldo es:', mayorSueldo, 'numero de legajo es',legajoMayor)   
print('el total de los salarios es:',totalSalarios)
print('los empleados que cobran mas de 200.000 son:',empleadoDoscientos)
print('los empleados que cobran menos de 50.000 y son categoria 3 son',empleadosMenorCincuenta)
print('son', sueldoCategoria3, "en total de la categoria 3")
print('son', sueldoCategoria2, "en total de la categoria 2")
print('son', sueldoCategoria1, "en total de la categoria 1")
print('promedio total de los sueldo es',promedio)
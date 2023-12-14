'''
ahorroTotal = int(input('ingrese el monto total que quiere ahorrar:'))
totalDepositos = 0
cantDepositos = 0
mayor_deposito = 0
menor_deposito = 0
posicion_mayor = 0
posicion_menor = 0

if ahorroTotal >= 80000 and ahorroTotal <= 100000 :
    print('monto valido')
else :
    print('monto invalido')


while totalDepositos < ahorroTotal:
   depositoSemanal = int(input('ingrese el deposito semanal:'))
   if depositoSemanal >= 5000 and depositoSemanal <= 10000:
       totalDepositos = totalDepositos + depositoSemanal
       cantDepositos = cantDepositos + 1
   else:
        print('monto invalido')
   if cantDepositos == 1:
       mayor_deposito = depositoSemanal
       menor_deposito = depositoSemanal
   else:
        if depositoSemanal > mayor_deposito:
            mayor_deposito = depositoSemanal
            posicion_mayor = cantDepositos
        elif depositoSemanal < menor_deposito:
            menor_deposito = depositoSemanal
            posicion_menor = cantDepositos


prom = totalDepositos / cantDepositos
print('la cantidad de depositos realizados son:', cantDepositos,'el promedio es de:', prom )
print("El mayor depósito fue de", mayor_deposito, "en la posición", posicion_mayor)
print("El menor depósito fue de", menor_deposito, "en la posición", posicion_menor)
'''
#resolucion del profe

totalDepositos = 0
cantDepositos = 0
mayor_deposito = 0
menor_deposito = 0
posicion_mayor = 0
posicion_menor = 0

ahorroTotal = int(input('ingrese el monto total que quiere ahorrar:'))
while ahorroTotal < 80000 or ahorroTotal > 100000:
    print('monto invalido')
    ahorroTotal = int(input('ingrese el monto total que quiere ahorrar:'))

while totalDepositos < ahorroTotal:
    depositoSemanal = int(input('ingrese el deposito semanal:'))
    while depositoSemanal < 5000 or depositoSemanal > 10000:
        print('el valor ingresado es incorrecto')
        depositoSemanal = int(input('ingrese el deposito semanal:'))
    cantDepositos = cantDepositos + 1
    if cantDepositos == 1:
       mayor_deposito = depositoSemanal
       menor_deposito = depositoSemanal
       posicion_mayor = cantDepositos
       posicion_menor = cantDepositos
    if depositoSemanal > mayor_deposito:
        mayor_deposito = depositoSemanal
        posicion_mayor = cantDepositos
    if depositoSemanal < menor_deposito:
        menor_deposito = depositoSemanal
        posicion_menor = cantDepositos
    totalDepositos = totalDepositos + depositoSemanal
    print('el acumulado hasta ahora es:', totalDepositos)
#para dejar 2 renglones vacios
print()
print()
prom = totalDepositos / cantDepositos
print('la cantidad de depositos realizados son:', cantDepositos,'el promedio es de:', round(prom,2))
print("El mayor depósito fue de", mayor_deposito, "en la posición", posicion_mayor)
print("El menor depósito fue de", menor_deposito, "en la posición", posicion_menor)
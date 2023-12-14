numeroInicio = int(input('ingrese un numero inicio:'))
numeroFinal = int(input('ingrese un numero limite:'))
acumuladorA = 0
acumuladorB = 0

condicionA = numeroInicio
condicionB = numeroFinal

while condicionA <= numeroFinal:
    #tmp = condicionA
    acumuladorA = acumuladorA + condicionA
    condicionA = condicionA + 1

print(acumuladorA)


# while numeroInicio >= condicionB:
#    tmp = condicionB
#    condicionB = condicionB +1
#    acumuladorB = acumuladorB + tmp
# print (acumuladorB)

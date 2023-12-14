Mayores = 0
Menores = 0
edades = int(input("ingrese edad:"))
sumaMenores = 0
sumaMayores = 0
print("hola")
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

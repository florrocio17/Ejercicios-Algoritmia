
'''
vec = []
i = 0
while i < 10:
    n = int(input('ingrese un numero:'))
    vec.append(n)
    i = i + 1

i = 9
while i >= 0:
    print(vec[i])
    i = i - 1
'''
def imprimirlista(vec):
    largo= len(vec)
    for i in range(largo): 
        print(vec[i],end="")
    print()

#Programaprincipal
v = [ ]
n = int(input("Ingrese unnúmero o -1 para terminar:")) 
while n != -1:
    v.append(n)
    n = int(input("Ingrese unnúmero o -1 para terminar:"))
# Segunda parte: Cálculo de la cantidad de elementos 
# # len( ) devuelve la longitud de la lista
largo =len(v)

if largo == 0:
    print("No se ingresaron valores")
else:
    mayor =v[0]
    pos=0
    for i in range(largo): 
        if v[i]>mayor:
            mayor=v[i]
            pos=i
imprimirlista(v)
print("El máximo es",mayor,"y se encontró en la posición",pos)
print("Borrando el",mayor)
del v[pos] 
imprimirlista(v)
#Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos
#repetidos. El valor de N se ingresa por teclado. Resolver este problema utilizando
#dos estrategias distintas:
#· Impidiendo el agregado de elementos repetidos
#· Eliminando los duplicados luego de generar la lista. Asegurarse que la
#cantidad final de elementos sea la solicitada.



import random
def crearlista(n):
    lista = []
    posiciones = 0
    #mientras la cantidad de posiciones sea menor al parametro puesto de cantidad, se debe agregar numero que no sea repetidos
    while posiciones < n :
        numero = random.randint(0,100)
        #para agregar el primer numero 
        if len(lista) == 0:
            lista.append(numero)
        
        numero_norepetido = True
        for i in range(len(lista)):
            #  si el numero random es igual a una que ya esta en la lista entonces la bandera pasa a false
            if numero == lista[i]:
                numero_norepetido = False
        # solo se debe agregar el numero que no sea igual, o sea que la bandera sea true
        if numero_norepetido == True:
            lista.append(numero)
        posiciones = posiciones + 1
    return lista


#programa principal
n = int(input('ingrese un numero:'))

lista1 = crearlista(n)

print(lista1)



#Eliminar de una lista de números enteros los valores que se encuentren en una
#segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
#resultante. Ambas listas deben rellenarse con números al azar. La cantidad y el
#rango de los valores los decide el programador.

import random
def crearlista(n):
    lista = []
    posiciones = 0
    while posiciones < n:
        numero = random.randint(0,50)
        lista.append(numero)
        posiciones = posiciones + 1
    return lista

def valoresAEliminar(listaoriginal, listaaeliminar): #  1, 4      1,1,5
    listanueva = []
    for i in range(len(listaoriginal)):
        flag = True
        for j in range(len(listaaeliminar)):
            if listaoriginal[i] == listaaeliminar[j]:
                flag = False
        if flag:
            listanueva.append(listaoriginal[i])
    return listanueva

listaA = crearlista(5)
listaB = crearlista(5)
listaC = valoresAEliminar(listaA,listaB)

print(listaA, listaB)
print(listaC)

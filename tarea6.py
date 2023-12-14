#Escribir una función que reciba como parámetros dos números enteros. Calcular
# y devolver el resultado de la multiplicación de ambos valores utilizando solamente
#sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .
'''
def multiplicacion(a,b):
   acumu = 0
   contador = 0
   while contador < b:
       contador = contador + 1
       acumu = acumu + a
   return acumu
'''
'''
prueba = multiplicacion(4,8) 
print(prueba)

#Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante
# multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar.
# Por ejemplo 43 = 4 * 4 * 4.

def potenciacion(a,b):
   acumu = 1
   contador = 0
   while contador < b:
       contador = contador +1
       acumu = multiplicacion(acumu, a)
   return acumu   
       

prueba = potenciacion(3,2) 
print(prueba)
'''
'''
#Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.
def columna_asteriscos(a):
    contador = 0
    resultado = ''
    while contador < a:
        contador = contador + 1
        resultado = resultado + "*\n"
    return resultado   

muestra = columna_asteriscos(4)

print(muestra)

#Devolver True si el número entero recibido como primer parámetro es múltiplo
#del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True
#y esmultiplo(50, 3) devuelve False.

#primer numero puede ser dividido por el segundo y que el resto de 0
#True
def multiplo (a,b):
    if a % b == 0:
        return True
    else:
        return False
    
prueba = multiplo (9,8)  
print(prueba)
'''
#Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o
#0 según el valor recibido sea positivo, negativo o nulo.

def signo(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1
    
prueba = int(input('ingrese un numero:'))
prueba2 = signo(prueba)
print(prueba2)
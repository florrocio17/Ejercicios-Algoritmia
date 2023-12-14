import random

# Funciones


def bienvenida_truco():
    print("Bienvenid@s al Truco. Para Ganar deberás llegar a 30 puntos antes que tu contricante lo haga. Aclaración importante: Se juega con Flor!")
    print()
    print("Le deseamos mucha suerte y exitos!")


def crear_mazo(n, m):
    matriz = []
    for f in range(n):
        matriz.append([])
        for c in range(m):
            matriz[f].append([])
    return matriz


def crear_baraja_truco():
    palos = ["Espada", "Basto", "Oro", "Copa"]
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    baraja_truco = [[valor, palo] for palo in palos for valor in valores]
    return baraja_truco


def asignar_cartas_jugadores(n, m, lista):
    matriz = crear_mazo(n, m)
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            aux = random.choice(lista)
            while aux in matriz[0] or aux in matriz[1]:
                aux = random.choice(lista)
            matriz[f][c].append(aux[0])
            matriz[f][c].append(aux[1])
    return matriz


def imprimir_cartas_jugador(cartas_jugadores):
    print()
    print()
    print("Tus cartas son las siguientes... ")
    print()
    for f in range(len(cartas_jugadores[0])):
        print(f+1, ") ", cartas_jugadores[0][f]
              [0], " de ", cartas_jugadores[0][f][1])


def calcular_envido(cartas_jugadores, n):
    envidos_jugadores = []
    envido = 0
    for f in range(len(cartas_jugadores)):
        if cartas_jugadores[f][0][1] != cartas_jugadores[f][1][1] and cartas_jugadores[f][1][1] != cartas_jugadores[f][2][1] and cartas_jugadores[f][0][1] != cartas_jugadores[f][2][1]:
            lista = [cartas_jugadores[f][0][0], cartas_jugadores[f]
                     [1][0], cartas_jugadores[f][2][0]]
            for j in range(len(lista)):
                if lista[j] in [10, 11, 12]:
                    lista[j] = 0
            envido = max(lista)
            envidos_jugadores.append(envido)

        elif (cartas_jugadores[f][0][1] == cartas_jugadores[f][1][1] and cartas_jugadores[f][1][1] != cartas_jugadores[f][2][1]) or (cartas_jugadores[f][0][1] == cartas_jugadores[f][2][1] and cartas_jugadores[f][2][1] != cartas_jugadores[f][1][1]) or (cartas_jugadores[f][1][1] == cartas_jugadores[f][2][1] and cartas_jugadores[f][2][1] != cartas_jugadores[f][0][1]):
            if cartas_jugadores[f][0][1] == cartas_jugadores[f][1][1]:
                if cartas_jugadores[f][0][0] in [10, 11, 12] and cartas_jugadores[f][1][0] not in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][1][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][0][0] not in [10, 11, 12] and cartas_jugadores[f][1][0] in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][0][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][0][0] in [10, 11, 12] and cartas_jugadores[f][1][0] in [10, 11, 12]:
                    envido = 20
                    envidos_jugadores.append(envido)
                else:
                    envido = 20 + \
                        cartas_jugadores[f][0][0] + cartas_jugadores[f][1][0]
                    envidos_jugadores.append(envido)
            if cartas_jugadores[f][0][1] == cartas_jugadores[f][2][1]:
                if cartas_jugadores[f][0][0] in [10, 11, 12] and cartas_jugadores[f][2][0] not in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][2][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][0][0] not in [10, 11, 12] and cartas_jugadores[f][2][0] in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][0][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][0][0] in [10, 11, 12] and cartas_jugadores[f][2][0] in [10, 11, 12]:
                    envido = 20
                    envidos_jugadores.append(envido)
                else:
                    envido = 20 + \
                        cartas_jugadores[f][0][0] + cartas_jugadores[f][2][0]
                    envidos_jugadores.append(envido)
            if cartas_jugadores[f][1][1] == cartas_jugadores[f][2][1]:
                if cartas_jugadores[f][1][0] in [10, 11, 12] and cartas_jugadores[f][2][0] not in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][2][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][1][0] not in [10, 11, 12] and cartas_jugadores[f][2][0] in [10, 11, 12]:
                    envido = 20 + cartas_jugadores[f][1][0]
                    envidos_jugadores.append(envido)
                elif cartas_jugadores[f][1][0] in [10, 11, 12] and cartas_jugadores[f][2][0] in [10, 11, 12]:
                    envido = 20
                    envidos_jugadores.append(envido)
                else:
                    envido = 20 + \
                        cartas_jugadores[f][1][0] + cartas_jugadores[f][2][0]
                    envidos_jugadores.append(envido)
        else:
            lista = [cartas_jugadores[f][0][0], cartas_jugadores[f]
                     [1][0], cartas_jugadores[f][2][0]]
            for j in range(len(lista)):
                if lista[j] in [10, 11, 12]:
                    lista[j] = 0
            envido = 20
            for i in range(len(lista)):
                envido = envido+lista[i]
            envidos_jugadores.append(envido)
    return envidos_jugadores


def mostrar_puntos(puntos_jugador, puntos_contricante):
    print(puntos_jugador, puntos_contricante)


def envido(calcular_envido, puntos_jugador, puntos_contricante):
    ganador = -1
    print()
    print("Tu envido es: ", calcular_envido[0])
    print()
    print("El envido del rival es: ", calcular_envido[1])
    print()
    if calcular_envido[0] > calcular_envido[1]:
        print("Felicitaciones! Has ganado el envido (+2 puntos)")
        puntos_jugador = puntos_jugador+2
        ganador = 0
    elif calcular_envido[0] < calcular_envido[1]:
        print("El rival tiene más envido que tu por lo tanto te ha ganado (+2 puntos el rival)")
        puntos_contricante = puntos_contricante+2
        ganador = 1
    else:
        # Cuando esté la funcion de ser mano, elegir el ganador
        print("Estan empatados, pero por ser mano gana: ", )
        ganador = 0
    return ganador, puntos_jugador, puntos_contricante


def realenvido(calcular_envido, puntos_jugador, puntos_contricante):
    print()
    print("Tu envido es: ", calcular_envido[0])
    print()
    print("El envido del rival es: ", calcular_envido[1])
    print()
    if calcular_envido[0] > calcular_envido[1]:
        print("Felicitaciones! Has ganado el Real envido (+3 puntos)")
        puntos_jugador = puntos_jugador+3
    elif calcular_envido[0] < calcular_envido[1]:
        print("El rival tiene más envido que tu por lo tanto te ha ganado. (+3 puntos el rival)")
        puntos_contricante = puntos_contricante+3
    else:
        # Cuando esté la funcion de ser mano, elegir el ganador
        print("Estan empatados, pero por ser mano gana: ", )
    return puntos_jugador, puntos_contricante


def faltaenvido(calcular_envido, puntos_jugador, puntos_contrincante):
    print()
    print("Tu envido es: ", calcular_envido[0])
    print()
    print("El envido del rival es: ", calcular_envido[1])
    print()
    if calcular_envido[0] > calcular_envido[1]:
        print("Felicitaciones! Has ganado el Falta envido!! (Has ganado +",
              30-puntos_contrincante, " puntos)")
        puntos_jugador = puntos_jugador+(30-puntos_contrincante)
    elif calcular_envido[0] < calcular_envido[1]:
        print("El rival tiene más envido que tu por lo tanto te ha ganado ((Has ganado +",
              30-puntos_jugador, " puntos)")
        puntos_contrincante = puntos_contrincante+(30-puntos_jugador)
    else:
        # Cuando esté la funcion de ser mano, elegir el ganador
        print("Estan empatados, pero por ser mano gana: ")
    return puntos_jugador, puntos_contrincante

def flor( puntos_jugador, puntos_contricante, cartas_jugadores):
    sublista = cartas_jugadores[0]
    sublista_computadora = cartas_jugadores[1]
    if (sublista[0][1] == sublista[1][1] == sublista[2][1]) and (sublista_computadora[0][1] == sublista_computadora[1][1] == sublista_computadora[2][1]):
        suma_jugador = sum([carta[0] for carta in sublista])
        suma_computadora = sum([carta[0] for carta in sublista_computadora])

        print(cartas_jugadores)

        if suma_jugador > suma_computadora:
            print("Felicitaciones! Has ganado la Flor (+3 puntos)")
            puntos_jugador += 3
        elif suma_jugador < suma_computadora:
            print("El rival tiene más Flor que tú, por lo tanto, te ha ganado. (+3 puntos el rival)")
            puntos_contricante += 3
        else:
            print("Están empatados en Flor, pero por ser mano, ganas: ")
            puntos_jugador += 3

    return puntos_jugador, puntos_contricante

# def flor(calcular_envido, puntos_jugador, puntos_contricante, cartas_jugadores):
#     sublista = cartas_jugadores[0]
#     sublista_computadora = cartas_jugadores[1]
#     print(cartas_jugadores)
#     print(sublista[0][1], sublista[1][1] ,sublista[2][1] , sublista_computadora[0][1],sublista_computadora[1][1], sublista_computadora[2][1] )
#     if (sublista[0][1] == sublista[1][1] == sublista[2][1]) and (sublista_computadora[0][1] == sublista_computadora[1][1] == sublista_computadora[2][1]):
#         if calcular_envido[0] > calcular_envido[1]:
#             print("Felicitaciones! Has ganado la Flor (+3 puntos)")
#             puntos_jugador = puntos_jugador+3
#         elif calcular_envido[0] < calcular_envido[1]:
#             print(
#                 "El rival tiene más Flor que tu por lo tanto te ha ganado. (+3 puntos el rival)")
#             puntos_contricante = puntos_contricante+3
#         else:
#             # Cuando esté la funcion de ser mano, elegir el ganador
#             print("Estan empatados, pero por ser mano gana: ", )
#     elif (cartas_jugadores[0][0] == cartas_jugadores[0][1] == cartas_jugadores[0][2]) and (cartas_jugadores[1][0] != cartas_jugadores[1][1] != cartas_jugadores[1][2]):
#         puntos_jugador = puntos_jugador+3
#         print("Computadora: Eso no se vale :(")
#         print()
#     elif (cartas_jugadores[0][0] != cartas_jugadores[0][1] != cartas_jugadores[0][2]) and (cartas_jugadores[1][0] == cartas_jugadores[1][1] == cartas_jugadores[1][2]):
#         puntos_contricante = puntos_contricante+3
#         print("No tienes Flor por lo tanto te ha ganado automaticamente")
#         print()
#     return puntos_jugador, puntos_contricante


# def truco(rondas_jugadas):
#     if rondas_jugadas == 3:
#         print("Se han jugado las 3 rondas")


def imprimir_puntos(puntos_jugador, puntos_contricante):
    print("Tus puntos son: ", puntos_jugador)
    print("Los puntos del rival son: ", puntos_contricante)


def imprimir_acciones():
    print("Que acción desea realizar?")
    actions = ["Envido", "Real Envido", "Falta Envido", "Flor",
               "Truco", "Re Truco", "Vale Cuatro", "Irse al Mazo", "Tirar Carta"]
    for i in range(len(actions)):
        print(i+1, ". ", actions[i])
    print("-----> Ingrese -1 para salir del juego <----")


def tirar_carta_jugador(cartas_jugadores):
    print("Tus cartas son las siguientes... ")
    print()
    for f in range(len(cartas_jugadores[0])):
        print(f+1, ") ", cartas_jugadores[0][f]
              [0], " de ", cartas_jugadores[0][f][1])
    print()
    carta = int(input("Ingrese el número de la carta que desea tirar: "))
    while carta < 1 or carta > 3:
        print("Ingrese un número de carta válido")
        carta = int(input("Ingrese la carta que desea tirar: "))
    return carta - 1


def tirar_carta_computadora(cartas_jugadores, carta_jugador):
    if carta_jugador == 0:  # Es la primera jugada
        carta_computadora = random.choice(cartas_jugadores[1])
    else:  # Si no es la primera jugada
        carta_jugada = cartas_jugadores[0][carta_jugador - 1]
        cartas_validas = [carta for carta in cartas_jugadores[1]
                          if carta[0] > carta_jugada[0]]
        if cartas_validas:
            carta_computadora = max(cartas_validas, key=lambda x: x[0])
        else:
            if random.choice([True, False]):
                print("Computadora: Me voy al mazo")
                return -1
            else:
                carta_computadora = random.choice(cartas_jugadores[1])

    print("Computadora: Tira la carta", carta_computadora)
    return cartas_jugadores[1].index(carta_computadora) + 1


def valor_carta(carta):
    valores = {
        (1, 'Espada'): 14,
        (1, 'Basto'): 13,
        (7, 'Espada'): 12,
        (7, 'Oro'): 11,
        (3, 'Espada'): 10,
        (3, 'Oro'): 10,
        (3, 'Copa'): 10,
        (3, 'Basto'): 10,
        (2, 'Espada'): 9,
        (2, 'Oro'): 9,
        (2, 'Copa'): 9,
        (2, 'Basto'): 9,
        (1, 'Copa'): 8,
        (1, 'Oro'): 8,
        (12, 'Espada'): 7,
        (12, 'Basto'): 7,
        (12, 'Oro'): 7,
        (12, 'Copa'): 7,
        (11, 'Espada'): 6,
        (11, 'Basto'): 6,
        (11, 'Oro'): 6,
        (11, 'Copa'): 6,
        (10, 'Espada'): 5,
        (10, 'Basto'): 5,
        (10, 'Oro'): 5,
        (10, 'Copa'): 5,
        (7, 'Copa'): 4,
        (7, 'Basto'): 4,
        (6, 'Espada'): 3,
        (6, 'Basto'): 3,
        (6, 'Oro'): 3,
        (6, 'Copa'): 3,
        (5, 'Espada'): 2,
        (5, 'Basto'): 2,
        (5, 'Oro'): 2,
        (5, 'Copa'): 2,
        (4, 'Espada'): 1,
        (4, 'Basto'): 1,
        (4, 'Oro'): 1,
        (4, 'Copa'): 1,
    }

    # Si no encuentra la carta, devuelve 0 puntos
    return valores.get(tuple(carta), 0)


def truco(ganadores, puntos_jugador, puntos_contrincante):
    if ganadores.count('jugador') >= 2:
        puntos_jugador += 1
        print("Como se cantó truco, sumas 2 puntos por el truco")
    elif ganadores.count('computadora') >= 2:
        puntos_contrincante += 1
        print("Como se cantó truco, la computadora suma 2 puntos por el truco")
    else:
        print("¡Han empatado! No se suman puntos.")

    return puntos_jugador, puntos_contrincante


def retruco(ganadores, puntos_jugador, puntos_contrincante):
    if ganadores.count('jugador') >= 2:
        puntos_jugador += 2
        print("Como se cantó retruco, sumas 3 puntos por el retruco")
    elif ganadores.count('computadora') >= 2:
        puntos_contrincante += 2
        print("Como se cantó retruco, la computadora suma 3 puntos por el retruco")
    else:
        print("¡Han empatado! No se suman puntos.")

    return puntos_jugador, puntos_contrincante


def vale4(ganadores, puntos_jugador, puntos_contrincante):
    if ganadores.count('jugador') >= 2:
        puntos_jugador += 3
        print("Como se cantó vale cuatro, sumas 4 puntos por el vale cuatro")
    elif ganadores.count('computadora') >= 2:
        puntos_contrincante += 3
        print(
            "Como se cantó vale cuatro, la computadora suma 4 puntos por el vale cuatro")
    else:
        print("¡Han empatado! No se suman puntos.")

    return puntos_jugador, puntos_contrincante


def sistema_de_tirada(baraja_truco, cartas_jugadores, puntos_jugador, puntos_contrincante, rondas_jugadas, truco_cantado, retruco_cantado, vale4_cantado):
    cantidad_de_jugadores = 2
    cantidad_de_cartas = 3
    cartas_jugadas = [[], []]
    ganadores = []

    for _ in range(3):
        carta_jugador = tirar_carta_jugador(cartas_jugadores)
        cartas_jugadas[0].append(cartas_jugadores[0][carta_jugador])

        carta_computadora = tirar_carta_computadora(
            cartas_jugadores, carta_jugador)
        if carta_computadora == -1:
            ganadores.append('jugador')
            print("Se reinicia la mano. Se han repartido nuevas cartas.")
            puntos_jugador += 1
            cartas_jugadores = asignar_cartas_jugadores(
            cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
            imprimir_cartas_jugador(cartas_jugadores)
            return puntos_jugador, puntos_contrincante, rondas_jugadas
            

        cartas_jugadas[1].append(
            cartas_jugadores[1][carta_computadora - 1])
        cartas_jugadores[0].pop(carta_jugador)
        cartas_jugadores[1].pop(carta_computadora - 1)
  

        if valor_carta(cartas_jugadas[0][-1]) > valor_carta(cartas_jugadas[1][-1]):
                ganadores.append('jugador')
        elif valor_carta(cartas_jugadas[0][-1]) < valor_carta(cartas_jugadas[1][-1]):
                ganadores.append('computadora')
        else:
                if _ < 2:
                    # Si hay empate en la primera o segunda ronda, se juega la siguiente ronda para definir
                    continue
                else:
                    # Si hay empate en la tercera ronda, el ganador de la segunda ronda gana la partida
                    if ganadores[1] == ganadores[0]:
                        ganadores.append(ganadores[1])
                    else:
                        # Si hay empate en la tercera ronda pero cada uno ganó una, se define el ganador de la primera
                        ganadores.append(ganadores[0])
        print("----> GANADOR DE LA JUGADA: ", ganadores[-1])
        rondas_jugadas += 1

    if ganadores[0] == 'empate':
        if ganadores[1] != 'empate':
            if ganadores[1] == 'jugador':
                puntos_jugador += 1
            else:
                puntos_contrincante += 1
    elif ganadores[1] == 'empate':
        if ganadores[0] != 'empate':
            if ganadores[0] == 'jugador':
                puntos_jugador += 1
            else:
                puntos_contrincante += 1
    else:
        if ganadores.count('jugador') > ganadores.count('computadora'):
            puntos_jugador += 1
        else:
            puntos_contrincante += 1

    if truco_cantado and not retruco_cantado and not vale4_cantado:
        puntos_jugador, puntos_contrincante = truco(
            ganadores, puntos_jugador, puntos_contrincante)

    if retruco_cantado and not vale4_cantado:
        puntos_jugador, puntos_contrincante = retruco(
            ganadores, puntos_jugador, puntos_contrincante)

    if vale4_cantado and ganadores.count('jugador') >= 2:
        puntos_jugador, puntos_contrincante = vale4(
            ganadores, puntos_jugador, puntos_contrincante)

    return puntos_jugador, puntos_contrincante, rondas_jugadas,


def main():
    bienvenida_truco()
    puntos_jugador = 0
    puntos_contrincante = 0
    baraja_truco = crear_baraja_truco()
    respuestas = ["Quiero", "No Quiero"]
    cantidad_de_jugadores = 2
    cantidad_de_cartas = 3
    cartas_jugadores = asignar_cartas_jugadores(
        cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
    imprimir_cartas_jugador(cartas_jugadores)
    envido_jugadores = calcular_envido(cartas_jugadores, cantidad_de_jugadores)
    accion = 0
    envido_cantado = False
    truco_cantado = False
    retruco_cantado = False
    vale4_cantado = False
    rondas_jugadas = 0
    imprimir_acciones()
    imprimir_puntos(puntos_jugador, puntos_contrincante)
    accion = int(input("Ingrese una opción: "))

    while accion != -1 and puntos_jugador <= 30 or puntos_contrincante <= 30:
        if accion == 1:
            if not envido_cantado:
                print("Envido!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    ganador, puntos_jugador, puntos_contrincante = envido(
                        envido_jugadores, puntos_jugador, puntos_contrincante)
                    envido_cantado = False  
                else:
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el envido")
                    envido_cantado = False
                
            else:
                print("Ya cantaste envido, no puedes volver a cantar")
                print()
        elif accion == 2:
            if not envido_cantado:
                print("Real Envido!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    puntos_jugador, puntos_contrincante = realenvido(
                        envido_jugadores, puntos_jugador, puntos_contrincante)
                else:
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el envido")
                envido_cantado = True
            else:
                print("Ya cantaste envido, no puedes volver a cantar")
                print()
        elif accion == 3:
            if not envido_cantado:
                print("Falta Envido!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    puntos_jugador, puntos_contrincante = faltaenvido(
                        envido_jugadores, puntos_jugador, puntos_contrincante)
                else:
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el envido")
                envido_cantado = True
            else:
                print("Ya cantaste envido, no puedes volver a cantar")
                print()
        elif accion == 4:
            print("Flor!")
            print()
            respuesta = random.choice(respuestas)
            if respuesta == "Quiero":
                print("Computadora: Quiero!")
                print()
                puntos_jugador, puntos_contrincante = flor(
                     puntos_jugador, puntos_contrincante, cartas_jugadores)
            else:
                print("Computadora: No quiero.")
                puntos_jugador = puntos_jugador+1
                print("Has ganado un punto por la flor")
        elif accion == 5:
            if not truco_cantado:
                print("Truco!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    truco_cantado = True
                    print("Computadora: Quiero!")
                    print()
                    print("Al jugar las 3 rondas, el ganador se llevará 2 puntos")
                else:
                    truco_cantado = True
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el truco no querido")
                    print("Se renueva la mano. Se han repartido nuevas cartas")
                    print()
                    cartas_jugadores = asignar_cartas_jugadores(
                    cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
                    envido_jugadores = calcular_envido(
                    cartas_jugadores, cantidad_de_jugadores)
                    imprimir_cartas_jugador(cartas_jugadores)
                    truco_cantado = False

            else:
                print("Ya cantaste truco, no puedes volver a cantar")
                print()
        elif accion == 6:
            if truco_cantado:
                print("Re Truco!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    retruco_cantado = True
                    print("Computadora: Quiero!")
                    print()
                    print("Al jugar las 3 rondas, el ganador se llevará 3 puntos")
                else:
                    retruco_cantado = True
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el retruco no querido")
                    print("Se renueva la mano. Se han repartido nuevas cartas")
                    print()
                    cartas_jugadores = asignar_cartas_jugadores(
                    cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
                    envido_jugadores = calcular_envido(
                    cartas_jugadores, cantidad_de_jugadores)
                    imprimir_cartas_jugador(cartas_jugadores)

            else:
                print("No puedes cantar re truco sin haber cantado truco antes")
                print()
        elif accion == 7:
            if retruco_cantado:
                print("Vale Cuatro!")
                print()
                respuesta = random.choice(respuestas)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    print("Al jugar las 3 rondas, el ganador se llevará 4 puntos")
                else:
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el vale cuatro no querido")
                    print("Se renueva la mano. Se han repartido nuevas cartas")
                    print()
                    cartas_jugadores = asignar_cartas_jugadores(
                    cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
                    envido_jugadores = calcular_envido(
                    cartas_jugadores, cantidad_de_jugadores)
                    imprimir_cartas_jugador(cartas_jugadores)

            else:
                print("No puedes cantar vale cuatro sin haber cantado retruco antes")
                print()
        elif accion == 8:
            print("Te has ido al mazo")
            puntos_contrincante = puntos_contrincante+1
            print()
            print("Se reinicia la mano. Computadora suma 1 punto. Se han repartido nuevas cartas.")
            cartas_jugadores = asignar_cartas_jugadores(
                    cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
            envido_jugadores = calcular_envido(
                    cartas_jugadores, cantidad_de_jugadores)
            imprimir_cartas_jugador(cartas_jugadores)
            envido_cantado = False
            truco_cantado = False
            retruco_cantado = False
            rondas_jugadas = 0

        elif accion == 9:
            puntos_jugador, puntos_contrincante, rondas_jugadas = sistema_de_tirada(baraja_truco,
                cartas_jugadores, puntos_jugador, puntos_contrincante, rondas_jugadas, truco_cantado, retruco_cantado, vale4_cantado)
            if rondas_jugadas == 3:
                print("Se han jugado las 3 rondas")
                print()
                print("Se han repartido nuevas cartas")
                print()
                cartas_jugadores = asignar_cartas_jugadores(
                    cantidad_de_jugadores, cantidad_de_cartas, baraja_truco)
                envido_jugadores = calcular_envido(
                    cartas_jugadores, cantidad_de_jugadores)
                imprimir_cartas_jugador(cartas_jugadores)
                envido_cantado = False
                truco_cantado = False
                retruco_cantado = False
                rondas_jugadas = 0
        else:
            print("Ingrese una opción válida")
            print()
        if puntos_jugador >= 30:
            print("Felicitaciones, has ganado el juego!")
            accion = -1
        elif puntos_contrincante >= 30:
            print("Lo sentimos, has perdido el juego :(")
            accion = -1
        mensaje = "Ronda " + str(rondas_jugadas+1) + " finalizada"
        imprimir_acciones()
        imprimir_puntos(puntos_jugador, puntos_contrincante)
        accion = int(input("Ingrese una opción: "))
        

    print("Gracias por jugar al Truco!")
    print("Esperamos que haya disfrutado del juego!")
    print("Vuelva pronto!")
    print("Fin del programa")


main()

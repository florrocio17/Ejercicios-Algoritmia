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


def flor(calcular_envido, puntos_jugador, puntos_contricante, cartas_jugadores):
    print()
    if (cartas_jugadores[0][0] == cartas_jugadores[0][1] == cartas_jugadores[0][2]) and (cartas_jugadores[1][0] == cartas_jugadores[1][1] == cartas_jugadores[1][2]):
        if calcular_envido[0] > calcular_envido[1]:
            print("Felicitaciones! Has ganado la Flor (+3 puntos)")
            puntos_jugador = puntos_jugador+3
        elif calcular_envido[0] < calcular_envido[1]:
            print(
                "El rival tiene más Flor que tu por lo tanto te ha ganado. (+3 puntos el rival)")
            puntos_contricante = puntos_contricante+3
        else:
            # Cuando esté la funcion de ser mano, elegir el ganador
            print("Estan empatados, pero por ser mano gana: ", )
    elif (cartas_jugadores[0][0] == cartas_jugadores[0][1] == cartas_jugadores[0][2]) and (cartas_jugadores[1][0] != cartas_jugadores[1][1] != cartas_jugadores[1][2]):
        puntos_jugador = puntos_jugador+3
        print("Computadora: Eso no se vale :(")
        print()
    elif (cartas_jugadores[0][0] != cartas_jugadores[0][1] != cartas_jugadores[0][2]) and (cartas_jugadores[1][0] == cartas_jugadores[1][1] == cartas_jugadores[1][2]):
        puntos_contricante = puntos_contricante+3
        print("No tienes Flor por lo tanto te ha ganado automaticamente")
        print()
    return puntos_jugador, puntos_contricante


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
    valor = carta[0]

    jerarquia = {
        1: 14,
        2: 13,
        3: 12,
        10: 11,
        11: 10,
        12: 9,
        7: 8,
        6: 7,
        5: 6,
        4: 5,
    }

    return jerarquia.get(valor, valor)


def sistema_de_tirada(cartas_jugadores, puntos_jugador, puntos_contrincante, rondas_jugadas):
    cartas_jugadas = [[], []]
    ganadores = []

    for _ in range(3):
        carta_jugador = tirar_carta_jugador(cartas_jugadores)
        cartas_jugadas[0].append(cartas_jugadores[0][carta_jugador])

        carta_computadora = tirar_carta_computadora(
            cartas_jugadores, carta_jugador)
        if carta_computadora == -1:
            ganadores.append('jugador')
        else:
            cartas_jugadas[1].append(
                cartas_jugadores[1][carta_computadora - 1])
            cartas_jugadores[0].pop(carta_jugador)
            cartas_jugadores[1].pop(carta_computadora - 1)

            if valor_carta(cartas_jugadas[0][-1]) > valor_carta(cartas_jugadas[1][-1]):
                ganadores.append('jugador')
            elif valor_carta(cartas_jugadas[0][-1]) < valor_carta(cartas_jugadas[1][-1]):
                ganadores.append('computadora')
            else:
                ganadores.append('empate')

        print("----> GANADOR DE LA RONDA JUGADA: ", ganadores[-1])
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
    rondas_jugadas = 0
    imprimir_acciones()
    imprimir_puntos(puntos_jugador, puntos_contrincante)
    accion = int(input("Ingrese una opción: "))

    while accion != -1:
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
                else:
                    print("Computadora: No quiero.")
                    puntos_jugador = puntos_jugador+1
                    print("Has ganado un punto por el envido")
                envido_cantado = True
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
                    envido_jugadores, puntos_jugador, puntos_contrincante, cartas_jugadores)

            else:
                print("Computadora: No quiero.")
                puntos_jugador = puntos_jugador+1
                print("Has ganado un punto por la flor")
        elif accion == 5:
            print("Truco!")
            print()
            respuesta = random.choice(respuestas)
            print("Computadora: ", respuesta)
            if respuesta == "Quiero":
                print("Computadora: Quiero!")
                print()
                puntos_jugador = puntos_jugador+2
                print("Has ganado dos puntos por el truco")
                truco_cantado = True
            else:
                print("Computadora: No quiero.")
                puntos_contrincante = puntos_contrincante+1
                print("Has ganado un punto por el truco")
        elif accion == 6:
            if truco_cantado:
                print("Re Truco!")
                print()
                respuesta = random.choice(respuestas)
                print("Computadora: ", respuesta)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    puntos_jugador = puntos_jugador+3
                    print("Has ganado tres puntos por el re truco")
                    retruco_cantado = True
                else:
                    print("Computadora: No quiero.")
                    puntos_contrincante = puntos_contrincante+1
                    print("Has ganado un punto por el re truco")
            else:
                print("No puedes cantar re truco sin haber cantado truco antes")
                print()
        elif accion == 7:
            if retruco_cantado:
                print("Vale Cuatro!")
                print()
                respuesta = random.choice(respuestas)
                print("Computadora: ", respuesta)
                if respuesta == "Quiero":
                    print("Computadora: Quiero!")
                    print()
                    puntos_jugador = puntos_jugador+4
                    print("Has ganado cuatro puntos por el vale cuatro")
                else:
                    print("Computadora: No quiero.")
                    puntos_contrincante = puntos_contrincante+1
                    print("Has ganado un punto por el vale cuatro")
            else:
                print("No puedes cantar vale cuatro sin haber cantado retruco antes")
                print()
        elif accion == 8:
            print("Te has ido al mazo")
            puntos_contrincante = puntos_contrincante+1
        elif accion == 9:
            puntos_jugador, puntos_contrincante, rondas_jugadas = sistema_de_tirada(
                cartas_jugadores, puntos_jugador, puntos_contrincante, rondas_jugadas)
            
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

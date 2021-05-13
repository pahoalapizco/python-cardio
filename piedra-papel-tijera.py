manos = ("Piedra", "Papel", "Tijeras")


def mostrar_menu():
    menu = """
    Escribe el número correspondiente a tu elección
        [0] - Piedra
        [1] - Papel
        [2] - Tijeras
    """
    print(menu)



def juego(jugador_uno, jugador_dos):
    ganador_uno = 1
    ganador_dos = 2
    if jugador_uno == "Piedra" and jugador_dos == "Tijeras":
        return ganador_uno
    if jugador_uno == "Tijeras" and jugador_dos == "Papel":
        return ganador_uno
    if jugador_uno == "Papel" and jugador_uno == "Piedra":
        return ganador_uno
    if jugador_dos == "Piedra" and jugador_uno == "Tijeras":
        return ganador_dos
    if jugador_dos == "Tijeras" and jugador_uno == "Papel":
        return ganador_dos
    if jugador_dos == "Papel" and jugador_uno == "Piedra":
        return ganador_dos
    if jugador_uno == jugador_dos:
        return 0


def run():
    ganados_jugador_uno = 0
    ganados_jugador_dos = 0

    while ganados_jugador_uno < 2 and ganados_jugador_dos < 2:
        mostrar_menu()
        sel_jugador_uno = int(input("Jugador uno: "))
        sel_jugador_dos = int(input("Jugador dos: "))
        ganador_partida = juego(manos[sel_jugador_uno], manos[sel_jugador_dos])

        if ganador_partida > 0:
            print('El ganador de la partida es el jugador # ' + str(ganador_partida))
            
        if ganador_partida == 1:
            ganados_jugador_uno += 1
        elif ganador_partida == 2:
            ganados_jugador_dos += 1        

    if ganados_jugador_uno > ganados_jugador_dos:
        print("El ganador es el jugador 1")
    else:
        print("El ganador es el jugador 2")



if __name__ == "__main__":
    run()
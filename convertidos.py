def millas_kilometros():
    KILOMETROS_EN_MILLAS = 1.609344
    millas = float(input("Millas: "))
    kilometros = millas * KILOMETROS_EN_MILLAS
    print(str(millas) + " son " + str(kilometros) + " kilometros")


def kilometros_millas():
    MILLAS_EN_KILOMETROS = 0.621371
    kilometros = float(input("Kilometros: "))
    millas = kilometros * MILLAS_EN_KILOMETROS
    print(str(kilometros) + " son " + str(millas) + " millas")
    pass


def run():
    menu = """
    Escribe el número correspondiente a tu elección
        [1] - Millas a kilometros
        [2] - Kilometros a millas

    Cualquier otra tecla finalizará el convertidor de unidades.
    Seleccionar: """

    seleccion = input(menu)

    if seleccion == "1":
        millas_kilometros()
    elif seleccion == "2":
        kilometros_millas()
    else:
        print("Convertidor finalizado.")


if __name__ == "__main__":
    run()
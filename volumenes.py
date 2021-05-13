PI = 3.1416


def volumen_cilindro():
    radio = float(input("Escribe el radio del cilindro: "))
    altura = float(input("Escribe la altura del cilindro: "))
    volumen = PI * pow(radio, 2) * altura
    print("El volumen del cilindro es de: " + str(volumen))


def volumen_cubo():    
    lado = float(input("Escribe el lado del cubo: "))
    volumen =  pow(lado, 3) 
    print("El volumen del cilindro es de: " + str(volumen))


def volumen_esfera():
    radio = float(input("Escribe el radio de la esfera: "))
    volumen = (4/3) * PI * pow(radio, 3)
    print("El volumen de la esfera es de: " + str(volumen))


def volumen_cono():
    radio = float(input("Escribe el radio del cono: "))
    altura = float(input("Escribe la altura del cono: "))
    volumen = (PI * pow(radio, 2) * altura) / 3
    print("El volumen del cilindro es de: " + str(volumen))


def run ():
    menu = """
    Escribe el número correspondiente a tu elección
        [1] - Cilindro
        [2] - Cubo
        [3] - Esfera
        [4] - Cono
    Cualquier otra tecla finalizará la calculadora.
    Seleccionar: """
    seleccion = input(menu)

    if seleccion == "1":
        volumen_cilindro()
    elif seleccion == "2":
        volumen_cubo()
    elif seleccion == "3":
        volumen_esfera()
    elif seleccion == "4":
        volumen_cono()
    else:
        print("Calculadora de volumen finalizada")   



if __name__ == "__main__":
    run()
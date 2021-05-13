def tipo_triangulo(base, altura):
    if base == altura:
        return "equilatero"
    elif base > altura:
        return "escaleno"
    else:
        return "isoceles"


def run():
    base = int(input("Escribe la base del triangulo: "))
    altura = int(input("Escribe la altura del triangulo: "))

    area = (base * altura) / 2

    print("El área del triangulo "+ tipo_triangulo(base, altura) +" es de " + str(area))


if __name__ == "__main__":
    run()
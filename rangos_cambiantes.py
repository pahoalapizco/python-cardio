def run():
    limite_inferior = int(input("Escribe el límite inferior: "))
    limite_superior = int(input("Escribe el límite superior: "))
    comparacion = int(input("Escribe el número de comparacion: "))

    while comparacion < limite_inferior or comparacion > limite_superior:
        if comparacion < limite_inferior:
            print(str(comparacion) + " esta por debajo de " + str(limite_inferior))            

        if comparacion > limite_superior:
            print(str(comparacion) + " esta por encima de " + str(limite_superior))

        comparacion = int(input("Escribe el número de comparacion: "))      

    if comparacion >= limite_inferior and comparacion <= limite_superior:
        print(str(comparacion) + " se encuentra en el rango de " + str(limite_inferior) + " y " + str(limite_superior))


if __name__ == "__main__":
    run()
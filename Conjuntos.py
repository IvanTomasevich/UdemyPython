# Obtener los sets del usuario, se llamaran A y B
# hacer funcion de union
# hacer funcion de interseccion
# hacer funcion de diferencia
# hacer funcion de diferencia simetrica


def union_conjunto(conjunto_a, conjunto_b):
    print("\n La union de A y B es {}\n".format(conjunto_a.union(conjunto_b)))


def interseccion_conjunto(conjunto_a, conjunto_b):
    print("\n La interseccion de A y B es {}\n".format(conjunto_a.intersection(conjunto_b)))


def diferencia_conjunto(conjunto_a, conjunto_b):
    print("Elije el orden de la diferencia a realizar: ")
    print("1 - A - B")
    print("2 - B - A")
    try:
        op = int(input("Opcion: "))
    except ValueError:
        print("\nIntroduce 1 o 2\n")
    else:
        if op == 1:
            print("\n La diferencia de A y B es {}\n".format(conjunto_a.difference(conjunto_b)))
        elif op == 2:
            print("\n La diferencia de B y A es {}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print(" No es una opcion valida. Intentalo nuevamente")
            diferencia_conjunto(conjunto_a, conjunto_b)


def diferencia_simetrica(conjunto_a, conjunto_b):
    print("\n La diferencia simetrica de A y B es {}\n".format(conjunto_a.symmetric_difference(conjunto_b)))


def ver_instrucciones():
    print("Puede realizar las siguientes operaciones: ")
    print("1 - Union")
    print("2 - Interceccion")
    print("3 - Diferencia")
    print("4 - Diferencia simetrica")
    print("5 - Ver instrucciones")
    print("6- Salir")


def calculadora_conjuntos():
    print("              ########  BIENVENIDO  #########")
    print(" Ingresa los elemntos de los conjuntos separados por espacios")
    print("por ejemplo - 4 62 7 45 1")
    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())
    ver_instrucciones()
    while True:
        try:
            opcion = int(input("¿Su opcion es? "))
        except ValueError:
            print("Introduse un numero del 1 - 6")
        else:
            if opcion == 1:
                print("Union")
                union_conjunto(conjunto_a, conjunto_b)
            elif opcion == 2:
                print("Interseccion")
                interseccion_conjunto(conjunto_a, conjunto_b)
            elif opcion == 3:
                print("Diferencia")
                diferencia_conjunto(conjunto_a, conjunto_b)
            elif opcion == 4:
                print("Diferencia simetrica")
                diferencia_simetrica(conjunto_a, conjunto_b)
            elif opcion == 5:
                ver_instrucciones()
            elif opcion == 6:
                print("\n Gracias!!!!\n")
                break
            else:
                print("No reconozco esa opcion. Intenta nuevamente")


calculadora_conjuntos()

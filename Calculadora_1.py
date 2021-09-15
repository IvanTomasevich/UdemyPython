# Desplegado de las instrucciones
# Obtener el numero de operacion
# Obtener los del usuario
# Realizar la operacion en base a la peticion del usuario
# Desplegar el resultado
# Preguntar si quiere realizar otra operacion
def realizarOperacion(operacion, valA, valB):
    if operacion == 1:
        return valA + valB
    elif operacion == 2:
        return valA - valB
    elif operacion == 3:
        return valA * valB
    else:
        return valA / valB

print()
print("Bienvenido a Pycalculator!!")
print()
while True:
    print("Puede realizar las siguientes operaciones: ")
    print("1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    try:
        operacion = int(input("Introduce el numero de la operacion a realizar: "))
        if operacion < 1 or operacion > 4:
            print("Este no es una opcion valida")
            continue
        valA = int(input("Ingresa el primer valor: "))
        valB = int(input("Ingresa el segundo valor: "))
    except ValueError:
        print("Por favor ingresa solo numeros")
    else:
        resultado = realizarOperacion(operacion, valA, valB)
        print("El resultado es ", resultado)
        continuar = input("Desea continuar? si/no: ")
        print()
        if continuar != "si":
            break
print("Gracias por calcular con Pycalculator!!")

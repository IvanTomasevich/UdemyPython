import datetime


def ver_opciones():

    print("1 - Ver la hora")
    print("2 - Ver la fecha y la hora")
    print("3 - Ver la hora en New York")
    print("4 - Ver la hora en San Francisco")
    print("5 - Ver las opciones nuevamente")
    print("6 - Salir")


def ver_hora(time_zone):
    if time_zone == -3:
        zone = "Argentina"
    elif time_zone == -4:
        zone = "New york"
    else:
        zone = "San Francisco"
    formato = "%H:%M:%S"
    time_zone = datetime.timezone(datetime.timedelta(hours=time_zone))
    hora_actual = datetime.datetime.now(time_zone).time()
    hora_format = hora_actual.strftime(formato)
    print("La hora en {} es {}".format(zone, hora_format))


def ver_fecha_hora():
    formato = "%B %d, %Y  %H:%M:%S"
    time_zone = datetime.timezone(datetime.timedelta(hours=-3))
    fecha_actual = datetime.datetime.now(time_zone)
    fecha_format = fecha_actual.strftime(formato)
    print("La fecha de ahora es {}".format(fecha_format))


def ver_reloj():

    print("Reloj mundial")
    print("Estas son las opciones")
    ver_opciones()

    while True:
        opcion = int(input("¿Que opcion?: "))

        if opcion == 1:
            ver_hora(-3)
        elif opcion == 2:
            ver_fecha_hora()
        elif opcion == 3:
            ver_hora(-4)
        elif opcion == 4:
            ver_hora(-7)
        elif opcion == 5:
            ver_opciones()
        elif opcion == 6:
            break
        else:
            print("No es una opcion valida")
    print("Gracias que tenga buen dia!")


ver_reloj()

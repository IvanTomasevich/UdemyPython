contactos = {}


def agregar_contacto():
    print("--------Agregue contacto----------")
    print()
    nombre = input("Nombre contacto: ")
    cel = input("Numero telefonico: ")
    contactos[nombre] = cel
    print(f"Se agrego el contacto {contactos[nombre]} con exito")
    print()


def remover_contacto():
    print("--------Elimine contacto----------")
    print()
    nombre = input("Nombre del contacto: ")
    try:
        del contactos[nombre]
    except KeyError:
        print("*****************************************")
        print("El contacto que decea eliminar no existe!")
        print("*****************************************")
    else:
        print("******************************************************")
        print(f"Se elimino el contacto {contactos[nombre]} con exito")
        print()


def actualizar_contacto():
    print("--------Actualizar contacto----------")
    print()
    nombre = input("Nombre contacto a actualizar: ")

    cel = input("Numero telefonico nuevo: ")
    contactos[nombre] = cel
    print("******************************************************")
    print(f"El contacto {nombre} se actualizo con exito!")
    print()


def mostrar_contacto():
    print("--------Contacto----------")
    print()
    nombre = input("Nombre del contacto: ")
    try:
        print(nombre + " Cel: " + contactos[nombre])
        print()
    except KeyError:
        print("*****************************************")
        print("El contacto no existe!")
        print("*****************************************")


def listar_contactos():
    print("--------Lista de contactos----------")
    print()
    if len(contactos) == 0:
        print("No tenes ningun contacto!")
    else:
        for contacto in contactos:
            print("Nombre: " + contacto + "-> Cel: " + contactos[contacto])
        print()


print("---------------Lista de contactos---------------")
while True:
    print("Puede realizar las siguientes operaciones: ")
    print("1 - Agregar contacto")
    print("2 - Remover contacto")
    print("3 - Actualizar contacto")
    print("4 - ver un contacto")
    print("5 - ver todos los contactos")
    print("6 - Salir")

    try:
        operacion = int(input("      ¿Que opcion? "))
        print()
    except ValueError:
        print()
        print("Por favor, ingrese una opcion del menu!!")
        print()
    else:
        if operacion == 1:
            agregar_contacto()
        elif operacion == 2:
            remover_contacto()
        elif operacion == 3:
            actualizar_contacto()
        elif operacion == 4:
            mostrar_contacto()
        elif operacion == 5:
            listar_contactos()
        elif operacion == 6:
            break
        else:
            print("Opcion invalida")

print("************************")
print("       Gracias!!")
print("************************")

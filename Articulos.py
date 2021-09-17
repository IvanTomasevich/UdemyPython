# Agregar articulos
# Remover articulos
# Ver articulos

articulos = []


def agregar_articulo():
    print("--------Agregue articulos----------")
    print()
    articulo = input("Agregar articulo: ")
    articulos.append(articulo.capitalize())
    print(f"Se agrego el articulo {articulo} exitosamente")
    print()


def remover_articulo():
    print("--------Elimine articulos----------")
    print()
    articulo = input("Eliminar articulo: ")
    articulos.remove(articulo.capitalize())
    print(f"Se elimino el articulo {articulo} con exito")
    print()



def listar_articulos():
    print("--------Lista de articulos----------")
    print()
    for i in articulos:
        print(i)
    print()


print("---------------Lista de compras---------------")
while True:
    print("Puede realizar las siguientes operaciones: ")
    print("1 - Agregar articulo")
    print("2 - Remover articulo")
    print("3 - Listar articulos")
    print("4 - Salir")
    operacion = int(input("      ¿Que opcion? "))

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        listar_articulos()
    else:
        break
print("************************")
print("       Gracias!!")
print("     vuelvas prontus")

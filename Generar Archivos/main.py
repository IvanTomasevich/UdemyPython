
"""archivoLista = open("lista.txt", "w")

archivoLista.write("Mi primer archivo creado con Python\nEsta es otra linea")

archivoLista.close()"""


def agregar_articulo(articulo):

    archivo_lista = open("lista.txt", "a")
    archivo_lista.write("{}\n".format(articulo))
    archivo_lista.close()

agregar_articulo(input("Articulo que agregar: "))
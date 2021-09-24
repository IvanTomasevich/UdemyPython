import random
# Mejorar y dar nivel de dificultad

def play():
    vidas = 0
    num_aleatorio = random.randint(1, 10)
    print("******************** Adivina el numero ********************")
    print("Estoy pensando un numero del 1 al 10")
    print("Adivina cual es!!!")
    print("Recuerda solo tienes 3 vidas")
    while vidas < 3:

        try:
            adivinanza = int(input("El numero es: "))
        except ValueError:
            print("Solamente numeros del 1 al 10 genio!")
        else:
            if adivinanza == num_aleatorio:
                print("******************** Adivina el numero ********************")
                print("ADIVINASTE!!!")
                print()
                one_more = input("Queres jugar una fichita mas? si/no: ")
                if one_more.lower() == "si":
                    play()
                else:
                    break
            elif adivinanza < num_aleatorio:
                print("******************** Adivina el numero ********************")
                print("Fallaste!! El numero es mas alto")
                print("Intentalo de nuevo")
                print()
            else:
                print("******************** Adivina el numero ********************")
                print("Fallaste!! El numero es mas bajo")
                print("Intentalo de nuevo")
                print()
            vidas += 1
            print("Vidas= {}/3 ".format(vidas))
    else:
        print("ahhh te quedaste sin viditas")
        print("Gracias por jugar!!")
        one_more = input("Queres jugar una fichita mas? si/no: ")

        if one_more.lower() == "si":
            play()


play()

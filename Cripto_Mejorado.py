from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import random

#1.Elija un mensaje de cumpleaños
birthday_messages = [
    'esta es una fiesta',
    'y NO estas invitado',
    'este NO es un mensaje',
    'mensaje final',
    'destino final',
    'final destiny',
    'mensaje :D',
    'elJAJAS',
    'atodogas',
    'ELBROMAS',
    'xD',
    'ELjajas',
    ' :p '
]

def elegirMensaje():
    b_message = random.choice(birthday_messages)
    b_message.encode()
    return b_message

bir_mensa = elegirMensaje().encode()



#2.Genera una clave AES aleatoria.
def generarLlaveAES():
    clave = Fernet.generate_key()
    with open("llave_AES.txt", "wb") as archivo_clave:
        archivo_clave.write(clave)

def cargarLlaveAES():
    return open("llave_AES.txt", "rb").read()



#3.Cifre el mensaje de cumpleaños con la clave AES aleatoria. Esta será la tarjeta.
def generarTarjeta(x):
    bir_mensa = x
    aes_key = cargarLlaveAES()

    f = Fernet(aes_key)
    encriptado = f.encrypt(bir_mensa)

    with open("tarjeta.txt", "wb") as tarjeta_archivo:
        tarjeta_archivo.write(encriptado)

    sad = f.decrypt(encriptado)
    guardar(sad)

XG = ''
def guardar(g):
    global XG
    XG = g



#4.Cifre la clave AES aleatoria con la clave pública RSA. Este será el sobre.
def generarSobre():
    f = open("llave_AES.txt", "rb")
    llave_AES = f.read()
    f.close()

    llave_pub_rsa = RSA.importKey(open("generador_rsa/llavepublica.pub", "rb").read())
    cifrado_rsa = PKCS1_OAEP.new(llave_pub_rsa)
    cifrar_mensaje_rsa = cifrado_rsa.encrypt(llave_AES)

    with open("sobre.txt", "wb") as archivo_sobre:
        archivo_sobre.write(cifrar_mensaje_rsa)


generarLlaveAES()
print("Llaves generadas\n")
generarTarjeta(bir_mensa)
print("Tarjeta generadas\n")
generarSobre()



#5.Imprime (o envía, lo que sea) la tarjeta y el sobre a la víctima festejada.
def imprimirPaso5():
    f = open("tarjeta.txt", "rb")
    paso5_tarjeta = f.read()
    f.close()
    g = open("sobre.txt", "rb")
    paso5_sobre = g.read()
    g.close
    print("Es usted Bienvenido a Nuestra fiesta, esta es su tarjeta")
    print(paso5_tarjeta)
    print()
    print("Y este es su sobre")
    print(paso5_sobre)



imprimirPaso5()
print()
print()


#6.Pídale a CrytpoJoker que descifre la tarjeta (por favor).
#7.Pídale a la víctima que responda una pregunta sencilla.
#Se recomienda utilizar un simple pregunta aritmética, como: “2 + 3 =”, y espere un número como respuesta.
#Utilice preguntas diferentes, no siempre lo mismo.
#8.Si la respuesta es correcta, pida el sobre.


def pedirJoker():
    print("_______________________________________")
    print("Bienvenido a la fiesta del Joker, ¿Que deseas?")
    print("_______________________________________")
    print()
    print("Opciones disponibles:")
    print("1. Descifrar la Tarjeta")
    print("0. Salir")
    print()



def menu():
    while True:
        pedirJoker()
        try:
            entrada_usuario = int(input("Seleccione una opcion: "))

            if entrada_usuario in range(2):

                print("Usted eligió la opcion {} !\n".format(entrada_usuario))
                print()

                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    quit()
                    break
                elif entrada_usuario == 1:

                    print("Antes resuelva la siguiente pregunta: ")

                    banco_preguntas = {
                        "3 + 3":6,
                        "1 + 1":2,
                        "2 + 2":4,
                        "8 + 1":9,
                        "7 - 3":4
                    }

                    pregunta, respuesta = random.choice(list(banco_preguntas.items()))

                    print(pregunta)
                    respuesta_a_pregunta = int(input())

                    if respuesta == respuesta_a_pregunta:
                        print("La espuesta es: ", respuesta_a_pregunta, "\n")
                        break
                    else:
                        print("Te equivocaste")
                        quit()
                        break


            else:
                print('Error, solo de aceptan numeros del 0 al 4')

        except ValueError:
            print("Error, ingrese solamente numeros")
            quit()
        break


menu()


#9.Descifre el sobre con la clave privada secreta RSA e imprímalo
#(este es el AES clave privada, ¿recuerdas?)
def descifrarSobre():
    s = open("sobre.txt", "rb")
    sobre_por_descifrar = s.read()
    s.close()

    llave_priv_rsa = RSA.importKey(open("generador_rsa/llaveprivada.pem", "rb").read())
    cifrado = PKCS1_OAEP.new(llave_priv_rsa)
    sobre_dedscifrado = cifrado.decrypt(sobre_por_descifrar)

    archivo_sobre_descifrado = open("sobreDescifrado_claveAES.txt", "wb")
    archivo_sobre_descifrado.write(sobre_dedscifrado)
    archivo_sobre_descifrado.close()
    print("Sobre Descifrado\n")



descifrarSobre()



#10. Descifre la tarjeta utilizando el sobre descifrado.
#       Puede desarrollar su propio programa para descifrarlo o utilizar
#       alguna función de descifrado AES en línea. De cualquier manera,
#       necesita dos datos: el mensaje cifrado y la clave secreta.
def descifrarTarjeta():
    llave_aes = cargarLlaveAES()

    f = open("sobreDescifrado_claveAES.txt", "rb")
    ar_x_comparar = f.read()
    f.close()

    g = open("llave_AES.txt", "rb")
    ar_y_comparar = g.read()
    g.close()

    if ar_x_comparar == ar_y_comparar:
        h = open("mensaje.txt", "wb")
        h.write(XG)
        h.close()
    else:
        print("error 404")

    print("Tarjeta descifrada\n")


descifrarTarjeta()

#11. Disfrute del mensaje de felicitación.
def mostrarMensaje():
    f = open("mensaje.txt", "rb")
    mensaje = f.read()
    f.close()

    print("El mensaje original es: ", mensaje)

mostrarMensaje()


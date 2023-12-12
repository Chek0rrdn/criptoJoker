import random
import signal
import sys
import pathlib
import time
import os

from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA


__birthday_messages = (
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
)

#MANEJO DEL Ctrl. + C
def def_handler(sig, frame):
    print("\nSaliendo...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


#LIMPIAR PANTALLA
def limpiar_pantalla():
    comando = 'clear'
    if os.name in ('nt', 'dos'):  # Si la maquina esta corriendo Windows se utiliza cls
        comando = 'cls'
    os.system(comando)


##MEDIR TIEMPO
def tiempo_de_ejecucion(func):
    def envoltura(*args, **kwargs):
        tiempo_inicial = time.time()
        func(*args, **kwargs)
        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final-tiempo_inicial
        tiempo_transcurrido = round(tiempo_transcurrido, 3)
        print(f"Transcurrieron: {tiempo_transcurrido} segundos")

    return envoltura



#SELECCIONAR UN MENSAJE ALEATORIO
def elegir_mensaje():
    b_message = random.choice(__birthday_messages)
    b_message.encode()
    return b_message



DIRECTORIO_ACTUAL = pathlib.Path().resolve()
DIRECTORIO_LLAVES = DIRECTORIO_ACTUAL.joinpath("keys")



#LLAVES RSA
def generar_llaves_RSA():
    tam = 4096
    llave = RSA.generate(tam)


    if not DIRECTORIO_LLAVES.exists():
        DIRECTORIO_LLAVES.mkdir()


    if pathlib.Path(DIRECTORIO_LLAVES / "llaveprivada.pem").exists():
        pass
    else:
        with open(pathlib.Path(DIRECTORIO_LLAVES / "llaveprivada.pem"), mode='wb') as file:
            file.write(llave.export_key('PEM'))



    if pathlib.Path(DIRECTORIO_LLAVES / "llavepublica.pub").exists():
        pass
    else:
        with open(pathlib.Path(DIRECTORIO_LLAVES / "llavepublica.pub"), mode='wb') as file:
            file.write(llave.public_key().export_key('PEM'))



def obtener_llave_pub_RSA():
    return open(DIRECTORIO_LLAVES / "llavepublica.pub", "rb").read()


def obtener_llave_priv_RSA():
    return open(DIRECTORIO_LLAVES / "llaveprivada.pem", 'rb').read()



#LLAVES AES
def generar_clave_AES():
    clave = Fernet.generate_key()
    with open(DIRECTORIO_LLAVES / "llave_AES.txt", "wb") as archivo_clave:
        archivo_clave.write(clave)

def obtener_llaves_AES():
    return open(DIRECTORIO_LLAVES / "llave_AES.txt", 'rb').read()



##MENUS
def pedir_joker():
    print(
        """
        ________________________________________________________
            Bienvenido a la fiesta del Joker, ¿Que deseas?      
        ________________________________________________________
        
        Opciones disponibles:
            1. Descifrar la Tarjeta
            0. Salir
        """
    )

def menu():
    while True:
        pedir_joker()
        try:
            entrada_usuario = int(input("Seleccione una opción: "))

            if entrada_usuario in range(2):

                print(f"Usted eligió la opción {entrada_usuario} !\n")
                # print()

                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    quit()
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
                        print(f"La respuesta es: {respuesta_a_pregunta}, por lo tanto su respuesta es CORRECTA\n")
                        limpiar_pantalla()
                        break
                    else:
                        print("Te equivocaste, Adios perdedor!!!")
                        quit()


            else:
                print('Error, solo de aceptan números del 0 al 4')
                time.sleep(1.2)
                limpiar_pantalla()
                # quit()

        except ValueError:
            print("Error, ingrese solamente números")
            # quit()



DIRECTORIO_ARCHIVOS = DIRECTORIO_ACTUAL.joinpath("files")

def guardar(nombre_archivo, archivo):
    ruta = str(DIRECTORIO_ARCHIVOS) + str(f'/{nombre_archivo}.txt')

    if not DIRECTORIO_ARCHIVOS.exists():
        DIRECTORIO_ARCHIVOS.mkdir()

    with open(ruta, mode='w')as file:
        archivo = str(archivo)
        file.write(archivo)
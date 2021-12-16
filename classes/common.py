import random

from sobre import *
from tarjeta import *

from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA


_birthday_messages = (
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


def elegir_mensaje():
    b_message = random.choice(_birthday_messages)
    b_message.encode()
    return b_message


#LLAVES RSA
def generar_llaves_RSA():
    tam = 4096
    llave = RSA.generate(tam)

    with open('../keys/llaveprivada.pem', mode='wb') as file:
        file.write(llave.export_key('PEM'))

    with open('../keys/llavepublica.pub', mode='wb') as file:
        file.write(llave.public_key().export_key('PEM'))

def obtener_llaves_RSA():
    return open("../keys/llavepublica.pub", "rb").read().decode()


#LLAVES AES
def generar_clave_AES():
    clave = Fernet.generate_key()
    with open("../keys/llave_AES.txt", "wb") as archivo_clave:
        archivo_clave.write(clave)

def obtener_llaves_AES():
    return open("../keys/llave_AES.txt", "rb").read().decode()

def preguntas():
    pass


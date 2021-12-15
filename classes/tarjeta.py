from cryptography.fernet import Fernet


class Tarjeta:
    def __init__(self, mensaje, clave_aes):
        self.__mensaje = mensaje
        self.clave_aes = clave_aes
        self.__tarjeta_cifrada = None
        self.__tarjeta_descifrada = None

        self.__cifrar_mensaje()


    # al cifrar el mensaje se convierte en Tarjeta
    def __cifrar_mensaje(self):
        f = Fernet(self.clave_aes)
        encriptado = f.encrypt(self.__mensaje)

        self.__tarjeta_cifrada = encriptado
        self.__tarjeta_descifrada = f.decrypt(self.__tarjeta_cifrada)

    
    def mostrar_tarjeta_cifrada(self):
        return self.__tarjeta_cifrada.decode()

    # al descifrar la tarjeta, se obtiene el mismo resultado que el MENSAJE
    def mostrar_tarjeta_descifrada(self):
        return self.__tarjeta_descifrada.decode()

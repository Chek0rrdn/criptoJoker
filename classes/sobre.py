from Crypto.Cipher import PKCS1_OAEP

class Sobre:
    def __init__(self, clave_aes, llave_pub_rsa):
        self.clave_aes = clave_aes
        self.__llave_pub_rsa = llave_pub_rsa
        self.__sobre_cifrado = None

        self.__cifrar_clave_rsa()

    
    # al cifrar la clave RSA este se convierte en el Sobre.
    def __cifrar_clave_rsa(self):
        cifrado_rsa = PKCS1_OAEP.new(self.__llave_pub_rsa)
        cifrar_mensaje_rsa = cifrado_rsa.encrypt(self.clave_aes)

        self.__sobre_cifrado = cifrar_mensaje_rsa

    
    def mostrar_sobre_cifrado(self):
        return self.__sobre_cifrado
    
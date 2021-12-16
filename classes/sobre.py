from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class Sobre:
    def __init__(self, clave_aes, llave_pub_rsa, llave_priv_rsa):
        self.clave_aes = clave_aes
        self.__llave_pub_rsa = llave_pub_rsa
        self.__llave_priv_rsa = llave_priv_rsa
        
        self.__sobre_cifrado = None
        self.__sobre_descifrado = None

        self.__cifrar_clave_rsa()

    
    # al cifrar la clave RSA este se convierte en el Sobre.
    def __cifrar_clave_rsa(self):
        llave_pub_rsa_ = RSA.import_key(self.__llave_pub_rsa)
        cifrado_rsa = PKCS1_OAEP.new(llave_pub_rsa_)
        cifrar_mensaje_rsa = cifrado_rsa.encrypt(self.clave_aes)

        self.__sobre_cifrado = cifrar_mensaje_rsa
        self.__descifrar_sobre()

    #se descifra a partir de el sobre descifrado
    def __descifrar_sobre(self):
        llave_priv_rsa_ = RSA.importKey(self.__llave_priv_rsa)
        cifrado = PKCS1_OAEP.new(llave_priv_rsa_)
        self.__sobre_descifrado = cifrado.decrypt(self.__sobre_cifrado)


    def mostrar_sobre_cifrado(self):
        return self.__sobre_cifrado
    
    def mostrar_sobre_descifrado(self):
        return self.__sobre_descifrado
from criptoJoker import tarjeta
from criptoJoker import sobre
from criptoJoker import common as cm

if __name__ == '__main__':
    ####ESTO ES PARA VER EL FUNCIONAMIENTO DE TARJETA
    cm.generar_clave_AES()
    tarjeta_ = tarjeta.Tarjeta(
        mensaje=cm.elegir_mensaje().encode(), 
        clave_aes=cm.obtener_llaves_AES()
    )
    print(f'clave AES:\t\t{tarjeta_.clave_aes.decode()} \n')
    print(f'tarjeta cifrada:\t{tarjeta_.mostrar_tarjeta_cifrada()} \n')
    print(f'tarjeta descifrada:\t{tarjeta_.mostrar_tarjeta_descifrada()} \n')
    print(f'mensaje:\t\t{tarjeta_.mensaje.decode()}\n\n\n')


    print('*'*150)
    print('\n')

    ####ESTO ES PARA VER EL FUNCIONAMIENTO DE SOBRE
    sobre_ = sobre.Sobre(
        clave_aes=cm.obtener_llaves_AES(), 
        llave_pub_rsa=cm.obtener_llave_pub_RSA(), 
        llave_priv_rsa=cm.obtener_llave_priv_RSA()
    )
    print(f'clave AES:\t\t{sobre_.clave_aes.decode()}\n')
    print(f'sobre cifrado:\n{sobre_.mostrar_sobre_cifrado()} \n')
    print(f'sobre descifrado:\t{sobre_.mostrar_sobre_descifrado().decode()} \n')
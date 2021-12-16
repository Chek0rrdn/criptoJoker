from classes import tarjeta as t
from classes import sobre as s
from classes import common as cm

if __name__ == '__main__':
    ####ESTO ES PARA VER EL FUNCIONAMIENTO DE TARJETA
    cm.generar_clave_AES()
    tarjeta = t.Tarjeta(
        mensaje=cm.elegir_mensaje().encode(), 
        clave_aes=cm.obtener_llaves_AES()
    )
    print(f'clave AES:\t\t{tarjeta.clave_aes} \n')
    print(f'tarjeta cifrada:\t{tarjeta.mostrar_tarjeta_cifrada()} \n')
    print(f'tarjeta descifrada:\t{tarjeta.mostrar_tarjeta_descifrada()} \n\n\n')


    print('*'*150)
    print('\n')

    ####ESTO ES PARA VER EL FUNCIONAMIENTO DE SOBRE
    sobre = s.Sobre(
        clave_aes=cm.obtener_llaves_AES(), 
        llave_pub_rsa=cm.obtener_llave_pub_RSA(), 
        llave_priv_rsa=cm.obtener_llave_priv_RSA()
    )
    print(f'clave AES:\t\t{sobre.clave_aes}\n')
    print(f'mostrar sobre cifrado:\n{sobre.mostrar_sobre_cifrado()} \n')
    print(f'sobre descifrado:\t{sobre.mostrar_sobre_descifrado()} \n')
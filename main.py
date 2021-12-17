from criptoJoker import tarjeta
from criptoJoker import sobre
from criptoJoker import common as cm

if __name__ == '__main__':

    cm.generar_clave_AES()
    print("Se generaron la nueva llave AES")

    tarjeta_ = tarjeta.Tarjeta(
        mensaje=cm.elegir_mensaje().encode(), 
        clave_aes=cm.obtener_llaves_AES()
    )

    sobre_ = sobre.Sobre(
        clave_aes=cm.obtener_llaves_AES(), 
        llave_pub_rsa=cm.obtener_llave_pub_RSA(), 
        llave_priv_rsa=cm.obtener_llave_priv_RSA()
    )

    print(f'Esta es su Tarjeta: \t{tarjeta_.mostrar_tarjeta_cifrada()}\n')
    cm.guardar(
        'tarjeta', 
        tarjeta_.mostrar_tarjeta_cifrada()
    )
    print(f'Este es su Sobre: \t{sobre_.mostrar_sobre_cifrado()}\n')
    cm.guardar(
        'Sobre',
        sobre_.mostrar_sobre_cifrado()
    )


    cm.menu()
    cm.limpiar_pantalla()


    print(f'Este es su Sobre Descifrado: {sobre_.mostrar_sobre_descifrado().decode()} \n')
    cm.guardar(
        'sobre-descifrado',
        sobre_.mostrar_sobre_descifrado().decode()
    )
    print(f'Esta es su Tarjeta Descifrada, asi que su mensaje original era "{tarjeta_.mostrar_tarjeta_descifrada()}" \n')
    cm.guardar(
        'tarjeta-descifrada-\'MENSAJE\'',
        tarjeta_.mostrar_tarjeta_descifrada()
    )
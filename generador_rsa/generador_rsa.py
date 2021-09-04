from Crypto.PublicKey import RSA

tam = 4096

llave = RSA.generate(tam)

with open("llaveprivada.pem", "wb") as x:
	x.write(llave.exportKey('PEM'))

with open("llavepublica.pub", "wb") as d:
	d.write(llave.publickey().exportKey('PEM'))
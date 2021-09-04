# The Joker Birthday Card
## Applied Cryptography Final Project 


## Introduction

The challenge is to implement a simple cryptosystem based on envelope encryption. Envelope
encryption is a technique to perform double encryption on a given data using symmetric and
asymmetric algorithms. The symmetric algorithm is used to encrypt and decrypt the data, and the
asymmetric algorithm is used to encrypt and encrypt the symmetric key.
In this project you will write a program (The CryptoJoker) to encrypt a message with a symmetric
algorithm and a randomly generated private key encrypted with an asymmetric algorithm acting as an
envelope.

## Algorithm
The algorithm goes like this:
- [**CryptoJoker**] : Pick a birthday message (the text can be gotten from a stored list or hash map or let The Joker to type it).
- [**CryptoJoker**] : Generate a random AES key.
- [**CryptoJoker**] : Encrypt the birthday message using the random AES key. This will be the **card**.
- [**CryptoJoker**] : Encrypt the random AES key using RSA public key. This will be the **envelope**.
- [**CryptoJoker**] : Print (or send, whatever) the card and the envelope to the ~~victim~~ celebrated.
- [**Victim**] : Ask to CrytpoJoker to decrypt the card (please). 
- [**CryptoJoker**] : Ask the victim to answer an easy question. It is recommended to use a simple  arithmetic question, like: “2+3=”, and wait for a number in response. Use different questions, not  always the same.
- [**CryptoJoker**] : If the answer is correct, ask for the envelope.
- [**CryptoJoker**] : Decrypt the envelope using the secret RSA private key and print it (this is the AES  private key, remember?) 
- [**Victim**] : Decrypt the card using the decrypted envelope. You can either develop your own  program to decrypt it or use some online AES decryption function. Either way you need two  data: the encrypted message, and the secret key. 
- [**Victim**] : Enjoy the congratulation message.  


## Installation

> **Note**: To run the main program it is necessary to install all the required packages.
This can be done with the command:


```sh
pip3 install -r requirements.txt 
```

> and once installed, run the program:

```sh
generador_rsa.py 
```

>file found in "rsa generator" folder
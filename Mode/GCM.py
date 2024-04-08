from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

import base64


def encrypt(text, passphrase):
    # generiamo il salt
    kdf_salt = get_random_bytes(16)

    # deriviamo la chiave
    key = PBKDF2(passphrase, kdf_salt)

    # creiamo l'oggetto cifrario AES in modalità GCM
    cipher = AES.new(key, AES.MODE_GCM)

    # cifriamo il testo
    cipher_text, tag = cipher.encrypt_and_digest(text.encode('utf-8'))

    # otteniamo il nonce utilizzato durante la cifratura
    nonce = cipher.nonce

    # costruiamo il messaggio formattato
    formatted_message = base64.b64encode(cipher_text).decode('utf-8') + '\n' + base64.b64encode(tag).decode('utf-8') + '\n' + base64.b64encode(nonce).decode('utf-8') + '\n' + base64.b64encode(kdf_salt).decode('utf-8')

    # aggiungiamo l'header la messaggio
    message = 'CAP01' + formatted_message

    # prints of the result
    print(f"\n||----------------------------||")
    print("\n\tRESULTS:")
    print(f"\nCipher_text :   {cipher_text.hex()}")
    print(f"Tag        :   {tag.hex()}")
    print(f"Nonce      :   {nonce.hex()}")
    print(f"Key        :   {key.hex()}")
    print(f"\n--------------------------------")
    print(f"\nTRANSMITTED MESSAGE:")
    print(f"{message}")
    print(f"\n||----------------------------||")

    return message


def decrypt(message, passphrase):
    # estrariamo i componenti dal messaggio formattato
    message_components = message[5:].split('\n')
    cipher_text = base64.b64decode(message_components[0])
    tag = base64.b64decode(message_components[1])
    nonce = base64.b64decode(message_components[2])
    kdf_salt = base64.b64decode(message_components[3])

    # deriviamo la chiave
    key = PBKDF2(passphrase, kdf_salt)

    # creiamo il cifrario AES nella modalità GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # decifriamo il testo cifrato e verfichiamo il tag/MAC
    try:
        decrypted_text = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted_text.decode('utf-8')
    except ValueError as e:
        print("\nMAC validation failed during decryption.")
        print(str(e))
        return -1

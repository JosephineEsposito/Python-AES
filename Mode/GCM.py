from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

import base64


def encrypt(text, passphrase, kdf_salt):
    # generating encryption key
    key = PBKDF2(passphrase, kdf_salt)
    # creating the object
    cipher = AES.new(key, AES.MODE_GCM)
    cipherText, tag = cipher.encrypt_and_digest(text)

    # nonce will be generated randomly if not provided explicitly
    nonce = cipher.nonce
    message = nonce, tag, cipherText, kdf_salt

    # prints of the result
    print(f"\n||----------------------------||")
    print("\n\tRESULTS:")
    print(f"\nCipherText :   {(cipherText)}")
    print(f"Tag        :   {tag}")
    print(f"Nonce      :   {nonce}")
    #print(f"KDF Salt   :   {(kdf_salt)}")
    #print(f"Key        :   {(key)}")
    #print(f"\n--------------------------------")
    #print(f"\nTRANSMITTED MESSAGE:")
    #print(f"{message}")
    print(f"\n||----------------------------||")

    return message


def decrypt(text, passphrase):
    # vars
    nonce, tag, cipherText, kdf_salt = text
    #add a control to separate them by a delim

    # generating decryption key from passphrase and salt
    key = PBKDF2(passphrase, kdf_salt)
    print("Decryption Key is: " + str(key))

    # validation of MAC and decrypt
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    
    try:
        decrypted_data = cipher.decrypt_and_verify(cipherText, tag)
        print(f"\nDECRYPTED DATA:")
        print(f"\nData: {decrypted_data}")
        return decrypted_data
    except ValueError as mac_mismatch:
        print("\nMAC validation failed during decryption.")
        return -1
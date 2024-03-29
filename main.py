#2024
#Author @josephineesposito
#Using PyCryptoDome lib

#region | Imports
import Mode.GCM as GCM
import base64
#endregion

# --- This is the main code --- #

# method selection

# passphrase selection
print("\nDo you want to generate a new passphrase?")
selection = 'n' #input("[y/n] : ")
if selection == "n":
    passphrase = "PippoBaudo202420"
else:
    passphrase = input("Please input a new passphrase: ")

kdf_salt = GCM.get_random_bytes(16)

# text to encrypt and decrypt
print("\nPlease input the text to encrypt and decrypt:")
text = "Josephine2024".encode('utf-8') #input()
txt = text.hex()

#print("\nHex text is: " + str(txt))

result = GCM.encrypt(txt.encode('utf-8'), passphrase, kdf_salt)
#print("\n\nResult in str: " + str(result))

de_result = GCM.decrypt(result, passphrase)

print("\nHex encode is: " + str(txt.encode('utf-8')))
ans = de_result.decode('utf-8')
byte_values = bytes.fromhex(ans)
result_string = byte_values.decode('utf-8')
print("Dehex text is: " + str(result_string))
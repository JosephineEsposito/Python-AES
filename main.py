#2024
#Author @josephineesposito
#Using PyCryptoDome lib

#region | Imports
import Mode.GCM as GCM
#endregion

# --- This is the main code --- #

# method selection
# ...

# passphrase selection
passphrase = "JE2000ME1964ME2004SD1971"


# text to encrypt and decrypt
#print("\nPlease input the text to encrypt and decrypt:")
text = "Josephine2024".encode('utf-8') #input()
txt = text.hex()

#print("\nHex text is: " + str(txt))

result = GCM.encrypt(txt, passphrase)
#print("\n\nResult in str: " + str(result))

de_result = GCM.decrypt(result, passphrase)


print(f"\nInput  text: {bytes.fromhex(txt).decode('utf-8')}")
print(f"Output text: {bytes.fromhex(de_result).decode('utf-8')}")
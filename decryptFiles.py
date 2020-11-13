from cryptography.fernet import Fernet

# this function decrypts a file
def decrypt(filename, key):

    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

# This function loads the key from the current directory named key.key
def load_key():

    return open("key.key", "rb").read()

key = load_key()

file = "hfs.txt"

decrypt(file, key)
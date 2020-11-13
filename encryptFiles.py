from cryptography.fernet import Fernet

# Fernet is an implementation of symmetric authenticated cryptography.

# This function generates key and saves it to a file
def write_key():

    key = Fernet.generate_key()
    # generate.key() function generates a fresh fernet key

    with open("key.key", "wb") as key_file:
        key_file.write(key)

# This function loads the key from the current directory named key.key
def load_key():

    return open("key.key", "rb").read()

# This function encrypts a file given the name of the file and the key
def encrypt(filename, key):
    
    f = Fernet(key)
    # Given a filename (str) and key (bytes), it encrypts the file and writes it

    # read the file
    with open(filename, "rb") as file:
        file_data = file.read() # read all the file data

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file using the same name as the plain text file, so it will
    # overwrite the original
    with open(filename, "wb") as file:
        file.write(encrypted_data)

write_key()

key = load_key()

file = "hfs.txt"

encrypt(file, key)

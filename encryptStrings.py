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

# String encryption:

write_key() # generate and write a new key

key = load_key() # load the previously generated key

message = "some secret message".encode()
# encode() function converts the string to bytes suitable for encryption using utf-8 codec

#initialize the Fernet class
f = Fernet(key)

# encrypt the message
encrypted = f.encrypt(message)

# f.encrypt() function encrypts the data passed to it
# result is known as a "Fernet token"

print("\nThe encrypted message is: ")
print(encrypted)

#decrypt the message
decrypted = f.decrypt(encrypted)

# f.decrypt() decrypts a Fernet token

print("\nThe decrypted message is: ")
print(decrypted)
print("\n")
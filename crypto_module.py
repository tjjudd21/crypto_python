from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()

# value of key is assigned to a variable
cipher_suite = Fernet(key)

# the plaintext is converted to ciphertext
cipher_text = cipher_suite.encrypt(b"This is an example using the cryptography module.")

# decrypt the ciphertext
plain_text = cipher_suite.decrypt(cipher_text)

#print the encrypted message
print(cipher_text)

#print the plaintext message
print(plain_text)
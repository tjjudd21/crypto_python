import onetimepad

cipher = onetimepad.encrypt('One Time Cipher', 'random')
print("cipher text is: ")
print(cipher)
print("plain text: ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)
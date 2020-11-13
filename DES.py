import pyDes

data = b"DES Algorithm Implementation example"

CBC = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad = None, padmode = pyDes.PAD_PKCS5)
ECB = pyDes.des(b"DESCRYPT", pyDes.ECB, pad = None, padmode = pyDes.PAD_PKCS5)

c = CBC.encrypt(data)
e = ECB.encrypt(data)

print("ECB Encrypted: %r" % e)
print("ECB Decrypted: %r" % ECB.decrypt(e))
assert ECB.decrypt(e, padmode=pyDes.PAD_PKCS5) == data

print("CBC Encrypted: %r" % c)
print("CBC Decrypted: %r" % CBC.decrypt(c))
assert CBC.decrypt(c, padmode=pyDes.PAD_PKCS5) == data
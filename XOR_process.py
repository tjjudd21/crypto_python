"""
XOR algorithm converts the plain text in the format of ASCII bytes and uses XOR procedure to 
convert it to a specified byte. It is hard to hack by brute-force.
"""
def encryptDecrypt(inpString):
    #define XOR key--any character will work
    xorKey = 'P'

    #calculate length of input string
    length = len(inpString)

    #perform XOR operation on key
    #with every character in string
    for i in range(length):

        inpString = (inpString[:i] +
            chr(ord(inpString[i]) ^ ord(xorKey)) +
            inpString[i + 1:])
        print(inpString[i], end = "")

    return inpString

if __name__=='__main__':
    sampleString = "Encrypt this text"

    print("Encrypted string: ", end = "")
    sampleString = encryptDecrypt(sampleString)
    print("\n")

    print("Decrypted string: ", end = "")
    encryptDecrypt(sampleString)
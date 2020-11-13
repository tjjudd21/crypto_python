"""
The Caesar Cipher

Algorithm:
* The Caesar Cipher technique is a simple and easy method of encryption
* It is a type of substitution cipher
* Each letter pf plain text is replaced by a corresponding letter some fixed number of positions down the alphabet
"""

def encrypt(text,s):
    result = ""
    #traverse the plain text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        #Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

#check the above function
text = "CAESAR CIPHER DEMO"
s = 4

print ("Plain Text: " + text)
print ("Shift pattern: " + str(s))
print ("Cipher: " + encrypt(text,s))

"""
Explination:
* The plain text characters are traversed one at a time.
* Each letter is shifted "to the right" by s letters.
* Ex. s = 4; therefore, C + 4 = G. This is repeated for every letter in plain text
"""


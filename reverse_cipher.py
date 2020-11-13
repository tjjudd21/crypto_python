"""
This program demonstrates the the reverse cipher.

Algorithm:
    * Reverse Cipher uses a pattern of reversing the string of plain text to convert as cipher text
    * The process of encryption and decryption is the same
    * To decrypt cipher text, the user simply needs to reverse the cipher text to get the plain text

Drawback: Very weak encryption
"""

msg = 'This is a program to demonstrate the reverse cipher.'
translated ='' #cipher text is stored in this variable

i = len(msg) - 1

while i >= 0:
    translated = translated + msg[i]
    i = i - 1
print("The cipher text is: ", translated)

"""
* Plain text is stored in the variable message and the translated variable is used to store the cipher text
* The length of plain text is calculated using a for loop and with the help of an index number. The 
  characters are stored in the cipher text variable translated, which is printed in the last line. 
"""
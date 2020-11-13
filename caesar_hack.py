"""
The Brute Force Technique can be used to decode a message encoded using the Ceasar cipher
Brute Force involves trying every possible decryption key.
"""

message = 'GEIWEVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):

    translated = ''

    for symbol in message:

        if symbol in LETTERS:

            num = LETTERS.find(symbol)
            num = num - key

            if num < 0:

                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:

            translated = translated + symbol

    print('Hacking key #%s: %s' % (key, translated))

"""
The program shifts all the letters in the cipher text by s = 1, 2, 3...25 and prints each result
Key #4 (obviously) produces the readable plain text
"""
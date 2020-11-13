"""
Transposition Cipher:
cryptographic algorithm where the order of alphabets in the plaintext is rearranged to form a cipher text.
The actual plain text alphabets are not included.

* The plaintext message is written out in rows of fixed length and then read out again column by column, and 
the columns are chosen in some scrambled order.
* Width of the rows and the permutation of the columns are usually defined by a keyword.
* Spaces are filled with nulls, left blank, or replaced by characters.
* The message is read off in columns in the order specified by the keyword.
"""

import math

key = "HACK"

def encryptMessage(msg):
    cipher = ""

    # track key indices
    key_index = 0

    msg_length = float(len(msg))
    msg_list = list(msg)
    key_list = sorted(list(key))

    # calculate row length of the matrix
    row = len(key)

    # calculate the maximum column depth of the matrix
    col = int(math.ceil(msg_length / row))

    # add the padding character '_' in empty cells of the matrix
    fill_null = int((row * col) - msg_length)
    msg_list.extend('_' * fill_null)

    # create matrix and insert message and padding characters row-wise
    matrix = [msg_list[i: i + col]
                for i in range(0, len(msg_list), col)]
    
    for _ in range(col):
        current_index = key.index(key_list[key_index])
        cipher += ''.join([row[current_index]
                            for row in matrix])
        key_index += 1
    
    return cipher

def decryptMessage(cipher):
    msg = ""

    # track key indices
    key_index = 0

    # track message indices
    msg_index = 0
    msg_length = float(len(cipher))
    msg_list = list(cipher)

    # calculate column of the matrix
    row = len(key)

    # calculate maximum row of the matrix
    col = int(math.ceil(msg_length / row))

    # convert key into list and sort alphabetically so we can 
    # access each character by its alphabetical position
    key_list = sorted(list(key))

    # create an empty matrix to store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    
    # arrange the matrix column-wise according to permutation
    # order by adding into new matrix
    for _ in range(col):
        current_index = key.index(key_list[key_index])

        for j in range(row):
            dec_cipher[j][current_index] = msg_list[msg_index]
            msg_index += 1
        key_index += 1

    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    
    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]
    
    return msg

# Driver
msg = "Geeks for Geeks"

cipher = encryptMessage(msg)
print("Encrypted Message: {}".
                format(cipher))

print("Decrypted Message: {}".
                format(decryptMessage(cipher)))
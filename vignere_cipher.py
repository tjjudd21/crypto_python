alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    'abcdefghijklmnopqrstuvwxyz' + \
    '0123456789' + \
    ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, key):
    encrypted = ''
    
    # split the message to the length of the key
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    
    # convert the message to index and add the key (mod 26)
    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1
    
    return encrypted

def decrypt(cipher, key):
    decrypted = ''

    # split the cipher to the length of the key
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))]

    # convert cipher to index and subtract key (mod 26)
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1
    
    return decrypted

def main():
    key = 'banana'
    message = 'HOTEL FOXTROT SIERRA! It really worked.'
    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)

    print('You entered: ' + message)
    print('Encrypted message: ' + encrypted_message)
    print('Decrypted message: ' + decrypted_message)

main()
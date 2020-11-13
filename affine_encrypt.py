"""
The Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet is mapped to its numeric equivalent, 
encrypted using a simple mathematical function, and converted back into a letter. The encryption process relies on working modulo m (the
length of the alphabet used). In the Affine cipher, the letter of an alphabet of size m are first mapped to the integers in the range 
0...(m - 1)
The key to the cipher consists of two numbers (a and b). 'a' and 'm' should be co-prime (a should have no factors in common with m).
Formula: E(x) = (ax + b) mod m
"""

# Affine cipher encryption function
# returns cipher text
def affine_encrypt(text, key): 
	''' 
	C = (a*P + b) % 26 
	'''
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
				+ ord('A')) for t in text.upper().replace(' ', '') ])

#driver

def main():
    #declaring text and key
    text = 'TWENTY FIFTEEN'
    key = [17, 20]

    #calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)
    print('Encrypted Text: {}'.format(affine_encrypted_text))

if __name__ == '__main__':
    main()


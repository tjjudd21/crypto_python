import random, sys, os, Rabin_Miller, cryptomath

def main():
   makeKeyFiles('RSA_demo', 1024)

"""
The process begins with the selection of two prime numbers, p and q, and then calculating their product, n.
"""
def generateKey(keySize):
   # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
   print('Generating p prime...')
   p = Rabin_Miller.generateLargePrime(keySize)
   print('Generating q prime...')
   q = Rabin_Miller.generateLargePrime(keySize)
   n = p * q
	
   # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
   print('Generating e that is relatively prime to (p-1)*(q-1)...')
   while True:
      e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
      if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
         break
   
   """
   The specified pair of numbers, n and e, form the RSA public key. e is a number that is greater than 1 but less than
   (p - 1) and (q - 1) and e is coprime to (p - 1) and (q - 1).
   """
   # Step 3: Calculate d, the mod inverse of e.
   print('Calculating d that is mod inverse of e...')
   d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
   publicKey = (n, e)
   privateKey = (n, d)
   print('Public key:', publicKey)
   print('Private key:', privateKey)
   return (publicKey, privateKey)

"""
The private key, d, is calculated from the numbers p, q, and e using the following mathematical relationship: 
ed = 1 % (p - 1)*(q - 1).
"""
def makeKeyFiles(name, keySize):
   # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' 
   #(where x is the value in name) with the the n,e and d,e integers written in them,
   # delimited by a comma.
   if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
       sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))
   
   publicKey, privateKey = generateKey(keySize)
   print()
   print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1])))) 
   print('Writing public key to file %s_pubkey.txt...' % (name))
   
   fo = open('%s_pubkey.txt' % (name), 'w') 
   fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
   fo.close()
   print()
   print('The private key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
   print('Writing private key to file %s_privkey.txt...' % (name))
   
   fo = open('%s_privkey.txt' % (name), 'w')
   fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
   fo.close()

# If makeRsaKeys.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
   main()
import random, string, simple_substitution, sys

def main():
    for i in range(1000):
        key = simple_substitution.getRandomKey()
        message = random_string()
        print('Test %s String: "%s.."' % (i + 1, message[:50]))
        print("Key: " + key)
        encrypted = simple_substitution.translateMessage(message, key, 'E')
        decrypted = simple_substitution.translateMessage(encrypted, key, 'D')

        if decrypted != message:
            print('ERROR: Decrypted: "%s" Key: %s' % (decrypted, key))
            sys.exit()
        print('Substitution test passed!')

def random_string(size = 5000, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    main()
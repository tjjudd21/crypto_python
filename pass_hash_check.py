"""
The program below is used to create a password and its hash. It also includes logic for verifying the password.
"""
import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number of the specified password
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the database is: ' + hashed_password)
old_pass = input('Now please enter the password again to verify: ')

if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('Passwords do not match')

"""
hashlib package is used for storing passwords in a database. salt is used to add a random sequence to the password string
before implementing the hash function
"""
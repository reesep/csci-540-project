import hashlib
import string
import random

MAX_LENGTH = 6

def get_salt(password):

    charset = string.ascii_lowercase + string.digits

    while len(password) != MAX_LENGTH:

        password += random.choice(charset)

    return password
    


def main():

    password = input("Enter password: ")
    hashed = hashlib.md5(password.encode()).hexdigest()
    print("Password hash with no salt",hashed)

    salted = get_salt(password)
    print('Password with salt is "',salted,'"',)
    hash_val = hashlib.md5(salted.encode())

    print("New salted hash is",hash_val.hexdigest())
    
        


if __name__ == "__main__":
    main()

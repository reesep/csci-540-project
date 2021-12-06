
import hashlib
import random
import string

size = random.randint(5,15)

characters = string.printable

file = open("user.csv","a")

for x in range(50):

    user = ""
    password = ""
    for i in range(size):

        digit1 = characters[random.randint(0,len(characters)-1)]
        digit2 = characters[random.randint(0,len(characters)-1)]

        user += str(digit1)
        password += str(digit2)

    
    user = hashlib.md5(user.encode())
    password = hashlib.md5(password.encode())
    
    line = str(user.hexdigest()) + "," + str(password.hexdigest()) +"\n"
    file.write(line)


file.close()
    
    

    

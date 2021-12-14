
import hashlib
import random
import string

def generate_non_hashed_sequence():

    words = []
    words_file = open("words.txt","r")
    for each in words_file:
        words.append(each.strip())
    words_file.close()
    answer = random.choice(words)
    return answer



size = random.randint(5,15)

characters = string.printable

file = open("user.csv","a")

for x in range(50):

    user = ""
    password = ""
    ssn = ""
    for i in range(size):

        digit1 = characters[random.randint(0,len(characters)-1)]
        digit2 = characters[random.randint(0,len(characters)-1)]
        digit3 = characters[random.randint(0, len(characters) - 1)]


        user += str(digit1)
        password += str(digit2)
        ssn += str(digit3)
    
    user = hashlib.md5(user.encode())
    password = hashlib.md5(password.encode())
    address = generate_non_hashed_sequence() + generate_non_hashed_sequence()
    ssn = hashlib.md5(ssn.encode())
    id = generate_non_hashed_sequence()

    line = str(user.hexdigest()) + "," + str(password.hexdigest()) + "," + address + "," + str(ssn.hexdigest()) + "," + id + "\n"
    file.write(line)


file.close()
    
    

    

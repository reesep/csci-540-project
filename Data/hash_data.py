

import hashlib
import random
import string



file = open("weak-passwords.csv","r")
file.readline()

passwords = []

for each in file:
    line = each.split(",")

    passwords.append(line[0])

file.close()


file = open("weak-passwords-hashed.csv","w")

for each_password in passwords:
    md5 = hashlib.md5(each_password.encode())
    sha1 = hashlib.sha1(each_password.encode())
    
    line = str(each_password) + "," + str(md5.hexdigest()) + "," + str(sha1.hexdigest()) +"\n"
    file.write(line)

file.close()

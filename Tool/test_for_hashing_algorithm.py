

import os
import re

def test():
    print("--- Testing for Hashing Algorithm Choice ---")
    for filename in os.listdir("../Website"):

        file = open("../Website/" + filename,"r")

        text = file.read()
        patterns = ["md5","sha1"]

        found = False

        for each in patterns:

            if re.search(each,text):
                
                print(filename,": Hashing algorithm",each,"was detected ---->Consider using a more secure hashing algorithm")
                found = True
                break
            
        if not found:
            print(filename,": Hashing algorithm was not detected. Please ensure you are using a secure hashing algorithm")
            





if __name__ == "__main__":
    test()

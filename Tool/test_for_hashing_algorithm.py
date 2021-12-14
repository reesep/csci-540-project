

import os
import re

def test():

    for filename in os.listdir("../Website"):

        file = open("../Website/" + filename,"r")

        text = file.read()
        print(text)
        patterns = ["md5(","sha1("]

        for each in patterns:

            if re.search(each,text):
                print("Hashing algorithm",each,"was detected")
                print("Consider using a more secure hashing algorithm")

                return

        print("Hashing algorithm was not detected. Please ensure you are using a secure hashing algorithm")
            





if __name__ == "__main__":
    test()

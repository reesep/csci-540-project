
import os

def test():

    for filename in os.listdir("../Website"):

        file = open("../Website/" + filename,"r")
    

        unsafe_func = [ ("system(","PHP System System Call")]

        # mysql_real_escape_string
        # prepare statement

        text = file.read()

        if "mysqli" in text: ## if the file does some kind of sql interaction
            print("---------",filename,"----------")

            #find 
            
        


if __name__ == "__main__":
    test()


import os

def test():
    print("--- Testing for SQL Injection and Sanitation --- ")

    i1 = []
    i2 = []

    for filename in os.listdir("../Website"):
        file = open("../Website/" + filename,"r")

        text = file.read()
        res = False
        prep = False

        if "mysqli" in text: ## if the file does some kind of sql interaction
            #print("******************************",filename)
            #print(text)
            if "mysql_real_escape_string" not in text:
                i1.append(filename)

            if "->prepare" not in text:
                i2.append(filename)



    if i1 != []:
        print("Escape string functions not used. Please check"," and ".join(i1),"files ")
    if i2 != []:
        print("SQL prepare statments not functions not used. Please check"," and ".join(i2),"files ")
    if i2 == [] and i1 == []:
        print("Escape string functions and prepare statements both used ✓")





            #find 
            
        


if __name__ == "__main__":
    test()

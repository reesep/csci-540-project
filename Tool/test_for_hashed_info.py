

## Tests for plaintext password


import string
import statistics


def test_for_hashed_info():

    characters = string.ascii_lowercase[:6] + string.digits

    file = open("../Data/user.csv")

    char_freq = {}

    for each_char in characters:
        char_freq[each_char] = 0

    columns = file.readline().strip().replace('"',"").split(",")
    print(columns)
    index = columns.index("password")

    for each_line in file:
        each_line = each_line.strip().replace('"',"").split(",")

        for each_char in each_line[index]:

            if each_char in char_freq:
                char_freq[each_char] += 1
            else:
                char_freq[each_char] = 0


    for key,val in char_freq.items():
        print(key,val)


    freq = list(char_freq.values())
    
    var = statistics.stdev(freq)
    m = statistics.mean(freq)
    
    spread = var / m

    if spread < .5:
        print("Column seems to be hashed")
        return True
    else:
        print("Column is not hashed")
        return False



    

        

        
    






if __name__ == "__main__":

    test_for_hashed_info()



## Tests for plaintext password


import string
import statistics

def test(each,word_list):

    characters = string.ascii_lowercase[:6] + string.digits

    char_freq = {}

    for each_char in characters:
        char_freq[each_char] = 0



    for each_word in word_list:


        for each_char in each_word:

            if each_char in char_freq:
                char_freq[each_char] += 1
            else:
                char_freq[each_char] = 0


    freq = list(char_freq.values())
    
    var = statistics.stdev(freq)
    m = statistics.mean(freq)
    
    spread = var / m

    if spread < .6:  ## .6 is a "calibrated" value.... but still sus
        print("--- Testing for Hashed Column ---")
        print("Column '" + each +"' seems to be hashed")
        return True
    else:
        print("--- Testing for Hashed Column ---")
        print("WARNING: Column '" +each+"' is not hashed")
        return False


if __name__ == "__main__":
    test_for_hashed_info()

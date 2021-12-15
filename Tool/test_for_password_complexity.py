import string

def minimum_length(password):
    if len(password) < 6:
        return False
    else:
        return True

def contains_uppercase(password):

    for char in password:
        if char.isupper():
            return True
    return False

def contains_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def contains_special_char(password):
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "?", '"', "'", "_", "-", "+", "<", ">", "[", "]", "{", "}", "~", "`", ":", ";"]
    special = False
    for c in password:
        if c in special_char:
            special = True
    return special

def test(password_list):

    results = []

    for password in password_list:

        if (contains_number(password) and contains_special_char(password) and contains_uppercase(password) and minimum_length(password)):
            #print("password complexity is valid")
            pass
        if (not minimum_length(password)):
            #print("password must be longer")
            results.append("Password must be longer")
        if (not contains_uppercase(password)):
            #print("Password must contain an uppercase letter")
            results.append("Password must contain at least one uppercase letter")
        if (not contains_special_char(password)):
            #print("password must contain a special character")
            results.append("Password must contain atleast one special character")
        if (not contains_number(password)):
            #print("password must contain a digit")
            results.append("Password must contain atleast one digit")
        #else:
            #print("password must contain at least\n 1 uppercase letter \n one number \n one special character \n minimum length of 6")
        
    print("--- Testing for password complexity ---")
    if results == []:
        print("Password policy is strong")
    else:
        print("Weak password policy detected, please ensure you are enforcing the following rules: ")
        results = set(results)
        for each in results:
            print("*",each)

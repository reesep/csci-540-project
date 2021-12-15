import string

def minimum_length(password):
    if len(password) < 6:
        return False
    else:
        return True

def contains_uppercase(password):
    if password.ascii_uppercase:
        return True
    else:
        return False

def contains_number(password):
    if password.digits:
        return True
    else:
        return False

def contains_special_char(password):
    special_char = ["!", "@", "#", "$", "%", "^", "&", "*", "?", '"', "'", "_", "-", "+", "<", ">", "[", "]", "{", "}", "~", "`", ":", ";"]
    special = False
    for c in password:
        if c in special_char:
            special = True
    return special

def test(password_list):
    for password in password_list:

        if password == (contains_number and contains_special_char and contains_uppercase and minimum_length):
            print("password complexity is valid")
        if password == (contains_number and contains_special_char and contains_uppercase and not minimum_length):
            print("password must be longer")
        if password == (contains_number and contains_special_char and minimum_length and not contains_uppercase):
            print("Password must contain an uppercase letter")
        if password == (contains_number and contains_uppercase and minimum_length and not contains_special_char):
            print("password must contain a special character")
        if password == (contains_uppercase and contains_special_char and minimum_length and not contains_number):
            print("password must contain a digit")
        else:
            print("password must contain at least\n 1 uppercase letter \n one number \n one special character \n minimum length of 6")
        

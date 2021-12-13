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

def main():
    if contains_number and contains_special_char and contains_uppercase and minimum_length:
        print("password complexity is valid")
    if contains_number and contains_special_char and contains_uppercase:
        print("password must be longer")
    if contains_number and contains_special_char and minimum_length:
        print("Password must contain an uppercase letter")
    if contains_number and contains_uppercase and minimum_length:
        print("password must contain a special character")
    if contains_uppercase and contains_special_char and minimum_length:
        print("password must contain a digit")
    else:
        print("password must contain at least\n 1 uppercase letter \n one number \n one special character \n minimum length of 6")
    
main()
import hashlib

def weak_password_list():
    file = open("../Data/weak_passwords.csv")
    passwords = file.readline()
    wp = []
    for password in file:
        password = password.strip()
        md5 = hashlib.md5(password.encode())
        sha1 = hashlib.sha1(password.encode())
        sha256 = hashlib.sha256(password.encode())
        sha512 = hashlib.sha512(password.encode())
        wp.append([password, md5.hexdigest(),sha1.hexdigest(),sha256.hexdigest(),sha512.hexdigest()])
    return wp

def password_detector(wp, password):

    for weak_password in wp:
            for each_type in weak_password:
                #print(password,each_type)
                if password == str(each_type):
                    print("Weak password detected:",password)


def test(password_list):
    print("--- Testing for Weak Passwords ---")
    for password in password_list:
        wp = weak_password_list()
        password_detector(wp, password)
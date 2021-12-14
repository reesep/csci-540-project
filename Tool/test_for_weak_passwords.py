import hashlib

def weak_password_list():
    file = open("../Data/weak_passwords.csv")
    passwords = file.readline
    wp = []
    for password in file:
        md5 = hashlib.md5(password.encode())
        sha1 = hashlib.sha1(password.encode())
        sha256 = hashlib.sha256(password.encode())
        sha512 = hashlib.sha512(password.encode())
        wp.append([password, md5,sha1,sha256,sha512])
    return wp
def password_detector(wp, password):
    if wp == password:
        print("Weak password detected")
    else:
        print("not a weak password")

def test(password_list):
    for password in password_list:
        wp = weak_password_list()
        password_detector(wp, password)
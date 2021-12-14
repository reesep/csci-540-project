import hashlib

def weak_password_list():
    file = open("/csci-540-project/Data/weak_passwords.csv")
    passwords = file.readline
    wp = []
    for password in passwords:
        md5 = hashlib.md5(password)
        sha1 = hashlib.sha1(password)
        sha256 = hashlib.sha256(password)
        sha512 = hashlib.sha512(password)
        return wp[md5, sha1, sha256, sha512]
def password_detector(wp, password):
    if wp == password:
        print("Weak password detected")
    else:
        print("not a weak password")

def test(password_list):
    for password in password_list:
        wp = weak_password_list()
        password_detector(wp, password)
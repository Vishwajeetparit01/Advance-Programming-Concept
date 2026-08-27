import re

def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_-]).{8,}$'

    if re.match(pattern, password):
        return True
    else:
        return False

password = input("Enter your password: ")

if check_password(password):
    print("Strong password")
else:
    print("Weak password")
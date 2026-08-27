import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Za-z0-9.]+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

email = input("Enter your email address: ")

if validate_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
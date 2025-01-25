import re
email = str(input("Enter an E-mail: "))
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
if valid:
    print("Good, Valid E-mail Address")
else:
    print("InValid E-mail Address")
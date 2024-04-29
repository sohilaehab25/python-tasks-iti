import re
def check(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.fullmatch(regex, email)
 

name = input("Enter your name: ")
while not name: 
    print("Please enter a valid name.")
    name = input("Enter your name: ")

email = input("Enter your email address: ")
while not check(email):
    print("Please enter a valid email address.")
    email = input("Enter your email address: ")

print("name:", name)
print("email:", email)



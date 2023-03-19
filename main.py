import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("Password length: "))
password = ''

for i in range(length):
    c = random.choice(chars)
    password += c

print(f"Your random password is: {password}")
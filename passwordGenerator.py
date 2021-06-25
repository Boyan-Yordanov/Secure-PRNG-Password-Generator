import string
import random

specialChar = '\!@$%^&*?:|/([)];-.,<>'

# sizeofpass = 30
sizeofpass = input("What size do you want your password to be? \n")

def generation(sizeofpass):
    possibleCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + specialChar
    password = ''.join(random.SystemRandom().choice(possibleCharacters) for _ in range(int(sizeofpass)))
    return password

print(generation(sizeofpass))

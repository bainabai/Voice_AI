import random
import string

def random_password(length=12):
    passkeys = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(passkeys) for i in range(length))
    return password


password = random_password()
print("Generated Password:", password)

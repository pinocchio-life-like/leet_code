import random
import string

def generate_password(length):
    """Generate a random password of the specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password of length 12
password = generate_password(12)
print(password)

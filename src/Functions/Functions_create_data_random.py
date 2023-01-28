import random
import string


def create_random_email():
    email = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return email.lower()+"@gmail.com"


def create_random_user():
    user = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return user


def create_random_password():
    password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return password

import random
import string


def create_random_email():
    """this function return a random email"""
    email = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return email.lower()+"@gmail.com"


def create_random_user():
    """this function return a random user"""
    user = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return user


def create_random_password():
    """this function return a random password"""
    password = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return password

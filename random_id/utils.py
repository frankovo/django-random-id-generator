import string
import random

LENGTH = 11


def generate_random_string():
    """
    Generates random ID.
    """
    random_string = string.digits + string.ascii_uppercase
    new_id = ''.join([random.SystemRandom().choice(random_string) for i in range(random.randint(11, LENGTH))])
    return new_id

import string
from random import sample


def get_random_password(n=8) -> str:
    ALPHA = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return sample(ALPHA, n)


print(get_random_password())

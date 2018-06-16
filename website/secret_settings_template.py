import random
import string


def get_secret_key(debug):
    if debug is True:
        from website.secret_settings import secret_key
        return secret_key
    else:
        secret_key_length = 50
        return ''.join(random.choice(string.ascii_letters + string.digits) for n in range(secret_key_length))

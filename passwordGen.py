import string
import random
def get_random_string(password):
    letters = string.ascii_lowercase
    if password.specialChar:
        letters += string.punctuation
    if password.digit:
        letters += string.digits
    if password.up:
        letters += string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(password.length))
    return result_str
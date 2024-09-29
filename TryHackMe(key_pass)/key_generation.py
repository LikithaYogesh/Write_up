import random
import string

def check_key(key):

    if len(key) != 5 or ord(key[0]) % 5 != 3 or ord(key[1]) % 4 != 2 or not key[2].isdigit() or not key[3].islower() or not ord(key[4]) <= ord(key[3]) + 5 :
        return False
    return True

def crack_key():
    while True:
        key = [None] * 5

        # Generate key[0] such that ord(key[0]) % 5 == 3
        key[0] = chr(random.choice([i for i in range(256) if i % 5 == 3]))

        # Generate key[1] such that ord(key[1]) % 4 == 2
        key[1] = chr(random.choice([i for i in range(256) if i % 4 == 2]))

        # Generate key[2] as a digit and ensure valid key[5]
        while True:
            key[2] = random.choice(string.digits)
            if any(i > int(key[2]) + 2 for i in range(10)):
                break

        # Generate key[3] as a lowercase letter and ensure valid key[6]
        while True:
            key[3] = random.choice(string.ascii_lowercase)
            if any(ord(c) < ord(key[3]) - 3 for c in string.ascii_lowercase):
                break

        # Generate key[4] such that ord(key[4]) <= ord(key[3]) + 5 and allows valid key[7]
        while True:
            key[4] = chr(random.choice([i for i in range(256) if i <= ord(key[3]) + 5]))
            if any(ord(c) < ord(key[4]) - 4 for c in string.ascii_uppercase):
                break

        key = ''.join(key)

        if check_key(key):
            return key

while True:
    key = crack_key()
    valid = check_key(key)
    print(f"{key} - {valid}")

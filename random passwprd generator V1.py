# Build a random password generator. It should include characters, numbers and symbols and the length should be 8 min.

import random
import string

chrac = string.ascii_letters
num = string.digits
sym = "!@#$%^&*?"

combo = chrac + num + sym

random_num = random.randint(8, 12)

Password = ''.join(random.choice(combo) for _ in range(random_num))

print("Here is your password: ", Password)
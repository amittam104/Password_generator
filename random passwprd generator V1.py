# Build a random password generator. It should include characters, numbers and symbols and the length should be 8 min.
# But it should use any one symbol only once.

import random
import string

characters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*?"

# Only one symbol needs to be added in the generated password
sym = random.choice(symbols)
remaining_sym = symbols.replace(sym,'')

random_num = random.randint(8, 12)
length = random.randint(8, 12)
combo = characters + numbers

# Create a list of password only with charaters and numbers.
Password1 = [random.choice(combo) for _ in range(length -1)]

# Add any one random symbol in the password 
Position1 = random.randint(0, length -1)
Password1.insert(Position1, sym)

Password = ''.join(Password1)

print("Here is your password: ", Password)
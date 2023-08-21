# Build a random password generator. It should include characters, numbers and symbols and the length should be 8 min.

# Import both random and string. String is imported to ease out the listing of all the uppercase, lowercase letter and numbers.

import random
import string

# Define the variables for String, numbers and symbols
chrac = string.ascii_letters
num = string.digits
sym = "!@#$%^&*?"

# Combine all there varilabes to set a new varibale for the password
combo = chrac + num + sym

# genrate a random integer between 8 to 12

random_num = random.randint(8, 12)

# Generate the password using .join (to concatenate) and random.choice for 
Password = ''.join(random.choice(combo) for _ in range(random_num))

print("Here is your password: ", Password)
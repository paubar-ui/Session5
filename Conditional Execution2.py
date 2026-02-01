# 2nd (if + else)
# We can only use this way if there are 2 clear options - even and odd/ true or false

import random

number = random.randint(1, 100)
print(number)
#We get radom variables between 1 and 100.
if number % 2 == 0:
    print("even")
else:
    print("odd")

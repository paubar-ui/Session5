#3rd way: this is for variables that can result in more than 2 options

import random
a = random.randint(1, 10)
b = random.randint(1, 10)
print("a=", a)
print("b=", b)

if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("a < b")


money = 100
if money > 10 **9:
    print("welcome to the Forbes list")
elif money > 10 **8:
    print("welcome to the forbes up and coming")
elif money > 10 **7:
    print("hope you like your ferraris")
else:
    print("sorry, you are poor")
#we can put as many elif as desired.


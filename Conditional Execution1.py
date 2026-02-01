#So far we have done simple things in a sequential order, but in order to continue with complexity, we need to make decisions.
from random import choice

#There are 3 ways to do an if:
# 1st (the simplest)
name = input("what is your name? ")
choice = input("Do you want a greeting? (yes/no) ")
if choice == "yes":
    print("Hello ", name + "!")
    print("goodbye", name)
#After If we need to put something which will be either true or false
#the ":" means that after that will be a tab/ block that connects to the part above.
print("buenos días")  #the if has no power here for example

# 2nd (if and else)


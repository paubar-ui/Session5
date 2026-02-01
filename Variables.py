# programming allows us to do abstraction, which is giving names to things and using that name to get that value.
# we assign values with the symbol "=". The left hand side of the expression is the name we call the variable, and the right hand side is the value of it.
# There is no limit in the length of the variables.
# The name of the variables can only contain numbers, letters or underscore. However, it cannot begin with a number.

name = input("What is your name? ")
print("hello", name)
age = input("Enter your age: ")
try:
    age = int(age)  # by doing this, we are adapting the type of data so we don't get any errors
    print("you were born in", 2025 - age)
except ValueError:
    print("I am sorry", name, "but that is not a valid age.")
except ZeroDivisionError:
    print("You can't divide by zero")
else:  # else is only when no exception happens
    print("thank you for playing fair")
finally:
    print("goodbye")  # this will happen no matter what

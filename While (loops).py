num = 1
while num <= 10:
    print(num)
    num = num + 1

import random
money = 10000
counter = 1

while money > 0:
    print(money)
    expense = random.randint(1, 100)
    print("iteration:",counter, "expense=", expense)
    counter = counter + 1
    money = money - expense

#infinite loop w escape mechanism
while True > 0:
    if money < 0:
        break #stop the loop
    print(money)
    expense = random.randint(1, 100)
    print("iteration:",counter, "expense=", expense)
    counter = counter + 1
    money = money - expense


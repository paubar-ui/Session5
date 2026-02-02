try:
    Gross = int(input("Enter a your gross salary: "))
    Children = int(input("Enter a number of children: "))

    if Gross < 1000:
        tax = 0.1
    if 1000 < Gross < 2000:
        tax = 0.12
    if 2000 < Gross < 4000:
        tax = 0.14
    else:
        tax = 0.18

    if Gross < 2000:
        tax -= Children * 0.01
    else:
        tax -= Children * 0.005

    net = Gross * (1 - tax)
    print("Your net salary is =", net)

except ValueError:
    print("Please enter a numeric value")



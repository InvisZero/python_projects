print("Hello, welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")

# Day 3.2
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    # % is the modulo operator which gives the remainder of the division of the left hand operand by the right hand operand
    print("This is an even number.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Pay 5.")
    elif age <= 18:
        print("Pay 7.")
    else:
        print("Pay 17.")
else:
    print("This is an odd number.")

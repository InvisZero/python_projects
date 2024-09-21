year = int(input("which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    # if the year is divisible by 100 but not by 400, it is not a leap year
    # if the year is divisible by 4 and 100 and 400, then it is a leap year

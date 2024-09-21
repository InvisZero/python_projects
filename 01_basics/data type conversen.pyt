no_of_charater = len(input("what is your name? "))

new_charater = str(no_of_charater)
# this will convert the integer to string [str(integer_name)]

print("Yout name has " + new_charater + " charater")

a = 123
print(type(a))
# this will print the type of the variable

a = str(a)
# this will convert the integer to string [str(integer_name)]
print(type(a))

a = float(a)
# this will convert the string to float [float(string_name)]
print(type(a))

a = bool(a)
# this will convert the float to boolean [bool(float_name)]
print(type(a))

print(40 + float("100.5"))
# trhis will print 140.5 as 40 + 100.5 = 140.5

print(str(70) + str(100))
# this will print 70100 as 70,100 this acts as a string
# we can't do any mathematical operation on string
# we can only concatenate the string
# we can't do any mathematical operation on boolean
# we can only do and, or, not operation on boolean

score = 10
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
# this is called f-string
# this is used to concatenate the string and variable together
# we can also do mathematical operation in f-string

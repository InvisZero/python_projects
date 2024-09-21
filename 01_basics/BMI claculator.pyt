# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

hight = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(hight) ** 2
print(int(bmi))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")
